.PHONY: bootstrap
bootstrap:
	aptly repo create -distribution=stable -component=main cha0s-dev

.PHONY: clean
clean:
	./gradlew clean

.PHONY: build
build:
	./gradlew build buildDeb buildRpm
	aptly repo add -force-replace cha0s-dev build/distributions

.PHONY: publish
publish:
	aptly publish update -gpg-key="cha0sdev-apt" -force-overwrite stable
	az storage blob sync -s "$(HOME)/.aptly/public/" -c \$$web --account-name cha0sapt

.PHONY: export-gpg
export-gpg:
	gpg --output cha0sapt.gpg --armor --export cha0sdev-apt
	mv cha0sapt.gpg ~/.aptly/public/pub.gpg
