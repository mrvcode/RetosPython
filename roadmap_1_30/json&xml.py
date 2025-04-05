import os
import xml.etree.ElementTree as xml
import json


data = {
    "name": "Miguel Rubio",
    "edad": 46,
    "birthdate": "27/04/1978",
    "languages": ["python", "c++", "c#"],
}

xml_file = "miguelrubio.xml"
json_file = "miguelrubio.json"

# XML


def create_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)


create_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)


# JSON


def create_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)


create_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)

"""
Extra
"""
create_xml()
create_json()
