from services.secret_service import SecretService


class KubernetesController:
    def __init__(self, logger):
        self._logger = logger
        self._secret_service = SecretService(logger)

    def check_secret_existence(self, secret_name: str):
        self._logger.info(
            "Request received to check secret "
            f"existence with secret_name: {secret_name}"
        )

        secret = self._secret_service.get_secret(secret_name)
        self._logger.debug(f"Found secret: {secret}")
