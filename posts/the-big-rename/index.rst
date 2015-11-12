.. title: The Big Rename - why?
.. slug: the-big-rename
.. date: 2015-11-09 19:52:03 UTC
.. tags: openstack, designate, code, refactor
.. category: OpenStack
.. link:
.. description: Why are we doing such a big refactor?
.. type: text
.. previewimage: https://upload.wikimedia.org/wikipedia/commons/1/1a/Code.jpg

Update
======

Due to unforeseen circumstances I will not be able to continue work on this until
Monday, so we will have to extend the freeze until Tuesday the 17th.

The following message will be put on the patches affected by the freeze.

.. listing:: big-rename-2-update-message.txt text

.. image:: https://upload.wikimedia.org/wikipedia/commons/1/1a/Code.jpg

[1]_

The Big Rename
==============

So from tomorrow (2015-11-10) until Friday (2015-11-13) Designate will be frozen for new code.

I send an email to the openstack-dev list before the summit `[2]`_ so, it shouldn't be a surprise (I hope)

So, why are we doing this?

When Designate started it had a v1 API, which used the term domains for DNS Domains. This was pre Keystone's Domain support, but unfortunately they also decided to use it. AS Designate was not even incubated at the time, there was not much we could do, but continue on.

When we started the v2 API, we decided to avoid confusion and expose "Domains" as "Zones".

This worked for a while, but as we worked on the V2 API, we had to write code to translate the internal code (which referenced Domains) to Zones. this caused code like:

.. listing:: big-rename-render.py python

and

.. listing:: big-rename-error-render.py python


which proved to be quite fragile. (Yes that last bit of code is trying to walk the error path of a JSONSchema Error and rename the path to the new terminology)

We are also logging messages about domains - which could prove to be quite confusing when we remove the v1 API and users are only interacting with zones.

So tomorrow morning-ish (UTC) we will start to rename every occurrence of "domain" in the code base to "zone" (without breaking Keystone domain support).

Anything that does not have the "the-big-rename" topic on Gerrit will be getting a procedural -2 from me or the designate-core team.

.. listing:: big-rename-2-message.txt text


.. [1] By Crusher95 (Own work) [CC BY-SA 4.0 (http://creativecommons.org/licenses/by-sa/4.0)], via Wikimedia Commons
.. _[2]: http://lists.openstack.org/pipermail/openstack-dev/2015-October/077442.html