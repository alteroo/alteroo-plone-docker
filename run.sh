# Sets permission in docker container
setfacl  -R -m u:500:rwX src/
setfacl -dR -m u:500:rwX src/
getfacl src/ 
# Runs container
docker run -p 8080:8080 -v $(pwd)/src/flyjamaica.site:/plone/instance/src/flyjamaica.site -e ADDONS="flyjamaica.site" -e DEVELOP="src/flyjamaica.site" -v $(pwd)/buildout.cfg:/plone/instance/buildout.cfg plone:5 fg
