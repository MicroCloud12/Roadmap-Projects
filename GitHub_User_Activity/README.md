# GitHub Activity CLI

En este proyecto, construirás una interfaz de línea de comandos (CLI) simple para obtener la actividad reciente de un usuario de GitHub y mostrarla en la terminal. Este proyecto te ayudará a practicar tus habilidades de programación, incluyendo el trabajo con APIs, el manejo de datos JSON y la construcción de una aplicación CLI sencilla.

## Requisitos

La aplicación debe ejecutarse desde la línea de comandos, aceptar el nombre de usuario de GitHub como argumento, obtener la actividad reciente del usuario utilizando la API de GitHub y mostrarla en la terminal. El usuario debe poder:

* Proporcionar el nombre de usuario de GitHub como argumento al ejecutar la CLI. El formato esperado es:
    ```bash
    github-activity <username>
    ```

* Obtener la actividad reciente del usuario de GitHub especificado utilizando la API de GitHub. Puedes usar el siguiente endpoint para obtener la actividad del usuario:
    ```
    # Endpoint general
    [https://api.github.com/users/](https://api.github.com/users/)<username>/events

    # Ejemplo
    [https://api.github.com/users/kamranahmedse/events](https://api.github.com/users/kamranahmedse/events)
    ```

* Mostrar la actividad obtenida en la terminal. El formato de salida debería ser similar a este:
    ```
    Output:
    - Pushed 3 commits to kamranahmedse/developer-roadmap
    - Opened a new issue in kamranahmedse/developer-roadmap
    - Starred kamranahmedse/developer-roadmap
    ...
    ```

* Manejar errores de forma adecuada, como nombres de usuario inválidos o fallos en la API.
* Utilizar un lenguaje de programación de tu elección para construir este proyecto.
* **No utilizar librerías o frameworks externos** para realizar la consulta a la API de GitHub (se deben usar las capacidades nativas del lenguaje para peticiones HTTP y manejo de JSON).

## Más Información sobre la API de GitHub

Puedes [aprender más sobre la API de GitHub aquí](https://roadmap.sh/projects/github-user-activity).