Descargar votaciones
====================

Descargar PDFs de votaciones nominales.

## Requisitos

    Python (>= 2.7)
    BeautifulSoup (4.1.3)


## Como usar

Ejemplo:

    $ python get_votaciones.py --url http://www.diputados.gov.ar/secadmin/ds_electronicos/periodo/2013/index.html --folder votaciones_2013

    Otras URL de ejemplo:
    http://www.diputados.gov.ar/secadmin/ds_electronicos/periodo/2012/index.html
    http://www.diputados.gov.ar/secadmin/ds_electronicos/periodo/2009/index.html
    etc.

Para ver las opciones de uso:

    $ python  get_votaciones.py --help

    Descargar PDFs de votaciones nominales

    optional arguments:
      -h, --help       show this help message and exit
      --folder FOLDER  Carpeta destino para PDF descargados
      --keep-links     Conservar links de PDF en un archivo llamado links.txt
      --url URL        URL del período de votaciones nominales Ej.: http://www.di
                       putados.gov.ar/secadmin/ds_electronicos/periodo/2013/index.
                       html

## License

Junto con este proyecto, deberías recibir un archivo denominado ``LICENSE`` con los términos de la licencia.
