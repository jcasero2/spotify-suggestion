  
"""
soptify-suggestion python package configuration.
Jorge Casero <jcasero@umich.edu>
Sid Murthy <smurthy@umich.edu>
"""

from setuptools import setup

setup(
	name='spotify-suggester',
    version='0.1.0',
	description='BMS and Blynk functionality for Raspberry Pi controlled e-longboard',
	author='Jorge Casero, Sid Murthy',
	author_email='jcasero@umich.edu, smurthy@umich.edu',
	license='GPL-3.0',
	url='https://github.com/jcasero2/spotify-suggestion',
    packages=[
		'src',
	],
    include_package_data=True,
    install_requires=[
		'psutil==5.7.0',
		'pytest==4.6.9',
		'pytest-xdist==1.31.0',
    ],
)
