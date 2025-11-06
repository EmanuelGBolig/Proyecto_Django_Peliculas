Proyecto Final: Catálogo de Películas

Este es el proyecto final para el curso "Desarrollo de Sistemas Web". Es una aplicación web completa que funciona como un catálogo de películas, permitiendo a los usuarios ver un listado de películas y disfrutar de una interfaz moderna y adaptable.

El sitio está desplegado en Render y se puede visitar en la siguiente URL:
[https://proyecto-peliculas-el7d.onrender.com/](https://proyecto-peliculas-el7d.onrender.com/)**

Autor
* Emanuel Gomez Bolig

---

Acceso al Administrador (Producción)

Puedes acceder al panel de administrador del sitio desplegado para gestionar el contenido (crear, editar o eliminar películas).

* **URL del Admin:** **[https://proyecto-peliculas-el7d.onrender.com/admin/](https://proyecto-peliculas-el7d.onrender.com/admin/)**
* **Usuario:** `admin`
* **Contraseña:** `emanuel2001`

---

Funcionalidades Implementadas

Este proyecto cumple con todos los requisitos mínimos y añade varias funcionalidades extra para una nota superior:

* **Proyecto Django funcional** con una app (`catalogo`).
* **Base de Datos PostgreSQL** para el despliegue en producción (Render).
* **Gestión de Archivos Multimedia (Cloudinary)**: El modelo `Pelicula` utiliza el campo nativo **`CloudinaryField`** de la librería. Esto conecta automáticamente el panel de administrador con Cloudinary para almacenar de forma persistente las imágenes subidas.
* **Despliegue en Render** (usando Gunicorn, Whitenoise y la configuración de Cloudinary).
* **Interfaz con Bootstrap 5**, incluyendo Navbar, Cards y un Carrusel.
* **Herencia de Plantillas** (`base.html` y plantillas hijas).
* **Vistas Basadas en Clases (CBV)**, incluyendo `ListView` y `DetailView`.
* **Diseño 100% Adaptable (Responsive)**:
    * Navbar con menú "hamburguesa" funcional en móviles.
    * Carrusel de inicio que muestra 3 películas en PC y 1 en móvil.
    * Controles del carrusel optimizados para no superponerse al contenido.
* **Selector de Tema (Claro/Oscuro)**: Un interruptor en el navbar que guarda la preferencia del usuario usando JavaScript y `localStorage`.
* **Modelo de Datos Completo**: El modelo `Pelicula` incluye `CloudinaryField`, puntuación (con estrellas), sinopsis y campos de texto adicionales.
* **Página de Inicio Dinámica**: Muestra un carrusel con las 6 películas mejor puntuadas.
* **Panel de Administrador Funcional**: El admin está activo en producción y permite la gestión completa de las películas.

---

Pasos para Ejecutar en Local

Para clonar y ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. Prerrequisitos
Tener `Python 3.11+` y `git` instalados.

2. Clonar el Repositorio

git clone [https://github.com/EmanuelGBolig/Proyecto_Django_Peliculas.git](https://github.com/EmanuelGBolig/Proyecto_Django_Peliculas.git)
cd Proyecto_Django_Peliculas

3. Crear y Activar un Entorno Virtual

Para Windows

python -m venv venv

.\venv\Scripts\activate

Para macOS/Linux

python3 -m venv venv

source venv/bin/activate


4. Instalar Dependencias

pip install -r requirements.txt

5. Crear el Archivo de Entorno .env
   
Este proyecto usa un archivo .env para manejar las claves locales.

Crea un archivo llamado .env en la raíz del proyecto.

Copia y pega el siguiente contenido, añadiendo tu API Secret de Cloudinary:

Archivo .env para desarrollo local

SECRET_KEY='django-insecure-local-key-para-probar-@#123'

DEBUG='True'

Dejamos DATABASE_URL vacío para que use SQLite por defecto

DATABASE_URL=

Tus claves de Cloudinary (para que funcionen las imágenes en local)

CLOUD_NAME='dpynpe2sw'

API_KEY='332323673199339'

API_SECRET='4y-1p91hrC1TuSi5FvaODKrd1dM'


6. Aplicar Migraciones y Crear un Usuario
   
Esto creará tu base de datos local db.sqlite3.

python manage.py migrate

python manage.py createsuperuser


7. Ejecutar el Servidor:
   
python manage.py runserver

El sitio estará disponible en http://127.0.0.1:8000/
