# Chat Colaborativo WebSocket

## Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Git

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/ivancidev/chat-collaborative
cd chat-collaborative
```

2. Crear y activar entorno virtual:

En Windows:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
.\venv\Scripts\activate

# Verificar que está activado (deberías ver (venv) al inicio de la línea de comandos)
```

En Linux/Mac:

```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Verificar que está activado (deberías ver (venv) al inicio de la línea de comandos)
```

3. Instalar todas las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Ejecución

1. Iniciar el servidor:

```bash
python src/server.py
```

El servidor WebSocket estará corriendo en `Servidor WebSocket corriendo en ws://localhost:12345`

2. Iniciar el cliente:

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

## Capturas de Pantalla

-Al abrir el cliente debe pedirte el nombre de usuario:

[![Captura-de-pantalla-2025-05-11-234900.png](https://i.postimg.cc/zDQYTzgS/Captura-de-pantalla-2025-05-11-234900.png)](https://postimg.cc/G9vfC1zH)

-Demostración de mensajes entre usuarios:

[![Captura-de-pantalla-2025-05-11-231937.png](https://i.postimg.cc/RZsFt54k/Captura-de-pantalla-2025-05-11-231937.png)](https://postimg.cc/sMWsFLBm)

## Notas

- Para desactivar el entorno virtual cuando termines, simplemente escribe `deactivate` en la terminal
- Si cierras la terminal, necesitarás activar el entorno virtual nuevamente usando los comandos del paso 2
