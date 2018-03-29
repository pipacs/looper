# Copyright (c) Akos Polster. All rights reserved.

/usr/local/lib/looper:
	mkdir -p /usr/local/lib
	rm -rf /usr/local/lib/looper
	cp -Rf looper /usr/local/lib

/usr/local/lib/looper.py: looper.py
	mkdir -p /usr/local/lib
	cp $< $@
	chmod a+r $@

.PHONY: /usr/local/lib/looper
