from services.kubernetes_service import KubernetesService
from kubernetes.client.rest import ApiException


class SecretService:
    def __init__(self, k8s_service: KubernetesService, logger):
        self._logger = logger
        self._k8s_service = k8s_service

    def get_secret(self, namespace: str, secret_name: str):
        self._logger.debug(
            "Fetching secret data from cluster "
            f"kubernetes with secret_name: {secret_name}"
            f"in a specific namespace: {namespace}"
        )

        try:
            secrets = (
                self._k8s_service.get_core_v1_api().list_namespaced_secret(
                    namespace=namespace
                )
            )
            for secret in secrets.items:
                self._logger.debug(f"secret_name: {secret.metadata.name}")
                if self._check_secret_name(secret.metadata.name, secret_name):
                    return True

        except ApiException as e:
            print(f"Exception when calling Kubernetes API: {e}")
            return False

        self._logger.debug(
            f"Secret {secret_name} not found in namespace {namespace}"
        )
        return False

    def _check_secret_name(self, secret1: str, secret2: str):
        return secret1 == secret2
