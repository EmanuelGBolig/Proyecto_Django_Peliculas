# Proyecto Final - Catálogo de Películas

Proyecto final para el curso "Introducción a la Programación Web con Django".

Este proyecto es un catálogo web de películas que permite listar todas las películas de la base de datos y ver una página de detalle para cada una, mostrando su imagen, sinopsis y puntuación.

### Autor

* [Emanuel Gomez Bolig]

---

### Pasos para Ejecutar en Local

Para levantar este proyecto en un entorno local, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone [LA-URL-DE-TU-REPOSITORIO]
    cd [NOMBRE-DE-LA-CARPETA-DEL-PROYECTO]
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar las migraciones:**
    (Esto creará la base de datos `db.sqlite3` con las tablas necesarias)
    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario:**
    (Para poder acceder al admin en `/admin/` y cargar películas)
    ```bash
    python manage.py createsuperuser
    ```

6.  **Ejecutar el servidor:**
    ```bash
    python manage.py runserver
    ```

7.  Abrir `http://127.0.0.1:8000/` en el navegador.