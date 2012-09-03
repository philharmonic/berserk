from setuptools import setup, Extension

memory = Extension('memory',
                   sources = ["extensions/memorymodule.c"])

setup(name = 'berserk',
      version = '0.1',
      description = 'Controllable-load benchmark program',
      license = 'GPLv3',
      #packages = ['berserk'],
      ext_modules = [memory])
