import bjoern
from app import app
host = "0.0.0.0"
port = 5008

print("Bjoern is up and running")
bjoern.run(app, host, port)



# pm2 start /var/www/the-name-of-the-URL-goes-here/api/serve.py --interpreter "/var/www/the-name-of-the-URL-goes-here/api/venv/bin/python3.8" --name the-name-of-the-URL-goes-here


# https://jmonagas-mvp-full-stack.ml/