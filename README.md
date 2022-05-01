# PlusSBackTest

1. Asegurarse de tener instalado docker y docker-compose.
2. Instalar la imagen de postgres para docker (https://hub.docker.com/_/postgres o correr docker pull postgres en la terminal)
3. Abrir el projecto e instalar rest_framework (https://www.django-rest-framework.org/ o utilizar el comando pip install djangorestframework)
4. Luego, escribir el comando docker-compose up en la consola para levantar la base de datos. Asegurarse de no tener ninguna base de datos corriendo en el puerto 5432.
5. Correr el comando: python manage.py makemigrations inquiry
6. Correr el comando: python manage.py migrate
7. Finalmente correr el comando: python manage.py runserver para levantar el server

Para crear usuarios o consultas:
1. Entrar a: http://127.0.0.1:8000/
2. Ingresar a "user": http://127.0.0.1:8000/user/
3. Completar el mail, usuario y clickear en POST.
4. Volver a: http://127.0.0.1:8000/ e ingresar a "area": http://127.0.0.1:8000/area/
5. Completar el nombre del area y clickear en POST.
6. Finalmente ingresar a "inquiry": http://127.0.0.1:8000/inquiry/
7. Completar los campos correspondientes y clickear en POST.
8. Se crearon un area, un usuario y una consulta. Cada vez que se entra al link se va a ver un listado de todos los objetos correspondientes.
9. Tambien se va a poder crear usuarios, areas y consultas desde postman, haciendo un POST a la url antes mencionada, o utilizando http://localhost:8000/(postObject)/. Tambien se puede utilizar el get para obtener un listado de las distintas entidades creadas en cada tabla.
