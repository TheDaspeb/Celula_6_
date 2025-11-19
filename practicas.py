import json
import os
import csv
archivo = "estudiantes.json"
archivo_csv = "estudiantes.csv"


def cargar():
    if not os.path.exists(archivo):
        return []
    with open(archivo, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

estudiantes = cargar()

def guardar(estudiantes):
    with open(archivo, "w") as file:
        json.dump(estudiantes, file, indent=4)

def crear(estudiantes):
    nombre = input("Digita el nombre: ")
    edad = int(input("Digita la edad: "))
    estudiante = {
        "id": len(estudiantes),
        "estudiante": nombre,
        "edad": edad
    }
    estudiantes.append(estudiante)
    guardar(estudiantes)  

def view(estudiantes) : 
    for usuario in estudiantes :
        print(f"id: {usuario['id']} |Nombre: {usuario['estudiante']} |Edad: {usuario['edad']}") 
        
def actualizar_ids(estudiantes):
    for new_id, usuario in enumerate(estudiantes):
        usuario["id"] = new_id

def delete(estudiantes) : 
    search = int(input("Que estudiante vas a eliminar: ")) 
    for usuario in estudiantes : 
        if usuario['id'] == search : 
            estudiantes.remove(usuario) 
            actualizar_ids(estudiantes)
            guardar(estudiantes)

def actualizar(estudiantes) : 
    search = int(input("id del estudiante a actualizar: ")) 
    locate = False 
    for actualizar in estudiantes : 
        if search == actualizar['id'] : 
            locate = True
            cambio = int(input("1. cambiar nombre \n2. cambiar edad\nselecciona : ")) 
            if cambio == 1: 
                new_name = input("nuevo nombre del estudiante: ") 
                actualizar['estudiante'] = new_name
                guardar(estudiantes)
            elif cambio == 2: 
                new_edad = int(input("nueva edad del estudiante: "))
                actualizar['edad'] = new_edad
                guardar(estudiantes) 
    if locate == False : 
        print("id no encontrado")

def exportCsv(estudiantes, archivo_csv):
    if not estudiantes:
        print("lista vacia")
        return
    columnas = estudiantes[0].keys()
    with open(archivo_csv, "w", newline="", encoding="utf-8") as file:
        escritor = csv.DictWriter(file, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(estudiantes)
    print(f"\nEstudiantes exportados a '{archivo_csv}' correctamente.\n")

def menu() : 
    print("--------bienvenido---------")    
    
    check = True
    while check : 
        select = int(input("1. Crear estudiante \n2. actualizar estudiante \n3. eliminar estudiante \n4. mirar lista de estudiantes \n5. exportar a csv \n6. salir \nselecciona: ")) 
        if select == 1: 
            crear(estudiantes) 
        elif select == 2: 
            actualizar(estudiantes) 
        elif select == 3: 
            delete(estudiantes) 
        elif select == 4: 
            view(estudiantes) 
        elif select == 5: 
            exportCsv(estudiantes, archivo_csv) 
        elif select == 6: 
            break
        else :
            print("seleccion no valida")

menu()           


