
'''

    Tentado utilizar a biblioteca geopandas, porém era suportado apenas a leitura
    nativa de Paradas, sem ler os trechos de Shapes do arquivo.

'''

import geopandas as gpd
import fiona

KML_FILE = 'KML.kml'

def main():     
    gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

    stops = gpd.read_file(KML_FILE, driver='KML')

    print(stops.head)
    print('\n')
    print(stops.shape)

    # Apenas lista os pontos, mas não as shapes

if __name__ == "__main__":
    main()
