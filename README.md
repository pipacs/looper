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

### Installing Dependencies

1. Install the Unicorn Hat HD software according to [https://github.com/pimoroni/unicorn-hat-hd](https://github.com/pimoroni/unicorn-hat-hd)
2. Then install these extra packages:

    ```sh
    pip3 install Pillow
    pip3 install requests
    pip3 install holidays
    pip3 install feedparser
    pip3 install PyYAML
    pip3 install pyowm
    pip3 install pygame
    pip3 install ip2geotools
    pip3 install chest
    pip3 install astral
    ```

### Installing Looper

Run ```sudo make``` from this directory. Then run ```looper``` from the command line.

To run Looper when the system boots, add this line to /etc/rc.local:

```sh
nohup /usr/local/bin/looper &
```

## Configuration

Configure looper by editing it's configuration file. The system configuration file is  ```/usr/local/lib/looper/looper.yaml```, the user configuration file is ```~/.looper.yaml```.

If present, the user configuration file is used, otherwise the system configuration file.

### Configuring OpenWeatherMap

Looper is using OpenWeatherMap to display the current weather. OpenWeatherMap requires an API key that can be requested at [https://openweathermap.org/api](https://openweathermap.org/api). After receiving the key, add it to ```~/.looper.yaml```:

```yaml
owm:
    key: "my-api-key"
```

## Developing on the Mac

* Install Homebrew

* Install the rest of the dependencies:
  ```
  brew install python3
  brew install sdl2
  pip3 install Pillow
  pip3 install requests
  pip3 install holidays
  pip3 install feedparser
  pip3 install PyYAML
  pip3 install pyowm
  pip3 install pygame==2.0.0.dev6
  pip3 install ip2geotools
  pip3 install chest
  pip3 install astral
  ```
