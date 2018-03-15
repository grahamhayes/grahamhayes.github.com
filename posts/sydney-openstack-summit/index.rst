.. title: Sydney OpenStack Summit
.. slug: sydney-openstack-summit
.. date: 2017-11-22 19:35:33 UTC
.. tags: openstack, summit, travel, tokyo
.. category: OpenStack
.. link:
.. description:
.. type: text
.. previewimage: https://lh3.googleusercontent.com/9v91EBE02VNZ1fSWcd8JoH7TgPLYhSKXuKrMkqQgSwMHcsw8Im71eM01j6zolH-GuP5XqrAeq4m-GT9Yx4dZXZ_DfND-XWgqvIP64oQwQC-vZgnoLZZ3O-mnOPhQRpouOBscymYBkNelPpg5g2RRy6mXnT9e6lAVy6HGewxRRTL0VOdNApenH_zr-FeRLu_rAOs6WArITF2EbvBsXH74b3EPIGO3BeKlejiC2kSp5Xdj5u7KADXphRazHEVuB8sHegnu0CbZZ2xVLynxvgoSUBPlcwtMUhr87J8_clj0aXIksl-PAWFbhgt7xYlzBkoA1DHsDs5Vw7Cuuah-nycRYRhcSzcFIOvW7L8qWpwHXoD7Xay-DXlqfIYEZjfZc0drpV4AEAnzIaKgIa2PJsFfpiq4hqMv9T59bSIj-EX_wdQ2vXCOzokeZp2t9xCtbIeync9QR_Ij7eXJh_2XHAlLXoR7XrLsY8RiDfrmXSQWVgjEiDGd7urFn6-r3kHLj8QsYRL3ehjfr7GlMtHWuXLkadhblQYpIhnSI-aeEe6NjlXicdMKC43tpWGZkELO9Xm6I82xxycCU68q_g5Sy7BW2_BF7ERp8rNOZg2W4WFJXoySa2fsJitydiJJUvlLSnopYp5GUytsxiMie9fEXQwriFItXlFnXtZsOB8=w1440-h691-no

.. image:: https://lh3.googleusercontent.com/9v91EBE02VNZ1fSWcd8JoH7TgPLYhSKXuKrMkqQgSwMHcsw8Im71eM01j6zolH-GuP5XqrAeq4m-GT9Yx4dZXZ_DfND-XWgqvIP64oQwQC-vZgnoLZZ3O-mnOPhQRpouOBscymYBkNelPpg5g2RRy6mXnT9e6lAVy6HGewxRRTL0VOdNApenH_zr-FeRLu_rAOs6WArITF2EbvBsXH74b3EPIGO3BeKlejiC2kSp5Xdj5u7KADXphRazHEVuB8sHegnu0CbZZ2xVLynxvgoSUBPlcwtMUhr87J8_clj0aXIksl-PAWFbhgt7xYlzBkoA1DHsDs5Vw7Cuuah-nycRYRhcSzcFIOvW7L8qWpwHXoD7Xay-DXlqfIYEZjfZc0drpV4AEAnzIaKgIa2PJsFfpiq4hqMv9T59bSIj-EX_wdQ2vXCOzokeZp2t9xCtbIeync9QR_Ij7eXJh_2XHAlLXoR7XrLsY8RiDfrmXSQWVgjEiDGd7urFn6-r3kHLj8QsYRL3ehjfr7GlMtHWuXLkadhblQYpIhnSI-aeEe6NjlXicdMKC43tpWGZkELO9Xm6I82xxycCU68q_g5Sy7BW2_BF7ERp8rNOZg2W4WFJXoySa2fsJitydiJJUvlLSnopYp5GUytsxiMie9fEXQwriFItXlFnXtZsOB8=w1440-h691-no

********************
OpenStack Down Under
********************

This year the travelling circus that is the OpenStack summit migrated to
Sydney. A lot of us in Europe / North America found out exactly how far away
from our normal venues it really is. (#openstacksummit on twitter for the days
before the summit was an entertaining read :) )

Sunday Board / Joint Leadership Meeting
=======================================

As I was in Sydney, and staying across the road from the meeting, I decided to
drop in and listen. It was an interesting discussion, with a couple of
highlights.

Chris Dent had a very interesting item about developer satisfaction - he has
blogged about it on his blog: `anticdent.org`_ and it is well worth the read.

Johnathon Bryce lead the presentation of a proposed new expansion of the
foundation, which he touched on in the Keynote the next day - I have a few
concerns, but they are all much longer term issues, and may just be my own
interal biases. I think the first new addition to the foundation will let us
know how the rest of the process is going to go.

Colleen Murphy and Julia Kreger told us that they (along with Flavio Percoco)
will be starting research to help improve our inclusiveness in the community.

The last item was brought forward by 2 board members, and they focused on LTS
(Long Term Support / Stable) branches. The time from an upstream release until
a user has it in production is actually long than expected - with a lot of time
being used by distros packaging and ensuring installers are up to date.

This means that by the time users have a release in production, the upstream
branches may be fully deprecated. There was a follow up Forum Session, and
there is now an effort to co-ordinate a new methodology for long term
collaboration in the `LTS Etherpad`_.

There seems to be an assumption that distros are keeping actual git branches
around for the longer term, and not layering patches inside of deb / rpm files,
which I think is much more likely. I hope this effort succeeds, but my cynical
side thinks this is more of a "fix it for us" cry, than "help us fix it". I
suppose we will see if people show up.

One slide from this section was not discussed but concerned me. It was talking
about having an enforced "TC Roadmap" which had lines from various workgroups
and SIGs. Coming from a project that gets a lot of "Can you do `x` feature?"
(to which I usually respond with "Do you have anyone to write the code?") this
concerns me. I understand that it can be hard to get things changed in
OpenStack, really I do, but a top down enforced "Roadmap" is not the way
forward.
Honestly, that two board members of an Open Source foundation think it
is is worrying.

Designate
=========

Designate had 3 sessions in Sydney:

 * Our project update
 * Project On Boarding
 * Ops Feedback

The project update was good - much improved from Boston, where the 2 presenters
were not paid to work on the project. We covered the major potential features,
where we were for Cycle goals (both Queens goals completed, and Pike goals
underway).

Project on boarding was not hugely attended, but I am hoping that was a side
effect of the summit being both smaller and far away.

.. image:: /images/small_far_away.gif

Ops feedback was great - we got a lot of bugs that were impacting our users and
deployers, and collected it in our `Feedback Etherpad`_ (any comments welcome).


Cross Project Work
==================

I went to quite a few cross project sessions - there was a good amount of
discussion, and some useful work came out of it.

Application Tokens
------------------

This is something that had completely slipped past me until now, but the ideas
were great, and it would have made things I have done in previous companies
much much easier.

Healthchecks per service
------------------------

We came to a good agreement on how we can do standardised health checks across
OpenStack, we now need to write a spec and start coding a new piece of
middleware :)

Edge Computing
--------------

Not so sure this was worth a vist - it was much more crowded than any of the
other Forum sessions I went to, and ended up Bike Shedding on where the Edge
ends (we literally spent 10 mins talking about if a car was part of the Edge
or a thing managed by the edge.)

I kept hearing "smaller and lighter OpenStack" in that session, but have yet
to hear what is too heavy about what we currently have. Nearly all our service
scale down to some extent, and you can run a complete infrastructure on an 8GB
VM.

Overall, it was a good summit - not too busy, and short. Looking forward to not
traveling for the next PTG, I think the DUB -> DOH -> SYD and back drained the
enthusiasm for flights for the next few months.



.. _Feedback Etherpad: https://etherpad.openstack.org/p/SYD-forum-designate-feedback
.. _LTS Etherpad: https://etherpad.openstack.org/p/LTS-proposal
.. _anticdent.org: https://anticdent.org/openstack-developer-satisfaction.html