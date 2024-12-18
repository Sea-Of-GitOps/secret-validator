from services.kubernetes_service import KubernetesService


class SecretService:
    def __init__(self, k8s_service: KubernetesService, logger):
        self._logger = logger
        self._k8s_service = k8s_service

    def get_secret(self, secret_name: str):
        self._logger.debug(
            "Fetching secret data from cluster "
            f"kubernetes with secret_name: {secret_name}"
        )

        return secret_name
