def write():
    file = "checklist.md"
    output = open(file, 'w')

    output.write("#Onboarding checklist for new employees\n")
    output.write('- [ ] introduce with team members\n')
    output.write('- [ ] introduce with department\n')
    output.write('- [ ] get some coffee\n')

    output.close()
