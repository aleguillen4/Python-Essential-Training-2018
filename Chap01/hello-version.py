#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform #Access to underlying platform’s identifying data

#print('This is python version {}'.format(platform.python_version()))  #string with the .format option, it uses positional arguments, platform.python_version() outputs the python version
print(f"This is python version {platform.python_version()}") #would result in the same utput
print(f"This is the architecture {platform.architecture()}")# platform.architecture() outputs the architecture and the OS
print(f"This is the ISA {platform.machine()}")#Outputs the ISA