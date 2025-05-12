# Chat Colaborativo WebSocket

## Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Git

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/ivancidev/chat-collaborative
cd chat-colaborativo-websocket-python
```

2. Crear y activar entorno virtual:

En Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

En Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar todas las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Ejecución

1. Asegúrate de que el entorno virtual esté activado (verás `(venv)` al inicio de tu línea de comandos)

2. Iniciar el servidor:

```bash
python src/server.py
```

El servidor WebSocket estará corriendo en `Servidor WebSocket corriendo en ws://localhost:12345`

3. Iniciar el cliente:

Hay varias formas de abrir el cliente HTML:

a) Usando Python (servidor HTTP simple):

```bash
python -m http.server 8000
```

Luego abre en tu navegador: `http://localhost:8000/src/client.html`

b) Usando Live Server en VS Code:

- Instala la extensión "Live Server"
- Click derecho en `src/client.html`
- Selecciona "Open with Live Server"

c) Abriendo directamente el archivo:

- Navega a la carpeta `src`
- Haz doble clic en `client.html` para abrirlo en tu navegador predeterminado

## Captura de Pantalla

[![Captura-de-pantalla-2025-05-11-231937.png](https://i.postimg.cc/RZsFt54k/Captura-de-pantalla-2025-05-11-231937.png)](https://postimg.cc/sMWsFLBm)

## Notas

- Para desactivar el entorno virtual cuando termines, simplemente escribe `deactivate` en la terminal
- Si cierras la terminal, necesitarás activar el entorno virtual nuevamente usando los comandos del paso 2
