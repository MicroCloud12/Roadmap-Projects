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

