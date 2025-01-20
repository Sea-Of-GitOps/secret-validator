package main

import (
	"log"
	"secret-validator/clients"
)

func main() {
	config, err := clients.GetClusterConfig()
	if err != nil {
		log.Fatalf("Errore nel caricare la configurazione del cluster: %v", err)
	}

	log.Println(config)
}
