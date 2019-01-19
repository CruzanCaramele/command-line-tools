import pytest
from pgbackup import cli

url = "postgres://user@exmaple.com:5432/db_one"
unknown_driver = "azure"

@pytest.fixture
def parser():
        return cli.create_parser()

def test_parser_without_driver(parser):
        """
        The parser will exit without a specified driver
        """
        with pytest.raises(SystemExit):
                # parser = cli.create_parser()
                parser.parse_args([url])


def test_parser_with_driver(parser):
        """
        The parser will exit if it received a driver with no destination
        # """
        with pytest.raises(SystemExit):
                # parser = cli.create_parser()
                parser.parse_args([url, "--driver", "local"])


def test_parser_with_unknown_driver(parser):
        """
        The parser will exit if the driver name is unknown.
        """
        with pytest.raises(SystemExit):
                parser.parse_args([url, '--driver', 'azure', 'destination'])


def test_parser_with_known_drivers(parser):
        """
        The parser will not exit if the driver is known
        """
        # parser = cli.create_parser()
        for driver in ["local", "s3"]:
                assert parser.parse_args([url, "--driver", driver, "destination"])


def test_parser_with_driver_and_destination(parser):
        """
        The parse will not exit if all arguments are provided, driver & destination
        """
        # parser = cli.create_parser()
        args = parser.parse_args([url, "--driver", "local", "/some/path"])

        assert args.url == url
        assert args.driver == "local"
        assert args.destination == "/some/path"

