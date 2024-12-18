from config.logger import logger
from controllers.factories import create_kubernetes_controller


def main():
    logger.info("Run Secret Validator microservice.")
    namespace = "secret-validator-ns"

    kubernetes_controller = create_kubernetes_controller(logger)
    logger.debug(f"Kubernetes Controller is created: {kubernetes_controller}")

    kubernetes_controller.get_pods(namespace)


if __name__ == "__main__":
    main()
