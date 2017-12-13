.. role:: hl1
.. role:: hl2
.. role:: ext-icon

.. |lArr| unicode:: U+021D0 .. leftwards double arrow
.. |rArr| unicode:: U+021D2 .. rightwards double arrow
.. |X| unicode:: U+02713 .. check mark

.. _n2t: https://www.n2t.net
.. _Identifier Basics: https://confluence.ucop.edu/display/DataCite/Identifier+Basics 
.. _Identifier Conventions: https://confluence.ucop.edu/display/Curation/Identifier+Conventions 
.. _Test server: https://n2t-stg.n2t.net/

The N2T API
=======================

//BEGIN//

Overview
---------

The Name-to-Thing (N2T) service provides public resolution of identifiers – ARKs, DOIs, etc.  Identifiers used by the public look like an acronym, a colon, and a string (eg, ark:/12345/fk1234), all appended to a URL based at n2t.net, for example

  https://n2t.net/ark:/12345/fk1234

  http://n2t.net/doi:10.12345/FK4321

When an identifier is presented to N2T for resolution, the web server is configured to do a database lookup and ask that the target (URL) bound under the identifier be returned in the form of an HTTP redirect. Arbitrary name/value pairs may be bound under an identifier.  

Targets are bound under the reserved metadata element name, "_t".  If a target URL is found, the server redirects the client to it.  Other metadata elements support inflections and content negotiation.

Identifiers and metadata are created and maintained via the N2T API, which is the subject of this document.  The API supports
- minting – generating randomized strings that can be used in creating identifiers, and

- binding – associating metadata name/value pairs with identifier strings meant to be published as URLs.

Under the hood, N2T uses the EggNog software, with egg binders and nog minters behind an Apache HTTP server.  Minting and binding require HTTP Basic authentication over SSL.  The base test server URL for operating the API is https://www.n2t.net, abbreviated as $b below. You'll need an N2T user name (known as a populator, "sam" below) and a password ("xyzzy", not a real password).  The following shell definitions are used to shorten examples in this document.::

  b=https://n2t-stg.n2t.net
  alias wg='wget -q -O - --no-check-certificate --user=sam --password=xyzzy'

//END//
