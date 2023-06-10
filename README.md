# API for shortening URLs and redirects

This project was raised as a coding interview problem.

## The problem

Unser Kunde benötigt einen Service, der eine API bereitstellt, um aus gegebenen URLs mit
Metadaten eine Short-URL erzeugt. Beim Aufruf der Short-URL soll der Benutzer auf die Ziel-URL
weitergeleitet werden.


Zur Umsetzung gibt es folgende Rahmenbedingungen:
- Python-basierter Web-Service
- REST API zur Verwaltung von URLs (CRUD) inkl. Short-URL Generierung mit Redirect-Möglichkeit
- Um Auswertungen zu ermöglichen soll die Klicks auf die Short-URL getrackt werden
- Die Request/Response Strukturen des Services sollten im JSON Format sein
- Daten sollen in einer beliebigen Datenbank gespeichert werden

Der Service sollte folgende fachlichen Operationen ermöglichen
- Auflisten aller bisherigen URLs mit Metadaten, z.B. Bezeichner, Lang URL, Short-URL, Identifier, Erstellungsdatum, Anzahl Zugriffe
- Anlegen einer neuen Short-URL
- Löschen einer Short-URL
- Zugriff auf die Metadaten einer Short-URL
- Auflösen der Short-URL mit Redirect auf Ziel URL.

Der Service soll als Docker Container zur Verfügung gestellt werden.

## Notes

### apis

Most used http methods:

* post: to create data
  * @app.post()
* get: to retrieve data
  * @app.get()
* put: to update data
  * @app.put()
* delete: to remove data
  * @app.delete()

### curl request

* curl -X GET http://127.0.0.1/
* curl -X POST http://127.0.0.1/0

### pydantic

* performs data validation
* can be used to declare request bodies

### mariadb

* start container
  * podman run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -v ./data:/var/lib/mysql -d docker.io/library/mariadb
* connect to container:
  * podman exec -it mariadbtest bash
* connect to it mysql -h 127.0.0.1 -u root -p

### podman build container

* podman build -f ./DOCKERFILE -t mypyapp

### podman commands

* podman run --network="host" mypyapp:latest

## tox

Install via

`pip install tox`

Run via

`tox run [-e environment]`

# Usage

Install the application via

`pip install .`

and run it by executing:

`run_app`