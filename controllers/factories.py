from controllers.kubernetes_controller import KubernetesController


def create_kubernetes_controller(logger):
    return KubernetesController(logger)
