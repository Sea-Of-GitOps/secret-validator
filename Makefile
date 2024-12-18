# Kind cluster name
KIND_CLUSTER_NAME := secret-validator-cluster
# Docker image name and tag
DOCKER_IMAGE := secret-validator:0.1.0
# Kind configuration file path
KIND_CONFIG := k8s/kind/kind-cluster.EXAMPLE.yaml
# Directory containing Kubernetes manifests
K8S_MANIFEST_DIR := k8s/

.PHONY: test-k8s create-kind build-docker load-docker apply-k8s

test-k8s: create-kind build-docker load-docker apply-k8s

create-kind:
	@if ! kind get clusters | grep -q $(KIND_CLUSTER_NAME); then \
		echo "Creating Kind cluster $(KIND_CLUSTER_NAME)..."; \
		kind create cluster --config=$(KIND_CONFIG) --name $(KIND_CLUSTER_NAME); \
	else \
		echo "Kind cluster $(KIND_CLUSTER_NAME) already exists."; \
	fi

build-docker:
	echo "Building Docker image $(DOCKER_IMAGE)..."
	docker build -t $(DOCKER_IMAGE) .

load-docker:
	echo "Loading Docker image $(DOCKER_IMAGE) into Kind cluster $(KIND_CLUSTER_NAME)..."
	kind load docker-image $(DOCKER_IMAGE) --name $(KIND_CLUSTER_NAME)

apply-k8s:
	echo "Applying Kubernetes manifests from directory $(K8S_MANIFEST_DIR)..."
	kubectl apply -f $(K8S_MANIFEST_DIR)

clean:
	echo "Deleting Kind cluster $(KIND_CLUSTER_NAME)..."
	kind delete cluster --name $(KIND_CLUSTER_NAME)
	echo "Removing Docker image $(DOCKER_IMAGE)..."
	docker image rm -f $(DOCKER_IMAGE) || true
	echo "Clean up completed."

clean-deployment:
	kubectl delete -f k8s/deployment.EXAMPLE.yaml
