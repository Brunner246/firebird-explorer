FROM jacobalberty/firebird:latest

ENV ISC_PASSWORD masterkey

COPY database/CONTENT_3D.FDB /firebird/data/

EXPOSE 3050


# docker build -t cw-firebird-db .
# docker run -d -p 3050:3050 --name cw-firebird-db cw-firebird-db
# check if container runs => docker ps