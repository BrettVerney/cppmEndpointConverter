import xml.etree.ElementTree as ET
from xml.dom import minidom
import argparse
import datetime

def prettify(elem):
    """
    Return a pretty-printed XML string for the Element.
    :param elem: XML Element to be pretty-printed
    :return: A string representing the pretty-printed XML
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def get_group_name(args):
    """
    Get the group name from command line arguments or prompt the user for input.
    :param args: Parsed command line arguments
    :return: A valid group name (32 characters or less)
    """
    group_name = args.groupname if args.groupname else input("Enter the ClearPass Group Name (32 characters max): ").strip()
    while len(group_name) > 32:
        print("Group name must be 32 characters or less.")
        group_name = input("Enter the ClearPass Group Name (32 characters max): ").strip()
    return group_name

def process_mac_addresses(input_file, output_file_base, group_name):
    """
    Process the MAC addresses from the input file and create an XML structure with a timestamp.
    :param input_file: Path to the file containing MAC addresses
    :param output_file_base: Base name for the output XML file
    :param group_name: The group name to be used as tagValue in EndpointTags
    """
    # Create the root XML structure
    root = ET.Element("TipsContents", xmlns="http://www.avendasys.com/tipsapiDefs/1.0")
    ET.SubElement(root, "TipsHeader", exportTime="Tue Dec 05 14:17:28 AEST 2023", version="6.9")
    endpoints = ET.SubElement(root, "Endpoints")
    tag_dicts = ET.SubElement(root, "TagDictionaries")
    ET.SubElement(tag_dicts, "TagDictionary", allowMultiple="false", mandatory="false", dataType="String", attributeName="Group Name", entityName="Endpoint")

    # Read and process each MAC address in the input file
    with open(input_file, 'r') as file:
        for line in file:
            mac = line.strip()
            if mac:  # Ignore empty lines and whitespace
                endpoint = ET.SubElement(endpoints, "Endpoint", macAddress=mac, status="Known")
                ET.SubElement(endpoint, "EndpointTags", tagName="Group Name", tagValue=group_name)

    # Generate a timestamped output filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    output_file = f"{output_file_base}-{timestamp}.xml"

    # Write the final XML structure to the output file
    with open(output_file, 'w') as file:
        file.write(prettify(root))

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Process MAC addresses and create a timestamped XML file for ClearPass.")
    parser.add_argument("-g", "--groupname", help="GroupName for EndpointTags (supports spaces, enclose in quotes)")
    args = parser.parse_args()

    # Get a valid group name (either from arguments or user input)
    group_name = get_group_name(args)

    # Process MAC addresses and create the XML file with a timestamp
    process_mac_addresses('maclist.txt', 'endpointImport', group_name)
