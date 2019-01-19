from argparse import Action, ArgumentParser

known_drivers = ["local", "s3"]

class DriverAction(Action):
        def __call__(self, parser, namespace, values, option_string=None):
                driver, destination = values
                if driver.lower() not in known_drivers:
                        parser.error("Unknow driver. Available drivers are local and S3")
                namespace.driver = driver.lower()
                namespace.destination = destination


def create_parser():
        parser = ArgumentParser(description="backup databases locally or to AWS S3 buckets")
        parser.add_argument("url", help="URL for the database")
        parser.add_argument("--driver",
                           help="how & where to store the backup",
                           nargs=2,
                           action=DriverAction,
                           metavar=('driver', 'destination'),
                           required=True)
        return parser