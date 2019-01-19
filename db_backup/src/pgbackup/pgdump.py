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