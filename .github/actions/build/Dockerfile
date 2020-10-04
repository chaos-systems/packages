FROM azul/zulu-openjdk:14

RUN apt-get update \
    && apt-get install -y \
    make

ENTRYPOINT ["/usr/bin/make"]
