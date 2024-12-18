from services.kubernetes_service import KubernetesService
from kubernetes.client.rest import ApiException


class SecretService:
    def __init__(self, k8s_service: KubernetesService, logger):
        self._logger = logger
        self._k8s_service = k8s_service

    def get_secret(self, namespace: str, secret_name: str):
        try:
            secrets = (
                self._k8s_service.get_core_v1_api().list_namespaced_secret(
                    namespace=namespace
                )
            )
            for secret in secrets.items:
                if secret.metadata.name == secret_name:
                    return True
        except ApiException as e:
            self._logger.error(f"API Exception: {e}")
            raise Exception("Failed to retrieve secret data from Kubernetes.")
        return False

    def _check_secret_name(self, secret1: str, secret2: str):
        return secret1 == secret2
