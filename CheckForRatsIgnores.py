#!/usr/bin/python3

"""
    :brief RATS to JUNIT Converter
    :date 24.10.2024
    :version v1.0.0
    :author Severin Sprenger
"""

import xml.etree.ElementTree as ET
import platform
import datetime
import sys
import os

rats_output = ET.parse(sys.argv[2])
rats_output_root = rats_output.getroot()

for vuln in rats_output_root.findall("vulnerability"):
    for currFile in vuln.findall("file"):
        currFileLines = open(os.path.join(sys.argv[1], str(currFile.find("name").text)), "r").read().splitlines()
        for line in currFile.findall("line"):
            commentString = currFileLines[int(line.text) - 1].split(" // ")[-1]
            if commentString.startswith("rats-suppress") and str(vuln.find("type").text) in commentString:
                print("Found ignore in file \"" + currFile.find("name").text + "\" at line " + str(line.text))
                currFile.remove(line)

tree = ET.ElementTree(rats_output_root)
try:
    os.remove(sys.argv[3])
except OSError:
    pass
tree.write(sys.argv[3])
