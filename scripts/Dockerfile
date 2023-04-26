FROM alpine/git AS CLONE
RUN mkdir /temp
WORKDIR /temp

ARG VERSION
ARG REPOSITORY

RUN git clone --branch ${VERSION} ${REPOSITORY}


FROM ignitehq/cli:v0.26.1 AS BUILD
COPY --from=CLONE /temp/kyve-chain /kyve-chain
WORKDIR /kyve-chain
USER root
RUN chmod -R 777 /kyve-chain/go.mod
RUN ignite chain build
CMD [  "chain","serve","--skip-proto" ]