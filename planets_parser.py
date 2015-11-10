import xml.etree.ElementTree as tree
print "Source"
planets_tree = tree.parse('planets.xml')
root=planets_tree.getroot()
print root.attrib['name']

print "list of planets"
for child in root:
     print "tag=",child.tag, " attrib=", child.attrib['name']

print "list of moons"
for element  in planets_tree.iter(tag='moon'):
    print element.attrib
