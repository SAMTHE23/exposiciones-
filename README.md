
Demo para el Taller de desarrollo de software.

- Python 3.10 o superior (verifica con `python --version`)

```
pip install -r requirements.txt
```


```
uvicorn main:app --reload
```
Luego abre en el navegador: http://127.0.0.1:8000/docs


1. **GET /carros** -> serialización (objeto Python a JSON)
2. **POST /carros** con este JSON -> deserialización:
```json
{ "marca": "Mazda", "modelo": "3", "precio": 25000 }
```
3. **POST /carros** con `"precio": -5000` -> error **422** (validación de Pydantic)
4. **GET /carros** otra vez -> aparece el carro nuevo


- **Modelo:** clase `Carro` (Pydantic)
- **Controlador:** clase `CarroControlador`
- **Vista:** rutas de FastAPI y JSON de respuesta
