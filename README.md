# Proyecto Prueba Backend Iberpixel

## Requisitos

- Python 3.10+
- pip

## Instrucciones de Instalación

1. Clonar el repositorio:
  ```bash
  git clone https://github.com/villalobos-05/prueba-backend-iberpixel.git
  cd prueba-backend-iberpixel
  ```

2. Crear un entorno virtual:
  ```bash
  python -m venv .venv
  ```

3. Activar el entorno virtual:

  - En Windows:
    ```bash
    .\venv\Scripts\activate
    ```
  - En macOS o Linux:
    ```bash
    source venv/bin/activate
    ```

4. Instalar las dependencias:
  ```bash
  pip install -r requirements.txt
  ```

## Cómo Ejectuar el Proyecto

1. Activar el entorno virtual (si no se ha activado).

2. Crear archivo .env (para las variables de entorno). Y añade las variables "MONGODB_URI"="(la uri de la base de datos remota o local)" y "MONGODB_DATABASE"="(el nombre de la base de datos principal)"

2. Ejecutar la aplicación:
  ```bash
  fastapi dev /app/main.py
  ```

3. La aplicación estará disponible en `http://127.0.0.1:8000`. Y la documentación interactiva estará disponible en `http://127.0.0.1:8000/redoc`

## Estructura del proyecto

### /app

La carpeta `/app` contiene el código fuente de la aplicación.

### /app/main.py

El punto de entrada de la aplicación, donde se instancia FastAPI y se definen las rutas.

### /app/models 

Contiene los modelos de datos de entrada que se usan en los endpoints. En este caso solo está creado los modelos de los libros (books.py).

### /app/schemas

Contiene los esquemas que se usan para la correcta salida de datos (respuesta) de los endpoints. 

### /app/routers

Contiene las diferentes rutas de la aplicación, organizados por funcionalidad o tipos.

### /app/routers/books.py

Archivo que contiene los endpoints para interactuar con mongodb.

### /app/routers/localBooks.py

Archivo que contiene las endpoints para interactuar con la base de datos local en memoria (la constante BOOKS). 

### /app/database.py

Archivo donde se establece la conexión a la base de datos de mongodb.

### /app/utils

Contiene utilidades y funciones auxiliares que son utilizadas en diferentes partes del proyecto. Estas funciones están diseñadas para ser reutilizables, facilitando la implementación de tareas comunes y la mejora de la mantenibilidad del código. 

### .env

Archivo donde se encuentran todas las variables de entorno del proyecto. Este archivo no se versiona, por lo que no se sube al repositorio remoto. Aquí se definen variables que no deberían ser públicas, como API keys. En este caso se encuentran las variables "MONGODB_URI"="(la uri de la base de datos remota o local)" y "MONGODB_DATABASE"="(el nombre de la base de datos principal)".

### /requirements.txt

Archivo donde se encuentran el nombre de todas las librerías externas con sus versiones que se usan en el proyecto.

### /.venv

Entorno virtual que contiene todas las librerías externas usadas en el proyecto. Esta carpeta no se versiona, se crea ejecutando el comando 'python -m venv .venv'. Y aquí se instalan automáticamente las liberías ya mencionadas con el comando 'pip install -r requirements.txt'.

### /.gitignore

Archivo donde se especifica a git las carpetas o archivos que no quieres que sean versionadas (que no se suban al repositorio). Por ejemplo el archivo .env

### /.vscode

Carpeta donde se especifíca la configuración de vscode. En este caso lo he configurado para que al guardar un archivo se autoformate el código con black (librería para formatear código de python) Esto no tiene nada que ver con el proyecto, solo para mejorar la experiencia de desarrollo.

## Decisiones Técnicas

1. Usar FastAPI como framework por su simplicidad y su rapidez a la hora de programar. Ya que te ahorra tener que validar los datos manualmente, al igual que autogenerar documentación OpenAPI Swagger, que se encuentra en `http://127.0.0.1:8000/redoc`.

2. Utilizar Pydantic para la validación de datos y la creación de modelos. Pydantic permite definir los modelos de datos de una manera clara y concisa, y se integra perfectamente con FastAPI para la validación automática de las solicitudes y respuestas.

3. Implementar un sistema de rutas modularizado. Al dividir las rutas en diferentes módulos dentro de la carpeta '/app/routers', se facilita la organización y el mantenimiento del código, permitiendo una mejor escalabilidad del proyecto.

4. Configurar un entorno virtual para gestionar las dependencias del proyecto. Esto asegura que todas las librerías necesarias estén instaladas y evita conflictos con otras versiones de librerías que puedan estar presentes en la propia máquima del desarrollador.

5. Utilizar un archivo '.env' para gestionar las variables de entorno sensibles.

6. Utilizar un formateador de código (Black) que me ha ayudado a tener estilo de código consistente y ordenado.

## ¿Qué mejoraría si tuviera más tiempo?

1. Mejoraría las queries para poder filtrar por libros leídos y no leídos, al igual que por fecha.

2. Crearía los endpoints con los métodos DELETE, para poder eliminar libros de la base de datos.

3. Añadaría paginación al recoger todos los libros.

4. Haría tests simples para cada endpoint y comprobar que todo funciona como lo esperado.


