## Catalog
This is the production version of the code from [Item Catalog](https://github.com/pekerow/item-catalog). Putting the application on a secure server requires us to configure a web server (Apache) and an acquire an SSL certificate. We must also migrate from SQLite to Postgresql. This process is detailed at the [linux-server-config](https://github.com/pekerow/linux-server-config) repo. As most of this work is done on the server side, very little of the original application code has been changed. I have set up this repo mainly for cloning purposes. Details about the application logic and the purpose of the web app are unchanged, and can be viewed at the original [Item Catalog](https://github.com/pekerow/item-catalog) 

## Summary of changes made
* Renamed ``catalog.py`` to ``__init__.py``, which wsgi looks for to run the Flask application logic.</p>

* In the files ``__init.py__``, ``catalog_setup.py`` and ``music.py``, ``engine = create_engine('sqlite:///musiccatalog.db')`` is changed to ``engine = create_engine('postgresql://catalog:catalog@localhost/catalog')``to replace SQLite with Postgresql. 

* The ``catalog_setup.pyc`` and ``music.db`` files used by SQLite have been deleted.

* The line ``h = httplib2.Http(".cache")`` is changed to ``h = httplib2.Http()`` because the argument ``.cache`` is optional. Its purpose is to enable a log, but this has been made redundant by the error log and access log files enabled in the ``catalog.conf`` file, which is used by Apache to serve the app.

* Changed ``from catalog_setup import Base, Genre, Album`` to ``from catalog.catalog_setup import Base, Genre, Album`` which is necessary after the switch from SQLite to Postgresql.

* Changed path of ``client_secrets.json`` in ``__init__.py`` to the absolute path of ``/var/www/catalog/client_secrets.json``.

* In ``__init__.py``, removed the parameters of the ``run()`` method.
