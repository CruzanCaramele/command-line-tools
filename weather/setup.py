from setuptools import setup, find_packages

with open('README.md', encoding='UTF8') as f:
	readme = f.read()

setup (
	name='weather',
	version='0.1.0',	
	description='Command line weather tool',
	long_description=readme,
	author='Hamza',
	author_email='letters2hamza@gmail.com',
	install_requires=['requests>=2.0.0'],
	packages=find_packages('src'),
	package_dir={'','src'},
	entry_points={
		'console_scripts': [
			'weather=weather.cli:main',
		],
	}
)