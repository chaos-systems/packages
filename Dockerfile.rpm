FROM chaossystems/build-rpm:master
MAINTAINER Greg Orzell <devops@keen.io>

ENV HOME /root
WORKDIR /rpm-build

# Install base packages
RUN dnf makecache && \
    dnf install -y fish vim && \
    dnf clean all

# Install AWS MFA Tools
RUN pip install aws-mfa

CMD ["/bin/bash"]
