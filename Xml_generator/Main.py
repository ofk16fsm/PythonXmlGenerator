from Choice import Choice
from Xml_generator import XmlGenerator

class Main:
    def __init__(self):
        self.root = None
        self.child = None

    @classmethod
    def show_menu(cls):
        menu = ["Lägg till ett rotelement", "Lägg till ett barn element", "Lägg till ett underbarnelement", "Ta bort ett underbarnelement", "Läsa alla underbarnelement", "Skapa XML", "Skapa XMl från sträng", "Validera XML", "Avsluta programmet"]
        for num, choice in enumerate(menu, 1):
            print("{}. {}".format(num, choice))
        print()

    @staticmethod
    def main():
        filename = "products.xml"
        text_products = input("Kopiera ditt XML och klistra in för att skapa XML från sträng\n"+ 
        "Eller tryck på enter för att gå vidare\n") or "<products><product><id>102012</id><name>Gudfadern</name><price>99</price><type>DVD</type><playtime>152</playtime></product></products>"

        # Exempel för XML från sträng 
        # Eller man kan använda det här som hårdkodat.
        #<products><product><id>102012</id><name>Gudfadern</name><price>99</price><type>DVD</type><playtime>152</playtime></product></products>
        
        x = XmlGenerator(filename)
        try:
            while True:
                Main.show_menu()
                userChoice = int(input("Välj ett alternativ:\n"))
                print()
                if userChoice == Choice["ADD_ROOT"].value:
                    rootInput = input("Välj tag för rot element\n")
                    x.createRoot(rootInput)
                    print()
                elif userChoice == Choice["ADD_CHILD"].value:
                    childInput = input("Välj tag för barn element\n")
                    x.createChild(childInput)
                    print()
                elif userChoice == Choice["ADD_SUBCHILD"].value:
                    print("Använd mellanslag mellan tag och text för tag\n")
                    subChildInput = input("Välj tag för underbarn element och text för elementet\n")
                    subChildTextInput = input("Välj text för elementet\n")
                    x.createSubChild(subChildInput, subChildTextInput)
                    print()
                elif userChoice == Choice["DEL_SUBCHILD"].value:
                    x.deleteSubChild(0,0,0)
                    print()
                elif userChoice == Choice["READ_ELEMENT"].value:
                    x.readElements()
                    print()
                elif userChoice == Choice["CREATE_XML"].value:
                    x.createXml(filename)
                    print()
                elif userChoice == Choice["XML_FROM_STR"].value:
                    x.createXmlFromString(text_products)
                    print()
                elif userChoice == Choice["VALIDATE"].value:
                    x.validateXml()
                    print()
                elif userChoice == Choice["QUIT_APP"].value:
                    break
        except ValueError:
            print("Du borde använda en siffra\n")

Main.main()
