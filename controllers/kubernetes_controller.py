from services.secret_service import SecretService
from services.pod_service import PodService
from services.kubernetes_service import KubernetesService


class KubernetesController:
    def __init__(self, logger):
        self._logger = logger
        self._k8s_service = KubernetesService(logger)
        self._secret_service = SecretService(self._k8s_service, logger)
        self._pod_service = PodService(self._k8s_service, logger)

    def get_pods(self, namespace: str):
        self._logger.info(
            "Request received to get pods "
            f"existence with namespace: {namespace}"
        )

        self._pod_service.get_pods(namespace)

    def check_secret_existence(self, secret_name: str):
        self._logger.info(
            "Request received to check secret "
            f"existence with secret_name: {secret_name}"
        )

        secret = self._secret_service.get_secret(secret_name)
        self._logger.debug(f"Found secret: {secret}")
