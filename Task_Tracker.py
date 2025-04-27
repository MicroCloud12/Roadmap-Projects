import json
import sys
import os
from datetime import datetime, UTC

JSON_FILE = "task_traker.json"

def load_task():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, 'r') as f:
            task = json.load(f)
            return task
    except(IOError, json.JSONDecodeError):
        # Manejar error si el archivo está corrupto o no se puede leer
        print("Error: No se pudo leer el archivo de tareas o está corrupto.")
        return [] # O podrías salir del script: sys.exit(1)
    
def save_tasks(task):
    try:
        with open(JSON_FILE, 'w') as f:
            json.dump(task, f, indent=4)
    except IOError:
        print("Error: No se pudo escribir en el archivo de tareas.")
        # Podrías querer salir aquí también si guardar falla

def update_tasks(tasks, id_a_actualizar, nueva_descripcion):
    for task in tasks:
        if task['id'] == id_a_actualizar:
            task['description'] = nueva_descripcion
            task['updatedAt'] = datetime.now(UTC).isoformat()
            return True
    return False

def update_task_status(tasks, nuevo_status):
    for task in tasks:
        if task['id'] == id_a_actualizar:
            task['status'] = nuevo_status
            return True
    return False

if __name__ == "__main__":
    tasks = load_task()

    if len(sys.argv) < 2:
        print("Uso: python task_cli.py <comando> [argumentos...]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Falta la descripción de la tarea.")
            print("Uso: python task_cli.py add \"<descripción de la tarea>\"")
            sys.exit(1) # Salir del script indicando un error

        # Si llegamos aquí, sabemos que sys.argv[2] existe
        description = sys.argv[2]
        print(f"Descripción recibida: {description}") # Solo para probar por ahora

        initial_status = "Pentiente"
        print(f"Estado Inicial Establecido a: {initial_status}")
        
        createdat = datetime.now(UTC).isoformat()
        updateat = datetime.now(UTC).isoformat()

        print(f"Timestamp generado: {createdat}, {updateat}")

        if not tasks:
            new_id = 1
        else:
            max_id = 0
            for task in tasks:
                if task['id'] > max_id:
                    max_id = task['id']
            new_id = max_id + 1

        print(f"Nuevo ID Generado: {new_id}")

            # 1. Crear el diccionario para la nueva tarea
        new_task = {
            "id": new_id,
            "description": description,
            "status": initial_status, # Que era "todo"
            "createdAt": createdat,
            "updatedAt": updateat
         }

        # 2. Añadir el nuevo diccionario a la lista existente en memoria
        tasks.append(new_task)

        # 3. Guardar la lista completa (actualizada) en el archivo JSON
        save_tasks(tasks)

        # Mensaje de éxito (como en el ejemplo del README.md)
        print(f"Task added successfully (ID: {new_id})")
        pass

    elif command == "list":
        if not tasks:
            print("No hay datos para mostrar")
        
        filter_status = None
        if len(args) > 0:
            filter_status = args[0].lower()
            valid_status = ["pendiente", "en progreso", "terminado"]
            if filter_status not in valid_status:
                print(f"Error: Estado de filtro inválido '{args[0]}'. pendiente, en progreso, terminado.")

        print("----------Lista de Tareas--------------")
        for task in tasks:
            if filter_status is None or task['status'] == filter_status:
                # Imprimir la tarea formateada
                print(f"ID: {task['id']} | Desc: {task['description']} | Status: {task['status']} | Created: {task.get('createdAt', 'N/A')} | Updated: {task.get('updatedAt', 'N/A')} |")
                print("-" * 39) # Separador
                found_tasks = True
            # Si se aplicó un filtro y no se encontró nada
            if filter_status is not None and not found_tasks:
                print(f"No se encontraron tareas con el estado '{filter_status}'.")
            # Si la lista no estaba vacía pero el filtro hizo que no se imprimiera nada.
            elif not found_tasks and tasks: # Evita doble mensaje si la lista estaba vacía inicialmente
                print("No hay tareas que coincidan con el filtro aplicado.")
                print(f"ID: {task['id']} - Status: {task['status']} - Desc: {task['description']}")
                pass 
    
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Faltan argumentos para actualizar.")
            print("Uso: python task_cli.py update <ID> \"<nueva descripción>\"")
            sys.exit(1) # Salir indicando error
        try:
            id_a_actualizar = int(sys.argv[2])
        except ValueError:
            print(f"El valor {sys.argv[2]}, no es un valor valido")

        nueva_descripcion = sys.argv[3]
        print(f"La Informacion a Cambiar es la siguiente: ID = {id_a_actualizar} | Descripcion = {nueva_descripcion}")

        success = update_tasks(tasks, id_a_actualizar, nueva_descripcion)
        print(f"Se encontro el registro asociado al ID {id_a_actualizar} y se modifico con la nueva descrpcion")
        pass

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Faltan argumentos para actualizar.")
            print("Uso: python task_cli.py update <ID> \"<nueva descripción>\"")
            sys.exit(1) # Salir indicando error
        try:
            id_a_actualizar = int(sys.argv[2])
        except ValueError:
            print(f"El valor {sys.argv[2]}, no es un valor valido")

        nuevo_status = "in-progress"
        success = update_task_status(tasks, id_a_actualizar, nuevo_status)

        if success == True:
            save_tasks(tasks)
            print(f"Tarea {id_a_actualizar} marcada como '{nuevo_status}'.")
        else:
            print(f"Error: No se encontró tarea con ID {id_a_actualizar}.")

    elif command == "mark-done":
        if len(sys.argv) < 5:
            print("Error: Faltan argumentos para actualizar.")
            print("Uso: python task_cli.py update <ID> \"<nueva descripción>\"")
            sys.exit(1) # Salir indicando error
    else:
        print(f"Error: Comando desconocido '{command}'")
        sys.exit(1)