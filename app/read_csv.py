import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile,delimiter=",")
        header = next(reader) #con el next obtengo la primera linea/fila del archivo, los encabezados
        data = []

        for row in reader: #recorro cada celda del archivo
            iterable = zip(header,row) #asigno el valor de cada celda con el encabezado correspondiente
            country_dict = {key:value for key,value  in iterable} #Convierto las listas de iterables a diccionario
            data.append(country_dict)
        return data

if __name__ == "__main__":
    data=read_csv("world_population.csv")
    print(data)