# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:42:03 2021

Práctica final Fundamentos de Proframación
Consta de un menú en el que dependiendo de la opción que eligas se te otorga
cierta información sobre la población española.

@author: Pablo Gascó LLopis y HUgo Toledo Escrivá
Versión 2.0

Fichero que se pide al usuario: PrFinal_c.EvolMun2011.csv
"""

import matplotlib.pyplot as plt

FICHERO = 'PrFinal_c.ListMun2012.csv'


class InfoMunicipio:
    def __init__(self):
        self.ine = str()
        self.municipio = str()
        self.superficie = float()
        self.capitalidad = str()
        self.ano = str()
        self.ubi = Ubicacion()
        
class Ubicacion:
    def __init__(self):
        self.ca = list()
        self.pv = list()
        self.pj = list()

class InfoHabitantes:
    def __init__(self):
        self.ine = str()
        self.municipio = str()
        self.habitantes = list()
        
        
        
def LeerFichero2(FICHERO)->(list):
    '''
    Parameters
    -------
    FICHERO: str
    
    Returns
    -------
    lista de todos los datos del excel.
        
    Explicación
    -------
    Esta función lee todo el ficheropara devolvernos una lista organizada de 
    todos los municipios.
    '''
    try:
        f = open(FICHERO, encoding='UTF-8')
    except:
        print("Error a la hora de abrir el fichero")
        ok = False
    else:
        ok = True
        #Guardamos la información
        Info = []
        f.readline()
        linea = f.readline()
        while linea != "\n":
            Municipio = InfoMunicipio()
            linea = linea.split(";")
            Municipio.ine = linea[0]
            Municipio.municipio = linea[1]
            linea[2].replace(",",".")
            Municipio.superficie = linea[2]
            Municipio.capitalidad = linea[3]
            Municipio.ano = linea[4]
            Municipio.ubi.ca = linea[5:7]
            Municipio.ubi.pv = linea[7:9]
            Municipio.ubi.pj = linea[9:11]
            Info.append(Municipio)
            linea = f.readline()
        f.close()
        return Info, ok



def LeerLineas(FICHERO_EVOLMUN) -> (list):
    '''
    Parameters
    -------
    FICHERO_EVOLMUN (constante): str
    
    Returns
    -------
    lista de todos los datos del excel.
        
    Explicación
    -------
    Esta función lee todo el ficheropara devolvernos una lista organizada de 
    todos los municipios.
    '''
    try:
        f = open(FICHERO_EVOLMUN, encoding='UTF-8')
    except:
        ok = False
        
    else:
        ok = True
        #Creaamos la lista de años:
        linea = f.readline()
        linea = linea.split(";")
        linea2 = linea[2:len(linea)-1]
        lista_años = []
        for año in linea2:
            año = año.replace("p","")
            lista_años.append(año)
        lista_años[0] = lista_años[0].replace("\n","")
        #creamos la lista de registros:
        linea = f.readline()
        InfoHabitantes = []
        while linea != "":
            linea = linea.split(";")
            ine = linea[0]
            if len(ine) == 4:
                ine = "0" + ine
            municipio = linea[1]
            del linea[0]
            del linea[0]
            habitantes = linea[0:15]
            poblacion = GuardarInfoPoblacion(ine, municipio, habitantes)
            InfoHabitantes.append(poblacion)
            linea = f.readline()
        
        f.close()
        return InfoHabitantes, lista_años, ok
    
    
    
def GuardarInfoPoblacion(ine:str, municipio:str, 
                         habitantes:list) -> InfoHabitantes:
    '''
    Parameters
    -------
    ine(str), municipio(str), habitantes(lista)
    
    Returns
    -------
    Un registro de todos
        
    Explicación
    -------
    Almacena todos los datos de los parametros en los registros organizados.
    '''

    poblacion = InfoHabitantes()
    poblacion.ine = ine
    poblacion.municipio = municipio
    for i in range(0, len(habitantes)):
        poblacion.habitantes.append(int(habitantes[i]))
    
    return poblacion


    
def MayorMenorPoblación(InfoHabitantes:list, InfoMunicipio:list,
                        provincia: str, año: int, 
                        lista_años: list)->(str, str):
    
    '''
    Parameters
    -------
    InfoHabitantes(list), InfoMunicipio(list)
                        provincia(str), año(int), 
                        lista_años(list)
    
    Returns
    -------
    municipio_mayor(str), municipio_menor(str)
        
    Explicación
    -------
    La función compara todos los datos de una provincia y un año y devulve que
    municipio es el que tiene más habitantes y el que menos.
    '''
    
    mayor = 0
    menor = 999999999 #Año muy grande que no se pueda superar
    municipio_mayor = ""
    municipio_menor = ""
    
    
    for i in range (len(InfoHabitantes)): #Para determinar el num de provincia
        if provincia in InfoMunicipio[i].ubi.pv[1]:
            n_provincia = InfoMunicipio[i].ubi.pv[0]
    
    
    for i in range(len(lista_años)): #Para determinar el indice
        if lista_años[i] == str(año):
            año_p = i
            
    
    for i in range (len(InfoMunicipio)): #Para determinar el mayor municipio
        if n_provincia == InfoHabitantes[i].ine[0:2]:
            if (InfoHabitantes[i].habitantes[año_p]) > mayor:
                mayor = InfoHabitantes[i].habitantes[año_p]
                municipio_mayor = InfoHabitantes[i].municipio

    
    for i in range (len(InfoMunicipio)): #Para determinar el menor municipio
        if n_provincia == InfoHabitantes[i].ine[0:2]:
            if (InfoHabitantes[i].habitantes[año_p]) < menor:
                menor = InfoHabitantes[i].habitantes[año_p]
                municipio_menor = InfoHabitantes[i].municipio 
    
    return municipio_mayor, municipio_menor
        
        

def TotalPoblación(InfoHabitantes:list, InfoMunicipio:list, provincia:str,
                   año:int, lista_años:list)->int:
    '''
    Parameters
    -------
    poblaciones(list), info(list), 
    provincia(str), año(int), lista_años(list)
    
    Returns
    -------
    Total(int)
        
    Explicación
    -------
    Esta función compara todos los datos de una provincia y un año y calcula
    su población total para ese año,
    Devuelve los resultados obtenidos.
    '''
    for i in range(len(lista_años)): #Para determinar el indice
        if lista_años[i] == str(año):
            año_p = i
    
    total = 0 #Variable contadora
    
    #Usamos el número de provincia
    for i in range (len(InfoMunicipio)): #Para determinar el num de provincia
            if provincia in InfoMunicipio[i].ubi.pv[1]:
                n_provincia = InfoMunicipio[i].ubi.pv[0]
                
    for i in range (len(InfoMunicipio)): #Para determinar el total
            if n_provincia == InfoHabitantes[i].ine[0:2]:
                total += InfoHabitantes[i].habitantes[año_p]

    return total


    
def Representardensidades(densidades: list, años:list, 
                          pob: str):
    '''
    Parameters
    -------
    densidades(list), años(list), indices(int), pob(str)
    
    Returns
    -------
    None
        
    Explicación
    -------
    Esta función muestra en una gráfica generada la densidad de población a lo 
    largo del tiempo.
    '''
    #Primero necesitamos darle la vuelta a la lista de años:
    años = list(reversed(años))
    plt.plot(años, densidades, label="Densidad de población por años")
    plt.title("Densidad de población a lo alrgo del tiempo " + pob)
    plt.xlabel("Años")
    plt.ylabel("Densidad (hab/km2)")
    plt.legend(loc='best')
    
    plt.show()
    
    
        
def abrirfichero(cp: str, p: str)-> (bool, str):
    '''
    Parameters
    -------
    cp(str), p(str)
    
    Returns
    -------
    (ok)bool, fichero(str)
        
    Explicación
    -------
    Esta función elimina los espacios y los cambia por barra bajas.
    '''
    #Eliminamos los espacios del excel en el municipio si los hay
    #y agrgamos el "barra baja" para que así el nombre del fichero
    #no de error ya que no sirven todos los caracteres
    p = p.split(" ")
    if len(p) > 1:
        prov = ""
        for i in range (len(p)):
            prov += p[i] + "_"
    else: 
        if "/" in p[0]:
            prov = " "
            a = p[0].find("/")
            b = p[0]
            for i in range(0, a):
                    prov  += b[i]
            prov = prov + "_"
        else:
            prov = p[0] + "_"
    
    try:
        fichero = open(cp + "_" + prov + "2011.dat", 'w', encoding='UTF-8')
    except:
        ok = False
        print("Error")
    else:
        ok = True
            
    return ok, fichero



def Calcularsuperficie(municipio: str, Lista: list)-> (float, int):
    '''
    Parameters
    -------
    municipio(str), Lista(list)
    
    Returns
    -------
    superficie(float), indice(int)
        
    Explicación
    -------
    Esta función calcula la superficie de un municipio.
    '''
    for i in range(0, len(Lista)):
            if Lista[i].municipio == municipio:
                superficie = Lista[i].superficie.split(",")
                indice = i
        
    superficie = superficie[0] + "." + superficie[1] #Coma por punto
    superficie = float(superficie)
    
    return superficie, indice



def Crearlista(indice:int, poblaciones: list, superficie: float
                )->(list):
    '''
    Parameters
    -------
    indice(int), poblaciones(list), superficie(float)
    
    Returns
    -------
    lista_dens_mun(list), lista_años(list)
        
    Explicación
    -------
    Esta función crea una lista de densidades del municipio y de años.
    '''
    lista_dens_mun = []
    for i in range(0, len(poblaciones[indice].habitantes)):
        lista_dens_mun.append(poblaciones[indice].habitantes[i]/superficie)
        

    lista_dens_mun = list(reversed(lista_dens_mun)) #Le damos la vuelta
    
    return lista_dens_mun



def Pedirprovincia(Lista:list)->(str, str):
    '''
    Parameters
    -------
    Lista(list)
    
    Returns
    -------
    cp(str), prov(str)
        
    Explicación
    -------
    Esta función pide una provincia(no hace falta que esté escriita
                                    igual que en el excel pero si que
                                    tenga sentido)
    Después devuelve el verdadero nombre y el código de provincia
    '''
    p = input("Dime una provincia:")
    prov = 0
    while prov == 0:
        
        p = p.split(" ")
        #Si tiene más de una palabra nos quedamos con la más larga para luego
        #buscar en el excel
        if len(p) > 1:
            pr = p[0]
            for i in range (1, len(p)):
                if len(p[i]) > len(pr):
                    pr = p[i]
        else:
            pr = p[0]
            
        for i in range(0, len(Lista)):
            if pr in Lista[i].ubi.pv[1]:
                prov = Lista[i].ubi.pv[1]
                cp = Lista[i].ubi.pv[0]
                
        if prov == 0:
            print("la provincia no existe")
            p = input("Dime una provincia:")
    
    return cp, prov



def Escribirfichero(ine: str, incremento: int, densidad: float, 
                    superf: float, poblaciones: list, g: str, i:int):
    '''
    Parameters
    -------
    ine(str), incremento(int), densidad(float), 
    superf(float), poblaciones(list), g(str), i(int)
    
    Returns
    -------
    None
        
    Explicación
    -------
    Esta función escribe en el fichero todos los datos.
    '''
    g.write(ine + ":" + poblaciones[i].municipio + "\n")
    g.write("El incremento de población es: " + str(incremento) + " hab")
    g.write("\n" + "Densidad último año: " + str(densidad) + " hab/km^2" + "\n")
    g.write("Superficie: " + str(superf) + " km^2" + "\n")
    g.write("-"*20 + "\n")
    
    
    
def InfoProvincia(prov:str, g:str, Lista:list, poblaciones:list):
    '''
    Parameters
    -------
    prov(str), g(str), Lista(list), poblaciones(list)
    
    Returns
    -------
    None
        
    Explicación
    -------
    Esta función coge el indice para utilizarlo en otra función.
    '''
    for i in range(0, len(Lista)):
                
        if prov in Lista[i].ubi.pv[1]:
            ine = Lista[i].ine
            superficie = Lista[i].superficie.split(",")
            superficie = superficie[0] + "." + superficie[1]
            superf = float(superficie)
            x = poblaciones[i].habitantes
            densidad = (x[0]/superf)       
            incr = x[0] - x[len(x)-1]
            ind = i #Esta vez necesitamos guardar el indice para llevarlo a la
                    #siguiente función
            Escribirfichero(ine, incr, densidad, superf, poblaciones, g, ind)
            
 

def MostrarMenu():
    '''
    Parameters
    -------
    None
    
    Returns
    -------
    None
        
    Explicación
    -------
    Simplemente muestra el menú por pantalla.
    '''
    
    print("Elige una de las siguientes opciones:\n")
    print("1. Municipio de mayor y menor población(de una provincia y un año)")
    print("2. Total de población de una provincia en un determinado año")
    print("3. Gráfica evolución de la densidad de población de un municipio")
    print("4. Guardar en un fichero la siguiente información: el código INE,")
    print("la información del incremento total de habitantes ", end='')
    print("la densidad de población en el último año ", end='')
    print("y la superficie de los municipios de una provincia concreta")
    print("0. Salir")
    
def Menu()->(int):
    '''
    Parameters
    -------
    None
    
    Returns
    -------
    a(int)
        
    Explicación
    -------
    Esta función muestra las opciones que hay en un menú y hace elegir una al 
    usuario.
    '''
    a = 1000000000
    while 4 < a or a < 0:
        
        MostrarMenu()
    
        a = int(input("Cual es tu elección:"))
          
    return a       
        


def main():
    
    #Pedimos el nombre del fichero de habitantes al usuario
    FICHERO_EVOLMUN = input("Dime el nombre del fichero de habitantes: ")
    
    #lista de registros, de años y si se ha podido o no abrir el fichero
    InfoHabitantes, lista_años, ok = LeerLineas(FICHERO_EVOLMUN)
    
    if not ok:
        print("Error a la hora de abrir el fichero")
    
    #lista de registros del segundo fichero y si se ha podido o no abrir
    InfoMunicipio, ok = LeerFichero2(FICHERO)
    
    if not ok:
        print("Error a la hora de abrir el fichero")
    
    #mostramos al usuario el menú
    opc = Menu()
    
    if opc == 1:
        
        provincia = input("Dime una provincia:")
        año = int(input("Dime un año:"))
        m_mayor, m_menor = MayorMenorPoblación(InfoHabitantes,
                                                          InfoMunicipio,
                                                          provincia, año,
                                                          lista_años)
        
        print("El municipio con más habitantes de la provincia de", provincia,
          "en", año,"es", m_mayor,"y el municipio con menos "
          "habitantes es", m_menor)
                                                       
    elif opc == 2:
        provincia = input("Dime una provincia:")
        año = int(input("Dime un año:"))
        total = TotalPoblación(InfoHabitantes, InfoMunicipio, provincia,
                       año, lista_años)
        
        print("La población de la provincia de", provincia, "en", año,"era de",
          total, "habitantes")
        
    elif opc == 3:
        
        municipio = input("Dime el municipio:")
        #El indice es para saber en todo momento en que posición de la lista
        #está el municipio
        superficie, indice = Calcularsuperficie(municipio, InfoMunicipio)
        #Lista con la densidad de cada año
        lista_dens_mun = Crearlista(indice, InfoHabitantes, superficie)
        #Nombre del municipio
        mun = InfoHabitantes[indice].municipio
        #Representamos la información
        Representardensidades(lista_dens_mun, lista_años, mun)
        
        
    elif opc == 4:
        #Pedimos la provincia y obtenemos además su código
        cp, prov = Pedirprovincia(InfoMunicipio)
             
        #Utilizamos el codigo y la provincia para abrir el fichero
        ok, g = abrirfichero(cp, prov)
        
        if ok: #Sacamos la información de la provincia
            InfoProvincia(prov, g, InfoMunicipio, InfoHabitantes)
            print("se ha podido abrir el fichero y guardar la información")
        else:
            print("Error a la hora de abrir el fichero")
            print("No se ha podido guardar la información")
            
    elif opc == 0:
        print("Has salido del menú")
    
    
if __name__ == '__main__':
    main()
    
    

        
        
