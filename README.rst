

Family Tree
===========

Author: Ashley Murphy

Email: amurphy9956@live.com

Description: This is a CLI application written in Python that allows you to query relationships on a family tree. You can also add a child to a couple and give a person a new spouse. Please see input instructions for more details.

Setup
-----

It is recommended you setup a virtual Python environment to use this application.

To install the **family_tree** application simply run the install.sh script in the main directory.

Once installed you can simply run the commands in the following section.

Commands
--------

Please note the following list of valid relationships:

- Mother
- Father
- Sons
- Daughters
- Grandfather
- Grandmother
- Grandsons
- Grandaughters
- Uncles
- Aunts
- Cousins
- Husband
- Wife
- Brothers
- Sisters

Querying the tree: *family_tree Person='Name' Relation='TypeOfRelation'* eg. Person=Alex Relation=Brothers

Adding a spouse: *family_tree Husband='Name' 'Wife=Name'* eg. Husband=Bern Wife=Julia

Adding a child: *family_tree Mother='Name' Son='Name'* eg. Mother=Julia Son=Boris

Data
----

The data the tree is based on is read from a JSON file located here: family_tree/data/tree.json

Project Strcuture
-----------------

proj root/
  -- data/
     -- tree.json
family_tree/
  -- tests/

  -- main python files

setup.py

requirements.py

install.sh

README.rst

Third Party Libraries
---------------------

- Pytest: Because it makes testing quicker and easier