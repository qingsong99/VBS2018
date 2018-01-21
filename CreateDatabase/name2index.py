import xml.etree.ElementTree as ET
import pickle
root = ET.parse('metadata.xml').getroot()

dict = {}

for child in root:
    dict[child[1].text] = child[0].text

pickle.dump(dict, open('name2index.pickle', 'wb'))
