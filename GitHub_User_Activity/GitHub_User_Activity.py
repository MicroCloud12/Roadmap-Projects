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
    print("Datos crudos (bytes):", raw_data_bytes)
else:
    print(f"No se conecto correctamente, código de error: {status_code}")
    sys.exit(1)

