# Looper

_Copyright &copy; Akos Polster. All rights reserved._

Loops info on a Raspberry Pi eqipped with a Unicorn Hat HD:

- Current time
- Current weather
- A panda

# Installation

Run ```sudo make``` from this directory.

To run it after system boot, add this line to /etc/rc.local:

```
(cd /usr/local/lib; nohup python3 looper.py &)
```

# Dependencies

- Python 3: ```sudo apt-get install python3```
- Weather: ```sudo pip3 install weather-api```
- Pillow: ```sudo pip3 install Pillow```
- Requests: ```sudo pip3 install requests```