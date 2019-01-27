import sys
import subprocess


def dump(url):
        """
        function that returns the pg_dump and its url that is given as argument
        """
        try:
                return subprocess.Popen(["pg_dump", url], stdout=subprocess.PIPE)
        except OSError as error:
                print(f"Error: {error}")
                sys.exit(1)


def  dump_file_name(url, timestamp=None):
        db_name = url.split("/")[-1]
        db_name = db_name.split("?")[0]
        if timestamp:
                return f"{db_name}-{timestamp}.sql"
        else:
                return f"{db_name}.sql"
