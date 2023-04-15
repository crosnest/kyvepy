FROM alpine/git AS CLONE
RUN mkdir /temp
WORKDIR /temp
RUN git clone https://github.com/chain4energy/c4e-chain


FROM ignitehq/cli AS BUILD
COPY --from=CLONE /temp/c4e-chain /c4e-chain
WORKDIR /c4e-chain
USER root
RUN chmod -R 777 /c4e-chain/go.mod
RUN ignite chain build
CMD [  "chain","serve","--skip-proto" ]