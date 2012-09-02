from distutils.core import setup, Extension

memory = Extension('memory',
                   sources = ["memorymodule.c"])

setup(name = 'berserk',
      version = '0.1',
      description = 'Controllable-load benchmark program',
      ext_modules = [memory])
