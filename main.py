from config.logger import logger
from clients.secret_client import SecretClient
from fastapi import FastAPI
import uvicorn

if __name__ == "__main__":
    logger.info("Run Secret Validator microservice.")

    app = FastAPI()
    app.add_api_route(
        "/check-secret", SecretClient(logger).check_secret, methods=["POST"]
    )

    uvicorn.run(app, host="0.0.0.0", port=5000)
