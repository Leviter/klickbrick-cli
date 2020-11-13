#!/usr/bin/env python3
"""
Author: Marcel van den Brink <marcel.vandenbrink@gmail.com>
Purpose: Onboard new employees
"""

import argparse
import sys
import subprocess
import inspect
import os.path
import requests

from shutil import copyfile


def email_template_replace(template, firstname, lastname):
    template = template.replace("{{firstname}}", firstname)
    template = template.replace("{{lastname}}", lastname)
    return template


def email_write(firstname, lastname):
    if firstname is None or lastname is None:
        raise ValueError("Missing firstname and/or lastname! Cannot create IT request")

    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    template_file = open(path + "/resources/email.template", "r")
    template = template_file.read()
    template_file.close()

    email = email_template_replace(template, firstname, lastname)
    print(email)
    send_email(email)


def send_email(email):
    receiver = "it@mycompany.org"
    subject = "New employee"
    command = "mailto:{}?subject={}&body={}".format(receiver, subject, email)
    subprocess.Popen(["open", command])


def checklist_write():
    file = "checklist.md"
    output = open(file, "w")

    output.write("#Onboarding checklist for new employees\n")
    output.write("- [ ] introduce with team members\n")
    output.write("- [ ] introduce with department\n")
    output.write("- [ ] get some coffee\n")

    output.close()


def show_install_tool_name(name):
    print("\n#### Installing [{}]...".format(name))


def show_configure_tool_name(name):
    print("\n#### Configuring [{}]...".format(name))


def install_brew():
    show_install_tool_name("brew")
    cmd = "echo '/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh\"'"
    print(subprocess.check_output(cmd, shell=True).decode("utf-8"), end="")


def install_git():
    show_install_tool_name("git")
    cmd = "echo 'brew install git'"
    print(subprocess.check_output(cmd, shell=True).decode("utf-8"), end="")


def configure_git():
    show_configure_tool_name("git")
    cmd = "echo 'git config --global resources/git_message.template ~/.gitmessage.txt'"
    print(subprocess.check_output(cmd, shell=True).decode("utf-8"), end="")


def installer_install():
    install_brew()
    install_git()
    configure_git()


def get_commands_parser():
    parser = argparse.ArgumentParser(description="The klickbrick application")

    parser.add_argument("onboard", nargs="?", help="Start onboarding people")
    parser.add_argument("help", nargs="?", help="Display help on commands that can be used")

    return parser


def get_help_argument_parser():
    parser = argparse.ArgumentParser(description="Help on the klickbrick application")

    parser.add_argument("help", help="Get help on the help command")
    parser.add_argument("command", nargs="?", choices=["onboard"], help="Get help on given command")

    return parser


def get_onboard_argument_parser():
    parser = argparse.ArgumentParser(description="Help with onboarding new employees")

    checklist_group = parser.add_argument_group(title="Checklist")
    checklist_group.add_argument(
        "-c",
        "--checklist",
        action="store_true",
        default=False,
        help="Generate a checklist with manual steps",
    )

    it_request_group = parser.add_argument_group(title="IT request")
    it_request_group.add_argument(
        "-t",
        "--it-request",
        action="store_true",
        default=False,
        help="Generate an email to be sent to IT",
    )
    it_request_group.add_argument("--first-name", help="The first name")
    it_request_group.add_argument("--last-name", help="The last name")

    install_group = parser.add_argument_group(title="Install tools")
    install_group.add_argument("-i", "--install", metavar="install", help="Install a set of developer tools")

    return parser


def get_init_argument_parser():
    parser = argparse.ArgumentParser(description="Initialise a new project")

    parser.add_argument("-n", "--name", required=True, help="The name of the project")
    parser.add_argument("-p", "--path", default=os.getcwd(), help="The path where the project will be stored under")

    return parser


def onboard(arguments):
    parser = get_onboard_argument_parser()

    if len(arguments) == 1 and (arguments[0] == "-h" or arguments[0] == "--help"):
        parser.print_help()
        return

    args = parser.parse_args(arguments)

    if not args.checklist and not args.install and not args.it_request:
        checklist_write()
        installer_install()
        email_write(args.first_name, args.last_name)

    if args.checklist:
        checklist_write()

    if args.install:
        installer_install()

    if args.it_request:
        email_write(args.first_name, args.last_name)


def init(arguments):
    parser = get_init_argument_parser()

    if len(arguments) == 0:
        parser.print_help()
        return

    args = parser.parse_args(arguments)

    path = args.path + os.path.sep + args.name

    if os.path.isdir(path):
        print("There already is a directory present with this name: {}".format(path))
        print("Bailing out...")
        return

    os.makedirs(path)
    subprocess.run(["git", "init"], cwd=path)

    filename = inspect.getframeinfo(inspect.currentframe()).filename
    current_path = os.path.dirname(os.path.abspath(filename)) + os.sep + "resources"

    copyfile(current_path + os.sep + "CONTRIBUTING.md", path + os.sep + "CONTRIBUTING.md")
    copyfile(current_path + os.sep + "README.md", path + os.sep + "README.md")


def help(arguments):
    parser = get_help_argument_parser()

    if len(arguments) == 0:
        parser.print_help()
        return

    args = parser.parse_args(arguments)
    run_command(args.help, ["-h"])


def run(arguments):
    number_of_arguments = len(arguments)

    if number_of_arguments == 0:
        run_command(None, None)
    elif number_of_arguments == 1:
        run_command(arguments[0], [])
    else:
        run_command(arguments[0], arguments[1:])


def run_command(command, arguments):
    parser = get_commands_parser()
    args = parser.parse_args([command])

    if args.onboard is None and args.help is None:
        parser.print_help()
        sys.exit(1)

    call_method(command, arguments)
    send_event({"command":"".join(command), "parameters":"".join(arguments), "os":"macOS", "python_version:":"3.9"})


def call_method(command, arguments):
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(command)
    if not method:
        raise NotImplementedError("Method %s not implemented" % command)
    method(arguments)


def send_event(data):
    url = 'http://localhost:8080/event'
    try:
        response = requests.post(url, json=data, timeout=1000)
        print(response.status_code)
    except requests.exceptions.Timeout as ex:
        print(str(ex))
    except requests.exceptions.ConnectionError as ex:
        print(str(ex))


def main():
    run(sys.argv[1:])


if __name__ == "__main__":
    main()
