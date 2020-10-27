#!/usr/bin/env python3
"""
Author: Marcel van den Brink <marcel.vandenbrink@gmail.com>
Purpose: Onboard new employees
"""

import argparse
import sys
import subprocess


def checklist_write():
    file = "checklist.md"
    output = open(file, 'w')

    output.write("#Onboarding checklist for new employees\n")
    output.write('- [ ] introduce with team members\n')
    output.write('- [ ] introduce with department\n')
    output.write('- [ ] get some coffee\n')

    output.close()


def show_install_tool_name(name):
    print('\n#### Installing [{}]...'.format(name))


def show_configure_tool_name(name):
    print('\n#### Configuring [{}]...'.format(name))


def install_brew():
    show_install_tool_name('brew')
    cmd = "echo '/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh\"'"
    print(subprocess.check_output(cmd, shell=True).decode('utf-8'), end='')


def install_git():
    show_install_tool_name('git')
    cmd = "echo 'brew install git'"
    print(subprocess.check_output(cmd, shell=True).decode('utf-8'), end='')


def configure_git():
    show_configure_tool_name('git')
    cmd = "echo 'git config --global resources/git_message.template ~/.gitmessage.txt'"
    print(subprocess.check_output(cmd, shell=True).decode('utf-8'), end='')


def installer_install():
    install_brew()
    install_git()
    configure_git()


def get_argument_parser():
    parser = argparse.ArgumentParser(description='Help with onboarding new employees')

    parser.add_argument('onboard', metavar='onboard', type=str, default='')

    checklist_group = parser.add_argument_group(title='Checklist')
    checklist_group.add_argument('-c', '--checklist', action="store_true", default=False,
                                 help='Generate a checklist with manual steps')

    it_request_group = parser.add_argument_group(title='IT request')
    it_request_group.add_argument('-t', '--it-request', action='store_true', default=False,
                                  help='Generate an email to be sent to IT')
    it_request_group.add_argument('--first-name', metavar='firstname', help='The first name')
    it_request_group.add_argument('--last-name', metavar='lastname', help='The last name')

    install_group = parser.add_argument_group(title='Install tools')
    install_group.add_argument('-i', '--install', metavar='install', help='Install a set of developer tools')

    return parser


def parse_arguments(parser, args):
    """Get the command-line arguments"""
    return parser.parse_args(args)


def run(arguments):
    argument_parser = get_argument_parser()
    args = parse_arguments(argument_parser, arguments)
    if args.onboard == '':
        parse_arguments(argument_parser, ['-h'])
        sys.exit(0)

    if args.checklist:
        checklist_write()

    if args.install:
        installer_install()


def main():
    run(sys.argv[1:])


if __name__ == '__main__':
    main()
