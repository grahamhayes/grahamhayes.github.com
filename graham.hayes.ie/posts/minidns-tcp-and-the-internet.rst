.. title: MiniDNS, TCP, and the internet
.. slug: minidns-tcp-and-the-internet
.. date: 2016-03-04 20:50:00 UTC
.. tags: openstack, eventlet, networking, bugs
.. category: Designate
.. link:
.. description: Tracking down TCP send errors.
.. type: text

.. role:: python(code)
   :language: python


.. role:: bash(code)
   :language: bash


***************************************
MiniDNS, TCP, Eventlet and the internet
***************************************

We had `this bug <https://bugs.launchpad.net/designate/+bug/1552864>`_ come
in yesterday.

It was a bit unexpected - as we tested it pretty extensively when it was being
developed.

The line in question was this:

.. code-block:: python

    client.send(tcp_response)

In eventlet 0.17.x this behaved like the standard
:python:`socket.sendall()` , instead of :python:`socket.send()`

(It was `this commit`_ as it turns out - it was noted in the release notes `here`_ but we missed it)


The other major problem is that the bug did not manifest itself until we pushed
the AXFR over a long range connection.

.. TEASER_END

To test it, I booted a VM in West US (California I believe), installed designate
and populated a DB with a large zone using

.. listing:: generate-zone-rrsets.sh bash

Then from Dublin I started to run to see what was happening.

:bash:`dig @IP -p 5354 largetestzone.tld. AXFR`

.. code-block:: bash

    dig @IP -p 5354 largetestzone.tld. AXFR

What was interesting was that I had to get to 3 TCP messages before I started to see any issues,
and that those issues did not appear when I was testing from the same geographical region.

What did we learn
=================

* Network stuff is hard.
* Eventlet *will* change api's.
* Read Eventlet Release Notes

I think that we can start looking for ways to test this in the gate as well. having a gate check that loads
a large zone, adds latency + packet loss to fake a long range connection, and then ensures we
get a proper result from an API query would definitly catch real world errors like this.

If anyone wants to implement this, just hop in to `#openstack-dns`_  on freenode :)

Patches are definitly welcome.

Other Bugs Found
================

So, in the testing of this fix - we found a new bug. I am sure it will be the focus of a new blog (whenever we track it down)
but, it seems a large amount of traffic can cause eventlets :python:`socket.sendall()` to explode, and not send the complete traffic.

.. listing:: eventlet-sendall-bug-logs.log

We decided that as all of the DNS servers we support will retry, and designate has retry semantics for updates, we should be
OK merging this fix, and finding the new bugs root cause in the near future.


.. _this commit: https://github.com/eventlet/eventlet/commit/c315ee86dac996ac533b738f7c8777f4d01a0472
.. _here: http://eventlet.net/doc/changelog.html#id5

.. _#openstack-dns: irc://irc.freenode.net/openstack-dns
