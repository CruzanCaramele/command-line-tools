## Weathery

Weathery is a small command line python tool that users the openweathermap.org API to retrieve the weather information of cities.

### Usage

Commands can be run by themselves, or stacked.

Sample Usage:

    hamzz: weathery (master) $ sudo python3.6 setup.py install 
    hamza: weathery (master) $ weathery -h
    usage: weathery [-h] city country
    Get the current weather information for your city

    positional arguments:
    city        name of city to get weather for
    country     country code the city belongs to

    optional arguments:
    -h, --help  show this help message and exit

    hamza: weathery (master) $ weathery texas us
    +-------+-------------+---------+---------+
    |  City | Temperature | Forcast | Details |
    +-------+-------------+---------+---------+
    | Texas |    282.53   |  Clouds |  Clouds |
    +-------+-------------+---------+---------+


### Dependencies

- [openweathermap.org](https://openweathermap.org) API key 
- Sign up [here](https://home.openweathermap.org/users/sign_up) to obtain a free API key
- export the API to your environmental variables

### Configuring
- Clone repository: ``git clone https://github.com/CruzanCaramele/command-line-tools.git``
- move into the weather directory: ``cd weather``
- run command: ``python3.6 setup.py install``

