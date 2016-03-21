prueba para twitter ads
=======================

el script que ejecuta que crea la campaaña es main.py

el script puede recibir 2 parametros
ACCOUNT_ID y INSTRUMENT_ID

si no se le da ningun parametro imprime todas las cuentas disponibles

si sse le da solo el id de la cuenta imprime todos los instrumentos disponibles

si se le asigna los 2 parametros creara una campaña y un anuncion asignandole
los objetivos

SETTINGS
========

el arvhico de settings.py es donde se guarda la comfiguracion de los tokens
para el oauth

el campo de debug si es true usa los datos dummys del ejemplo de la documentacion
de twitter de como administrar una campaña

si el campo es false entonces hara las peticiones a la url
