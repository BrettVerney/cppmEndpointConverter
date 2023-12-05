A script to convert MAC address lists to an Aruba CleaPass readible XML file

mac2xml.py

Author: Brett Verney
Version: v0.1 | 5-12-2023

# ClearPass MAC Address Converter

A Python script for converting newline-separated MAC address lists into ClearPass compatible XML files.

## Background

The ClearPass MAC Address Converter script is designed to ease the complexities associated with managing MAC addresses in ClearPass, especially during bulk operations. While ClearPass is a powerful tool, its interface can be require XML file formats. 

This script converts a simple text file of MAC addresses into an XML format, ideal for ClearPass import, thus addressing the manual and error-prone process of XML file creation. It is tailored for operators who prefer the simplicity of text files, ensuring both accuracy and efficiency in the conversion process.

At this point in time, I only require the "Group Name" attribute to assign to endpoints so I can indentify devices in policy and exclude them from certain functions.

## Usage

### With Command Line Argument

Run the script with the `-g` option followed by the group name.

```python mac2xml.py -g "Group Name"```


### Without Command Line Argument

If the script is run without any arguments, it will prompt the user to enter the ClearPass Group Name. The name should be 32 characters or less.


## Usage

### Running with Command Line Argument

```python mac2xml.py -g "Guest-MAC-Bypass"```


### Running without Command Line Argument

The script will prompt for the Group Name.
