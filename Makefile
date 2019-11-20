
.PHONY: clean
clean:
	./gradlew clean

.PHONY: build
build:
	./gradlew build buildDeb buildRpm

.PHONY: publish
publish:
	./gradlew bintrayUpload bintrayPublish
