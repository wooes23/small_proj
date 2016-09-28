import xmltodict

with open("MEDLINE sample.xml") as xml:
    xml = xmltodict.parse(xml.read())

first = xml["MedlineCitationSet"]["MedlineCitation"][0]
for i in first:
    print i
