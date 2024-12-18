KIND_CLUSTER_NAME := secret-validator-cluster
DOCKER_IMAGE := secret-validator:0.1.0
KIND_CONFIG := k8s/kind/kind-cluster.EXAMPLE.yaml
K8S_MANIFEST_DIR := k8s/
NAMESPACE = secret-validator-ns

.PHONY: all clean test test-k8s create-kind build-docker load-docker apply-k8s port-forward-service-k8s

all: create-kind build-docker load-docker clean-deployment apply-k8s

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

port-forward-service-k8s:
	kubectl port-forward svc/secret-validator-service 5000:5000 -n $(NAMESPACE)

clean:
	echo "Deleting Kind cluster $(KIND_CLUSTER_NAME)..."
	kind delete cluster --name $(KIND_CLUSTER_NAME)
	echo "Removing Docker image $(DOCKER_IMAGE)..."
	docker image rm -f $(DOCKER_IMAGE) || true
	echo "Clean up completed."

clean-deployment:
	@if kubectl get deployment secret-validator-service -n $(NAMESPACE) > /dev/null 2>&1; then \
		echo "Deleting deployment..."; \
		kubectl delete -f k8s/deployment.EXAMPLE.yaml; \
	else \
		echo "Deployment not found, nothing to delete."; \
	fi

create-secrets:
	@echo "Creating secrets with expiration dates in namespace $(NAMESPACE)"
	@kubectl create secret generic service-a-secrets --from-literal=certs-expiration=$(shell date -d '+1 year' --utc +%Y-%m-%dT%H:%M:%S%z) --namespace=$(NAMESPACE) --dry-run=client -o yaml | kubectl apply -f -
	@kubectl create secret generic service-b-secrets --from-literal=certs-expiration=$(shell date -d '+2 days' --utc +%Y-%m-%dT%H:%M:%S%z) --namespace=$(NAMESPACE) --dry-run=client -o yaml | kubectl apply -f -
	@kubectl create secret generic service-c-secrets --from-literal=certs-expiration=$(shell date -d '+7 days' --utc +%Y-%m-%dT%H:%M:%S%z) --namespace=$(NAMESPACE) --dry-run=client -o yaml | kubectl apply -f -
	@kubectl create secret generic service-d-secrets --from-literal=certs-expiration=$(shell date -d '-1 day' --utc +%Y-%m-%dT%H:%M:%S%z) --namespace=$(NAMESPACE) --dry-run=client -o yaml | kubectl apply -f -
	@echo "Secrets created and applied successfully"

clean-secrets:
	@echo "Cleaning up secrets in namespace $(NAMESPACE)"
	@kubectl delete secret service-a-secrets --namespace=$(NAMESPACE) || echo "service-a-secrets not found"
	@kubectl delete secret service-b-secrets --namespace=$(NAMESPACE) || echo "service-b-secrets not found"
	@kubectl delete secret service-c-secrets --namespace=$(NAMESPACE) || echo "service-c-secrets not found"
	@kubectl delete secret service-d-secrets --namespace=$(NAMESPACE) || echo "service-d-secrets not found"
	@echo "Secrets deleted successfully"
