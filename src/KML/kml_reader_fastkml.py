
'''

    Tentado utilizar a biblioteca fastkml, porém era suportado apenas a leitura
    nativa de Paradas, sem ler os trechos de Shapes do arquivo.

'''

from fastkml import kml

KML_FILE = '../../source/KML_points.kml'

def main():     
    with open(KML_FILE, 'r') as kmlFile:
        print('\n')

        doc = kmlFile.read()
        doc.replace('link href=""', 'link href="https://play.google.com/store/apps/details?id=com.ilyabogdanovich.geotracker"')

        k = kml.KML()
        k.from_string(doc.encode('utf-8'))
        
        print(len(list(k.features())))

        print('\n')

if __name__ == "__main__":
    main()