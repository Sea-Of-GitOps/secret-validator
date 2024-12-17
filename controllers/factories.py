from controllers.kubernetes import KubernetesController


def create_kubernetes_controller(logger):
    return KubernetesController(logger)
