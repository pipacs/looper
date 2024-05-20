# Copyright (c) Akos Polster. All rights reserved.

all: \
	/usr/local/bin/looper \
	/usr/local/lib/looper \
	/usr/local/lib/looper.py

/usr/local/bin/looper: looper.sh
	mkdir -p /usr/local/bin
	cp -f $< $@
	chmod a+rx $@

/usr/local/lib/looper:
	mkdir -p /usr/local/lib
	rm -rf /usr/local/lib/looper
	cp -Rf looper /usr/local/lib

/usr/local/lib/looper.py: looper.py
	mkdir -p /usr/local/lib
	cp -f $< $@
	chmod a+r $@

test-mac:
	mkdir -p ~/lib
	python3 -m venv ~/lib/looper.venv
	source ~/lib/looper.venv/bin/activate; \
		pip3 -q install 'Pillow<=9.5.0' requests holidays feedparser PyYAML \
			pyowm pygame ip2geotools astral tzlocal; \
		python3 looper.py

.PHONY: /usr/local/lib/looper
