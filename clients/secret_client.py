from controllers.factories import create_kubernetes_controller
from pydantic import BaseModel
from fastapi import HTTPException


class SecretClientRequest(BaseModel):
    namespace: str
    secret_name: str


class SecretClient:
    def __init__(self, logger):
        self._kubernetes_controller = create_kubernetes_controller(logger)
        self._logger = logger

    async def check_secret(self, request: SecretClientRequest):
        self._logger.debug(f"Request is: {request}")
        exists = self._kubernetes_controller.check_secret_existence(
            request.namespace, request.secret_name
        )

        if exists:
            return {
                "message": f"The secret '{request.secret_name}' "
                f"exists in the namespace '{request.namespace}'."
            }
        else:
            raise HTTPException(
                status_code=404,
                detail=f"The secret '{request.secret_name}' does not "
                f"exist in the namespace '{request.namespace}'.",
            )
