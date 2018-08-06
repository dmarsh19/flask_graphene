#!/bin/bash

as_root()
{
  # Make sure we are root
  if [ $(id -u) -ne 0 ]
    then
      echo "Insufficient privileges."
      exit -1
  fi
}
as_root

PROJECT_NAME=flask_graphene
SRV_DEST=/srv/nginx/${PROJECT_NAME}_project

python3 -m pip install -r requirements.txt

mkdir -m 0755 $SRV_DEST
cp -r ${PROJECT_NAME} settings.py wsgi.py ${PROJECT_NAME}.ini atmo.sqlite $SRV_DEST
chown -R www-data:www-data $SRV_DEST

mkdir -m 0740 /var/log/${PROJECT_NAME}
chown -R www-data:www-data /var/log/${PROJECT_NAME}

cp ${PROJECT_NAME}.service /etc/systemd/system
systemctl start ${PROJECT_NAME}

cat > /etc/nginx/sites-available/${PROJECT_NAME} << EOF_NGINX
server {
    listen 80;
    server_name localhost;

    location ~ /? {
        include uwsgi_params;
        uwsgi_pass unix:/tmp/${PROJECT_NAME}-uwsgi.sock;
    }
}

EOF_NGINX

ln -s /etc/nginx/sites-available/${PROJECT_NAME} /etc/nginx/sites-enabled/${PROJECT_NAME}
rm /etc/nginx/sites-enabled/default

# test syntax errors
sudo nginx -t

systemctl restart nginx
systemctl restart flask_graphene
systemctl daemon-reload

exit 0

