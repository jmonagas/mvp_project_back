import bjoern
from app import app
host = "0.0.0.0"
port = 5008

print("Bjoern is up and running")
bjoern.run(app, host, port)



# pm2 start /var/www/jmonagas-mvp-full-stack.ml/api/serve.py --interpreter "/var/www/jmonagas-mvp-full-stack.ml//api/venv/bin/python3.8" --name the-name-of-the-URL-goes-here


# https://jmonagas-mvp-full-stack.ml/


# <VirtualHost *:80>
#   ServerName jmonagas-mvp-full-stack.ml
#   ServerAlias www.jmonagas-mvp-full-stack.ml
#   Redirect permanent / https://jmonagas-mvp-full-stack.ml
# </VirtualHost>

# <VirtualHost *:443>
#   ServerName jmonagas-mvp-full-stack.ml
#   ServerAlias www.jmonagas-mvp-full-stack.ml
#   DocumentRoot "/var/www/jmonagas-mvp-full-stack.ml/mvp2dist"

#   ProxyPreserveHost On
#   ProxyPass /api http://127.0.0.1:5008/api
#   ProxyPassReverse /api http://127.0.0.1:5008/api

#   SSLEngine On
#   SSLCertificateFile /etc/letsencrypt/live/jmonagas-mvp-full-stack.ml/fullchain.pem
#   SSLCertificateKeyFile /etc/letsencrypt/live/jmonagas-mvp-full-stack.ml/privkey.pem
# </VirtualHost>