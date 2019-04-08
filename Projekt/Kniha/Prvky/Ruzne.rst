Různé
======

.. only:: extra

   :EXTRA: Něco extra!

.. contents:: Lokální obsah
   :local:
   :backlinks: none

Dvojice pro křížové odkazy
---------------------------

Kotvy
^^^^^

Každý nadpis je lokální kotva, např. `Domény`_.

In-line kotva (lokální, rST)::

   This is what an _`inline internal target` looks like.

   Link to the target like this `inline internal target`_.

.. _identifikator-kotvy:

Explicitní kotva na blok (i bez nadpisu, globální, Sphinx)::

   .. _identifikator-kotvy:

   Blok (např. odstavec nebo obrázek)

Reference na :ref:`blokovou kotvu <identifikator-kotvy>`.

Poznámka pod čarou
^^^^^^^^^^^^^^^^^^

.. todo::

   Definice::

      kod

   Reference::

      kod

Citace
^^^^^^

.. todo::

   Definice::

      kod

   Reference::

      kod



Slovník
^^^^^^^

glossary + term

.. todo::

   Definice::

      kod

   Reference::

      kod


.. index::
   pair: rejstřík; tvorba

Obecný rejstřík
^^^^^^^^^^^^^^^

Tohle je normální :index:`odstavec`, který obsahuje několik
:index:`položek rejstříku <pair: rejstřík; položka>`.

.. only:: format_html

   :ref:`Odkaz na obecný rejstřík <genindex>`


Domény
------

.. code-block:: rst

   .. py:function:: pyfunc(ppp)

      Popisuje funkci v Pythonu.

      :param str ppp: Popis parametru

   Reference na :py:func:`pyfunc`.

.. py:function:: pyfunc(ppp)

   Popisuje funkci v Pythonu.

   :param str ppp: Popis parametru

Reference na :py:func:`pyfunc` (název funkce uvést bez závorek).



