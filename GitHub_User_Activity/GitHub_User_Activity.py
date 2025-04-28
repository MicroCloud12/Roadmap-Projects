''''
import sys
import json
import urllib.request as request


if len(sys.argv) < 2:
    print("Introduce un Usuario valido")
    sys.exit(1)
username = sys.argv[1]
print(f"Obteniendo actividad para el usuario: {username}") # Mensaje de prueba


URL = f"https://api.github.com/users/{username}/events"
print(f"URL de la API a consultar: {URL}") # Mensaje de prueba
req = request.Request(URL)
response = request.urlopen(req)
status_code = response.getcode()

if status_code == 200:
    print(f"Código de estado: {status_code}") # Para probar
    raw_data_bytes = response.read()
    data_decode = raw_data_bytes.decode('utf-8')
    activity_data = json.loads(data_decode)
    
    for data in activity_data:
        #print(data)
        if data['type'] == 'PushEvent':
            nombre_repo = data['repo']['name']
            lista_de_commits = data['payload']['commits']
            numero_commits = len(lista_de_commits)
            print(f"- Pushed {numero_commits} commits to {nombre_repo}")
        elif data['type'] == 'IssuesEvent':
            nombre_repo = data['repo']['name']
            action = data['payload']['action']
            if action == 'opened':
                print(f"- Opened a new issue in {nombre_repo}")
else:
    print(f"No se conecto correctamente, código de error: {status_code}")
    sys.exit(1)
'''
import sys
import json
import urllib.request
import urllib.error # Necesitamos importar esto para manejar errores HTTP específicos

# --- Constantes (Buena práctica ponerlas al inicio) ---
BASE_API_URL = "https://api.github.com/users/"
# Un User-Agent genérico o uno personalizado para tu app
USER_AGENT = 'MiScriptDeActividadGitHub/1.0'

def fetch_github_activity(username):
    """
    Obtiene los eventos de actividad pública de un usuario de GitHub.

    Args:
        username (str): El nombre de usuario de GitHub.

    Returns:
        str: Un string con el JSON de los eventos si la petición es exitosa.
        None: Si ocurre un error (ej: usuario no encontrado, error de red).
    """
    # 1. Construir la URL completa
    url = f"{BASE_API_URL}{username}/events"
    print(f"Consultando URL: {url}") # Mensaje útil para depuración

    # 2. Preparar la petición con la cabecera User-Agent
    headers = {'User-Agent': USER_AGENT}
    req = urllib.request.Request(url, headers=headers)

    # 3. Intentar hacer la petición y manejar posibles errores
    try:
        # Abrir la URL (enviar petición y obtener respuesta)
        with urllib.request.urlopen(req) as response:
            # Verificar si el estado es OK (urlopen maneja redirecciones,
            # pero lanzará HTTPError para errores como 404, 500)
            # No es estrictamente necesario verificar response.status == 200 aquí
            # si capturamos HTTPError, pero no hace daño si quieres ser explícito.

            # Leer los bytes crudos de la respuesta
            raw_data_bytes = response.read()

            # Decodificar los bytes a un string UTF-8
            data_string = raw_data_bytes.decode('utf-8')

            # Devolver el string con el JSON
            return data_string

    except urllib.error.HTTPError as e:
        # Error específico de HTTP (ej: 404 Not Found, 403 Forbidden)
        print(f"Error HTTP al consultar la API: {e.code} {e.reason}")
        if e.code == 404:
            print(f"  (Posiblemente el usuario '{username}' no existe)")
        return None # Indicar que hubo un error
    except urllib.error.URLError as e:
        # Otros errores de URL (ej: no se puede conectar al servidor)
        print(f"Error de URL al consultar la API: {e.reason}")
        return None # Indicar que hubo un error
    except Exception as e:
        # Capturar cualquier otro error inesperado
        print(f"Ocurrió un error inesperado: {e}")
        return None # Indicar que hubo un error

# --- Cómo usar la función en tu bloque principal ---

if __name__ == "__main__":
    # ... (tu código para obtener 'username' de sys.argv) ...
    if len(sys.argv) < 2:
        print("Error: Falta el nombre de usuario de GitHub.")
        print("Uso: python github_activity.py <username>")
        sys.exit(1)
    username = sys.argv[1]

    # Llamar a la nueva función
    json_string_data = fetch_github_activity(username)

    # Verificar si la función devolvió datos o None (error)
    if json_string_data is not None:
        # Si obtuvimos datos, ahora parseamos el JSON
        try:
            activity_data = json.loads(json_string_data)

            # Verificar si la lista de actividad está vacía
            if not activity_data:
                 print(f"No se encontró actividad pública reciente para '{username}'.")
            else:
                # Procesar y mostrar la actividad (tu bucle for con if/elif)
                print(f"\nActividad reciente de {username}:")
                for event in activity_data:
                    if event['type'] == 'PushEvent':
                        # ... tu lógica para PushEvent ...
                        repo_name = event['repo']['name']
                        # Manejo seguro de commits (puede no existir la clave)
                        commit_count = len(event.get('payload', {}).get('commits', []))
                        if commit_count > 0:
                             print(f"- Pushed {commit_count} commit(s) to {repo_name}")

                    elif event['type'] == 'IssuesEvent':
                        # ... tu lógica para IssuesEvent ...
                         repo_name = event['repo']['name']
                         action = event.get('payload', {}).get('action', 'N/A')
                         if action == 'opened':
                            print(f"- Opened a new issue in {repo_name}")
                        # Podrías añadir lógica para otras acciones si quieres

                    elif event['type'] == 'WatchEvent':
                        # ... lógica para WatchEvent (Starred) ...
                         repo_name = event['repo']['name']
                         print(f"- Starred {repo_name}")

                    # Puedes añadir más elif para otros event['type']

        except json.JSONDecodeError:
            print("Error: No se pudo procesar la respuesta de la API (formato JSON inválido).")
            sys.exit(1)
    else:
        # La función fetch_github_activity ya imprimió el error específico
        print("No se pudieron obtener los datos.")
        sys.exit(1)