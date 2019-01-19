# Looper

_Copyright &copy; Akos Polster. All rights reserved._

Loops info on a Raspberry Pi equipped with the [Unicorn Hat HD](https://shop.pimoroni.com/products/unicorn-hat-hd):

* Current date
* Current time
* Current weather
* A panda
* Current holiday, if any
* Latest news headlines from Reuters
* Phase of the moon

![alt text](docs/looper.gif "Screen shot")

## Installation

Run ```sudo make``` from this directory. Then run ```looper``` from the command line.

To run Looper when the system boots, add this line to /etc/rc.local:

```
nohup /usr/local/bin/looper &
```

## Configuration

Configure looper by editing it's configuration file. The system configuration file is  ```/usr/local/lib/looper/looper.yaml```, the user configuration file is ```~/.looper.yaml```.

If present, the user configuration file is used, otherwise the system configuration file.

## Dependencies

1. Install the Unicorn Hat HD software according to [https://github.com/pimoroni/unicorn-hat-hd](https://github.com/pimoroni/unicorn-hat-hd)
2. Then install these extra packages:

```
pip3 install weather-api
pip3 install Pillow
pip3 install requests
pip3 install holidays
pip3 install feedparser
pip3 install PyYAML
pip3 install pyowm
```
