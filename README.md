# Looper

_Copyright &copy; Akos Polster. All rights reserved._

Loops info on a Raspberry Pi equipped with a Unicorn Hat HD:

- Current time
- Current weather
- A panda

# Installation

Run ```sudo make``` from this directory. Then run ```looper``` from the command line.

To run Looper when the system boots, add this line to /etc/rc.local:

```
nohup /usr/local/bin/looper &
```

# Dependencies

- Python 3: ```sudo apt-get install python3```
- Weather: ```sudo pip3 install weather-api```
- Pillow: ```sudo pip3 install Pillow```
- Requests: ```sudo pip3 install requests```
