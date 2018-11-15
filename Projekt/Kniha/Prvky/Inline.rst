Řádkové prvky
=============

V textu můžete *slabě* nebo **silně** zvýraznit úseky textu.
Dokonce i v rámci jednoho slova, např. re\ **Structured**\ Text.
Když potřebujete hvězdičku nebo jiný řídící znak, tak použijte zpětné lomítko
k odescapování, např.: ``\*`` -> \*

Když vás nebaví opakovaně psát něco tak dlouhého jako je |rst|,
použijte substituci [#pozn]_ (odkaz na poznámku pod čarou).

.. only:: extra

   :EXTRA: Něco extra!

Základní
--------

.. list-table::
   :header-rows: 1

   * - Název
     - Implicitní zápis
     - Explicitní zápis
     - Výstup
   * - Literál/kód
     - ````print()````
     - ``:code:`print()```
     - :code:`print()`
   * - Slabé zvýraznění
     - ``*slabé*``
     - ``:emphasis:`slabé```
     - :emphasis:`slabé`
   * - Silné zvýraznění
     - ``**silné**``
     - ``:strong:`silné```
     - :strong:`silné`
   * - Dolní index (subscript)
     - ---
     - ``H\ :sub:`2`\ O``
     - H\ :sub:`2`\ O
   * - Horní index (superscript)
     - ---
     - ``2\ :sup:`8` = 256``
     - 2\ :sup:`8` = 256


Odkazy a reference
------------------

Implicitní:

* parsované z URI
   - URL http://example.com
   - URN urn:my:python:mod
* `Example.com <http://example.com>`_ (externí odkaz)
* `Řádkové prvky`_ (lokální nadpis)

Explicitní -- role:

* ``:ref:`identifikator-kotvy```, ``:ref:`popisek <identifikator-kotvy>```
   - např. :ref:`odkaz na odstavec <cislovany-seznam>`
* ``:doc:`/Cesta/k/Dokumentu```, ``:doc:`popisek </Cesta/k/Dokumentu>```
   - např. :doc:`odkaz na hlavní stránku dokumentace </index>`

Sémantika
----------

Odkaz do slovníku: ``:term:`pojem``` -> :term:`pojem`

Zkratka: ``:abbr:`LIFO (last-in, first-out)``` -> :abbr:`LIFO (last-in, first-out)`

Cesta k souboru: ``:file:`/usr/lib/python2.{x}/site-packages``` -> :file:`/usr/lib/python2.{x}/site-packages`

Popisek v GUI: ``:guilabel:`Odeslat``` -> :guilabel:`Odeslat`

Výběr z menu: ``:menuselection:`Menu --> Submenu --> Item``` -> :menuselection:`Menu --> Submenu --> Item`

A mnoho dalších.

Epilog
------

Substituce textu (definice nic neprodukuje)

.. |rst| replace:: reStructuredText

Poznámka pod čarou (definice)

.. [#pozn] Substituce musí být definována lokálně, je jedno kde.

   Poznámka pod čarou v HTML zůstane na místě, kde byla uvedena její definice.
