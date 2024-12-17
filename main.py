from config.logger import logger
from controllers.factories import create_kubernetes_controller
from kubernetes import client, config


def main(k8s):
    logger.info("Run Secret Validator microservice.")

    kubernetes_controller = create_kubernetes_controller(logger)
    logger.debug(f"Kubernetes Controller is created: {kubernetes_controller}")


if __name__ == "__main__":
    config.load_incluster_config()
    k8s = client.CoreV1Api()
    main(k8s)
