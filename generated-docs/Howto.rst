

Jak na to
=========

Tato sekce shrnuje základní postup pro generování dokumentace z kódu v Pythonu.
Python obsahuje podporu pro dokumentování API přímo v kódu zvanou *docstrings*
[DOCSTR]_. *Docstrings* se mohou vztahovat k balíku, modulu, třídě nebo funkci.

Jak dokumentovat Pythoní kód viz např. článek https://realpython.com/documenting-python-code/.

.. Important::

   Pokud mají dokumentované moduly externí závislosti, musí být nainstalované!

   Pro náš ukázkový modul :file:`TestingBotTestCase.py` doinstalujte:

   .. code-block:: bash

      pip install selenium
      pip install testingbotclient

#. V dokumentačním projektu spusťte aplikaci :program:`Apidoc`:

   .. code-block:: bash

      sphinx-apidoc -o modules/ ../python-modules/

   :program:`Apidoc` předgeneruje do adresáře :file:`modules` samo-dokumentovací
   prostředky podle struktury modulů v :file:`../python-modules`
   a vytvoří pro ně obsah ``toctree`` v souboru :file:`modules.rst`,
   který lze přidat do dokumentace například jako samostatnou kapitolu.

   V naší ukázce jsme do ``toctree`` v *master dokumentu* projektu
   (:file:`index.rst`) přidali položku :file:`modules/modules`.

#. Upravte konfiguraci v :file:`conf.py`:

   *Nastavení cesty* – Přidejte do ``sys.path`` adresář s dokumentovanými moduly,
   např. :file:`../python-modules/`:

   .. code-block:: python

      import os
      import sys
      sys.path.insert(0, os.path.abspath('../python-modules'))

   *Rozšíření* – Do seznamu ``extensions`` přidejte rozšíření **sphinx.ext.autodoc**:

   .. code-block:: python

      extensions = [
          'sphinx.ext.autodoc'
      ]

#. Spusťte :program:`build`, např.:

   .. code-block:: bash

      make html

   :program:`Build` vytahá *docstrings* z nakonfigurovaných modulů do výstupu.
   Pro ukázku vizte :doc:`modules/modules`.

.. Note:: Viz také:

   * :pep:`0257` -- obecné konvence *docstrings*
   * :pep:`0287` -- adopce rST jako standardního formátu pro *docstrings*

.. [DOCSTR]
   Documentation Strings.
   `Python Tutorial
   <https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings>`_
