import csv

def write_target(data, target_file):
    '''
    Escrever em CSV os dados da Dict List. Como parâmetros, envia-se os dados e depois o caminho de destino.
    '''
    
    keys = data[0].keys()

    with open(target_file, 'w', newline='')  as output_file:

        dict_writer = csv.DictWriter(output_file, keys)
        
        dict_writer.writeheader()
        
        dict_writer.writerows(data)