import xml.etree.ElementTree as et

tree=et.parse('hosts.xml')
print(tree)
print(tree.getroot().tag)
print(tree.getroot().attrib)

#select tag by tag name
for host_tag in tree.getiterator('host'):
    host_config=[]
    host_config.extend([host_tag.get('hostname'), int(host_tag.get('port'))])

    for child_tag in host_tag:
        host_config.append(child_tag.text)
    print(host_config)

print()

for host_tag in tree.getroot()[0],tree.getroot()[-1]:
    host_config = []
    host_config.extend([host_tag.get('hostname'), int(host_tag.get('port'))])

    for child_tag in host_tag:
        host_config.append(child_tag.text)
    print(host_config)

