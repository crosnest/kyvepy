FROM  ignitehq/cli:v0.26.1

ARG VERSION
ARG REPOSITORY

RUN git clone --branch $VERSION $REPOSITORY c4echain
WORKDIR c4echain

# Run the docker_imgs command when the container starts.
ENTRYPOINT ["ignite chain serve"]