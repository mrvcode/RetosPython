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


class Data:

    def __init__(self, name, age, birthdate, languages):
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.languages = languages


with open(xml_file, "r") as xml_data:
    root = xml.fromstring(xml_data.read())

    name = root.find("name").text
    age = int(root.find("edad").text)
    birthdate = root.find("birthdate").text
    programming_languages = []
    for item in root.find("languages"):
        programming_languages.append(item.text)

    xml_class = Data(name, age, birthdate, programming_languages)
    print(xml_class.__dict__)

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"],
        json_dict["edad"],
        json_dict["birthdate"],
        json_dict["languages"],
    )
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)
