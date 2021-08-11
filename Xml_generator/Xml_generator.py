from xml.etree import ElementTree as ET
from xml.dom import minidom
import lxml.etree as lxet
from xml.parsers.expat import ExpatError
from lxml.etree import XMLSchema

class XmlGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.xmlDoc = ET.parse(self.filename)
        self.root = None
        self.child = None
        self.subChild = None

    def createRoot(self, tagName):
        self.root = ET.Element(tagName)
        self.root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.root.set("xsi:noNamespaceSchemaLocation", "products.xsd")
    
    def createChild(self, tagName):
        self.child = ET.SubElement(self.root, tagName)

    def createSubChild(self, tagName, text):
        self.subChild = ET.SubElement(self.child, tagName)
        self.subChild.text = text

    def deleteSubChild(self, index, index1, index2):
        self.root = self.xmlDoc.getroot()
        self.root[index].remove(self.root[index1][index2])
        self.createXml(self.filename)
       
    def readElements(self):        
        self.root = self.xmlDoc.getroot()                
        for elem in self.root:
            for subelem in elem:
                print(f"{subelem.tag}: {subelem.text}")

    def createXml(self, filename):
        data = ET.tostring(self.root, encoding="utf-8")
        parsed = minidom.parseString(data)
        xmlFile = open(filename, "wb")
        xmlFile.write(parsed.toprettyxml(indent="\t", encoding="utf-8"))

    def createXmlFromString(self, text):
        data = ET.fromstring(text)
        newData = ET.tostring(data)
        parsed = minidom.parseString(newData)
        xmlFile = open("test.xml", "wb")
        xmlFile.write(parsed.toprettyxml(indent="\t", encoding="utf-8"))

    def validateXml(self):
        try:
            xmlFile = lxet.parse(self.filename)
            xmlSchema = XMLSchema(file="products.xsd")
            isValid = xmlSchema.validate(xmlFile.getroot())
            if(isValid == True):
                print("XML fil är giltig och", isValid)
            else:
                print("XML fil är ogiltig och", isValid)
            
        except ExpatError as ex:
            print(ex)

