import xml.etree.ElementTree as ET
import script_test_events as events

def test_app(node, app_name):
    if node.attrib.get('text') == app_name:
        position = node.attrib.get('bounds').split(']')[0]
        position = position.replace("[", "").split(",")
        print("Testando APP")
        events.tap_screen(app_name, position[0], position[1])
    else:
        for n in node.findall('node'):
            test_app(n, app_name)

def get_apps(name_app):
    xml = ET.parse('window_dump.xml')
    root = xml.getroot()
    app = test_app(root, name_app)