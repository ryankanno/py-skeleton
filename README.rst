py-skeleton
===========

.. image:: https://travis-ci.org/ryankanno/py-skeleton.png?branch=master
   :target: https://travis-ci.org/ryankanno/py-skeleton

.. image:: https://coveralls.io/repos/ryankanno/py-skeleton/badge.png
   :target: https://coveralls.io/r/ryankanno/py-skeleton

Are you:

- Starting new projects by copying old ones?
- Wishing you could use someone else's project as a starter template?
- Confused at how to start "Project FooBar"?

I'm always starting a new python projects by cutting and pasting an old one.
py-skeleton helps you fix that.  Uses `jinja2 <http://jinja.pocoo.org/>`_
and `py-configurator <https://github.com/ryankanno/py-configurator>`_.

basic usage
===========

.. code:: bash

    py-skeleton.py --source ../py-skeleton-templates/python/
                   --ext .tmpl
                   --destination ./build
                   --config ./python.ini

- --source is the directory path to your templates
- --ext is the extension path for your templates
- --destination is the directory path to where everything will end up
- --config is the file path to where your configuration file lives

todo
====

- logging
- add other project templates I use
