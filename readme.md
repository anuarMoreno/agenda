# Django CRUD Application: Tasks and Contacts

Este repositorio contiene una aplicación CRUD (Create, Read, Update, Delete) simple construida con Django. El proyecto te permite gestionar tareas y contactos. A continuación, te guiaré a través de la configuración y el uso de esta aplicación.

## Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente instalado:

- Python 3.6 o superior
- Django 5.0.3
- PostgreSQL (Puedes usar otras bases de datos, pero este ejemplo utiliza PostgreSQL)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/anuarMoreno/agenda.git
    ```

2. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    cd agenda
    python -m venv venv
    source venv/bin/activate
    ```

3. Instala los paquetes requeridos:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura tus variables de entorno:

    Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:

    ```
    SECRET_KEY=a!)-i9hj5ovjhjsl_n8*_2(1$i_@e^a+&6u2k%(%$(p8jqwfmj
    DEBUG=True
    DATABASE_ENGINE=django.db.backends.postgresql
    DATABASE_NAME=agenda
    DATABASE_USER=@anuarmeng
    DATABASE_PASSWORD=0000000
    DATABASE_HOST=127.0.0.1
    DATABASE_PORT=5432
    ```

5. Ejecuta las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

6. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

## Uso

1. Accede a la aplicación en tu navegador en http://localhost:8000/.

2. Crea, actualiza y elimina tareas y contactos utilizando los formularios proporcionados.

3. Explora las diferentes funcionalidades de la aplicación CRUD.

## Contribuciones

Siéntete libre de contribuir a este proyecto abriendo problemas o solicitudes de extracción en el repositorio de GitHub.

## Licencia

Este proyecto está bajo la Licencia MIT.

---

¡Eso es todo! Ahora tienes una aplicación CRUD básica para gestionar tareas y contactos utilizando Django y PostgreSQL. Siéntete libre de personalizarlo y mejorarlo según tus necesidades. ¡Happy Code! 🚀