import sys
from xml.etree import cElementTree as et

def picklang(path, lang='en'):
    tr = et.parse(path)
    for element in tr.iter():
        for subelement in element:
            la = subelement.get('xmlns')
            if la is not None and la != lang:
                element.remove(subelement)
    return tr

if __name__ == '__main__':
    tr = picklang('fichierSimulation.xml')
    tr.write(sys.stdout)
    print
