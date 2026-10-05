FROM golang:1.21-alpine AS build
WORKDIR /src
COPY go.mod go.sum* ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o /es-demo ./cmd/es-demo

FROM alpine:3.19
RUN apk add --no-cache ca-certificates curl
COPY --from=build /es-demo /usr/local/bin/es-demo
ENTRYPOINT ["es-demo"]
CMD ["demo"]
