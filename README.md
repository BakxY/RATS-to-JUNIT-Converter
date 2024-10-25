# RATS to JUNIT Converter

This python scrypt converts a XML output of a [RATS](https://github.com/andrew-d/rough-auditing-tool-for-security) command to a JUNIT XML format to be used with a CICD like in Gitlab. 

## Arguments

- Arg1 => Argument 1 is the input XML file, crated by the RATS command
- Arg2 => Argument 2 is the output file where the converted XML should be written to (If file exists, file will be overwritten)

## Install

To install this script into your bin folder you can move it to a folder in your path varibale (ex. `/usr/local/bin/`) remove its file extention (remove`.py`) and set its permission to `755`. You can now use it just as any other command (`RatsToJunit [arg1] [arg2]`).