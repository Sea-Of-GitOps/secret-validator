package clients

import (
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
	"log"
)

func GetClusterConfig() (*rest.Config, error) {
	config, err := rest.InClusterConfig()
	if err != nil {
		log.Fatalf("Error duriing cluster configuration: %v", err)
	}
	return config, nil
}

func NewClientset(config *rest.Config) (*kubernetes.Clientset, error) {
	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		log.Fatalf("Errore nel creare il clientset: %v", err)
	}
	return clientset, nil
}
