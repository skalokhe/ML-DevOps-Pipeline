#!/bin/bash
vault server -config=secrets/hashicorp/vault_config.json &
sleep 5
vault operator init > vault_init.txt
vault operator unseal $(grep 'Unseal Key 1:' vault_init.txt | awk '{print $4}')
vault login $(grep 'Initial Root Token:' vault_init.txt | awk '{print $4}')
