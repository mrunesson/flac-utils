MAN_PAGES = flac-sync.1 flac-diff.1 flac-merge.1

DB2MAN = /usr/share/sgml/docbook/stylesheet/xsl/docbook-xsl/manpages/docbook.xsl
XP     = xsltproc --nonet --param man.charmap.use.subset "0"

.SUFFIXES: .1 .xml

.xml.1:
	$(XP) $(DB2MAN) $<

.PHONY: clean

all: ${MAN_PAGES}

clean:
	rm -f ${MAN_PAGES}
	rm -f *~