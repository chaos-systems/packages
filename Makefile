.PHONY=
SCALA_VERSION=2.12.4

default: build-repo

setup:
	mkdir -p rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
	mkdir -p repo/{x86_64,noarch}

clean:
	rm -rf rpmbuild
	rm -rf repo

s3-sync-from: setup
	aws --region eu-west-1 s3 sync s3://chaossystems-repositories/artifacts/rpm/chaossystems repo

s3-sync-to: build-repo
	aws --region eu-west-1 s3 sync --delete repo s3://chaossystems-repositories/artifacts/rpm/chaossystems

deploy: #: Deploy the repo to S3. This should only be used by CI, developers should use s3-sync-to.
	aws --region eu-west-1 s3 sync --delete --acl public-read repo s3://chaossystems-repositories/artifacts/rpm/chaossystems

build-repo: setup s3-sync-from ammonite-rpm chaossystems-repos-rpm chaossystems-i3-rpm chaossystems-devtools-rpm downloads ironkey-rpm
	for a in repo{/x86_64,/noarch} ; do \
	       createrepo -v --update --deltas $$a/ ; \
	       done

ammonite-rpm: setup
	cd ammonite; $(MAKE)
	cp rpmbuild/RPMS/noarch/ammonite-*.rpm repo/noarch/

ironkey-rpm: setup
	cd ironkey; $(MAKE)
	cp rpmbuild/RPMS/noarch/ironkey-*.rpm repo/noarch/

chaossystems-repos-rpm: setup
	cd chaossystems-repos; $(MAKE)
	cp rpmbuild/RPMS/noarch/chaossystems-repos-*.rpm repo/noarch/

chaossystems-i3-rpm: setup
	cd chaossystems-i3; $(MAKE)
	cp rpmbuild/RPMS/noarch/chaossystems-i3-*.rpm repo/noarch/

chaossystems-devtools-rpm: setup
	cd chaossystems-devtools; $(MAKE)
	cp rpmbuild/RPMS/noarch/chaossystems-devtools-*.rpm repo/noarch/

downloads: download-scala download-slack download-atom

download-scala:
	curl -LsO https://downloads.lightbend.com/scala/$(SCALA_VERSION)/scala-$(SCALA_VERSION).rpm
	cp scala-$(SCALA_VERSION).rpm repo/noarch/
	rm -f scala-$(SCALA_VERSION).rpm

download-slack:
	curl -LsO https://downloads.slack-edge.com/linux_releases/slack-3.0.5-0.1.fc21.x86_64.rpm
	cp slack-3.0.5-0.1.fc21.x86_64.rpm repo/noarch/
	rm -f slack-3.0.5-0.1.fc21.x86_64.rpm

download-atom:
	curl -LsO https://github.com/atom/atom/releases/download/v1.24.0/atom.x86_64.rpm
	cp atom.x86_64.rpm repo/noarch/
	rm -f atom.x86_64.rpm
