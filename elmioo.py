import json
import csv
import os

ARCHIVO = "estudiantes.json"
ARCHIVO_CSV = "estudiantes.csv"

# Leer datos
def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return []
    
    with open(ARCHIVO, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


# Función para guardar datos
def guardar_datos(estudiantes):
    with open(ARCHIVO, "w") as file:
        json.dump(estudiantes, file, indent=4)
    print("\nDatos guardados\n")


# Función para crear estudiante
def crear_estudiante(estudiantes):
    print("\n--- Crear nuevo estudiante ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    estudiante = {
        "id": len(estudiantes) + 1,
        "nombre": nombre,
        "edad": edad,
    }

    estudiantes.append(estudiante)
    guardar_datos(estudiantes)
    print("Se agregó el estudiante\n")


# Función para ver los estudiantes guardados
def ver_estudiantes(estudiantes):
    print("\n--- Lista de estudiantes ---")
    if not estudiantes:
        print("No hay estudiantes.\n")
        return
    
    for e in estudiantes:
        print(f"ID: {e['id']} | Nombre: {e['nombre']} | Edad: {e['edad']}")
    print()


# Función para buscar los estudiantes por ID
def buscar_por_id(estudiantes, id_buscar):
    for e in estudiantes:
        if e["id"] == id_buscar:
            return e
    return None


# Función para actualizar
def actualizar_estudiante(estudiantes):
    print("\n--- Actualizar estudiante ---")
    id_buscar = int(input("ID del estudiante: "))
    
    estudiante = buscar_por_id(estudiantes, id_buscar)
    if not estudiante:
        print("Estudiante no encontrado.\n")
        return

    print(f"Editando a: {estudiante['nombre']}")
    estudiante["nombre"] = input("Nuevo nombre: ") or estudiante["nombre"]
    estudiante["edad"] = int(input("Nueva edad: ") or estudiante["edad"])

    guardar_datos(estudiantes)
    print("Estudiante actualizado.\n")


# Función para eliminar estudiantes
def eliminar_estudiante(estudiantes):
    print("\n--- Eliminar estudiante ---")
    id_buscar = int(input("ID del estudiante a eliminar: "))

    estudiante = buscar_por_id(estudiantes, id_buscar)
    if not estudiante:
        print("Estudiante no encontrado.\n")
        return
    
    estudiantes.remove(estudiante)
    guardar_datos(estudiantes)
    print(f"El estudiante {estudiante ["nombre"]} con ID {id_buscar} fué eliminado")


# Función parar exportar json a CSV
def exportar_a_csv(estudiantes):
    if not estudiantes:
        print("No hay estudiantes para exportar.\n")
        return

    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as file:
        columnas = estudiantes[0].keys()
        escritor = csv.DictWriter(file, fieldnames=columnas)

        escritor.writeheader()
        escritor.writerows(estudiantes)

    print(f"\n Estudiantes exportados a '{ARCHIVO_CSV}' correctamente.\n")


# Menú
def menu():
    estudiantes = cargar_datos()

    while True:
        print("""
---------- CRUD Estudiantes (JSON Converti a CSV) ----------
1. Crear estudiante
2. Ver estudiantes
3. Actualizar estudiante
4. Eliminar estudiante
5. Exportar a CSV
6. Salir
""")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_estudiante(estudiantes)
        elif opcion == "2":
            ver_estudiantes(estudiantes)
        elif opcion == "3":
            actualizar_estudiante(estudiantes)
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
        elif opcion == "5":
            exportar_a_csv(estudiantes)
        elif opcion == "6":
            print("-------FIN DEL PROGRAMA-------")
            break
        else:
            print("Opción inválida.\n")

menu()