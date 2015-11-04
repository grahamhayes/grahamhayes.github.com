.. title: OpenStack Kosmos
.. slug: kosmos
.. date: 2015-10-01T00:00:00+00:00
.. description: Global Load Balancing for OpenStack
.. status: 1
.. link: https://wiki.openstack.org/wiki/Kosmos
.. github: https://github.com/openstack/kosmos
.. bugtracker: https://bugs.launchpad.net/kosmos/
.. role: Project Technical Lead
.. license: Apache 2
.. language: Python

Kosmos is a new project, formed initially from members of Designate and Neutron Lbaas, to provide global server load-balancing for openstack clouds.

This is separate from both LBaaS and Designate, but heavily leverages both.
Our long term aim is to create a global service (like Designate / Keystone) that allows cloud users to balance their traffic across multiple regions, or multiple cloud providers.
Both Neutron LBaaS and Designate will be first class citizens - the default install for Kosmos will use both, but we are adopting a plugin architecture that allows for different integrations, while maintaining a consistent API.

A standard setup may look like this:

Customer Applications running behind Neutron LB in multiple regions.
Kosmos will constantly monitor these endpoints, and the LBaaS Status API, and update DNS records in Designate to move traffic between the endpoints.