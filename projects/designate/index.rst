.. title: OpenStack Designate
.. slug: designate
.. date: 2014-01-01T00:00:00+00:00
.. description: DNSaaS for OpenStack
.. status: 5
.. link: https://wiki.openstack.org/wiki/Designate
.. logo: https://wiki.openstack.org/w/images/f/fc/Logo-designate.png
.. github: https://github.com/openstack/designate
.. bugtracker: https://bugs.launchpad.net/designate/
.. role: Project Technical Lead
.. license: Apache 2
.. language: Python

Designate provides DNSaaS services for OpenStack:

* REST API for domain/record management
* Multi-tenant
* Integrated with Keystone for authentication
* Framework in place to integrate with Nova and Neutron notifications (for auto-generated records)
* Support for PowerDNS and Bind9 out of the box