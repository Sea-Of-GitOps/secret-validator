class SecretService:
    def __init__(self, logger):
        self._logger = logger

    def get_secret(self, secret_name: str):
        self._logger.debug(
            "Fetching secret data from cluster "
            f"kubernetes with secret_name: {secret_name}"
        )

        return secret_name
