.. title: Equal Opportunities for all OpenStack Projects
.. slug: equal-opportunities-for-all-openstack-projects
.. date: 2016-07-25 21:25:00 UTC
.. tags: openstack, governance, tc, plugins
.. category: OpenStack
.. link:
.. description: What
.. type: text

**************************************************************
A week or 2 later - where are we on fairness for all projects?
**************************************************************

So, two weeks ago, I dropped a TC `motion`_ and a mailing list `post`_ and
waited for the other foot to drop.

I was pleasantly surprised - no one started shouting at me - but by trying
to not point fingers at individual teams I made the text too convoluted.

So, in an effort to clarify things, here is an overview of what has been said
so far, both in the mailing list and the gerrit review itself.

Feedback
========

.. epigraph::

   ... does this also include plugins within projects, like storage
   backends in cinder and hypervisor drivers in nova?

No - this was not clear enough. This change is aimed at projects that are
points of significant cross project interaction. While, in the future there may
come a point where Nova Compute Drivers are developed out of tree (though
I doubt it), that is not happening today. As a result, there is no projects in
the list of `projects`_ that would need to integrate with Nova.

.. epigraph::

   Could you please clarify: do you advocate for a generic plugin interface for
   every project, or that each project should expose a plugin interface that
   allows plugin to behave as in-tree components? Because the latter is what
   happens with Tempest, and I see the former a bit complicated.

For every project that has cross project interaction - tempest is a good
example.

For these projects, they should allow all projects in tree (like Nova,
Neutron, Cinder etc are today), or they should have a plugin interface
(like they currently do), but all projects *must* use it, and not use
parts of tempest that are not exposed in that interface.

This would mean that tempest would move the nova, neutron, etc tests to
use the plugin interface.

Now, that plugin could be kept in the tempest repo, and still maintained
by the QA team, but should use the same interface as the other plugins
that are not in that repository.

Of course, it is not just tempest - an incomplete list looks like:

* Tempest
* Devstack
* Grende
* Horizon
* OpenStack Client
* OpenStack SDK
* Searchlight
* Heat
* Mistral
* Celiometer
* Rally
* Documentation

And I am sure I have missed some obvious ones. (if you see a project missing
let me know on the `motion`_)

.. epigraph::

   I think I disagree here. The root cause is being addressed: external tests can
   use the Tempest plugin interface, and use the API, which is being stabilized.
   The fact that the Tempest API is partially unstable is a temporary things, due
   to the origin of the project and the way the scope was redefined, but again
   it's temporary.

This seems to be the core of a lot of the disagreement - this is only temporary,
it will all be fixed in the future, and it should stay this way.

Unfortunately the discrepancy between projects is not temporary. The specific
problems I have highlighted in the thread for one of the projects is temporary,
but I beleive the only long-term solution is to remove the difference between
projects.

.. epigraph::

   Before we start making lots of specific rules about how teams
   coordinate, I would like to understand the problem those rules are meant
   to solve, so thank you for providing that example.
   ...
   It's not clear yet whether there needs to be a new policy to change the
   existing intent, or if a discussion just hasn't happened, or if someone
   simply needs to edit some code.

Unfortunately there is a big push back on editing code to help plugins from
some of the projects. Again, having the differing access between projects will
continue to exacerbate the problem.


.. epigraph::

   "Change the name of the resolution"

   -- (Paraphrase from a few people)

That was done in the last patchset. I think the Level Playing Field title
bounced around my head from the other resolution that was titled Level Playing
Field. It may have been confusing alright.

Other Areas
===========

I feel like I have been picking on tempest a little too much, it just captures
the current issues perfectly, and a large number of the community have some
knowledge of it, and how it works.

There is other areas across OpenStack the need attention as well:

Horizon
-------

Horizon privileged projects have access to much more panels than
plugins (service status, quotas, overviews etc).
Plugins have to rely on tarballs of horizon

OpenStack Client
----------------

OpenStack CLI privileged projects have access to more commands, as
plugins cannot hook in to them (e.g. quotas)

Grenade
-------

Plugins may or may not have tempest tests ran (I think that patch
merged), they have to use parts of tempest I was told explicitly
plugins should not use to get the tests to run at that point.

Docs
----

We can now add install guides and hook into the API Reference, and API
guides. This is great - and I am really happy about it. We still have
issues trying to integrate with other areas in docs, and most non docs
privileged projects end up with massive amounts of users docs in
docs.openstack.org/developer/<project> , which is not ideal.







.. _motion: https://review.openstack.org/#/c/342366/
.. _post: http://lists.openstack.org/pipermail/openstack-dev/2016-July/099285.html
.. _projects: https://governance.openstack.org/reference/projects/index.html
