from kubernetes import client, config
import threading


class KubernetesService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, logger=None):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_k8s_client(logger)
        return cls._instance

    def _init_k8s_client(self, logger):
        self._logger = logger

        try:
            config.load_kube_config()
            self._logger.info(
                "Kubernetes configuration loaded from kubeconfig."
            )

        except Exception as e:
            self._logger.info(f"There isn't a kubeconfig configuration: {e}.")
            try:
                config.load_incluster_config()
                self._logger.info(
                    "Kubernetes configuration loaded in cluster."
                )
            except Exception as e:
                self._logger.error(
                    f"Error during loading kubernetes configuration: {e}."
                )
                raise

        self.api_client = client.ApiClient()
        self.core_v1_api = client.CoreV1Api(self.api_client)

    def get_core_v1_api(self):
        return self.core_v1_api
