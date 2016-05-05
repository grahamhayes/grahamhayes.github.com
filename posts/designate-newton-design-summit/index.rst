.. title: Designate Newton Design Summit
.. slug: designate-newton-design-summit
.. date: 2016-05-05 17:00:00 UTC
.. tags: openstack, summit, travel, austin
.. category: OpenStack
.. link:
.. description:
.. type: text
.. previewimage: https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Austin_Evening.jpg/1024px-Austin_Evening.jpg

.. role:: python(code)
   :language: python


.. role:: bash(code)
   :language: bash

.. image:: https://photos.smugmug.com/Misc/i-wSSCDSC/0/X3/IMG_20160427_201746-X3.jpg


I started writing this on a plane on the way home from Austin, TX where we just
finished up the Newton design summit for OpenStack, and finished it a few days
later - please excuse any wierdness in syntax or flow :)

Austin was its usual weird, wacky, wonderful self. Everytime we are here, I
have a great time, I just can't deal with the heat :).

The summit format this year worked really well - I pretty much stayed in the
design summit hotel for the week - and got some very good work done.

6 Months On: Where are we
=========================

One of the things I did before this design summit was to look at what we had
achived last cycle.

We had a quiet cycle overall, but we did merge some vital features.

Operators no longer need to use the awfull config format we created for pools
in Kilo, we now have a much easier to read YAML file that is loaded into the
database via the :bash:`designate-manage` cli, we now actually support multiple
pools in a real way with the addition of a schedular in
:bash:`designate-central`.


Where are we going?
===================

So - the point of the design summit is to plan the future of the projects - and
designate is no execption. We were in a (very nice boardroom) room for a few
hours - and we talked through quite a few things.

.. image:: https://photos.smugmug.com/Misc/i-p8SxMgH/0/X2/IMG_20160427_140741-X2.jpg

The collection of `etherpads`_ for the summit are available as well.


Golang Replacement of MiniDNS
-----------------------------

One of the nicer things about our current architecture is the flexibility that
we have because we use the standard DNS protocols to update the target DNS
servers. This has the downside however, that we are writing code that deals with
DNS packets in python, which is slow. timsim from RackSpace has writen a POC
in go that has a very large perfomance improvement.

This needs to documented, and permission requested from the TC to move this
component to Go, (and will be a separate post in its own right).

After we got back it turned out that we were not the only project considering
this, and swift actually have a feature branch with code in place. So, based on
this, we are going to collaborate with them on the integration of Go to
OpenStack.

Worker Model
------------

As we dicussed in Galway - we need to replace the current :bash:`*-manager` services
with a generic service that can scale out horizontally. As part of this we
planned out our upgrade and implementation plans for these services.

Docs, Deprications and more Docs
--------------------------------

Docs were a common theme - we were asked to improve them, and also have them
located in the main docs on the OpenStack.org website.

We had a member of the docs team in the room, who gave us some great guidenance
on how to include our docs in the correct place.

VMT - The application process
-----------------------------

On of the teams that supports OpenStack is the Vunrebility Management Team.
They deal with disclosures and assigning OSSA numbers to issues that could present
and issue to our deployers.

They had a session this summit on how that process might work, and designate
was one of the projects chosen to be used as a pilot as I have previously
produced Threat Analysis documentation for Designate inside of Hewlett Packard
Enterprise - this information is currently being processed for release to
the community.

Searchlight
-----------

Searchlight is a new (ish) project in OpenStack that enables true searching
capabilities on clouds. We have a designate plugin, but there are issues
with how we emit notifications from the v1 and the v2 API.

We decided that when we move the Horizon panels to v2, we will just listen for
v2 notifications in Searchlight.

API Docs
--------

There was an interesting session on how the community are moving to document
their APIs. It will now reside in the projects repo, and is based on a
custom sphinx extention that was written for OpenStack.

As this progresses we will migrate designate to these docs, and remove our
current docs, as they are much harder to read.


.. _etherpads: https://etherpad.openstack.org/p/newton-design-designate
