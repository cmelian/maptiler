from distutils.core import setup
import os, sys
import glob

if sys.platform in ['win32','win64']:
	import py2exe
if sys.platform == 'darwin':
	import py2app

from maptiler import version

setup(name='MapTiler',
      version=version,
      description = "MapTiler - Map Tile Generator for Mashups",
      long_description= "MapTiler is a powerful tool for online map publishing and generation of map overlay mashups. Your geodata are transformed to the tiles compatible with Google Maps and Earth - ready for uploading to your webserver.",
      url='http://www.maptiler.org/',
      author='Klokan Petr Pridal',
      author_email='klokan@klokan.cz',
      packages=['maptiler'],
      scripts=['maptiler.py'],
      windows=[ {'script':'maptiler.py', "icon_resources": [(1, os.path.join('resources', 'maptiler.ico'))] } ],
      app=['maptiler.py'],
      data_files=[
        ('gdaldata', glob.glob('gdaldata/*.*')),
        ('gdalplugins', glob.glob('gdalplugins/*.*')),
        ('', glob.glob('*.dll'))
      ],
      options={'py2exe':{'packages':['maptiler'],
                         'includes':['encodings','osgeo','osgeo.gdal','osgeo.osr'],
                         },
               'py2app':{'argv_emulation':True,
                         'iconfile':os.path.join('resources', 'maptiler.icns'),
                         'packages':['maptiler'],
                         'includes':['encodings'],
                         #'site_packages':True,
                         },
               },

)
