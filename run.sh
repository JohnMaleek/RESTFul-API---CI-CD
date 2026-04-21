#!/bin/bash
echo "starting api.."
docker run -d -p 5001:5000 --name myapi myapi 
echo"API running on port 5000"

