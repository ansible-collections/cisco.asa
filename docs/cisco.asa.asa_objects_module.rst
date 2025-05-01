.. _cisco.asa.asa_objects_module:


*********************
cisco.asa.asa_objects
*********************

**Object resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures and manages Objects on ASA platforms.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="7">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of Objects options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>object_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>network</li>
                                    <li>service</li>
                        </ul>
                </td>
                <td>
                        <div>The object type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>objects</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The objects.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The description for the object.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fqdn</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter this keyword to specify a FQDN</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fqdn_v4</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter this keyword to specify an IPv4 FQDN</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fqdn_v6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter this keyword to specify an IPv6 FQDN</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set this to specify a single host object.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies object ID</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nat</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enable NAT on a singleton object</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dynamic</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify NAT type as dynamic</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dns</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Use the created xlate to rewrite DNS record</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Use interface address as mapped IP</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Use IPv6 address(es) as mapped IP(s)</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mapped_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mapped IP address, network object/object-group name or IPv6 prefix</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pat_pool</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify object or object-group name for mapped source pat pool</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>block_allocation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable port block allocation</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>extended</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Extend PAT uniqueness to per destination instead of per interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>flat</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Translate TCP and UDP ports into flat range 1024-65535</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>include_reserve</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Translate TCP and UDP ports into flat range 1-65535</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Use interface address as mapped IP</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Use IPv6 address(es) as mapped IP(s)</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mapped_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mapped network object/object-group name</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>round_robin</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Specify to use PAT ip addresses in round robin instead one by one</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mapped_if</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Postnat interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>real_if</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Prenat interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>static</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify NAT type as static</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dns</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Use the created xlate to rewrite DNS record</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Use interface address as mapped IP</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Use IPv6 address(es) as mapped IP(s)</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mapped IP address, network object/object-group name or IPv6 prefix</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>net_to_net</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Use Net to net mapping of IPv4 to IPv6 address(es)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_proxy_arp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Disable proxy ARP on the egress interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_lookup</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Perform route lookup for this rule</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>service</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Define port mapping</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mapped_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify mapped port</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>tcp</li>
                                    <li>udp</li>
                                    <li>sctp</li>
                        </ul>
                </td>
                <td>
                        <div>Define transport protocol</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>real_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify real port</div>
                </td>
            </tr>



            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>range</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter this keyword to specify a range</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>service</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter this keyword to specify a service</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>destination_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Service destination port</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>eq</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port equal</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>gt</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port greater than</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>lt</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port less than</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>neq</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port not equal</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>range</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port in range</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>end</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port range end</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>start</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port range start</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>icmpopt</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>specify icmp option name</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>code</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify ICMP code</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify ICMP option name</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Protocol name or number</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Service source port</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>eq</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port equal</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>gt</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port greater than</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>lt</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port less than</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>neq</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port not equal</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>range</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port in range</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>end</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port range end</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>start</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port range start</div>
                </td>
            </tr>



            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>subnet</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter an IPv4 network address with space seperated netmask or IPv6 CIDR.</div>
                </td>
            </tr>


            <tr>
                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>running_config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook.  The <em>running_config</em> argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command.</div>
                </td>
            </tr>
            <tr>
                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>replaced</b>&nbsp;&larr;</div></li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in. There is no meaning of merged state, as an object can only have single configuration command, and they overwrite one another. So if an object already existed, merging would behave like replacement.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Cisco ASA Version 9.16
   - This module works with connection ``network_cli``. See `ASA Platform Options <../network/user_guide/platform_asa.html>`_.



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
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration after module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;after&#x27;: [{&#x27;object_type&#x27;: &#x27;network&#x27;, &#x27;objects&#x27;: [{&#x27;description&#x27;: &#x27;a test fqdn v4 object&#x27;, &#x27;fqdn_v4&#x27;: &#x27;microsoft.com&#x27;, &#x27;name&#x27;: &#x27;test_fqdn_obj&#x27;}]}]}</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>replaced</code>, <code>overridden</code>, <code>deleted</code> or <code>purged</code></td>
                <td>
                            <div>The configuration prior to the module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;before&#x27;: [{&#x27;object_type&#x27;: &#x27;network&#x27;, &#x27;objects&#x27;: [{&#x27;description&#x27;: &#x27;a test fqdn object&#x27;, &#x27;fqdn&#x27;: &#x27;google.com&#x27;, &#x27;name&#x27;: &#x27;test_fqdn_obj&#x27;}]}]}</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>merged</code>, <code>replaced</code>, <code>overridden</code>, <code>deleted</code> or <code>purged</code></td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;commands&#x27;: [&#x27;object network test_fqdn_obj&#x27;, &#x27;description a test fqdn v4 object&#x27;, &#x27;fqdn v4 microsoft.com&#x27;]}</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>gathered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>gathered</code></td>
                <td>
                            <div>Facts about the network resource gathered from the remote device as structured data.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;gathered&#x27;: [{&#x27;object_type&#x27;: &#x27;network&#x27;, &#x27;objects&#x27;: [{&#x27;description&#x27;: &#x27;a test fqdn object&#x27;, &#x27;fqdn&#x27;: &#x27;google.com&#x27;, &#x27;name&#x27;: &#x27;test_fqdn_obj&#x27;}]}]}</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>parsed</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>parsed</code></td>
                <td>
                            <div>The device native config provided in <em>running_config</em> option parsed into structured data as per module argspec.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;parsed&#x27;: [{&#x27;object_type&#x27;: &#x27;network&#x27;, &#x27;objects&#x27;: [{&#x27;description&#x27;: &#x27;a test fqdn object&#x27;, &#x27;fqdn&#x27;: &#x27;google.com&#x27;, &#x27;name&#x27;: &#x27;test_fqdn_obj&#x27;}]}]}</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>rendered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>rendered</code></td>
                <td>
                            <div>The provided configuration in the task rendered in device-native format (offline).</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;rendered&#x27;: [&#x27;object network test_fqdn_obj&#x27;, &#x27;description a test fqdn object&#x27;, &#x27;fqdn google.com&#x27;]}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Vladimir Rulev (@rulev)
