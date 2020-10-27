#!/usr/bin/env python3
"""
Author: Marcel van den Brink <marcel.vandenbrink@gmail.com>
Purpose: Onboard new employees
"""

import checklist
import installer

import argparse
import sys


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
        checklist.write()

    if args.it_request:
        installer.install()

    return args.checklist


def main():
    print(run(sys.argv[1:]))


if __name__ == '__main__':
    main()
