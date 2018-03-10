.. role:: hl1
.. role:: hl2
.. role:: ext-icon

.. |lArr| unicode:: U+021D0 .. leftwards double arrow
.. |rArr| unicode:: U+021D2 .. rightwards double arrow
.. |X| unicode:: U+02713 .. check mark
.. |sm| unicode:: U+2120 .. service mark superscript

.. _EZID: https://ezid.cdlib.org
.. _ARK: https://confluence.ucop.edu/display/Curation/ARK
.. _DOI: https://www.doi.org
.. _EZID.cdlib.org: https://ezid.cdlib.org
.. _DataCite: https://www.datacite.org
.. _California Digital Library: https://www.cdlib.org
.. _N2T Partners: /e/partners.html
.. _N2T API Documentation: /e/n2t_apidoc.html
.. _Original N2T vision: /e/n2t_vision.html


.. _PDF version: https://n2t.net/ark:/13030/c7cv4br18
.. _TXT version: /e/ark_spec.txt 
.. _Towards Electronic Persistence Using ARK Identifiers: /e/Towards_Electronic_Persistence_Using_ARK_Identifiers.pdf

//BEGIN//

ARK
=============

ARKs are URLs designed to support long-term access to information objects.
In 2001 ARKs were introduced to identify objects of any type:

- digital objects – documents, databases, images, software, websites, etc.
- physical objects – books, bones, statues, etc.
- living beings and groups – people, animals, companies, orchestras, etc.
- intangible objects – places, chemicals, diseases, vocabulary terms, performances, etc.

ARKs are assigned for a variety of reasons:

- affordability – there are no fees to assign or use ARKs
- self-sufficiency – you can host ARKs on your own web server, eg, Noid (Nice
  Opaque Identifiers) open source software
- portability – you can move ARKs to other servers without losing their core
  identities
- global resolvability – you can host ARKs at a well-known server, eg, at the
  N2T.net (Name-to-Thing) resolver
- density – ARKs handle mixed case, permitting shorter identifiers (CD, Cd,
  cD, cd are all distinct)

Some advantages of ARKs:

- simplicity – access relies only on mainstream web "redirects" and ordinary
  "get" requests
- utility – with "inflections" (different endings), an ARK should access data
  , metadata, promises, and more
- compatibility – inflections don't conflict with "linked data content
  negotiation" (a harder and limited way to access metadata)
- versatility – ARKs support persistence statements to describe different
  kinds of long-term access
- transparency – no identifier can guarantee stability, and ARK inflections
  help users make informed judgements
- visibility – syntax rules make ARKs easy to extract from texts and to
  compare for variant and containment relationships
- openness – unlike other persistent identifiers, ARKs don't lock you into
  one specific, fee-based management and resolution infrastructure
- impact – ARKs appear in Thomson Reuters’ Data Citation Index |sm| and
  ORCID researcher profiles

Since 2001 over 550 organizations spread across fifteen countries registered
to assign ARKs.  Registrants include libraries, archives, museums (Smithsonian)
, publishers, government agencies, academic institutions (Princeton), and
technology companies (Google). Some of the major users are

- The California Digital Library
- The Internet Archive
- National Library of France (Bibliothèque nationale de France)
- Portico Digital Preservation Service
- University of California Berkeley
- University of North Texas
- University of Chicago
- University College Dublin
- The British Library

There is a discussion group for ARKs (Archival Resource Keys) at

  https://groups.google.com/group/arks-forum

The group is intended as a public forum for people interested in sharing with
and learning from others about how ARKs have been or could be used in
identifier applications.

The forum is also intended as a mechanism for the CDL, in its role as the ARK
scheme maintenance agency, to seek community feedback on a number of longer
term issues and activities, including

- finalizing the ARK specification as an Internet RFC,
- clarifying local and global resolution options, and
- promoting metadata retrieval in a linked data environment.

Here is a brief summary of other resources relevant to ARKs.

- The ARK Identifier Scheme Specification PDF version     TXT version
- Towards Electronic Persistence Using ARK Identifiers (July 2003)
- ARK and CDL Identifier conventions
- Archival Resource Key - Wikipedia
- Noid (Nice Opaque Identifiers) open source software for minting and resolving ARKs on your own
- ARK plugin for Omeka that creates and manages ARKs for the Omeka open source web-publishing platform
- EZID service: long term identifiers made easy, if you would rather not install and maintain those services yourself
- N2T.net resolver: Name-to-Thing, a single global resolver at n2t.net

//END//
