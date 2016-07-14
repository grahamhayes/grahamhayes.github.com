.. title: OpenStack - A leveler playing field
.. slug: openstack-a-leveler-playing-field
.. date: 2016-07-14 19:30:07 UTC
.. tags: openstack, governance, tc, plugins
.. category: OpenStack
.. link:
.. description: Why I think we need more plugins
.. type: text


I just proposed a review to `openstack/governance`_  repo [0] that aims
to have everything across OpenStack be plugin based for all cross
project interaction, or allow all projects access to the same internal
APIs and I wanted to give a bit of background on my motivation, and how
it came about.

Coming from a smaller project, I can see issues for new projects,
smaller projects, and projects that may not be seen as "important".

As a smaller project trying to fit into cross project initiatives,
(and yes, make sure our software looks at least OK in the
Project Navigator) the process can be difficult.

A lot of projects / repositories have plugin interfaces, but also
have project integrations in tree, that do not follow the plugin
interface. This makes it difficult to see what a plugin can, and
should do.

When we moved to the big tent, we wanted as a community to move to
a flatter model, removing the old integrated status.

Unfortunately we still have areas when some projects are more equal -
there is a lingering set of projects who were integrated at the point
in time that we moved, and have preferential status.

A lot of the effects are hard to see, and are not insurmountable, but
do cause projects to re-invent the wheel.

For example, quotas - there is no way for a project that is not nova,
neutron, cinder to hook into the standard CLI, or UI for setting
quotas. They can be done as either extra commands
(openstack dns quota set --foo bar) or as custom panels, but not
the way other quotas get set.

Tempest plugins are another example. Approximately 30 of the 36
current plugins are using resources that are not supposed to be
used, and are an unstable interface. Projects in tree in tempest
are at a much better position, as any change to the internal
API will have to be fixed before the gate merges, but other
out of tree plugins are in a place where they can be broken at any
point.

None of this is meant to single out projects, or teams. A lot
of the projects that are in this situation have inordinate amounts of
work placed on them by the big-tent, and I can emphasize with why things
are this way. These were the examples that currently stick out
in my mind, and I think we have come to a point where we need to make
a change as a community.

By moving to a "plugins for all" model, these issues are reduced.
It undoubtedly will cause more, but it is closer to our goal
of Recognizing all our community is part of OpenStack, and
differentiate projects by tags.

This won't be a change that happens tomorrow, next week, or even next
cycle, but think as a goal, we should start moving in this direction
as soon as we can, and start building momentum.

.. note:: This was originally posted to the `openstack-dev`_ mailing list.


.. _openstack-dev: http://lists.openstack.org/pipermail/openstack-dev/2016-July/099285.html
.. _openstack/governance: https://review.openstack.org/342366
