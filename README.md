# Aplicacion NutriDex

## Pasos para instalar la aplicacion y correr en local

1. Haz un clone del repo
2. El fichero env tiene un ambiente virtual de python [https://virtualenv.pypa.io/en/latest/user_guide.html] lo activas de la siguiente manera
..* source/bin/activate 
3. instalas las dependencias (no estoy seguro si las necesites dado que ahi esta el fichero del ambiente virtual) pip3 install requirements.txt
4. Ya instalado el desmadre, entras al fichero nutrion y corres el servidor local. ./manage runserver
5. Te va a tronar esa madre :v
6. tienes que tener postresSQL instalado y configurar las credenciales para la base de datos. Eso se hace en el archivo settings.py [https://docs.djangoproject.com/en/3.0/intro/tutorial02/]
7. Dentro del fichero nutrion/nutrion/ETL ahi vas a encontrar un fichero patients.py un MOCK_DATA.csv es un mock data de 1k de usuarios, nomas corre esa madre y te lo debe poblar. Modifica la ultima columna segun el id de tu superusuario. 
..* ./manage createsuperuser     sigue los pasos y te crear un superuser
8. Te va a tronar.
9. Me dices si olvide algo
