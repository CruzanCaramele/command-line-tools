from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
        readme = f.read()

setup(
        name='pgbackup',
        version='0.1.0',
        description='Database backup to local folder or S3 bucket.',
        long_description=readme,
        author='Hamza',
        author_email='letters2hamza@gmail.com',
        install_requires=['boto3'],
        packages=find_packages('src'),
        package_dir={'': "src"},
        entry_points={
                'console_scripts': [
                        'pgbackup=pgbackup.cli:main',
                ],
        }
)