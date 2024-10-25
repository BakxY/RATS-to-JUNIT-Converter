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

rats_output = ET.parse(sys.argv[1])
rats_output_root = rats_output.getroot()

root = ET.Element("testsuites", name="RATS")
testsuites = ET.SubElement(root, "testsuite", 
    name="RATS", 
    timestamp=str(datetime.datetime.now()), 
    hostname=platform.node(), 
    tests=str(len(rats_output_root.findall("analyzed"))), 
    errors="0", failures="0", skipped="0", 
    time=str(rats_output_root.find("timing/total_time").text)
)

errorCount = 0

for files in rats_output_root.findall("analyzed"):
    testcase = ET.SubElement(testsuites, "testcase", 
        name=str(files.text), 
        classname="RATS report", 
        time="1.0"
    )

    for vulnerabilities in rats_output_root.findall("vulnerability"):
        for affectedFiles in vulnerabilities.findall("file"):
            if(str(files.text) == str(affectedFiles.find("name").text)):
                volnMessage = str(vulnerabilities.find("message").text).replace("\n", "")

                volnType = ""

                if(vulnerabilities.find("type") != None):
                    volnType += "Type:" + str(vulnerabilities.find("type").text) + ", "

                if(vulnerabilities.find("severity") != None):
                    volnType += "Severity:" + str(vulnerabilities.find("severity").text)

                errorElement = ET.SubElement(testcase, "error")

                errorElement.text = volnType + "\n" + volnMessage + "on \n"

                for lines in affectedFiles.findall("line"):
                    errorElement.text += "Line " + str(lines.text) + "\n"
                    errorCount += 1
            
testsuites.attrib["errors"] = str(errorCount)

tree = ET.ElementTree(root)
try:
    os.remove(sys.argv[2])
except OSError:
    pass
tree.write(sys.argv[2])