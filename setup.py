from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
       version='0.0.1',
       description='script for sorting files in folders by extension',
       url='https://github.com/Nevskiy911/',
       author='Oleksandr Malieiev',
       author_email='maleev1820@gmail.com',
       license='MIT',
       packages=find_namespace_packages(),
       entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})
