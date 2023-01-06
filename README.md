# Proyecto_3_Fazt

### Descripcion

EL proyecto consiste en el uso de fastapi, uvicorn y MySQL

### Pasos para ejecutar el proyecto

- Ingresar a cmd y verificar que se cuenta con `virtualenv`
- En caso de no tenerlo, instalar con el comando `pip install venv`
- Crear un entorno virtual desde el cmd teniendo en cuenta la ruta del repositorio del proyecto
- En el `cmd` ejecutar: `python -m venv (ruta del repositorio)\ env `
- Abrir el IDE de preferencia y proceder a activar el entorno virtual creado `env`

### Pasos para activar el env

- Ubicarnos en el la rutal del repositorio y dirigirnos a la carpeta `env`
- Luego ejecutamos `Scripts\activate`
- Una vez iniciado `env`, procedemos a instalar `requirements.txt` mendiante `pip install -r requirements.txt`
- Luego en la ruta de nuestro repositorio dirigirnos a la carpeta donde se encuetra el proyecto y ejecutar `uvicorn app:app --reload`
