# this setup.py is meant for people that
# don't have cython installed and just want
# to make seekwatcher go
#
from distutils.core import setup, Extension
import numpy
#import mpatch.version
#version=mpatch.version.version,
setup(name='seekwatcher',
        version="0.50",
      ext_modules=[
          Extension('seekwatcher.rundata',
          ['seekwatcher/rundata.c'],
          include_dirs = [numpy.get_include(),'.']),
          Extension('seekwatcher.blkparse',
          ['seekwatcher/blkparse.c'],
          include_dirs = [numpy.get_include(),'.'])
          ],
      scripts=['cmd/seekwatcher'],
      packages=['seekwatcher'])
