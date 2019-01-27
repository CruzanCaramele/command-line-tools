dbpackup
========

CLI tool for creating backups for databases either locally or aws-S3 buckets (currently supports postgres)

Preparing the Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone git@github.com:cruzancaramele/command-line-tools``
3. ``cd`` into the repository.
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in a full database URL, the storage driver, and the destination.

S3 Example w/ bucket name:

::
        $ pgpackup postgres://user@exmaple.com:5432/db_one --driver s3 backups

Local Example w/ local path:

::
        $ pgpackup postgres://user@exmaple.com:5432/db_one --driver local /var/local/dbbackup/dump.sql



Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

        $ make

If virtualenv is not active:

::

        $ pipenv run make