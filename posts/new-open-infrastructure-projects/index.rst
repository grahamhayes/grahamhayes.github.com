.. title: New Open Infrastructure Project(s)
.. slug: new-open-infrastructure-projects
.. date: 2019-04-20 00:3:50 UTC
.. tags: openstack, board, foundation, OIP
.. category: OpenStack
.. link:
.. description: Overview of the Openstack Board of Directors meeting on 2019-04-08
.. type: text

*************************************************
OpenStack Foundation - Board Meeting : 2019/04/08
*************************************************

.. note:: It was pointed out on `twitter`_ that the last section was a little vague - I have updated it to be a bit clearer.


New OIP (Open Infrastructure Projects)
======================================

In a long running program, started in Sydney at the OpenStack Foundation Board
meeting, the OpenStack Foundation (:abbr:`OSF (OpenStack Foundation)`) has added
the first new project to the Foundation under the
:abbr:`OIP (Open Infrastructure Projects)` program - `Kata Containers`_.

The foundation board has laid out a set of `requirements`_ for projects to meet
before they are fully "confirmed" into the foundation.

These fall under 5 broad areas:

 * Focus - does the project do something in an area the board has previously said is an area of interest. Also known as a Strategic Focus Area (SFA)
 * Governance - Does the project act democratically, and have they had a stable process for this.
 * Best Practices - does the project follow the lead of other foundation projects with technical practices - CI, code review, documentation, bug management and security processes.
 * Open-ness - Does the project abide by the `four opens`_.
 * Activity - How many people use the project, and contribute to it?

Kata Containers
---------------

`Eric Ernst`_ from the Kata Architectural Committee gave a very in depth
overview of Kata and what they are doing in the container space. The slides
for this are available on `Google Slides`_.


Focus
^^^^^

Kata strives to solve a large, known problem in the container space, which is a
listed :abbr:`SFA (Strategic Focus Area)` previously defined by the board. They
started as a pilot project in the foundation, with the merging of Intel and hyper.sh
IP.

Many public cloud providers have had to write something like Kata for their operations,
and Kata aims to bring this security to the Open Source space.

Governance
^^^^^^^^^^

The Kata governance is similar to the OpenStack Project governance - they have
contributors (ATCs), Maintainers (cores) and an Architecture Committee (TC).
There is no PTL role, but as a smaller project, that would be unnecessary.

Best Practices
^^^^^^^^^^^^^^

Kata is in a good place for this - they have CI on each PR, a good set of docs,
and a :abbr:`VMT (Vulnerability Management Team)` (Vulnerability Management Team) that is very similar to the
OpenStack one.

Open-ness
^^^^^^^^^

They keep everything in open forums - they use Slack but also bridge the
conversations into channels on freenode, so people can use IRC to talk to them,
the use open Google Docs for specifications, and allow people to comment on
specs to feedback.

They have attended summits before, and reach out to related communities
(hypervisors and kubernetes were given as examples).

Activity
^^^^^^^^

This was an area I was initially concerned about - but the names and number of
users (in production and R&D / testing) looks like it is gaining a growing
community. As is to be expected, a lot of people fall into the "pre prod" / R&D
phase - this is a very new technology, with no current enterprise offerings
which would make companies start out slow.

.. note::
    As a side note, if was an enterprise linux company, I would be pushing for us
    to produce a Kata + Firecracker + Kubeless extension to their Containers
    product ASAP, to beat the rest of the market. There is definite potential
    for this to be a major product line for hybrid customers.

After the presentation we moved to questions from the board to the Architecture
Committee - I have 2.5 pages of notes from this section, so I will not be
talking about every question asked here :)

Questions
^^^^^^^^^

How are Kata and OpenStack integrating, and using each other?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Zun is currently looking at integrating Kata as a container runtime, and
in the days since the board meeting I have seen mailing list posts on this, and
some people have been investigating Magnum as well. Currently there is no real
push from the Kata side, as they let end users drive features.

Is there any commercial distribution of Kata?
"""""""""""""""""""""""""""""""""""""""""""""

Currently, no. There is interest from customers, but currently no distro has
provided support. SUSE / RedHat / Ubuntu have started to work on support in
the linux distros, but not on a product version yet.

Most current users don't want a product version, they are happy to trail blaze
themselves.

How does Kata work with the Kubernetes community?
"""""""""""""""""""""""""""""""""""""""""""""""""

Kata and kubernetes do end to end testing with CRI.O and containerd. As the CRI
is the interface, Kata has been (and is) involved in the development of that
standard, and has helped drive some of the features.

At the end, Alan Clark proposed the board vote on "Approving confirmation of
Kata Containers as a Open Infrastructure Project in the OpenStack Foundation."
This was seconded by Imad Sousou. Of the directors present, all bar one voted
in favor. Arkady Kanevsky abstained (based on a disagreement on the timing of
the vote, not on the substantive motion itself.)

Zuul
----

`Monty Taylor`_ presented on behalf of the Zuul Maintainers. In true
`four opens`_ style, the `presentation`_ was produced on gerrit and zuul itself
in the open for the community to comment on as it was being written :).

I took a lot less notes on zuul, as I know the project, and in short it is
great. The users are a core part of the governance, and there are multiple
large installations outside of the OpenStack CI install. People use it to
test everything from kubernetes to network switches, which shows the level of
flexibility that is in place in the project.

Questions
^^^^^^^^^

Again, I am not going to cover every single question, just the ones I thought
were interesting.

Is there a published roadmap?
"""""""""""""""""""""""""""""
No - not in a traditional sense. The maintainers have a prioritised list of
features, that will get done as they get done (as soon as people show up to
write them).

What does the Zuul need from the OpenStack Foundation?
""""""""""""""""""""""""""""""""""""""""""""""""""""""
They need help with technical marketing (educating people about *how* Zuul
works, and why it is such a good thing), and outreach. For outreach,  Zuul
has been seen as an "OpenStack" only thing, and letting people know they can use
it without OpenStack would be a good thing for the project.

It was noted there has been cases where people adopted Zuul, and then decided
they wanted to bring in OpenStack to help manage the pool of CI VMs.

Licenses - does the board need to pass a specific exception for the GPLv3 sections?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

No - the board has already approved the use of GPLv3 in certain areas of the
Zuul code base (mainly around ansible integrations, but also in the zuul-preview
service). However the board got concerned, and decided to wait until the meeting
in Denver to approve Zuul, and the text of any license exception.

By Laws Update
==============

.. epigraph::

    4.16 Open Meetings and Records. Except as necessary to protect attorney-client
    privilege, sensitive personnel information, discuss the candidacy of
    potential Gold Member and Platinum Members, *and discuss the review and
    approval of Open Infrastructure Projects,* the Board of Directors shall:
    (i) permit observation of its meetings by Members via remote teleconference or
    other electronic means, and (ii) publish the Board of Directors minutes and
    make available to any Member on request other information and records of the
    Foundation as required by Delaware Corporate Law.

   -- New OpenStack Foundation By-Laws (change in italics)

At a previous meeting, the board expressed a wish to be able to talk about adding
a project in an executive session. The above change was posted to the foundation
mailing list a week or so before the meeting.

What this allows for is the board to decide that they want to talk about the new
project behind closed doors, where the discussions are not public (people on the
phone or in the room have to leave), and the people in the session cannot talk
about what was discussed other then in general terms.

I object to having this ability as I think it violates our core principals of
the `four opens`_ - namely the open governance pillar. For something like this -
adding a new member to the family of Open Source Infrastructure projects I think
we should stick to the rules we expect these projects to live by.

There was a quote on the agenda that said "Feedback from the community is
amenable to the addition w/some requests for word changes", which was
unfortunately not quite true.

I had replied to the thread a day or two after it was sent, but it seems most
directors do not read the foundation@lists.openstack.org mailing list.

.. epigraph::

   I am still not sure what could be required for an executive session that
   is not covered by "sensitive personnel information" that would require
   this.

   Personally, for me, this looks like we are not abiding by our own ethos
   of the Four Opens - I do understand if there is personel issues with a
   potential project, we would want to have it discussed behind closed
   doors, but everything else should be in the open. If the project
   that is about to be included has large enough personnel issues that
   they could cause issues for its inclusion in the foundation, there
   is a very high chance that they are going to fail some of the
   confirmation guidelines, and that *is* something the community
   should have visibility into.

   Even from an optics perspective - the board deciding to include or
   not include a project behind closed doors is not something that
   is representative of the OpenStack community, and not something
   I think the community should be supporting.

   -- http://lists.openstack.org/pipermail/foundation/2019-April/002749.html

After sending this there was a discussion in the `#openstack-tc`_ channel about
the change. This should show that the community is not "generally amenable" to
the change.

Personally I cannot see the reason for this change - I do not want to
oversimplify this, but if there is not a **legal restriction** for a director to
say why they are for or against a project being included, and the director will
only say if they support or do not support a project in an executive session,
they need to examine their reasons for being there.

There is a train of thought that we should trust our elected board members -
which I do - I remember to trust but verify. If there was a discussion at an
executive session, they would not be able to raise a flag to the community
that something was amiss.

It is worth noting, that the line about Gold and Platinum members was added
as an amendment to the by-laws, and now the default route that a member goes
though is:

1. Presentation from the prospective member.
2. Executive Session
3. Vote appears out of the discussion in that session.

Is this what we want to have when we are including new project teams in our
community? Or should we do that same thing the that the Technical Committee
do when we look at adding a project, and do it all in the open?

So my questions to the directors would be this:

Why do you want to add this to the by-laws? When do you see it being used?

I will be at the board meeting in Denver, and I look forward to hearing the
reasoning.


.. _twitter: https://twitter.com/odyssey4me/status/1119411458905923584
.. _four opens: https://www.openstack.org/four-opens/
.. _requirements: https://wiki.openstack.org/wiki/Governance/Foundation/OSFProjectConfirmationGuidelines
.. _Kata Containers: https://katacontainers.io/
.. _Eric Ernst: https://github.com/egernst
.. _Google Slides: https://docs.google.com/presentation/d/1Vil7Px-KyjxrfjO4TT25hKRDb2O02_qmrn4RtFBq0d4/edit
.. _Monty Taylor: https://www.openstack.org/community/members/profile/72/monty-taylor
.. _presentation: https://zuul-ci.org/confirmation/
.. _#openstack-tc: http://eavesdrop.openstack.org/irclogs/%23openstack-tc/%23openstack-tc.2019-04-05.log.html#t2019-04-05T15:20:47
