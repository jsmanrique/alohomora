# alohomora
Very SS (Simple and Stupid) app/mock to create configuration files for GrimoireLab

Requirements
------------

* [CouchDB](http://couchdb.apache.org/)
* [python-couchdb](https://pythonhosted.org/CouchDB/)

How it works
------------

Just launch it:

```shell
$ python app.py
```

Visit your *alohomora* website at `http://localhost:8080/`

You can add new projects, and for each of them add data sources and check configuration json file too.

Each project configuration is stored as a document in a CouchDB database. You can learn more about CouchBD here:

* http://docs.couchdb.org/en/stable/intro/
* http://docs.couchdb.org/en/stable/intro/

As you might see in the code, I am not a developer, so don't expect any good practice there.

ToDo
----

A lot! This is a *proof of concept* of how a configuration manager for [GrimoireLab](http://grimoirelab.github.io) could works

And, why *alohomora*
---------------------

According to [Wikipedia](https://en.wikipedia.org/wiki/List_of_spells_in_Harry_Potter#Alohomora), it stands for:
```
Used to open and/or unlock doors, but doors can be bewitched so that this spell has no effect
```

So, it is the tool to open the doors to Grimoire platform (AKA [GrimoireLab](http://grimoirelab.github.io))
