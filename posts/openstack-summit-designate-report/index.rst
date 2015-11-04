.. title: OpenStack Summit - Designate Report
.. slug: openstack-summit-designate-report
.. date: 2015-11-04 21:18:41 UTC
.. tags: openstack, summit, travel, tokyo
.. category: OpenStack
.. link:
.. description: My overview of Tokyo, and what happened at the Mitaka Design Summit
.. type: text

Where to start?

Tokyo
=====

Oh, what a place. I thought I was ready for the experience, but this city has
to be visited to understand. From the 2 or 3 different metro systems that snake
across the city, to the 9 story electronics stores, it is something else.

Living in a city that has 3 metro lines that don't actually connect it was a nice
change to be able to get reliable public transport :).

Design Summit
=============

This was a much more relaxed summit for Designate. We had done a huge amount of
work in Vancouver, and we were nailing down details and doing cross project work.

We got a few major features discussed, and laid out our priorities for the next cycle.

We decided on the following:

1. Nova / Neutron Integration
2. Pool Scheduler
3. Pool Configuration migration to database
4. IXFR (Incremental Zone Transfer)
5. ALIAS Record type (Allows for CNAME like records at the root of a DNS Zone)
6. DNSSEC (this may drag on for a cycle or two)

Nova & Neutron Integration
--------------------------

This is progressing pretty well, and Miguel Lavalle has patches up for this. He,
Kiall Mac Innes and Carl Baldwin demoed this in a session on the Thursday. If
you are interested in the idea, it is definitely worth a watch `here`_

Pool Scheduler
--------------

A vital piece of the pools re architecture that needs to be finished out.
There is no great debate on what we need, and I have taken on the task of
finishing this out.

Pool Configuration migration to database
----------------------------------------

Are current configuration file format is quite complex, and moving it to an API
allows us to iterate on it much quicker, while reducing the complexity of the
config file. I recently had to write an ansible play to write out this file, and
it was not fun.

Kiall had a patch up, so we should be able to continue based on that.

IXFR
----

There was quite a lot of discussion on how this will be implemented, both in the
work session, and the 1/2 day session on the Friday. Tim Simmons has stepped up,
to continue the work on this.

ALIAS
-----

This is quite a sort after feature - but is quite complex to implement.
The DNS RFCs explicitly ban this behavior, so we have to work the solution
around them. Eric Larson has been doing quite a lot of work on this in Liberty,
and is going to continue in Mitaka.

DNSSEC
------

This is a feature that we have been looking at for a while, but we started to plan
out our roadmap for it recently.

We (I) am allergic to storing private encryption keys in Designate, so we had a
good conversation with Barbican about implementing a signing endpoint that we would
post a hash to. This work is on me to now drive for Mitaka, so we can consume it in N.

There is some raw notes in the `etherpad`_ and I expect we will soon be seeing
specs building out of them.

.. _etherpad: https://etherpad.openstack.org/p/mitaka-designate-summit-roadmap
.. _here: http://https://www.youtube.com/watch?v=AZbiARM9FPM