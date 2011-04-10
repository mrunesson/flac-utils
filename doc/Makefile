MAN_PAGES = flac-sync.1 flac-diff.1 flac-add-picture.1

DB2MAN = /usr/share/xml/docbook/stylesheet/docbook-xsl/manpages/docbook.xsl
XP     = xsltproc --nonet --param man.charmap.use.subset "0"

.SUFFIXES: .1 .xml

.xml.1:
	$(XP) $(DB2MAN) $<

.PHONY: clean

all: ${MAN_PAGES}

clean:
	rm -f ${MAN_PAGES}
	rm -f *~
