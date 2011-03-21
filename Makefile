DESTDIR=/

all:

install:
	install -d $(DESTDIR)/usr/bin $(DESTDIR)/usr/share/doc/flac-utils/
	install tools/flac-diff $(DESTDIR)/usr/bin
	install tools/flac-merge $(DESTDIR)/usr/bin
	install tools/flac-sync $(DESTDIR)/usr/bin
	install README $(DESTDIR)/usr/share/doc/flac-utils/

clean:

.PHONY: clean install
