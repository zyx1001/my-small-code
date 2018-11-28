# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as et
import os
xml_dir='G:\\biaoji\\1-300'
xmls=os.listdir(xml_dir)
path=os.path.join(xml_dir,xmls[1])
tree=et.parse(path)
root=tree.getroot()
file_path=root.findall('path')[0].text
objects=root.findall('object')
label=[]
for object in objects:
    if object.findall('name')[0].text=='plate':
        x1 = object.findall('bndbox')[0].findall('xmin')[0].text
        y1 = object.findall('bndbox')[0].findall('ymin')[0].text
        x2 = object.findall('bndbox')[0].findall('xmax')[0].text
        y2 = object.findall('bndbox')[0].findall('ymax')[0].text
        label.append([int(x1),int(y1),int(x2),int(y2)])
print(label)

