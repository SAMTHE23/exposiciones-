import json

persona = {"nombre": "Ana", "edad": 20}

texto = json.dumps(persona)
print(texto, type(texto))

objeto = json.loads(texto)
print(objeto, type(objeto))