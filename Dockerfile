FROM golang:1.23.4-alpine as builder
WORKDIR /app
COPY . .
RUN go mod tidy
RUN go build -o secret-validator .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /app/secret-validator /usr/local/bin/
WORKDIR /usr/local/bin
CMD ["secret-validator"]
