from distutils.core import setup

from cffi.setuptools_ext import execfile

execfile(filename='./__version__.py', glob="__version__")

INSTALL_REQUIRES = ['msgpack-python', 'pynacl']

TESTS_REQUIRE = [
    'pytest',
    'coverage',
    'pytest-cov',
    'pdbpp',
    'ipython'
]

setup(name='umbral',
      version='0.1.0-alpha',
      description='Umbral PRE implementation for NuCypher',
      extras_require={'testing': TESTS_REQUIRE},
      install_requires=INSTALL_REQUIRES,
      packages=['umbral'])
