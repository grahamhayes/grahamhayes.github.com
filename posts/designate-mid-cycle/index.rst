.. title: Designate Mid Cycle
.. slug: designate-mid-cycle
.. date: 2016-02-24 22:55:00 UTC
.. tags: openstack, summit, travel, galway
.. category: OpenStack
.. link:
.. description: What happened at the Designate mid cycle
.. type: text
.. previewimage: http://photos.gra.ham.ie/Designate-Mid-Cycle/i-S96NrNb/0/O/IMG_3854.jpg

.. image:: http://photos.gra.ham.ie/Designate-Mid-Cycle/i-S96NrNb/0/O/IMG_3854.jpg

*******************
Designate Mid Cycle
*******************

This was a little over a week ago, and I have been trying to get my thoughts down on
paper /  rst.

It was a good few days overall - we had our usual arguements about implementation of some
familiar features, we listed out reasons that our past selves were wrong about everything,
and how we should fix our mistakes.

.. TEASER_END

We actually kicked off a day earlier than expected - using a big table in the lobby of
the hotel as a confernce room :)

.. image:: https://pbs.twimg.com/media/CaoO47bWcAAzjU7.jpg:large

*Unoffical Day 0 conference room*

We planned what we thought we were going to do, and how long we thought it would
take - roughly. We had gathered feedback about what topics were important before hand on
an `etherpad`_ so we broke it down into half day buckets, while trying to avoid getting
into the discussion there and then. (Which, as you can imagine, is a lot easier said than done)

Monday
======

One of the most contraversial (based on how we would implment it) proposals was
`timsim`_'s Worker Model.

We had started to build bespoke services to cover different needs,
(pool-manager and zone-manager for starters) but it causes issues when we try to give
scaling advice to people, as some will need more zone-manager's while others will
need more mini-dns and pool-manager instances.

Tim had a very good spec for this - it is under final review `here`_

From that spec the new designate would be:

New  Architecture
-----------------

-  ``designate-api`` - To receive JSON and parse it for Designate
-  ``designate-central`` - To do validation/storage of zone/record data and
   send send CRUD tasks to ``designate-worker``.
-  ``designate-mdns`` - To **only** perfrom AXFRs from Designate's database
-  ``designate-worker`` - Any and all tasks that Designate needs to
   produce state on nameservers
-  ``designate-producer`` - To run periodic/timed jobs, and produce work
   for ``designate-worker`` that is out the normal path of API operations.
   For example: Periodic recovery.

Other necessary components:

-  Queue - Usually RabbitMQ
-  Database - Usually MySQL
-  Cache - (encouraged, although not necessary) Memcached, MySQL, Redis
-  A ``tooz`` backend (Zookeeper, Memcached, Redis)

This also has the nice side effect of no longer needing a mini-dns RPCAPI.
Long term, we all acknowledge that we will need to rewrite the mini-dns component
in something faster (Go, C/C++, Rust have all been proposed), and having to
write a compatibility layer for oslo.messaging in another language was not a small
task. [1]_

It allows mini-dns to just worry about serving DNS data (like a DNS Server should).

NIH Syndrome or Efficient ?
---------------------------

The next item up was "how ?". We have multiple libraries availible for doing
distributed tasks - there is even one in OpenStack itself - `TaskFlow`_ .

There was discomfort over using the extra complexity of TaskFlow vs a small
homegrown system that could just use tools like olso.messaging and rpc casts.

For this we had to try and map out the "flows" for each of our tasks. We
realised that some of our flows actually had a lot more moving parts than we expected

.. image:: http://photos.gra.ham.ie/Designate-Mid-Cycle/i-MkDmj2D/0/L/IMG_3847-3-L.jpg

*a flow that was more complex than we expected*


This is where the majority of the discussion went - there were proposals for many
libraries, and for writing our own. We decided that we should do some base
implementation testing later on in the week.

The session notes are here: `mid-cycle-workers`_

Tuesday
=======

We ran though a few proposals that were had implementation questions like
how we avoid the **stampeding herd** problem for nameserver changes. These were
done with fairly easily.

We also agreed on a few API additions (no breaking changes :))

API Changes
-----------

New Resource at the base of the API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We agreed to add a new */recordsets*  endpoint, which will show a user all the
recordsets that they have across all zones.

This will allow users to filter across all recordsets for data, for example if
a user wanted to see where they had used 8.8.8.8 they could do the following:

.. code-block:: http

    GET http://127.0.0.1:9001/v2/recordsets?data=8.8.8.8 HTTP/1.1
    Host: 127.0.0.1:9001
    Accept: application/json
    Content-Type: application/json

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "recordsets": [
            {
                "description": "This is an example record set.",
                "links": {
                    "self": "https://127.0.0.1:9001/v2/zones/2150b1bf-dee2-4221-9d85-11f7886fb15f/recordsets/f7b10e9b-0cae-4a91-b162-562bc6096648"
                },
                "updated_at": null,
                "records": [
                    "8.8.8.8"
                ],
                "ttl": 3600,
                "id": "f7b10e9b-0cae-4a91-b162-562bc6096648",
                "name": "service.other-example.net.",
                "zone_id": "2150b1bf-dee2-4221-9d85-11f7886fb15f",
                "created_at": "2010-01-54T17:49:27.000000",
                "version": 13,
                "type": "A"
            },
            {
                "description": "This is an example record set.",
                "links": {
                    "self": "https://127.0.0.1:9001/v2/zones/249502fa-620d-458f-8e29-9ecfc732c357/recordsets/e88f64d0-71ab-423e-9d84-eb8d76b51938"
                },
                "updated_at": null,
                "records": [
                    "8.8.8.8"
                ],
                "ttl": 3600,
                "id": "e88f64d0-71ab-423e-9d84-eb8d76b51938",
                "name": "service.example.org.",
                "zone_id": "249502fa-620d-458f-8e29-9ecfc732c357",
                "created_at": "2014-10-24T19:59:44.000000",
                "version": 25,
                "type": "A"
            }

        ]

    }


Add Serial to the recordset data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Internally within Designate we track the serial number for the last time a
recordset was updated. We decided to show that in the new response:

.. code-block:: json

    {
        "description": "This is an example record set.",
        "links": {
            "self": "https://127.0.0.1:9001/v2/zones/249502fa-620d-458f-8e29-9ecfc732c357/recordsets/e88f64d0-71ab-423e-9d84-eb8d76b51938"
        },
        "updated_at": null,
        "records": [
            "8.8.8.8"
        ],
        "ttl": 3600,
        "id": "e88f64d0-71ab-423e-9d84-eb8d76b51938",
        "serial": 1456351502,
        "name": "service.example.org.",
        "zone_id": "249502fa-620d-458f-8e29-9ecfc732c357",
        "created_at": "2014-10-24T19:59:44.000000",
        "version": 25,
        "type": "A"
    }

Structured Data for Recordsets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

And, for the *n-th* time we looked at structured data.

We have always wanted this - the `spec`_ has been around for a while - but we can seem to
find a way to allow for updates to the data.

It would allow us to do some nice things like break the record data up into meaningful
chunks (for people who do not know DNS RFC off the top oof their heads :) ) - for example:

.. code-block:: http

    GET /v2/zones/2150b1bf-dee2-4221-9d85-11f7886fb15f/recordsets/f7b10e9b-0cae-4a91-b162-562bc6096648 HTTP/1.1
    Host: 127.0.0.1:9001
    Accept: application/vnd.openstack.dns-v2+json

.. code-block:: http

    HTTP/1.1 200 OK
    Vary: Accept
    Content-Type: application/vnd.openstack.dns-v2+json

    {
        "description": "This is an example recordset.",
        "links": {
            "self": "https://127.0.0.1:9001/v2/zones/2150b1bf-dee2-4221-9d85-11f7886fb15f/recordsets/f7b10e9b-0cae-4a91-b162-562bc6096648"
        },
        "updated_at": null,
        "records": [
            {
                "algorithm": 1,
                "fp_type": 1,
                "fingerprint": "253d9636219be6aec03d06359837e0604b370372"
            }
        ],
        "ttl": 3600,
        "id": "f7b10e9b-0cae-4a91-b162-562bc6096648",
        "name": "example.org.",
        "zone_id": "2150b1bf-dee2-4221-9d85-11f7886fb15f",
        "created_at": "2014-10-24T19:59:44.000000",
        "version": 1,
        "type": "SSHFP"
    }


OpenStack Ireland Meetup Group
------------------------------

As there was a mid cycle in Ireland (that doesn't happen very much) we arranged for
a meetup evening for the OpenStack Ireland group.

Myself, `timsim`_, and `ionrock`_ gave a a `talk`_ about designate and a *live demo* [2]_

Wednesday
=========

We decided that we should dedicate Wednesday for actaully impmlementing something.
We got a bit done - the start of loading multiple pools into the DB with a sane syntax
(not the crazy stuff we have now),
a scheduler for allowing zones to cross pools, a method of designate services reporting
back with how healthy they are, and some new libraries for tasks like `ionrock`_'s `taskin`_ .


Thursday
========

We got lost in the floods in the west.

.. image:: http://photos.gra.ham.ie/Designate-Mid-Cycle/i-h4gGtxX/0/O/IMG_3869.jpg

*The floods*

.. image:: http://photos.gra.ham.ie/Designate-Mid-Cycle/i-StRbDp8/0/O/IMG_3871.jpg

*Us trying to figure out how to get out*

.. image:: http://photos.gra.ham.ie/Designate-Mid-Cycle/i-wRQhhwZ/0/O/IMG_3879.jpg

*We did get to see the* `burren`_ *though*



.. [1] I may or may not have written a oslo.messaging shim in C# previously. Lets not talk about that. It still hurts.
.. [2] Never do live demos. I had bug filed during this demo, based on something I did on a projector screen. Seriously, record it and hit play.

.. Links

.. _etherpad: https://etherpad.openstack.org/p/designate_2016_winter_midcycle_meetup
.. _timsim: https://twitter.com/timsimmons_
.. _here: https://review.openstack.org/#q,I731bab1b2c24a6f2c9392698914a6b09c12765af,n,z
.. _TaskFlow: http://docs.openstack.org/developer/taskflow/
.. _mid-cycle-workers: https://etherpad.openstack.org/p/designate_2016_winter_midcycle_meetup_workers
.. _spec: https://review.openstack.org/#q,Ie2db550547cb9ed3e95fdd313458ad6332ef34f4,n,z
.. _ionrock: http://twitter.com/ionrock
.. _talk: https://speakerdeck.com/graham/openstack-ireland-meetup-galway-feb-2016
.. _taskin: https://github.com/ionrock/taskin
.. _burren: http://https://en.wikipedia.org/wiki/The_Burren
