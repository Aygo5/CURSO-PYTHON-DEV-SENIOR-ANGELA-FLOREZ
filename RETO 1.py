from datetime import datetime 
import statistics

class Experimentos:
    def __init__(self, nombreproyecto, fecharealizacion, categoria, resultadosexperimento):
        self.nombreproyecto= nombreproyecto
        self.fecharealizacion= fecharealizacion
        self.categoria= categoria
        self.resultadosexperimento= resultadosexperimento


def AgregarExperimento(listaexperimentos):
    nombreproyecto= input("Nombre del proyecto: ")
    fecharealizacion_str=input("Ingrese la fecha en que se realizo el experimento (DD/MM/YYYY): ")
    try:
        fecharealizacion= datetime.strptime(fecharealizacion_str, "%d/%m/%Y")
    except ValueError:
        print("La fecha no es valida")
        return
    cat=0
    while True:  
        cat=int(input("Seleccione la categoria con el número indicado: 1. Química 2. Biologia 3. Fisica: "))               
        if cat==3:
            categoria="Física"
            break
                
        elif cat==2:
            categoria="Biología"
            break
            
        elif cat==1:
            categoria= "Química"  
            break
        else:
            print("Categoria no válida") 
    resultadosexperimento= input("Registre los resultados obtenidos durante el experimento, separe cada uno usando comas, si es un decimal, use punto para diferenciarlos, ej: 5, 6, 7.5, 8=  ")
    try:
        resultadosexperimento= list(map(float,resultadosexperimento.split(",")))
    except ValueError:
        print("La fecha no es valida")
        return    
    experimentos= Experimentos(nombreproyecto, fecharealizacion, categoria, resultadosexperimento)
    listaexperimentos.append(experimentos)
    print("Su experimento ha sido agregado con exito")

def VisualizarRegistros(listaexperimentos):
    if not listaexperimentos:
        print("Aun no se ha registrado ningun experimento")
        return
    for i, experimentos in enumerate(listaexperimentos,start=1):
        print(f"\nExperimento {i}")
        print(f"Nombre del experimento= {experimentos.nombreproyecto}")
        print(f"Fecha en la que se realizó el proyecto= {experimentos.fecharealizacion.strftime('%d/%m/%Y')}")
        print(f"Categoria del experimento= {experimentos.categoria}")
        print(f"Resultados del experimento= {experimentos.resultadosexperimento}")

def analisisresultados(listaexperimentos):
    if not listaexperimentos:
        print("Aun no se ha registrado ningun experimento")
        return
    for experimentos in listaexperimentos:
        promedio= statistics.mean(experimentos.resultadosexperimento)
        maximo= max(experimentos.resultadosexperimento)
        minimo= min(experimentos.resultadosexperimento)
        print(f"\nAnálisis de los resultados del experimento {experimentos.nombreproyecto}")
        print(f"\n*Promedio= {promedio}")
        print(f"\n*Resultado máximo= {maximo}")
        print(f"\n*Resultado mínimo= {minimo}")

def generarinforme(listaexperimentos):
    if not listaexperimentos:
        print("Aun no se ha registrado ningun experimento")
        return   
    with open("Informe de experimentos.txt","w") as archivo:
        for experimentos in listaexperimentos:
            archivo.write(f"Nombre:{experimentos.nombreproyecto}\n")
            archivo.write(f"Fecha en la que se realizó el experimento:{experimentos.fecharealizacion.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Categoria del experimento:{experimentos.categoria}\n")
            archivo.write(f"Resultados:{experimentos.resultadosexperimento}\n")
            archivo.write("\n")
    print("El informe se ha generado con exito como 'Informe de experimentos.txt' ")
def eliminar_experimento(listaexperimentos):
    if not listaexperimentos:
        print("Aun no se ha registrado ningun experimento")
        return
    while True:
        print("\n1.Eliminar todos los experimentos")
        print("2.Eliminar un experimento")
        print("3.Cancelar")
        sele=int(input("Seleccione una opción: "))
        if sele==1:
            print("ADVERTENCIA: TODOS LOS EXPERIMENTOS REGISTRADOS SERAN ELIMINADOS \n1.Confirmar\n2.Cancelar")
            while True:
                sel2=int(input("Seleccione una opción: "))
                if sel2==1:
                    listaexperimentos.clear()
                    print("SE HA ELIMINADO EL REGISTRO DE EXPERIMENTOS")
                    return listaexperimentos
                elif sel2==2:
                    print("\nNo se ha eliminado nigún experimento")
                    return listaexperimentos
                else:
                    print("Opción no válida")
        
        elif sele==2:
            VisualizarRegistros(listaexperimentos)
            while True:
                sel3=int(input("\nSeleccione el experimento que desea eliminar: \nEliminar experimento #"))
                if (sel3-1)<len(listaexperimentos):
                    print(f"Se eliminara el experimento {sel3}, esta acción no es reversible. \n1.Confirmar\n2.Cancelar")
                    while True:
                        sel4=int(input("Seleccione una opción: "))
                        if sel4==1:
                            listaexperimentos.pop(sel3-1)
                            print(f"Se ha eliminado exitosamente el experimento #{sel3}\n")
                            return listaexperimentos
                        elif sel4==2:
                            print("\nNo se ha eliminado nigún experimento")
                            return listaexperimentos
                        else:
                            print("No existe este experimento, intente nuevamente")     
        elif sele==3:
            print("\nNo se ha eliminado nigún experimento")
            return listaexperimentos
        else:
            print("Opción no válida, intente nuevamente")
def Menu():
    listaexperimentos= []
    while True:
        print("\nMENÚ DE OPCIONES:")
        print("1. Agregar experimento ")
        print("2. Visualizar experimentos ")
        print("3. Eliminar experimentos ")
        print("4. Análisis de resultados del experimento ")
        print("5. Generar informe ")      
        print("6. Salir del programa")
        
        sel=int(input("Seleccione una opción: "))
        if sel==1:
            AgregarExperimento(listaexperimentos)
        elif sel==2:
            VisualizarRegistros(listaexperimentos)
        elif sel==3:
            listaexperimentos= eliminar_experimento(listaexperimentos)
        elif sel==4:
            analisisresultados(listaexperimentos)
        elif sel==5:
            generarinforme(listaexperimentos)
        elif sel==6:
            print("Finalizando el programa, muchas gracias por usarlo, esperamos vuelva pronto...")
            break
        else:
            print("Opción no válida, intente nuevamente")
            
if __name__=="__main__":
    Menu()





