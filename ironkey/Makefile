.PHONY= build

default: build

build:
	rpmbuild -v -ba --clean --define "_topdir $(CURDIR)/../rpmbuild" --define "_srcdir $(CURDIR)" ironkey.spec;
