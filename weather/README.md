## Weathery

Weathery is a small command line python tool that users the openweathermap.org API to retrieve the weather information of cities.

### Usage

Commands can be run by themselves, or stacked.

Sample Usage:

    weathery (master) $ sudo python3.6 setup.py install 
    weathery (master) $ weathery -h
    weathery [-h] city country
    Get the current weather information for your city

    positional arguments:
    city        name of city to get weather for
    country     country name/code the city belongs to

    optional arguments:
    -h, --help  show this help message and exit

    hamza: weathery (master) $ weathery dodma tanzania
    +--------+-----------------------+-------------------------+----------+------------+
    |  City  | Temperature | Celcius | Temperature | Farenheit | Forecast |  Details   |
    +--------+-----------------------+-------------------------+----------+------------+
    | Dodoma |          30.0         |           86.0          |  Clouds  | few clouds |
    +--------+-----------------------+-------------------------+----------+------------+


### Dependencies

- [openweathermap.org](https://openweathermap.org) API key 
- Sign up [here](https://home.openweathermap.org/users/sign_up) to obtain a free API key
- export the API to your environmental variables

### Configuring
- Clone repository: ``git clone https://github.com/CruzanCaramele/command-line-tools.git``
- move into the weather directory: ``cd weather``
- run command: ``python3.6 setup.py install``
- run command to get a weather of a city: ``weathery city country``

example:
```
[root@localhost weather]# weathery nuuk greenland
+------+-----------------------+-------------------------+----------+------------------+
| City | Temperature | Celcius | Temperature | Farenheit | Forecast |     Details      |
+------+-----------------------+-------------------------+----------+------------------+
| Nuuk |          -3.0         |           26.6          |  Clouds  | scattered clouds |
+------+-----------------------+-------------------------+----------+------------------+
```

