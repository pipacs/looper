# Looper

_Copyright &copy; Akos Polster. All rights reserved._

Loops info on a Raspberry Pi equipped with the [Unicorn Hat HD](https://shop.pimoroni.com/products/unicorn-hat-hd):

- Current date
- Current time
- Current weather
- A panda
- Current holiday, if any

# Installation

Run ```sudo make``` from this directory. Then run ```looper``` from the command line.

To run Looper when the system boots, add this line to /etc/rc.local:

```
nohup /usr/local/bin/looper &
```

# Dependencies

1. Install the Unicorn Hat HD software according to https://github.com/pimoroni/unicorn-hat-hd

2. Then install these extra packages:

```
pip3 install weather-api
pip3 install Pillow
pip3 install requests
pip3 install holidays
```
