# secret-validator

## TO-DO
- input
    - service-account token
    - secret-name
- settings
    - cron polling
    - cron expiration
- "certs-expiration": 2025-02-10T22:27:12+01:00

## TEST
```bash
$ curl -X 'POST' \
   'http://127.0.0.1:5000/check-secret' \
   -H 'accept: application/json' \
   -H 'Content-Type: application/json' \
   -d '{
        "namespace": "secret-validator-ns",
        "secret_name": "service-a-secrets"
       }'
```
