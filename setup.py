import os
from distutils.core import setup

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "src")

about = {}
with open(os.path.join(src_dir, "umbral", "__about__.py")) as f:
    exec(f.read(), about)

INSTALL_REQUIRES = ['msgpack-python', 'pynacl']

TESTS_REQUIRE = [
    'pytest',
    'coverage',
    'pytest-cov',
    'pdbpp',
    'ipython'
]


setup(name=about['__title__'],
      version=about['__version__'],
      author=about['__author'],
      description=about["__summary__"],
      long_description_markdown_filename='README.md',
      extras_require={'testing': TESTS_REQUIRE},
      install_requires=INSTALL_REQUIRES,
      packages=['umbral'],
      classifiers=[
          "Natural Language :: English",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
        ]
      )
