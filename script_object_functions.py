import xml.etree.ElementTree as ET
import script_events as events

def test_objects(node, app_name):
    if node.attrib.get('text') == app_name:
        position = node.attrib.get('bounds').split(']')[0]
        position = position.replace("[", "").split(",")
        print("\nTestando...")
        events.tap_screen(app_name, position[0], position[1])
    else:
        for n in node.findall('node'):
            test_objects(n, app_name)

def get_objects(name_app):
    xml = ET.parse('window_dump.xml')
    root = xml.getroot()
    app = test_objects(root, name_app)

def test_objects1(node, app_name):
    if node.attrib.get('content-desc') == app_name:
        position = node.attrib.get('bounds').split(']')[0]
        position = position.replace("[", "").split(",")
        print("\nTestando...")
        events.tap_screen(app_name, position[0], position[1])
    else:
        for n in node.findall('node'):
            test_objects1(n, app_name)

def get_objects1(name_app):
    xml = ET.parse('window_dump.xml')
    root = xml.getroot()
    app = test_objects1(root, name_app)