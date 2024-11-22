# RatsToJunit.py

This script converts a XML output of a [RATS](https://github.com/andrew-d/rough-auditing-tool-for-security) command to a JUNIT XML format to be used with a CICD like in Gitlab. 

## Arguments

- Arg1 => Argument 1 is the input XML file, created by the RATS command or filter script
- Arg2 => Argument 2 is the output file where the converted XML should be written to (If file exists, file will be overwritten)

# CheckForRatsIgnores.py

This script is run on a [RATS](https://github.com/andrew-d/rough-auditing-tool-for-security) xml output to allow inline ignores, so known or intended issues don't get flaged.

## Arguments

- Arg1 => Argument Is the path to the source folder rats was originaly run on
- Arg2 => Argument 2 is the input XML file, created by the RATS command
- Arg3 => Argument 3 is the filtered output file where the converted XML should be written to (If file exists, file will be overwritten)

## How to add ignores

To add ignores you have to add a comment. Currently only C comments are supported, or any other programming language that uses `//` as a comment seperator. The following comment has to be added at the end of a line flagged by rats:

```c
// rats-suppress TYPE_OF_VULNERABILITY
```

If a lines is flagged for multible vulnerabilities, you can add multible types to ignore them.

# Install

To install this script into your bin folder you can move it to a folder in your path varibale (E.g. `/usr/local/bin/`) remove its file extention (remove`.py`) and set its permission to `755`. You can now use it just as any other command (E.g. `RatsToJunit [arg1] [arg2]`).