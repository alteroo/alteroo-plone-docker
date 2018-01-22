# Alteroo-Docker

A working example of `docker.plone` with add-on development for Alteroo.

## How does it work?

`run.sh` starts a plone container with local add-on source and `buildout.cfg` mounted as docker volumes.

[here](https://community.plone.org/t/docker-and-plone-for-add-on-development/5094/11).

```bash
docker run -p 8080:8080 -e ADDONS="flyjamaica.site" \
                        -e DEVELOP="src/flyjamaica.site" \
                        -v $(pwd)/src/flyjamaica.site:/plone/instance/src/flyjamaica.site \ 
                        -v $(pwd)/buildout.cfg:/plone/instance/buildout.cfg \
                        plone:5 fg

```

## Author
- [Jordan Jones](https://github.com/Pr0x1m4)