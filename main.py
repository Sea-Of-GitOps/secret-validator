from config.logger import logger
from controllers.factories import create_kubernetes_controller


def main():
    logger.info("Run Secret Validator microservice.")
    namespace = "secret-validator-ns"
    secret_name = "service-a-secrets"

    kubernetes_controller = create_kubernetes_controller(logger)
    logger.debug(f"Kubernetes Controller is created: {kubernetes_controller}")

    existence = kubernetes_controller.check_secret_existence(
        namespace, secret_name
    )
    logger.debug(f"Existance result: {existence}")


if __name__ == "__main__":
    main()
