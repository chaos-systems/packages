FROM azul/zulu-openjdk:13

RUN apt-get update \
    && apt-get install -y \
    make

ENTRYPOINT ["/usr/bin/make"]
