import xml.etree.ElementTree as tree

planets_tree = tree.parse('planets.xml')
root=planets_tree.getroot()
print root.attrib
