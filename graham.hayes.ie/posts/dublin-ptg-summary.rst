.. title: Dublin PTG Summary
.. slug: dublin-ptg-summary
.. date: 2018-03-15 19:23:00 UTC
.. tags: openstack, summit, dublin, snow, snowpenstack
.. category: OpenStack
.. link:
.. description:
.. type: text
.. previewimage: https://pbs.twimg.com/media/DXItoxEW4AAqaxV.jpg:medium

.. role:: bash(code)
   :language: bash

*******************************
OpenStack - without the flights
*******************************

.. image:: https://pbs.twimg.com/media/DXItoxEW4AAqaxV.jpg:large

Not getting on a plane was a nice change for an OpenStack event :) - especially
as it looks like I would not have made it home for a few days.

Cross Project Days (Monday / Tuesday)
=====================================

These days are where I think the major value of the PTG is. The cross project
days feel like the Summit of old, with more time for topics, and less running
around a conference centre trying to cram 2 weeks worth of talks / developer
sessions, and other meetings into a few days.

Unified Limits / olso.limits / keystone stored limit data
---------------------------------------------------------

First up for me was the keystone based limits API for unifying quota data in
keystone. It was decided to create oslo.limts (`olso.limits repo`_,
`olso.limits spec`_ & `oslo.limits etherpad`_). The keystone team already
created a `keystone-limits-api`_ that is currently experimental, and the
feeling in the room was that we should try and implement it using a new oslo
library to find where changes need to be made.

The migration procedure was discussed, and how we (the services) would need to
run multiple quota systems for quite a few cycles, due to partial upgrades
that happen in OpenStack. [1]_ Possible implementations were discussed, and
the `oslo.limits etherpad`_ has a good overview of them.


olso.healthcheck
----------------

This is an idea that I have been very interested in since it was discussed in
Sydney. We actually had 3 sessions on this in Dublin, across 3 different cross
project rooms - API-SIG, Oslo and Self Healing SIG.

Overall, most people were receptive - the commentary is that the spec is too
wordy, and contains my favorite description:

.. epigraph::
   It feels like OpenStack, but not really in a good way.

After listening to feedback, and talking offline to a few people I think I have
a handle on where the issues are, and I think I have a rough spec I can work flesh
out over the next few days. I think I will just start writing code at that
point as well - I think with a more concrete example it could help clear up
issues for people.

Edge Computing
--------------

I stopped by the Edge room on the Tuesday to listen in on the discussion.
Personally, I really think this group needs to stop bikesheding on, well,
everything, and actually go and implement a POC and see what breaks.

The push still seems to be "make OpenStack work on the edge" instead of (what
I think is the quickest / most productive way forward) "write extra tooling
to orchestrate OpenStack on the edge."

There was some interesting items brought up, like Glance, and image / data
residency. I think that actually engaging with the Glance team might have been
helpful, as they were completely unaware that the discussion was being held,
but the concepts raised sounded interesting.

I lasted about an hour or so, before I gave up. From my limited exposure, it
sounded exactly like the discussions I have heard on the Edge Calls, which
were the same as the ones I heard in Sydney.

Designate Sessions
==================

The Designate room was a quiet enough affair, but it marks the first time since
the PTG's started that getting a dedicated room was justified. We did some
onboarding with new folks, and laid out a plan for the cycle.

The plan so far looks like this:

* DNSSEC

    - A starting point, using signing keys in the Designate database, which we
      can use as a jumping point to storing keys in a HSM / Barbican
    - People are currently looking at PowerDNS's inline signing as a short term
      solution.

* Docs (it will never **not** be a priority :) )
* Shared Zones
* Improve the UI

    - This really relies on us either :bash:`rm -rf openstack/designate-dashboard`
      or finding people who understand Angular.

TC / QA / Tempest / Trademark Programs
======================================

If you follow the mailing list, or `openstack/governance`_ reviews, you may
have seen a long running discussion over where tempest tests used for Trademark
Programs should go. From memory I seem to remember this being raised in Boston,
but it could have been Barcelona. There was tension between QA, me, the InterOp
Work Group, and others about the location. Chris Dent covered this pretty well
in his `TC updates`_ over the last while, so I am not going to rehash it, but
it does look like we finally have some sort of agreement on the `location`_,
after what was 2 other times I thought we had agreement :).

Board of Directors Meeting
==========================

The OpenStack Board of Directors met on the first day of the PTG. This was an
issue in its own right, which was highlighted in a thread on the
`foundation list`_. Thankfully, I have been told that this situation will not
happen again (I can't seem to find any record of the decision, so it may have
been an informal board discussion, but if anyone from the board is reading,
replying to the `foundation list`_ would be great.).

As it met on day one, I didn't get to see much - I arrived to wait for the
Add On Trademark program approvals, and happened to catch a very interesting
`presentation`_ by Dims, Chris and Melvin. I then got to see the board approve
DNS as a Trademark add on, which is great for the project, and people who want
a constant DNSaaS experience across multiple clouds.

`Johnathon Price's Board Recap`_ is also a good overview, with links to things
that were presented at the meeting.

The Board, Community, and how we interact
-----------------------------------------

One topic that was highlighted by the `TC / QA / Tempest / Trademark Programs`_
discussion was that the QA team is very under resourced. This, combined with
the board discussing `future of the PTGs`_ due to cost makes me very worried.

The foundation has (in my mind) two main focuses.

1. Promote the use of the software or IP produced by people working on projects
   under the foundation, and protect its reputation.
2. Empower the developers working on said software or IP to do so.

In my eyes, Trademark programs are very much part of #1, and the board should
either:

1. Fund / find resources for the QA team, to ensure they have enough bandwidth
   to maintain all trademark programs, the associated tests, and tooling.
2. Fund / find a team that does it separately, but removes the entire burden
   from the QA team.

The PTG falls firmly under #2. I was initially a PTG skeptic, but I really
think it works as an event, and adds **much** more value than the old
mid-cycles did. I understand it has problems, but without it, teams will go
back to the mid cycles, which may have looked cheaper at first glance, but
for some people either meant multiple trips, or missing discussions.

One very disappointing thing to see was the list of Travel Support Program
donors - there was some very generous individuals in the community that stood
up and donated, but none of the corporate foundation members contributed. This,
with members being added to the foundation that seem to stop at paying the
membership fee (see `tencent`_ who were added at the Sydney board meeting),
makes me wonder about the value placed on the community by the board.

I know the OpenStack Foundation is diversifying its portfolio of projects
beyond just the OpenStack Project (this is going to get confusing :/), but
we should still be supporting the community that currently exists.

Other great write ups
=====================

This turned into a bit of a PTG + 2 weeks after update, so here are some other
write ups I have read over the last week or so, and prompted me to remember
things that I would have otherwise forgotten.

* `Chris Dent`_
* `Colleen Murphy`_
* `Adam Spiers`_
* `Mark Voelker`_

The Hotel
=========

And, I saved the best until last. The `Croke Park Hotel`_ was absolutely
amazing during the conference. When we needed to leave the main venue on
Thursday, they managed the transition of a few hundred developers into all the
public spaces we could find extremely well. They kept us fed, watered and happy
the entire time we were in the hotel. The fact they managed to do this, while
not leaving the hotel to go home and sleep themselves! I cannot say enough good
things about them, and encourage anyone who is looking for a hotel in Dublin to
stay there, or is running an event to use Croke Park and the hotel.

.. Recap links
.. _Mark Voelker: http://markvoelker.github.io/blog/dublin-ptg-edge-sessions/
.. _Adam Spiers: https://blog.adamspiers.org/2018/03/09/openstack-ptg-dublin/
.. _Colleen Murphy: http://www.gazlene.net/dublin-ptg.html
.. _Chris Dent: https://anticdent.org/tc-report-18-10.html
.. _Johnathon Price's Board Recap: http://lists.openstack.org/pipermail/foundation/2018-March/002570.html

.. oslo.limits links
.. _olso.limits spec: http://lists.openstack.org/pipermail/openstack-dev/2018-March/128175.html
.. _olso.limits repo: https://review.openstack.org/#/c/550491/
.. _oslo.limits etherpad: https://etherpad.openstack.org/p/unified-limits-rocky-ptg
.. _keystone-limits-api: https://developer.openstack.org/api-ref/identity/v3/index.html#unified-limits

.. TC / Tempest
.. _openstack/governance: https://github.com/openstack/governance
.. _TC Updates: https://anticdent.org/tag/tc.html
.. _location: https://review.openstack.org/#/c/550571/
.. _future of the PTGs: https://anticdent.org/tc-report-18-10.html#talking-about-the-ptg-at-the-ptg

.. BOD
.. _foundation list: http://lists.openstack.org/pipermail/foundation/2018-January/002558.html
.. _presentation: https://docs.google.com/presentation/d/1_N7xhzwk6HzCl0fMm_cWfQ2UFu8bOaZYD2OOAV4y5yQ/edit#slide=id.g33768e8068_2_244
.. _tencent: http://stackalytics.com/?release=all&company=tencent

.. Misc
.. _Croke Park Hotel: https://www.doylecollection.com/hotels/the-croke-park-hotel

.. [1] I have heard of companies running Newton / Ocata Designate (and other projects) on clouds as old as Liberty.
