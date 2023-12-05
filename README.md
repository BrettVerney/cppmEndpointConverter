A script to convert MAC address lists to an Aruba ClearPass readable XML file

mac2xml.py

Author: Brett Verney
Version: v0.1 | 5-12-2023

# ClearPass Endpoint Converter

A Python script for converting newline-separated MAC address lists into ClearPass compatible XML files.

## Background

The ClearPass Endpoint Converter script is designed to ease the complexities associated with managing MAC endpoint imports in ClearPass, especially during bulk operations. While ClearPass is a powerful tool, its interface sometimes requires XML file formats. 

This script converts a simple text file of MAC addresses into an XML format, thus addressing the manual and error-prone process of XML file creation. It is tailored for operators who prefer the simplicity of text files, ensuring both accuracy and efficiency in the conversion process.

At this point in time, I only require the "Group Name" attribute to assign to endpoints so I can indentify these devices in policy and exclude them from certain functions.

## Usage

### With Command Line Argument

Run the script with the `-g` option followed by the group name.

```python mac2xml.py -g "Group Name"```


### Without Command Line Argument

If the script is run without any arguments, it will prompt the user to enter the ClearPass Group Name. The name should be 32 characters or less.


## Usage

### Running with Command Line Argument

```python mac2xml.py -g "group-name"```

### Running without Command Line Argument

The script will prompt for the Group Name.

## Example

e.g. ```python mac2xml.py -g "barcode-scanners"```

produces an XML file:

```<?xml version="1.0" ?>
<TipsContents xmlns="http://www.avendasys.com/tipsapiDefs/1.0">
  <TipsHeader exportTime="Tue Dec 05 14:17:28 AEST 2023" version="6.9"/>
  <Endpoints>
    <Endpoint macAddress="aabbccddeeff" status="Known">
      <EndpointTags tagName="Group Name" tagValue="barcode-scanners"/>
    </Endpoint>
    <Endpoint macAddress="ffeeddccbbaa" status="Known">
      <EndpointTags tagName="Group Name" tagValue="barcode-scanners"/>
    </Endpoint>
    <Endpoint macAddress="a1b2c3d4e5f6" status="Known">
      <EndpointTags tagName="Group Name" tagValue="barcode-scanners"/>
    </Endpoint>
  </Endpoints>
  <TagDictionaries>
    <TagDictionary allowMultiple="false" mandatory="false" dataType="String" attributeName="Group Name" entityName="Endpoint"/>
  </TagDictionaries>
</TipsContents>```