import xml.etree.ElementTree as ET
import re, json


fileName = input('Enter xml file name (exclude filename extension): ')

##tree = ET.parse(fileName+'.xml')
##root = tree.getroot()
##weather = {}
##for child in root:
##    weather[child.tag] = child.attrib

try:
        with open(fileName+'.xml') as p:
            txt = p.read()
except:
        fileName = input('File not found. Try again: ')
newtxt = txt.split("\n",1)[1];
newtxt = newtxt.rsplit("\n",1)[0];

singleLine_pattern = re.compile(r'<.+>[\w\d]+</.+>') #<country>GB</country>
complete_pattern = re.compile(r'<.+\s([\d\w]+="[\w\d\s\-\.:%\?\+\*]+")+\s/>') #complete dict
incomplete_pattern = re.compile(r'<.+[^/]>') #incomplete dict
end_pattern = re.compile(r'</.+>') #end tag </city>
all_pt = re.compile(r'<.+>')

weather = {}
inTag = False
majorKey = '' #everytime there is a new major key a new major value must be create
majorValue = {}
matches = all_pt.finditer(newtxt)
for match in matches:
        line = match.group(0)
        if incomplete_pattern.match(line):
                if not end_pattern.match(line):
                        if singleLine_pattern.match(line): #complete dict in single line
                                subdict = re.match(r'<(?P<key>[\w\d]+)>(?P<value>[\w\d]+)</.+>', line)
                                subkey = subdict.group('key')
                                subvalue = subdict.group('value')
                                if inTag:
                                        majorValue[str(subkey)] = subvalue.strip('"')
                                else:
                                        weather[str(subkey)] = subvalue
                        elif '/' not in line:
                                if '=' in line: #incomplete dict
                                        majorKey = re.match(r'<[\w\d]+\s', line).group(0).strip('<>')
                                        inTag = True
                                        majorValue = {}
                                        subdict_pattern = re.compile(r'[\d\w]+="[\w\d\s\-\.:%\?\+\*]+"')
                                        subdict_matches = subdict_pattern.finditer(line)
                                        for elem in subdict_matches:
                                                subdict = elem.group(0).split('=')
                                                subkey = subdict[0]
                                                subvalue = subdict[1]
                                                majorValue[str(subkey)] = subvalue.strip('"')
                                else: #tag     
                                        majorKey = line.strip('<>')
                                        inTag = True
                else: #end tag
                        weather[majorKey] = majorValue
                        majorValue = {}
                        inTag = False
        elif complete_pattern.match(line):
                value = {}
                key = re.match(r'<[\w\d]+\s', line).group(0).strip('<>')
                subdict_pattern = re.compile(r'[\d\w]+="[\w\d\s\-\.:%\?\+\*]+"')
                subdict_matches = subdict_pattern.finditer(line)
                for elem in subdict_matches:
                        subdict = elem.group(0).split('=')
                        subkey = subdict[0]
                        subvalue = subdict[1]
                        value[str(subkey)] = subvalue.strip('"')
                if inTag:
                        majorValue[key] = value
                else:
                        weather[str(key)] = value

fileName = fileName         
jsonName = fileName+'.json'
with open(jsonName, 'w') as json_file:
        json.dump(weather, json_file)

print('Converted Successfully')
