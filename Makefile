# Copyright (c) Akos Polster. All rights reserved.

all: \
	/usr/local/bin/looper \
	/usr/local/lib/looper \
	/usr/local/lib/looper.py \
	/usr/local/lib/unicorn_hat_sim.py

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

/usr/local/lib/unicorn_hat_sim.py: unicorn_hat_sim.py
	mkdir -p /usr/local/lib
	cp -f $< $@
	chmod a+r $@

.PHONY: /usr/local/lib/looper
