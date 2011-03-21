install:
	install -o root tools/flac-diff /usr/bin/
	install -o root tools/flac-merge /usr/bin
	install -o root tools/flac-sync /usr/bin
	install -o root README /usr/share/doc/flac-utils/
	install -o root COPYING /usr/share/doc/flac-utils/

clean:

.PHONY clean install
