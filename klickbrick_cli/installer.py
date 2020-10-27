import subprocess


def show_tool_name(name):
    print('\n#### Installing [{}]...'.format(name))


def install_brew():
    show_tool_name('brew')
    cmd = "echo '/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh\"'"
    print(subprocess.check_output(cmd, shell=True).decode('utf-8'), end='')


def install_git():
    show_tool_name('git')
    cmd = "echo 'brew install git'"
    print(subprocess.check_output(cmd, shell=True).decode('utf-8'), end='')


def install():
    install_brew()
    install_git()
