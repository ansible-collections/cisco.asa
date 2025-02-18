.. Created with antsibull-docs 2.16.3

cisco.asa.asa_objects module -- Object resource module
++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `cisco.asa collection <https://galaxy.ansible.com/ui/repo/published/cisco/asa/>`_ (version 6.1.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install cisco.asa`.

To use it in a playbook, specify: ``cisco.asa.asa_objects``.

New in cisco.asa 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module configures and manages Objects on ASA platforms.


Aliases: objects






Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th colspan="7"><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td colspan="7" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config"></div>
      <p style="display: inline;"><strong>config</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>A list of Objects options.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="6" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/object_type"></div>
      <p style="display: inline;"><strong>object_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/object_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The object type.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;network&#34;</code></p></li>
        <li><p><code>&#34;service&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="6" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects"></div>
      <p style="display: inline;"><strong>objects</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>The objects.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="5" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/description"></div>
      <p style="display: inline;"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/description" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The description for the object.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="5" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/fqdn"></div>
      <p style="display: inline;"><strong>fqdn</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/fqdn" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Enter this keyword to specify a FQDN</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="5" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/fqdn_v4"></div>
      <p style="display: inline;"><strong>fqdn_v4</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/fqdn_v4" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Enter this keyword to specify an IPv4 FQDN</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="5" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/fqdn_v6"></div>
      <p style="display: inline;"><strong>fqdn_v6</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/fqdn_v6" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Enter this keyword to specify an IPv6 FQDN</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="5" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/host"></div>
      <p style="display: inline;"><strong>host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Set this to specify a single host object.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="5" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Specifies object ID</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="5" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat"></div>
      <p style="display: inline;"><strong>nat</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable NAT on a singleton object</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="4" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic"></div>
      <p style="display: inline;"><strong>dynamic</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify NAT type as dynamic</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/dns"></div>
      <p style="display: inline;"><strong>dns</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/dns" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Use the created xlate to rewrite DNS record</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/interface"></div>
      <p style="display: inline;"><strong>interface</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/interface" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Use interface address as mapped IP</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/interface/ipv6"></div>
      <p style="display: inline;"><strong>ipv6</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/interface/ipv6" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Use IPv6 address(es) as mapped IP(s)</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Mapped IP address, network object/object-group name or IPv6 prefix</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/pat_pool"></div>
      <p style="display: inline;"><strong>pat_pool</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/pat_pool" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify object or object-group name for mapped source pat pool</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/pat_pool/block_allocation"></div>
      <p style="display: inline;"><strong>block_allocation</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/pat_pool/block_allocation" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable port block allocation</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/pat_pool/extended"></div>
      <p style="display: inline;"><strong>extended</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/pat_pool/extended" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Extend PAT uniqueness to per destination instead of per interface</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/pat_pool/flat"></div>
      <p style="display: inline;"><strong>flat</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/pat_pool/flat" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Translate TCP and UDP ports into flat range 1024-65535</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/pat_pool/include_reserve"></div>
      <p style="display: inline;"><strong>include_reserve</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/pat_pool/include_reserve" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Translate TCP and UDP ports into flat range 1-65535</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/pat_pool/interface"></div>
      <p style="display: inline;"><strong>interface</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/pat_pool/interface" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Use interface address as mapped IP</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/pat_pool/interface/ipv6"></div>
      <p style="display: inline;"><strong>ipv6</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/pat_pool/interface/ipv6" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Use IPv6 address(es) as mapped IP(s)</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/pat_pool/name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/pat_pool/name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Mapped network object/object-group name</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/dynamic/pat_pool/round_robin"></div>
      <p style="display: inline;"><strong>round_robin</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/dynamic/pat_pool/round_robin" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify to use PAT ip addresses in round robin instead one by one</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>


  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="4" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/mapped_if"></div>
      <p style="display: inline;"><strong>mapped_if</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/mapped_if" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Postnat interface</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="4" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/real_if"></div>
      <p style="display: inline;"><strong>real_if</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/real_if" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Prenat interface</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="4" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static"></div>
      <p style="display: inline;"><strong>static</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify NAT type as static</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/dns"></div>
      <p style="display: inline;"><strong>dns</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/dns" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Use the created xlate to rewrite DNS record</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/interface"></div>
      <p style="display: inline;"><strong>interface</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/interface" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Use interface address as mapped IP</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/interface/ipv6"></div>
      <p style="display: inline;"><strong>ipv6</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/interface/ipv6" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Use IPv6 address(es) as mapped IP(s)</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Mapped IP address, network object/object-group name or IPv6 prefix</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/net_to_net"></div>
      <p style="display: inline;"><strong>net_to_net</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/net_to_net" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Use Net to net mapping of IPv4 to IPv6 address(es)</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/no_proxy_arp"></div>
      <p style="display: inline;"><strong>no_proxy_arp</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/no_proxy_arp" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Disable proxy ARP on the egress interface</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/route_lookup"></div>
      <p style="display: inline;"><strong>route_lookup</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/route_lookup" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Perform route lookup for this rule</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/service"></div>
      <p style="display: inline;"><strong>service</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/service" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Define port mapping</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/service/mapped_port"></div>
      <p style="display: inline;"><strong>mapped_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/service/mapped_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify mapped port</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/service/protocol"></div>
      <p style="display: inline;"><strong>protocol</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/service/protocol" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Define transport protocol</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;tcp&#34;</code></p></li>
        <li><p><code>&#34;udp&#34;</code></p></li>
        <li><p><code>&#34;sctp&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/nat/static/service/real_port"></div>
      <p style="display: inline;"><strong>real_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/nat/static/service/real_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify real port</p>
    </td>
  </tr>



  <tr>
    <td></td>
    <td></td>
    <td colspan="5" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/range"></div>
      <p style="display: inline;"><strong>range</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/range" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Enter this keyword to specify a range</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="5" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service"></div>
      <p style="display: inline;"><strong>service</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Enter this keyword to specify a service</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="4" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/destination_port"></div>
      <p style="display: inline;"><strong>destination_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/destination_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Service destination port</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/destination_port/eq"></div>
      <p style="display: inline;"><strong>eq</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/destination_port/eq" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port equal</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/destination_port/gt"></div>
      <p style="display: inline;"><strong>gt</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/destination_port/gt" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port greater than</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/destination_port/lt"></div>
      <p style="display: inline;"><strong>lt</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/destination_port/lt" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port less than</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/destination_port/neq"></div>
      <p style="display: inline;"><strong>neq</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/destination_port/neq" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port not equal</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/destination_port/range"></div>
      <p style="display: inline;"><strong>range</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/destination_port/range" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Port in range</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/destination_port/range/end"></div>
      <p style="display: inline;"><strong>end</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/destination_port/range/end" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port range end</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/destination_port/range/start"></div>
      <p style="display: inline;"><strong>start</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/destination_port/range/start" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port range start</p>
    </td>
  </tr>


  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="4" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/icmpopt"></div>
      <p style="display: inline;"><strong>icmpopt</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/icmpopt" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>specify icmp option name</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/icmpopt/code"></div>
      <p style="display: inline;"><strong>code</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/icmpopt/code" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify ICMP code</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/icmpopt/name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/icmpopt/name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify ICMP option name</p>
    </td>
  </tr>

  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="4" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/protocol"></div>
      <p style="display: inline;"><strong>protocol</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/protocol" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Protocol name or number</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="4" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/source_port"></div>
      <p style="display: inline;"><strong>source_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/source_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Service source port</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/source_port/eq"></div>
      <p style="display: inline;"><strong>eq</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/source_port/eq" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port equal</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/source_port/gt"></div>
      <p style="display: inline;"><strong>gt</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/source_port/gt" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port greater than</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/source_port/lt"></div>
      <p style="display: inline;"><strong>lt</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/source_port/lt" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port less than</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/source_port/neq"></div>
      <p style="display: inline;"><strong>neq</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/source_port/neq" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port not equal</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/source_port/range"></div>
      <p style="display: inline;"><strong>range</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/source_port/range" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Port in range</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/source_port/range/end"></div>
      <p style="display: inline;"><strong>end</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/source_port/range/end" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port range end</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/service/source_port/range/start"></div>
      <p style="display: inline;"><strong>start</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/service/source_port/range/start" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Port range start</p>
    </td>
  </tr>



  <tr>
    <td></td>
    <td></td>
    <td colspan="5" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config/objects/subnet"></div>
      <p style="display: inline;"><strong>subnet</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config/objects/subnet" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Enter an IPv4 network address with space seperated netmask or IPv6 CIDR.</p>
    </td>
  </tr>


  <tr>
    <td colspan="7" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-running_config"></div>
      <p style="display: inline;"><strong>running_config</strong></p>
      <a class="ansibleOptionLink" href="#parameter-running_config" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The <em>running_config</em> argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command.</p>
    </td>
  </tr>
  <tr>
    <td colspan="7" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The state the configuration should be left in. There is no meaning of merged state, as an object can only have single configuration command, and they overwrite one another. So if an object already existed, merging would behave like replacement.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;replaced&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;overridden&#34;</code></p></li>
        <li><p><code>&#34;deleted&#34;</code></p></li>
        <li><p><code>&#34;gathered&#34;</code></p></li>
        <li><p><code>&#34;rendered&#34;</code></p></li>
        <li><p><code>&#34;parsed&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>




Notes
-----

- Tested against Cisco ASA Version 9.16
- This module works with connection :literal:`network\_cli`. See \ `ASA Platform Options <../network/user_guide/platform_asa.html>`__.


Examples
--------

.. code-block:: yaml

    # Using Replaced

    # Before state:
    # -------------

    # ciscoasa# sh run object
    # object network test_fqdn_obj
    #  fqdn google.com
    #  description a test fqdn object
    # object network test_host_obj
    #  host 1.2.3.4
    #  description a test host object
    # object network test_nat_obj
    #  host 1.2.3.4
    #  description a test nat object
    # object network test_range_obj
    #  range 10.0.0.1 10.0.0.10
    #  description a test range object
    # object network test_subnet_obj
    #  subnet 10.0.0.0 255.255.255.0
    #  description a test subnet object
    # object service test_gre_obj
    #  service gre
    # object service test_icmp_echo_obj
    #  service icmp echo
    # object service test_icmp_echo_repl_code_obj
    #  service icmp echo-reply 0
    # object service test_tcp_eq_obj
    #  service tcp destination eq https
    # object service test_tcp_range_obj
    #  service tcp destination range www https
    # object service test_tcp_source_eq_obj
    #  service tcp source eq 5671
    # object service test_tcp_source_range_obj
    #  service tcp source range 5671 5672
    # ciscoasa# sh run nat | ex ^nat
    # object network test_nat_obj
    #  nat (any,any) static 5.6.7.8 net-to-net
    # ciscoasa#

    - name: Replace module attributes of given objects
      become: true
      cisco.asa.asa_objects:
        config:
          - object_type: network
            objects:
            - description: a test fqdn v4 object
              fqdn_v4: microsoft.com
              name: test_fqdn_obj
            - description: a test range object
              name: test_range_obj
              range: 10.0.0.1 10.0.0.10
            - description: another test host object
              host: 1.2.3.4
              name: test_host_obj_1
            - name: test_nat_obj
          - object_type: service
            objects:
            - name: test_tcp_source_range_obj
              service:
                protocol: tcp
                source_port:
                  range:
                    end: '5672'
                    start: '5671'
            - name: test_tcp_eq_obj
              service:
                destination_port:
                  eq: https
                protocol: tcp
            - name: test_icmp_echo_obj
              service:
                icmpopt:
                  name: echo
                  code: 8
                protocol: icmp
        state: replaced

    # Commands Fired:
    # ---------------
    #
    # object network test_fqdn_obj
    # description a test fqdn v4 object
    # fqdn v4 microsoft.com
    # object network test_host_obj_1
    # description another test host object
    # host 1.2.3.4
    # object network test_nat_obj
    # no description a test nat object
    # no nat (any,any) static 5.6.7.8 net-to-net
    # object service test_icmp_echo_obj
    # service icmp echo 8

    # After state:
    # ------------
    #
    # ciscoasa# sh run object
    # object network test_fqdn_obj
    #  fqdn v4 microsoft.com
    #  description a test fqdn v4 object
    # object network test_host_obj
    #  host 1.2.3.4
    #  description a test host object
    # object network test_nat_obj
    #  host 1.2.3.4
    # object network test_range_obj
    #  range 10.0.0.1 10.0.0.10
    #  description a test range object
    # object network test_subnet_obj
    #  subnet 10.0.0.0 255.255.255.0
    #  description a test subnet object
    # object service test_gre_obj
    #  service gre
    # object service test_icmp_echo_obj
    #  service icmp echo 8
    # object service test_icmp_echo_repl_code_obj
    #  service icmp echo-reply 0
    # object service test_tcp_eq_obj
    #  service tcp destination eq https
    # object service test_tcp_range_obj
    #  service tcp destination range www https
    # object service test_tcp_source_eq_obj
    #  service tcp source eq 5671
    # object service test_tcp_source_range_obj
    #  service tcp source range 5671 5672
    # object network test_host_obj_1
    #  host 1.2.3.4
    #  description another test host object
    # ciscoasa# sh run nat | ex ^nat
    # ciscoasa#

    # Using Overridden

    # Before state:
    # -------------

    # ciscoasa# sh run object
    # object network test_fqdn_obj
    #  fqdn google.com
    #  description a test fqdn object
    # object network test_host_obj
    #  host 1.2.3.4
    #  description a test host object
    # object network test_nat_obj
    #  host 1.2.3.4
    #  description a test nat object
    # object network test_range_obj
    #  range 10.0.0.1 10.0.0.10
    #  description a test range object
    # object network test_subnet_obj
    #  subnet 10.0.0.0 255.255.255.0
    #  description a test subnet object
    # object service test_gre_obj
    #  service gre
    # object service test_icmp_echo_obj
    #  service icmp echo
    # object service test_icmp_echo_repl_code_obj
    #  service icmp echo-reply 0
    # object service test_tcp_eq_obj
    #  service tcp destination eq https
    # object service test_tcp_range_obj
    #  service tcp destination range www https
    # object service test_tcp_source_eq_obj
    #  service tcp source eq 5671
    # object service test_tcp_source_range_obj
    #  service tcp source range 5671 5672
    # ciscoasa# sh run nat | ex ^nat
    # object network test_nat_obj
    #  nat (any,any) static 5.6.7.8 net-to-net
    # ciscoasa#

    - name: Overridden module attributes of given objects
      become: true
      register: result
      cisco.asa.asa_objects:
        config:
          - object_type: network
            objects:
              - description: a modified test fqdn object
                fqdn_v4: microsoft.com
                name: test_fqdn_obj
              - description: a test subnet object
                name: test_subnet_obj
                subnet: 10.0.0.0 255.255.255.0
              - description: a test range object
                name: test_range_another_obj
                range: 10.0.10.1 10.0.10.10
          - object_type: service
            objects:
              - name: test_gre_obj
                service:
                  protocol: gre
        state: overridden

    # Commands Fired:
    # ---------------
    #
    # no object network test_host_obj
    # no object network test_nat_obj
    # no object network test_range_obj
    # no object service test_icmp_echo_obj
    # no object service test_icmp_echo_repl_code_obj
    # no object service test_tcp_eq_obj
    # no object service test_tcp_range_obj
    # no object service test_tcp_source_eq_obj
    # no object service test_tcp_source_range_obj
    # object network test_fqdn_obj
    # description a modified test fqdn object
    # fqdn v4 microsoft.com
    # object network test_range_another_obj
    # description a test range object
    # range 10.0.10.1 10.0.10.10

    # After state:
    # ------------
    #
    # ciscoasa# sh run object
    # object network test_fqdn_obj
    #  fqdn v4 microsoft.com
    #  description a modified test fqdn object
    # object network test_subnet_obj
    #  subnet 10.0.0.0 255.255.255.0
    #  description a test subnet object
    # object service test_gre_obj
    #  service gre
    # object network test_range_another_obj
    #  range 10.0.10.1 10.0.10.10
    #  description a test range object
    # ciscoasa# sh run nat | ex ^nat
    # ciscoasa#

    # Using Deleted

    # Before state:
    # -------------

    # ciscoasa# sh run object
    # object network test_fqdn_obj
    #  fqdn google.com
    #  description a test fqdn object
    # object network test_host_obj
    #  host 1.2.3.4
    #  description a test host object
    # object network test_nat_obj
    #  host 1.2.3.4
    #  description a test nat object
    # object network test_range_obj
    #  range 10.0.0.1 10.0.0.10
    #  description a test range object
    # object network test_subnet_obj
    #  subnet 10.0.0.0 255.255.255.0
    #  description a test subnet object
    # object service test_gre_obj
    #  service gre
    # object service test_icmp_echo_obj
    #  service icmp echo
    # object service test_icmp_echo_repl_code_obj
    #  service icmp echo-reply 0
    # object service test_tcp_eq_obj
    #  service tcp destination eq https
    # object service test_tcp_range_obj
    #  service tcp destination range www https
    # object service test_tcp_source_eq_obj
    #  service tcp source eq 5671
    # object service test_tcp_source_range_obj
    #  service tcp source range 5671 5672
    # ciscoasa# sh run nat | ex ^nat
    # object network test_nat_obj
    #  nat (any,any) static 5.6.7.8 net-to-net
    # ciscoasa#

    - name: Delete module attributes of given objects
      become: true
      cisco.asa.asa_objects:
        config:
          - object_type: network
            objects:
              - name: test_range_obj
              - name: test_non_existent_obj
          - object_type: service
            objects:
              - name: test_icmp_echo_obj
        state: deleted

    # Commands Fired:
    # ---------------
    #
    # no object network test_range_obj
    # no object service test_icmp_echo_obj

    # After state:
    # ------------
    #
    # ciscoasa# sh run object
    # object network test_fqdn_obj
    #  fqdn google.com
    #  description a test fqdn object
    # object network test_host_obj
    #  host 1.2.3.4
    #  description a test host object
    # object network test_nat_obj
    #  host 1.2.3.4
    #  description a test nat object
    # object network test_subnet_obj
    #  subnet 10.0.0.0 255.255.255.0
    #  description a test subnet object
    # object service test_gre_obj
    #  service gre
    # object service test_icmp_echo_repl_code_obj
    #  service icmp echo-reply 0
    # object service test_tcp_eq_obj
    #  service tcp destination eq https
    # object service test_tcp_range_obj
    #  service tcp destination range www https
    # object service test_tcp_source_eq_obj
    #  service tcp source eq 5671
    # object service test_tcp_source_range_obj
    #  service tcp source range 5671 5672
    # ciscoasa# sh run nat | ex ^nat
    # object network test_nat_obj
    #  nat (any,any) static 5.6.7.8 net-to-net
    # ciscoasa#

    # Using DELETED without any config passed
    # "(NOTE: This will delete all of configured resource module attributes)"

    # Before state:
    # -------------

    # ciscoasa# sh run object
    # object network test_fqdn_obj
    #  fqdn google.com
    #  description a test fqdn object
    # object network test_host_obj
    #  host 1.2.3.4
    #  description a test host object
    # object network test_nat_obj
    #  host 1.2.3.4
    #  description a test nat object
    # object network test_range_obj
    #  range 10.0.0.1 10.0.0.10
    #  description a test range object
    # object network test_subnet_obj
    #  subnet 10.0.0.0 255.255.255.0
    #  description a test subnet object
    # object service test_gre_obj
    #  service gre
    # object service test_icmp_echo_obj
    #  service icmp echo
    # object service test_icmp_echo_repl_code_obj
    #  service icmp echo-reply 0
    # object service test_tcp_eq_obj
    #  service tcp destination eq https
    # object service test_tcp_range_obj
    #  service tcp destination range www https
    # object service test_tcp_source_eq_obj
    #  service tcp source eq 5671
    # object service test_tcp_source_range_obj
    #  service tcp source range 5671 5672
    # ciscoasa# sh run nat | ex ^nat
    # object network test_nat_obj
    #  nat (any,any) static 5.6.7.8 net-to-net
    # ciscoasa#

    - name: Delete module attributes of given objects
      become: true
      cisco.asa.asa_objects:
        state: deleted

    # Commands Fired:
    # ---------------
    #
    # no object network test_fqdn_obj
    # no object network test_host_obj
    # no object network test_nat_obj
    # no object network test_range_obj
    # no object network test_subnet_obj
    # no object service test_gre_obj
    # no object service test_icmp_echo_obj
    # no object service test_icmp_echo_repl_code_obj
    # no object service test_tcp_eq_obj
    # no object service test_tcp_range_obj
    # no object service test_tcp_source_eq_obj
    # no object service test_tcp_source_range_obj

    # After state:
    # ------------
    #
    # ciscoasa# sh run object
    # ciscoasa# sh run nat | ex ^nat
    # ciscoasa#

    # Using Gathered

    # Before state:
    # -------------

    # ciscoasa# sh run object
    # object network test_fqdn_obj
    #  fqdn google.com
    #  description a test fqdn object
    # object network test_host_obj
    #  host 1.2.3.4
    #  description a test host object
    # object network test_nat_obj
    #  host 1.2.3.4
    #  description a test nat object
    # object network test_range_obj
    #  range 10.0.0.1 10.0.0.10
    #  description a test range object
    # object network test_subnet_obj
    #  subnet 10.0.0.0 255.255.255.0
    #  description a test subnet object
    # object service test_gre_obj
    #  service gre
    # object service test_icmp_echo_obj
    #  service icmp echo
    # object service test_icmp_echo_repl_code_obj
    #  service icmp echo-reply 0
    # object service test_tcp_eq_obj
    #  service tcp destination eq https
    # object service test_tcp_range_obj
    #  service tcp destination range www https
    # object service test_tcp_source_eq_obj
    #  service tcp source eq 5671
    # object service test_tcp_source_range_obj
    #  service tcp source range 5671 5672
    # ciscoasa# sh run nat | ex ^nat
    # object network test_nat_obj
    #  nat (any,any) static 5.6.7.8 net-to-net
    # ciscoasa#

    - name: Gather the provided configuration with the exisiting running configuration
      register: result
      cisco.asa.asa_objects:
        config:
        state: gathered

    # Module Execution Result:
    # ------------
    #
    # "gathered": [
    #     {
    #         "object_type": "network",
    #         "objects": [
    #             {
    #                 "description": "a test fqdn object",
    #                 "fqdn": "google.com",
    #                 "name": "test_fqdn_obj"
    #             },
    #             {
    #                 "description": "a test host object",
    #                 "host": "1.2.3.4",
    #                 "name": "test_host_obj"
    #             },
    #             {
    #                 "description": "a test nat object",
    #                 "host": "1.2.3.4",
    #                 "name": "test_nat_obj",
    #                 "nat": {
    #                     "mapped_if": "any",
    #                     "real_if": "any",
    #                     "static": {
    #                         "name": "5.6.7.8",
    #                         "net_to_net": true
    #                     }
    #                 }
    #             },
    #             {
    #                 "description": "a test range object",
    #                 "name": "test_range_obj",
    #                 "range": "10.0.0.1 10.0.0.10"
    #             },
    #             {
    #                 "description": "a test subnet object",
    #                 "name": "test_subnet_obj",
    #                 "subnet": "10.0.0.0 255.255.255.0"
    #             }
    #         ]
    #     },
    #     {
    #         "object_type": "service",
    #         "objects": [
    #             {
    #                 "name": "test_gre_obj",
    #                 "service": {
    #                     "protocol": "gre"
    #                 }
    #             },
    #             {
    #                 "name": "test_icmp_echo_obj",
    #                 "service": {
    #                     "icmpopt": {
    #                         "name": "echo"
    #                     },
    #                     "protocol": "icmp"
    #                 }
    #             },
    #             {
    #                 "name": "test_icmp_echo_repl_code_obj",
    #                 "service": {
    #                     "icmpopt": {
    #                         "code": "0",
    #                         "name": "echo-reply"
    #                     },
    #                     "protocol": "icmp"
    #                 }
    #             },
    #             {
    #                 "name": "test_tcp_eq_obj",
    #                 "service": {
    #                     "destination_port": {
    #                         "eq": "https"
    #                     },
    #                     "protocol": "tcp"
    #                 }
    #             },
    #             {
    #                 "name": "test_tcp_range_obj",
    #                 "service": {
    #                     "destination_port": {
    #                         "range": {
    #                             "end": "https",
    #                             "start": "www"
    #                         }
    #                     },
    #                     "protocol": "tcp"
    #                 }
    #             },
    #             {
    #                 "name": "test_tcp_source_eq_obj",
    #                 "service": {
    #                     "protocol": "tcp",
    #                     "source_port": {
    #                         "eq": "5671"
    #                     }
    #                 }
    #             },
    #             {
    #                 "name": "test_tcp_source_range_obj",
    #                 "service": {
    #                     "protocol": "tcp",
    #                     "source_port": {
    #                         "range": {
    #                             "end": "5672",
    #                             "start": "5671"
    #                         }
    #                     }
    #                 }
    #             }
    #         ]
    #     }
    # ]

    # Using Rendered

    - name: Render the commands for provided  configuration
      become: true
      cisco.asa.asa_objects:
        config: "{{ initial_config }}"
        state: rendered

    # Module Execution Result:
    # ------------
    #
    # "rendered": [
    #     "object network test_fqdn_obj",
    #     "description a test fqdn object",
    #     "fqdn google.com",
    #     "object network test_host_obj",
    #     "description a test host object",
    #     "host 1.2.3.4",
    #     "object network test_nat_obj",
    #     "description a test nat object",
    #     "host 1.2.3.4",
    #     "nat (any,any) static 5.6.7.8 net-to-net",
    #     "object network test_range_obj",
    #     "description a test range object",
    #     "range 10.0.0.1 10.0.0.10",
    #     "object network test_subnet_obj",
    #     "description a test subnet object",
    #     "subnet 10.0.0.0 255.255.255.0",
    #     "object service test_gre_obj",
    #     "service gre",
    #     "object service test_icmp_echo_obj",
    #     "service icmp echo",
    #     "object service test_icmp_echo_repl_code_obj",
    #     "service icmp echo-reply 0",
    #     "object service test_tcp_eq_obj",
    #     "service tcp destination eq https",
    #     "object service test_tcp_range_obj",
    #     "service tcp destination range www https",
    #     "object service test_tcp_source_eq_obj",
    #     "service tcp source eq 5671",
    #     "object service test_tcp_source_range_obj",
    #     "service tcp source range 5671 5672"
    # ]

    # Using Parsed

    # _parsed.cfg
    # -------------

    # object network test_host_obj
    #  host 1.2.3.4
    #  description a test host object
    # object network test_subnet_obj
    #  subnet 10.0.0.0 255.255.255.0
    #  description a test subnet object
    # object network test_range_obj
    #  range 10.0.0.1 10.0.0.10
    #  description a test range object
    # object network test_fqdn_obj
    #  fqdn google.com
    #  description a test fqdn object
    # object network test_nat_obj
    #  description a test nat object
    #  host 1.2.3.4
    #  nat (any,any) static 5.6.7.8 net-to-net
    # object service test_tcp_eq_obj
    #  service tcp destination eq https
    # object service test_tcp_range_obj
    #  service tcp destination range www https
    # object service test_gre_obj
    #  service gre
    # object service test_icmp_echo_obj
    #  service icmp echo
    # object service test_icmp_echo_repl_code_obj
    #  service icmp echo-reply 0
    # object service test_tcp_source_eq_obj
    #  service tcp source eq 5671
    # object service test_tcp_source_range_obj
    #  service tcp source range 5671 5672

    - name: Parse the commands for provided configuration
      become: true
      cisco.asa.asa_objects:
        running_config: "{{ lookup('file', '_parsed.cfg') }}"
        state: parsed

    # Module Execution Result:
    # ------------
    #
    # "parsed": [
    #     {
    #         "object_type": "network",
    #         "objects": [
    #             {
    #                 "description": "a test fqdn object",
    #                 "fqdn": "google.com",
    #                 "name": "test_fqdn_obj"
    #             },
    #             {
    #                 "description": "a test host object",
    #                 "host": "1.2.3.4",
    #                 "name": "test_host_obj"
    #             },
    #             {
    #                 "description": "a test nat object",
    #                 "host": "1.2.3.4",
    #                 "name": "test_nat_obj",
    #                 "nat": {
    #                     "mapped_if": "any",
    #                     "real_if": "any",
    #                     "static": {
    #                         "name": "5.6.7.8",
    #                         "net_to_net": true
    #                     }
    #                 }
    #             },
    #             {
    #                 "description": "a test range object",
    #                 "name": "test_range_obj",
    #                 "range": "10.0.0.1 10.0.0.10"
    #             },
    #             {
    #                 "description": "a test subnet object",
    #                 "name": "test_subnet_obj",
    #                 "subnet": "10.0.0.0 255.255.255.0"
    #             }
    #         ]
    #     },
    #     {
    #         "object_type": "service",
    #         "objects": [
    #             {
    #                 "name": "test_gre_obj",
    #                 "service": {
    #                     "protocol": "gre"
    #                 }
    #             },
    #             {
    #                 "name": "test_icmp_echo_obj",
    #                 "service": {
    #                     "icmpopt": {
    #                         "name": "echo"
    #                     },
    #                     "protocol": "icmp"
    #                 }
    #             },
    #             {
    #                 "name": "test_icmp_echo_repl_code_obj",
    #                 "service": {
    #                     "icmpopt": {
    #                         "code": "0",
    #                         "name": "echo-reply"
    #                     },
    #                     "protocol": "icmp"
    #                 }
    #             },
    #             {
    #                 "name": "test_tcp_eq_obj",
    #                 "service": {
    #                     "destination_port": {
    #                         "eq": "https"
    #                     },
    #                     "protocol": "tcp"
    #                 }
    #             },
    #             {
    #                 "name": "test_tcp_range_obj",
    #                 "service": {
    #                     "destination_port": {
    #                         "range": {
    #                             "end": "https",
    #                             "start": "www"
    #                         }
    #                     },
    #                     "protocol": "tcp"
    #                 }
    #             },
    #             {
    #                 "name": "test_tcp_source_eq_obj",
    #                 "service": {
    #                     "protocol": "tcp",
    #                     "source_port": {
    #                         "eq": "5671"
    #                     }
    #                 }
    #             },
    #             {
    #                 "name": "test_tcp_source_range_obj",
    #                 "service": {
    #                     "protocol": "tcp",
    #                     "source_port": {
    #                         "range": {
    #                             "end": "5672",
    #                             "start": "5671"
    #                         }
    #                     }
    #                 }
    #             }
    #         ]
    #     }
    # ]




Return Values
-------------
The following are the fields unique to this module:

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th><p>Key</p></th>
    <th><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-after"></div>
      <p style="display: inline;"><strong>after</strong></p>
      <a class="ansibleOptionLink" href="#return-after" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>The resulting configuration after module execution.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> when changed</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;after&#34;: [{&#34;object_type&#34;: &#34;network&#34;, &#34;objects&#34;: [{&#34;description&#34;: &#34;a test fqdn v4 object&#34;, &#34;fqdn_v4&#34;: &#34;microsoft.com&#34;, &#34;name&#34;: &#34;test_fqdn_obj&#34;}]}]}</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-before"></div>
      <p style="display: inline;"><strong>before</strong></p>
      <a class="ansibleOptionLink" href="#return-before" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>The configuration prior to the module execution.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> when <em>state</em> is <code class='docutils literal notranslate'>replaced</code>, <code class='docutils literal notranslate'>overridden</code>, <code class='docutils literal notranslate'>deleted</code> or <code class='docutils literal notranslate'>purged</code></p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;before&#34;: [{&#34;object_type&#34;: &#34;network&#34;, &#34;objects&#34;: [{&#34;description&#34;: &#34;a test fqdn object&#34;, &#34;fqdn&#34;: &#34;google.com&#34;, &#34;name&#34;: &#34;test_fqdn_obj&#34;}]}]}</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-commands"></div>
      <p style="display: inline;"><strong>commands</strong></p>
      <a class="ansibleOptionLink" href="#return-commands" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>The set of commands pushed to the remote device.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> when <em>state</em> is <code class='docutils literal notranslate'>merged</code>, <code class='docutils literal notranslate'>replaced</code>, <code class='docutils literal notranslate'>overridden</code>, <code class='docutils literal notranslate'>deleted</code> or <code class='docutils literal notranslate'>purged</code></p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;commands&#34;: [&#34;object network test_fqdn_obj&#34;, &#34;description a test fqdn v4 object&#34;, &#34;fqdn v4 microsoft.com&#34;]}</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-gathered"></div>
      <p style="display: inline;"><strong>gathered</strong></p>
      <a class="ansibleOptionLink" href="#return-gathered" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>Facts about the network resource gathered from the remote device as structured data.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> when <em>state</em> is <code class='docutils literal notranslate'>gathered</code></p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;gathered&#34;: [{&#34;object_type&#34;: &#34;network&#34;, &#34;objects&#34;: [{&#34;description&#34;: &#34;a test fqdn object&#34;, &#34;fqdn&#34;: &#34;google.com&#34;, &#34;name&#34;: &#34;test_fqdn_obj&#34;}]}]}</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-parsed"></div>
      <p style="display: inline;"><strong>parsed</strong></p>
      <a class="ansibleOptionLink" href="#return-parsed" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>The device native config provided in <em>running_config</em> option parsed into structured data as per module argspec.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> when <em>state</em> is <code class='docutils literal notranslate'>parsed</code></p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;parsed&#34;: [{&#34;object_type&#34;: &#34;network&#34;, &#34;objects&#34;: [{&#34;description&#34;: &#34;a test fqdn object&#34;, &#34;fqdn&#34;: &#34;google.com&#34;, &#34;name&#34;: &#34;test_fqdn_obj&#34;}]}]}</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-rendered"></div>
      <p style="display: inline;"><strong>rendered</strong></p>
      <a class="ansibleOptionLink" href="#return-rendered" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>The provided configuration in the task rendered in device-native format (offline).</p>
      <p style="margin-top: 8px;"><b>Returned:</b> when <em>state</em> is <code class='docutils literal notranslate'>rendered</code></p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;rendered&#34;: [&#34;object network test_fqdn_obj&#34;, &#34;description a test fqdn object&#34;, &#34;fqdn google.com&#34;]}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Vladimir Rulev



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/cisco.asa/issues>`__
* `Repository (Sources) <https://github.com/ansible-collections/cisco.asa>`__
