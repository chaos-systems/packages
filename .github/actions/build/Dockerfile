FROM azul/zulu-openjdk:15

RUN apt-get update \
    && apt-get install -y \
    make

ENTRYPOINT ["/usr/bin/make"]
