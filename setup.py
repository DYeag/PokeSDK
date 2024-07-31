from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Partial SDK Coverage for PokeAPI'
LONG_DESCRIPTION = 'Not to be used in production'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="pokesdk",
    version=VERSION,
    author="Danny Yeager",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(where='src'),
    install_requires=['requests'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    package_dir={'': 'src'},
    python_requires='>=3.8'
)
