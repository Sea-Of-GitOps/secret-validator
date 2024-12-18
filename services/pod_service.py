from services.kubernetes_service import KubernetesService


class PodService:
    def __init__(self, k8s_service: KubernetesService, logger):
        self._logger = logger
        self._k8s_service = k8s_service

    def get_pods(self, namespace: str):
        self._logger.info(
            "Request received to get pods "
            f"existence with namespace: {namespace}"
        )

        pods = self._k8s_service.get_core_v1_api().list_namespaced_pod(
            namespace=namespace
        )
        for pod in pods.items:
            print(f"Pod name: {pod.metadata.name}")

        return pods
