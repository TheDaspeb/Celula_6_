import json
import os
import csv

ARCHIVO = "estudiantes.json"

# ---------------------------
# LEER DATOS
# ---------------------------
def leer_datos():
    if not os.path.exists(ARCHIVO):
        return []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

# ---------------------------
# GUARDAR DATOS
# ---------------------------
def guardar_datos(lista):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)


# ---------------------------
# CREAR ESTUDIANTE
# ---------------------------
def crear():
    estudiantes = leer_datos()

    nombre = input("Nombre del estudiante: ").strip()
    edad = input("Edad: ").strip()

    if not nombre:
        print(" El nombre no puede estar vacío.")
        return

    if not edad.isdigit():
        print(" La edad debe ser un número.")
        return

    nuevo_id = 1 if not estudiantes else estudiantes[-1]["id"] + 1

    nuevo = {
        "id": nuevo_id,
        "nombre": nombre,
        "edad": int(edad)
    }

    estudiantes.append(nuevo)
    guardar_datos(estudiantes)

    print(" Estudiante creado.")


# ---------------------------
# MOSTRAR ESTUDIANTES
# ---------------------------
def mostrar():
    estudiantes = leer_datos()

    if not estudiantes:
        print("\nNo hay estudiantes registrados.\n")
        return

    print("\n LISTA DE ESTUDIANTES:")
    for est in estudiantes:
        print(f"ID: {est['id']} | Nombre: {est['nombre']} | Edad: {est['edad']}")
    print()


# ---------------------------
# ACTUALIZAR ESTUDIANTE
# ---------------------------
def actualizar():
    estudiantes = leer_datos()

    if not estudiantes:
        print("No hay estudiantes para actualizar.")
        return

    mostrar()
    try:
        id_buscar = int(input("ID del estudiante a actualizar: "))
    except:
        print(" ID inválido.")
        return

    for est in estudiantes:
        if est["id"] == id_buscar:
            nuevo_nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
            nueva_edad = input("Nueva edad (deja vacío para no cambiar): ")

            if nuevo_nombre:
                est["nombre"] = nuevo_nombre
            
            if nueva_edad:
                if nueva_edad.isdigit():
                    est["edad"] = int(nueva_edad)
                else:
                    print(" Edad inválida.")

            guardar_datos(estudiantes)
            print(" Estudiante actualizado.")
            return

    print(" No existe un estudiante con ese ID.")


# ---------------------------
# ELIMINAR ESTUDIANTE
# ---------------------------
def eliminar():
    estudiantes = leer_datos()

    if not estudiantes:
        print("No hay estudiantes para eliminar.")
        return

    mostrar()
    try:
        id_buscar = int(input("ID del estudiante a eliminar: "))
    except:
        print(" ID inválido.")
        return

    nuevos = [est for est in estudiantes if est["id"] != id_buscar]

    if len(nuevos) == len(estudiantes):
        print(" No existe un estudiante con ese ID.")
        return

    guardar_datos(nuevos)
    print(" Estudiante eliminado.")

def Agregar_csv():
    with open('estudiantes.json', 'r') as listados_json:
        nombre =json.load(listados_json)

    nombre_grupo = nombre[0].keys()

    with open('datos.csv', "w", newline='', encoding='utf-8') as listado_csv:
        writer = csv.DictWriter(listado_csv, fieldnames=nombre_grupo)
        writer.writeheader()
        for i in nombre:
            writer.writerow(i)
        print('Estiduantes guardados')

# ---------------------------
# MENÚ PRINCIPAL
# ---------------------------
def menu():
    while True:
        print("""
=========================
 CRUD DE ESTUDIANTES
=========================
1. Ver estudiantes
2. Crear estudiante
3. Actualizar estudiante
4. Eliminar estudiante
5. Guardar CSV             
6. Salir
=========================
""")

        opcion = input("Opción: ")

        if opcion == "1":
            mostrar()
        elif opcion == "2":
           crear()
        elif opcion == "3":
            actualizar()
        elif opcion == "4":
            eliminar()
        elif opcion == "5":
            Agregar_csv()
        elif opcion == '6':
            print('👋 Saliendo...')
            break
        else:
            print(" Opción inválida.")


menu()
