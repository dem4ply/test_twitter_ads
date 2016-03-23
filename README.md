prueba para twitter ads
=======================

el script que ejecuta que crea la campaña es main.py.
el script de main_mock.py es para simular las peticiones usando los dummys
del archivo debug.

el script puede recibir 2 parametros
ACCOUNT_ID y INSTRUMENT_ID

si no se le da ningun parametro imprime todas las cuentas disponibles.

si sse le da solo el id de la cuenta imprime todos los instrumentos disponibles.

si se le asigna los 2 parametros creara una campaña y un anuncion asignandole
los objetivos.

SETTINGS
========

el archivo de settings.py es donde se guarda la comfiguracion de los tokens
para el oauth.
