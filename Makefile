VERSION := 3.4.10
TARBALL := zookeeper-$(VERSION).tar.gz

SRC = LICENSE ORIGINAL-README c.tgz pyzk_docstrings.h zookeeper.c zookeeper-sources

all: version-check build

version-check: setup.py
	@grep -q "version = '$(VERSION)'" $<

.PHONY: build
build: $(SRC) setup.py
	python setup.py --quiet sdist
	@echo dist/zc-zookeeper-static-$(VERSION).tar.gz

$(SRC): $(TARBALL)
	python get_source_files.py $(CURDIR)/$<

$(TARBALL):
	curl -O http://apache.mirrors.spacedump.net/zookeeper/zookeeper-$(VERSION)/zookeeper-$(VERSION).tar.gz

.PHONY: clean
clean:
	$(RM) $(TARBALL)
	$(RM) -r $(SRC) src dist zc_zookeeper_static.egg-info
