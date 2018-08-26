from setuptools import setup, find_packages

with open('Readme.rst', 'r') as f:
  readme = f.read()

setup(
  name='pulse',
  version='0.1',
  description='manage pulse stuff',
  long_description=readme,
  author='Alexei Lugovoi',
  author_email='ezziepat@gmail.com',
  packages=find_packages('src'),
  package_dir={'': 'src'},
  install_requires=['pulsectl'],
  entry_points={
    'console_scripts': [
       'pulse=pulse.cli:main',
    ]
  }
)
