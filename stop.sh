#!/bin/bash
echo "stopping api.."
docker stop myapi
docker rm myapi
echo "API stopped"

