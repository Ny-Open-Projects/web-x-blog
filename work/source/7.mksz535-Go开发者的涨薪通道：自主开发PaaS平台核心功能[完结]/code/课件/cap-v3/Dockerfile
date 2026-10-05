FROM alpine:latest
RUN  apk update && \
#     apk add ca-certificates && \
     apk add protoc && \
     rm -rf /var/cache/apk/*

COPY protoc-gen-go protoc-gen-micro /usr/bin/

ENTRYPOINT ["protoc"]
