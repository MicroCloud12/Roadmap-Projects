# Task Tracker CLI

Task Tracker es un proyecto para rastrear y gestionar tus tareas. Construirás una interfaz de línea de comandos (CLI) simple para llevar un registro de lo que necesitas hacer, lo que has hecho y en lo que estás trabajando actualmente. Este proyecto te ayudará a practicar tus habilidades de programación, incluyendo el trabajo con el sistema de archivos, el manejo de entradas de usuario y la construcción de una aplicación CLI sencilla.

* URL = https://roadmap.sh/projects/task-tracker

## Requisitos

La aplicación debe ejecutarse desde la línea de comandos, aceptar acciones y entradas del usuario como argumentos, y almacenar las tareas en un archivo JSON. El usuario debe poder:

* Añadir, actualizar y eliminar tareas.
* Marcar una tarea como "en progreso" o "hecha".
* Listar todas las tareas.
* Listar todas las tareas que están hechas (`done`).
* Listar todas las tareas que no están hechas (`todo`).
* Listar todas las tareas que están en progreso (`in-progress`).

## Restricciones

Estas son algunas restricciones para guiar la implementación:

* Puedes usar cualquier lenguaje de programación para construir este proyecto.
* Usa argumentos posicionales en la línea de comandos para aceptar las entradas del usuario.
* Usa un archivo JSON llamado `tasks.json` (o similar) para almacenar las tareas en el directorio actual.
* El archivo JSON debe crearse si no existe.
* Usa el módulo nativo del sistema de archivos de tu lenguaje de programación para interactuar con el archivo JSON.
* **No uses librerías o frameworks externos** para construir este proyecto.
* Asegúrate de manejar errores y casos excepcionales de manera adecuada.

## Ejemplos de Uso

La lista de comandos y su uso se muestra a continuación (asumiendo que el ejecutable se llama `task-cli`):

```bash
# Añadir una nueva tarea
task-cli add "Comprar víveres"
# Salida esperada: Task added successfully (ID: 1)

# Actualizar una tarea existente (por ID)
task-cli update 1 "Comprar víveres y preparar la cena"
# Salida esperada: Task 1 updated successfully

# Eliminar una tarea (por ID)
task-cli delete 1
# Salida esperada: Task 1 deleted successfully

# Marcar una tarea como "en progreso" (por ID)
task-cli mark-in-progress 1
# Salida esperada: Task 1 marked as in-progress

# Marcar una tarea como "hecha" (por ID)
task-cli mark-done 1
# Salida esperada: Task 1 marked as done

# Listar todas las tareas
task-cli list

# Listar tareas por estado
task-cli list done
task-cli list todo
task-cli list in-progress

