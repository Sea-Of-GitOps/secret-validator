from services.secret_service import SecretService
from services.kubernetes_service import KubernetesService


class KubernetesController:
    def __init__(self, logger):
        self._logger = logger
        self._k8s_service = KubernetesService(logger)
        self._secret_service = SecretService(self._k8s_service, logger)

    def check_secret_existence(self, namespace: str, secret_name: str):
        self._logger.info(
            "Request received to check secret "
            f"existence with secret_name: {secret_name}"
            f"in a specific namespace: {namespace}"
        )

        existence = self._secret_service.get_secret(namespace, secret_name)
        self._logger.debug(f"Found secret: {secret_name} in {namespace}")

        return existence
