DESTDIR=/

all: doc

install: all
	install -d $(DESTDIR)/usr/bin $(DESTDIR)/usr/share/doc/flac-utils/ 
        install -d $(DESTDIR)/share/man/man1
	install tools/flac-diff $(DESTDIR)/usr/bin
	install tools/flac-merge $(DESTDIR)/usr/bin
	install tools/flac-sync $(DESTDIR)/usr/bin
	install README $(DESTDIR)/usr/share/doc/flac-utils/
	install flac-sync-algorithm.txt $(DESTDIR)/usr/share/doc/flac-utils/
	install doc/*.1 $(DESTDIR)/share/man/man1

doc:
	cd doc ; ${MAKE} all

clean:
	cd doc ; ${MAKE} $@
	rm -f *~

.PHONY: clean install
