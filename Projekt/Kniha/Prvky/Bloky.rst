Blokové prvky
=============

Blokové prvky mohou být vnořené (\ *nested*).

.. only:: extra

   :EXTRA: Něco extra!

.. contents:: Lokální obsah
   :local:
   :backlinks: none

.. index:: odstavec

Odstavce
--------

Odstavec je základ.
Text odstavce musí být zarovnán vlevo na stejné úrovni.

Další odstavec musí být oddělen aslespoň jedním prázdným řádkem.
Odstavce nezachovávají zalomení řádků.

Pokud chcete řádek zalomit natvrdo, |br| |lbr|
musíte použít *raw* substituci pro každý výstupní formát zvlášť.

Odstavce mohou obsahovat :doc:`řádkové prvky jako třeba odkaz <Inline>`.

Seznamy
-------

Nečíslovaný seznam: [#lists]_

- A bullet list

  + Nested bullet list.
  + Nested item 2.

- Item 2.

  Paragraph 2 of item 2.

  * Nested bullet list.
  * Nested item 2.

    - Third level.
    - Item 2.

  * Nested item 3.

.. kotva bloku (zde před odstavcem):

.. _cislovany-seznam:

Číslovaný seznam: [#lists]_

1. Arabic numerals.

   a) lower alpha)

      (i) (lower roman)

          A. upper alpha.
             (Po tuto úroveň to zvládne LaTeX ve výchozím nastavení.)

..             I) upper roman)

2. Lists that don't start at 1:

   3. Three

   4. Four

   C. C

   D. D

   iii. iii

   iv. iv

#. List items may also be auto-numbered.

.. [#lists] Styl výsledného odrážkování nebo číslování seznamů závisí na stylu
   výstupního formátu.

Obrázky
--------

Obrázek |obr| na řádku pomocí substituce (viz `Epilog`_).

Obrázek obyčejný (image):

.. image:: /obrazky/obrazek.png
   :scale: 80 %

.. only:: format_latex

   |lpage|

Obrázek s titulkem (figure):

.. figure:: /obrazky/obrazek.png
   :align: center
   :scale: 50 %

   Titulek

   A legenda, ve které můžou být další bloky, např.

   * seznam


Tabulky
--------

* Implicitní (ASCII), viz `Grid and Simple Table
  <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#tables>`_
* Explicitní (direktivy), viz `CSV and List Table
  <http://docutils.sourceforge.net/docs/ref/rst/directives.html#tables>`_

Jednoduchá tabulka pomocí seznamu (list table):

.. LaTeX: určení šířky sloupců (musí být těsně před tabulkou)

.. tabularcolumns:: |p{0.15\textwidth}|p{0.79\textwidth}|
.. list-table::
   :header-rows: 1
   :widths: 20, 80

   * - Název
     - Identifikátor
   * - Funkce
     - \urn:my:python:func
   * - Proměnná
     - \urn:my:python:var
   * - Modul
     - \urn:my:python:mod

Výpis kódu
----------

.. code-block:: Python
   :caption: Příklad definice funkce
   :linenos:

   def print_greeting(greeting):
      print(greeting)

   print_greeting("Hello World!")

Upozornění (admonitions)
------------------------

.. Warning:: Pokud odpojíte disk z elektřiny, můžete přijít o data!

.. Important:: Po prvním přihlášení si změňte heslo!

.. Note:: Blokové prvky mohou být vnořené, je potřeba si ohlídat odsazení.

   Jako třeba tady.

.. Tip:: To si zapište za uši.

Surový obsah
------------

.. only:: format_html

   HTML výstup:

   .. raw:: html

      <hr width=50 size=10>

.. only:: format_latex

   LaTeX výstup:

   .. raw:: latex

      \rule{0.5cm}{0.5cm}

Surová data lze i načíst ze souboru, např.::

   .. raw:: html
      :file: inclusion.html


Epilog
------

Substituce obrázku (definice nic neprodukuje)

.. |obr| image:: /obrazky/ikona16.png
