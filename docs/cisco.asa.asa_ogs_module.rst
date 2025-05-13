.. _cisco.asa.asa_ogs_module:


*****************
cisco.asa.asa_ogs
*****************

**Object Group resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures and manages Objects and Groups on ASA platforms.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="6">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="6">
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
                        <div>A list of Object Group options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>object_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The object groups.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>The description for the object-group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group_object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure an object group as an object</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>icmp_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure an ICMP-type object</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>icmp_object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alternate-address</li>
                                    <li>conversion-error</li>
                                    <li>echo</li>
                                    <li>echo-reply</li>
                                    <li>information-reply</li>
                                    <li>information-request</li>
                                    <li>mask-reply</li>
                                    <li>mask-request</li>
                                    <li>mobile-redirect</li>
                                    <li>parameter-problem</li>
                                    <li>redirect</li>
                                    <li>router-advertisement</li>
                                    <li>router-solicitation</li>
                                    <li>source-quench</li>
                                    <li>time-exceeded</li>
                                    <li>timestamp-reply</li>
                                    <li>timestamp-request</li>
                                    <li>traceroute</li>
                                    <li>unreachable</li>
                        </ul>
                </td>
                <td>
                        <div>Defines the ICMP types in the group.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>Specifies object-group ID</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network_object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure a network object</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter an IPv4 network address with space seperated netmask.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
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
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter an IPv6 prefix.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter this keyword to specify a network object</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure a port object</div>
                </td>
            </tr>
                                <tr>
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
                        <div>Enter this keyword to specify a port</div>
                </td>
            </tr>
            <tr>
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
                        <div>Enter this keyword to specify a range of ports</div>
                </td>
            </tr>
                                <tr>
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
                        <div>Specify the end of the port range.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Specify the start of the port range.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                                    <li>tcp-udp</li>
                                    <li>udp</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies that object-group is for only specified protocol only.</div>
                        <div>Required when port-object need to be configured</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol_object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure a protocol object</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the protocols in the group.</div>
                        <div>User can either specify protocols directly/protocol numbers(0-255)</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>security_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure a security-group</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sec_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter this keyword to specify a security-group name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tag</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter this keyword to specify a security-group tag.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>service_object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure a service object</div>
                        <div>NEW &#x27;services_object&#x27; param is introduced at object_group level, please use the newer &#x27;services_object&#x27; param defined at object_group level instead of &#x27;service_object&#x27; param at object_group level, as &#x27;service_object&#x27; option will get deprecated and removed in a future release.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter this keyword to specify a service object</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ah</li>
                                    <li>eigrp</li>
                                    <li>esp</li>
                                    <li>gre</li>
                                    <li>icmp</li>
                                    <li>icmp6</li>
                                    <li>igmp</li>
                                    <li>igrp</li>
                                    <li>ip</li>
                                    <li>ipinip</li>
                                    <li>ipsec</li>
                                    <li>nos</li>
                                    <li>ospf</li>
                                    <li>pcp</li>
                                    <li>pim</li>
                                    <li>pptp</li>
                                    <li>sctp</li>
                                    <li>snp</li>
                                    <li>tcp</li>
                                    <li>tcp-udp</li>
                                    <li>udp</li>
                        </ul>
                </td>
                <td>
                        <div>Defines the protocols in the group.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>services_object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure list of service objects</div>
                        <div>Newer OGs services_object param which will replace service_object param</div>
                        <div>Relased with version 2.1.0</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Keyword to specify destination port</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Match only packets on a given port number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Match only packets with a greater port number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Match only packets with a lower port number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Match only packets not on a given port number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Port range operator</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Specify the end of the port range.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Specify the start of the port range.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enter this keyword to specify a service object</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the protocols in the group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Keyword to specify source port</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Match only packets on a given port number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Match only packets with a greater port number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Match only packets with a lower port number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Match only packets not on a given port number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Port range operator</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Specify the end of the port range.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Specify the start of the port range.</div>
                </td>
            </tr>



            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>user_object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures single user, local or import user group</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>user</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure a user objectUser name to configure a user object.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>User domain</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Enter the name of the user</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>user_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure a user group object.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Group domain</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Enter the name of the group</div>
                </td>
            </tr>



            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
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
                                    <li>icmp-type</li>
                                    <li>network</li>
                                    <li>protocol</li>
                                    <li>security</li>
                                    <li>service</li>
                                    <li>user</li>
                        </ul>
                </td>
                <td>
                        <div>The object group type.</div>
                </td>
            </tr>

            <tr>
                <td colspan="6">
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
                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Cisco ASA Version 9.10(1)11
   - This module works with connection ``network_cli``. See `ASA Platform Options <../network/user_guide/platform_asa.html>`_.



Examples
--------

.. code-block:: yaml

    # Using merged

    # Before state:
    # -------------
    #
    # ciscoasa# sh running-config object-group
    # object-group network test_og_network
    #  description test_network_og
    #  network-object host 198.51.100.1

    - name: "Merge module attributes of given object-group"
      cisco.asa.asa_ogs:
        config:
          - object_type: network
            object_groups:
              - name: group_network_obj
                group_object:
                  - test_og_network
              - name: test_og_network
                description: test_og_network
                network_object:
                  host:
                    - 192.0.2.1
                    - 192.0.2.2
                  address:
                    - 192.0.2.0 255.255.255.0
                    - 198.51.100.0 255.255.255.0
              - name: test_network_og
                description: test_network_og
                network_object:
                  host:
                    - 198.51.100.1
                    - 198.51.100.2
                  ipv6_address:
                    - 2001:db8:3::/64
          - object_type: security
            object_groups:
              - name: test_og_security
                description: test_security
                security_group:
                  sec_name:
                    - test_1
                    - test_2
                  tag:
                    - 10
                    - 20
          - object_type: service
            object_groups:
              - name: O-Worker
                services_object:
                  - protocol: tcp
                    destination_port:
                      range:
                        start: 100
                        end: 200
                  - protocol: tcp-udp
                    source_port:
                      eq: 1234
                    destination_port:
                      gt: nfs
              - name: O-UNIX-TCP
                protocol: tcp
                port_object:
                  - eq: https
                  - range:
                      start: 100
                      end: 400
          - object_type: user
            object_groups:
              - name: test_og_user
                description: test_user
                user_object:
                  user:
                    - name: new_user_1
                      domain: LOCAL
                    - name: new_user_2
                      domain: LOCAL
        state: merged

    # Commands fired:
    # ---------------
    #
    # object-group security test_og_security
    # description test_security
    # security-group name test_1
    # security-group name test_2
    # security-group tag 10
    # security-group tag 20
    # object-group network group_network_obj
    # group-object test_og_network
    # object-group network test_og_network
    # description test_og_network
    # network-object 192.0.2.0 255.255.255.0
    # network-object 198.51.100.0 255.255.255.0
    # network-object host 192.0.2.1
    # network-object host 192.0.2.2
    # object-group network test_network_og
    # network-object host 198.51.100.1
    # network-object host 198.51.100.2
    # network-object 2001:db8:3::/64
    # object-group service O-Worker
    # service-object tcp destination range 100 200
    # service-object tcp source eq 1234 destination gt nfs
    # object-group service O-UNIX-TCP tcp
    # port-object eq https
    # port-object range 100 400
    # object-group user test_og_user
    # description test_user
    # user LOCAL\new_user_1
    # user LOCAL\new_user_2

    # After state:
    # ------------
    #
    # ciscoasa# sh running-config object-group
    # object-group network group_network_obj
    #  group-object test_og_network
    # object-group network test_og_network
    #  description test_og_network
    #  network-object host 192.0.2.1
    #  network-object host 192.0.2.2
    #  network-object 192.0.2.0 255.255.255.0
    #  network-object 198.51.100.0 255.255.255.0
    #  network-object host 198.51.100.1
    # object-group network test_network_og
    #  description test_network_og
    #  network-object host 198.51.100.1
    #  network-object host 198.51.100.2
    #  network-object 2001:db8:0:3::/64
    #  group-object test_og_network
    # object-group security test_og_security
    #  security-group name test_1
    #  security-group name test_2
    #  security-group tag 10
    #  security-group tag 20
    # object-group service O-Worker
    #  service-object tcp destination range 100 200
    #  service-object tcp source eq 1234 destination gt nfs
    # object-group service O-UNIX-TCP tcp
    #  port-object eq https
    #  port-object range 100 400
    # object-group user test_og_user
    #  description test_user
    #  user LOCAL\new_user_1
    #  user LOCAL\new_user_2

    # Using Replaced

    # Before state:
    # -------------
    #
    # ciscoasa# sh running-config object-group
    # object-group network test_og_network
    #  description test_og_network
    #  network-object host 192.0.2.1
    #  network-object host 192.0.2.2
    #  network-object 192.0.2.0 255.255.255.0
    #  network-object 198.51.100.0 255.255.255.0
    # object-group network test_network_og
    #  description test_network_og
    #  network-object host 198.51.100.1
    #  network-object host 198.51.100.2
    #  network-object 2001:db8:0:3::/64
    #  group-object test_og_network
    # object-group security test_og_security
    #  security-group name test_1
    #  security-group name test_2
    #  security-group tag 10
    #  security-group tag 20
    # object-group service O-Worker
    #  service-object tcp destination range 100 200
    #  service-object tcp source eq 1234 destination gt nfs
    # object-group service O-UNIX-TCP tcp
    #  port-object eq https
    #  port-object range 100 400
    # object-group user test_og_user
    #  user LOCAL\new_user_1
    #  user LOCAL\new_user_2

    - name: "Replace module attributes of given object-group"
      cisco.asa.asa_ogs:
        config:
          - object_type: network
            object_groups:
              - name: test_og_network
                description: test_og_network_replace
                network_object:
                  host:
                    - 198.51.100.1
                  address:
                    - 198.51.100.0 255.255.255.0
          - object_type: protocol
            object_groups:
              - name: test_og_protocol
                description: test_og_protocol
                protocol_object:
                  protocol:
                    - tcp
                    - udp
        state: replaced

    # Commands Fired:
    # ---------------
    #
    # object-group protocol test_og_protocol
    # description test_og_protocol
    # protocol tcp
    # protocol udp
    # object-group network test_og_network
    # description test_og_network_replace
    # no network-object 192.0.2.0 255.255.255.0
    # no network-object 198.51.100.0 255.255.255.0
    # network-object 198.51.100.0 255.255.255.0
    # no network-object host 192.0.2.1
    # no network-object host 192.0.2.2
    # network-object host 198.51.100.1

    # After state:
    # -------------
    #
    # ciscoasa# sh running-config object-group
    # object-group network test_og_network
    #  description test_og_network_replace
    #  network-object host 198.51.100.1
    #  network-object 198.51.100.0 255.255.255.0
    # object-group network test_network_og
    #  description test_network_og
    #  network-object host 198.51.100.1
    #  network-object host 198.51.100.2
    #  network-object 2001:db8:0:3::/64
    #  group-object test_og_network
    # object-group security test_og_security
    #  security-group name test_1
    #  security-group name test_2
    #  security-group tag 10
    #  security-group tag 20
    # object-group service O-Worker
    #  service-object tcp destination range 100 200
    #  service-object tcp source eq 1234 destination gt nfs
    # object-group service O-UNIX-TCP tcp
    #  port-object eq https
    #  port-object range 100 400
    # object-group user test_og_user
    #  user LOCAL\new_user_1
    #  user LOCAL\new_user_2
    # object-group protocol test_og_protocol
    #  protocol-object tcp
    #  protocol-object udp

    # Using Overridden

    # Before state:
    # -------------
    #
    # ciscoasa# sh running-config object-group
    # object-group network test_og_network
    #  description test_og_network
    #  network-object host 192.0.2.1
    #  network-object host 192.0.2.2
    #  network-object 192.0.2.0 255.255.255.0
    #  network-object 198.51.100.0 255.255.255.0
    # object-group network test_network_og
    #  description test_network_og
    #  network-object host 198.51.100.1
    #  network-object host 198.51.100.2
    #  network-object 2001:db8:0:3::/64
    #  group-object test_og_network
    # object-group security test_og_security
    #  security-group name test_1
    #  security-group name test_2
    #  security-group tag 10
    #  security-group tag 20
    # object-group service O-Worker
    #  service-object tcp destination range 100 200
    #  service-object tcp source eq 1234 destination gt nfs
    # object-group service O-UNIX-TCP tcp
    #  port-object eq https
    #  port-object range 100 400
    # object-group user test_og_user
    #  user LOCAL\new_user_1
    #  user LOCAL\new_user_2

    - name: "Overridden module attributes of given object-group"
      cisco.asa.asa_ogs:
        config:
          - object_type: network
            object_groups:
              - name: test_og_network
                description: test_og_network_override
                network_object:
                  host:
                    - 198.51.100.1
                  address:
                    - 198.51.100.0 255.255.255.0
              - name: ANSIBLE_TEST
                network_object:
                  object:
                    - TEST1
                    - TEST2
          - object_type: protocol
            object_groups:
              - name: test_og_protocol
                description: test_og_protocol
                protocol_object:
                  protocol:
                    - tcp
                    - udp
        state: overridden

    # Commands Fired:
    # ---------------
    #
    # no object-group security test_og_security
    # no object-group service O-Worker
    # no object-group service O-UNIX-TCP
    # no object-group user test_og_user
    # object-group protocol test_og_protocol
    # description test_og_protocol
    # protocol tcp
    # protocol udp
    # object-group network test_og_network
    # description test_og_network_override
    # no network-object 192.0.2.0 255.255.255.0
    # no network-object 198.51.100.0 255.255.255.0
    # network-object 198.51.100.0 255.255.255.0
    # no network-object host 192.0.2.1
    # no network-object host 192.0.2.2
    # network-object host 198.51.100.1
    # no object-group network test_network_og
    # object-group network ANSIBLE_TEST
    # network-object object TEST1
    # network-object object TEST2

    # After state:
    # -------------
    #
    # ciscoasa# sh running-config object-group
    # object-group network test_og_network
    #  description test_og_network_override
    #  network-object host 198.51.100.1
    #  network-object 198.51.100.0 255.255.255.0
    # object-group network ANSIBLE_TEST
    #  network-object object TEST1
    #  network-object object TEST2
    # object-group protocol test_og_protocol
    #  protocol-object tcp
    #  protocol-object udp

    # Using Deleted

    # Before state:
    # -------------
    #
    # ciscoasa# sh running-config object-group
    # object-group network test_og_network
    #  description test_og_network
    #  network-object host 192.0.2.1
    #  network-object host 192.0.2.2
    #  network-object 192.0.2.0 255.255.255.0
    #  network-object 198.51.100.0 255.255.255.0
    # object-group network test_network_og
    #  description test_network_og
    #  network-object host 198.51.100.1
    #  network-object host 198.51.100.2
    #  network-object 2001:db8:0:3::/64
    #  group-object test_og_network
    # object-group security test_og_security
    #  security-group name test_1
    #  security-group name test_2
    #  security-group tag 10
    #  security-group tag 20
    # object-group service O-Worker
    #  service-object tcp destination range 100 200
    #  service-object tcp source eq 1234 destination gt nfs
    # object-group service O-UNIX-TCP tcp
    #  port-object eq https
    #  port-object range 100 400
    # object-group user test_og_user
    #  user LOCAL\new_user_1
    #  user LOCAL\new_user_2

    - name: "Delete given module attributes"
      cisco.asa.asa_ogs:
        config:
          - object_type: network
            object_groups:
              - name: test_og_network
              - name: test_network_og
          - object_type: security
            object_groups:
              - name: test_og_security
          - object_type: service
            object_groups:
              - name: O-UNIX-TCP
        state: deleted

    # Commands Fired:
    # ---------------
    #
    # no object-group network test_og_network
    # no object-group network test_network_og
    # no object-group security test_og_security
    # no object-group service O-UNIX-TCP

    # After state:
    # -------------
    #
    # ciscoasa# sh running-config object-group
    # object-group user test_og_user
    #  user LOCAL\new_user_1
    #  user LOCAL\new_user_2
    # object-group service O-Worker
    #  service-object tcp destination range 100 200
    #  service-object tcp source eq 1234 destination gt nfs

    # Using DELETED without any config passed
    # "(NOTE: This will delete all of configured resource module attributes)"

    # Before state:
    # -------------
    #
    # ciscoasa# sh running-config object-group
    # object-group network test_og_network
    #  description test_og_network
    #  network-object host 192.0.2.1
    #  network-object host 192.0.2.2
    #  network-object 192.0.2.0 255.255.255.0
    #  network-object 198.51.100.0 255.255.255.0
    # object-group network test_network_og
    #  description test_network_og
    #  network-object host 198.51.100.1
    #  network-object host 198.51.100.2
    #  network-object 2001:db8:0:3::/64
    #  group-object test_og_network
    # object-group security test_og_security
    #  security-group name test_1
    #  security-group name test_2
    #  security-group tag 10
    #  security-group tag 20
    # object-group user test_og_user
    #  user LOCAL\new_user_1
    #  user LOCAL\new_user_2

    - name: Delete ALL configured module attributes
      cisco.asa.asa_ogs:
        config:
        state: deleted

    # Commands Fired:
    # ---------------
    #
    # no object-group network test_og_network
    # no object-group network test_network_og
    # no object-group security test_og_security
    # no object-group user test_og_user

    # After state:
    # -------------
    #
    # ciscoasa# sh running-config object-group

    # Using Gathered

    # Before state:
    # -------------
    #
    # ciscoasa# sh running-config object-group
    # object-group network test_og_network
    #  description test_og_network
    #  network-object host 192.0.2.1
    #  network-object host 192.0.2.2
    #  network-object 192.0.2.0 255.255.255.0
    #  network-object 198.51.100.0 255.255.255.0
    # object-group network test_network_og
    #  description test_network_og
    #  network-object host 198.51.100.1
    #  network-object host 198.51.100.2
    #  network-object 2001:db8:0:3::/64
    #  group-object test_og_network
    # object-group security test_og_security
    #  security-group name test_1
    #  security-group name test_2
    #  security-group tag 10
    #  security-group tag 20
    # object-group user test_og_user
    #  user LOCAL\new_user_1
    #  user LOCAL\new_user_2

    - name: Gather listed OGs with provided configurations
      cisco.asa.asa_ogs:
        config:
        state: gathered

    # Module Execution Result:
    # ------------------------
    #
    # "gathered": [
    #         {
    #             "object_groups": [
    #                 {
    #                     "description": "test_security",
    #                     "name": "test_og_security",
    #                     "security_group": {
    #                         "sec_name": [
    #                             "test_2",
    #                             "test_1"
    #                         ],
    #                         "tag": [
    #                             10,
    #                             20
    #                         ]
    #                     }
    #                 }
    #             ],
    #             "object_type": "security"
    #         },
    #         {
    #             "object_groups": [
    #                 {
    #                     "description": "test_network_og",
    #                     "name": "test_network_og",
    #                     "network_object": {
    #                         "host": [
    #                             "198.51.100.1",
    #                             "198.51.100.2"
    #                         ],
    #                         "ipv6_address": [
    #                             "2001:db8:3::/64"
    #                         ]
    #                     }
    #                 },
    #                 {
    #                     "description": "test_og_network",
    #                     "name": "test_og_network",
    #                     "network_object": {
    #                         "address": [
    #                             "192.0.2.0 255.255.255.0",
    #                             "198.51.100.0 255.255.255.0"
    #                         ],
    #                         "host": [
    #                             "192.0.2.1",
    #                             "192.0.2.2"
    #                         ]
    #                     }
    #                 }
    #             ],
    #             "object_type": "network"
    #         },
    #         {
    #             "object_groups": [
    #                 {
    #                     "description": "test_user",
    #                     "name": "test_og_user",
    #                     "user_object": {
    #                         "user": [
    #                             {
    #                                 "domain": "LOCAL",
    #                                 "name": "new_user_1"
    #                             },
    #                             {
    #                                 "domain": "LOCAL",
    #                                 "name": "new_user_2"
    #                             }
    #                         ]
    #                     }
    #                 }
    #             ],
    #             "object_type": "user"
    #         }
    #     ]

    # After state:
    # ------------
    #
    # ciscoasa# sh running-config object-group
    # object-group network test_og_network
    #  description test_og_network
    #  network-object host 192.0.2.1
    #  network-object host 192.0.2.2
    #  network-object 192.0.2.0 255.255.255.0
    #  network-object 198.51.100.0 255.255.255.0
    # object-group network test_network_og
    #  description test_network_og
    #  network-object host 198.51.100.1
    #  network-object host 198.51.100.2
    #  network-object 2001:db8:0:3::/64
    #  group-object test_og_network
    # object-group security test_og_security
    #  security-group name test_1
    #  security-group name test_2
    #  security-group tag 10
    #  security-group tag 20
    # object-group user test_og_user
    #  user LOCAL\new_user_1
    #  user LOCAL\new_user_2

    # Using Rendered

    - name: Render the commands for provided  configuration
      cisco.asa.asa_ogs:
        config:
          - object_type: network
            object_groups:
              - name: test_og_network
                description: test_og_network
                network_object:
                  host:
                    - 192.0.2.1
                    - 192.0.2.2
                  address:
                    - 192.0.2.0 255.255.255.0
                    - 198.51.100.0 255.255.255.0
              - name: test_network_og
                description: test_network_og
                network_object:
                  host:
                    - 198.51.100.1
                    - 198.51.100.2
                  ipv6_address:
                    - 2001:db8:3::/64
          - object_type: security
            object_groups:
              - name: test_og_security
                description: test_security
                security_group:
                  sec_name:
                    - test_1
                    - test_2
                  tag:
                    - 10
                    - 20
          - object_type: user
            object_groups:
              - name: test_og_user
                description: test_user
                user_object:
                  user:
                    - name: new_user_1
                      domain: LOCAL
                    - name: new_user_2
                      domain: LOCAL
        state: rendered

    # Module Execution Result:
    # ------------------------
    #
    # "rendered": [
    #         "object-group security test_og_security",
    #         "description test_security",
    #         "security-group name test_1",
    #         "security-group name test_2",
    #         "security-group tag 10",
    #         "security-group tag 20",
    #         "object-group network test_og_network",
    #         "description test_og_network",
    #         "network-object 192.0.2.0 255.255.255.0",
    #         "network-object 198.51.100.0 255.255.255.0",
    #         "network-object host 192.0.2.1",
    #         "network-object host 192.0.2.2",
    #         "object-group network test_network_og",
    #         "description test_network_og",
    #         "network-object host 198.51.100.1",
    #         "network-object host 198.51.100.2",
    #         "network-object 2001:db8:3::/64",
    #         "object-group user test_og_user",
    #         "description test_user",
    #         "user LOCAL\new_user_1",
    #         "user LOCAL\new_user_2"
    #     ]

    # Using Parsed

    # parsed.cfg
    #
    # object-group network test_og_network
    #   description test_og_network
    #   network-object host 192.0.2.1
    #   network-object 192.0.2.0 255.255.255.0
    # object-group network test_network_og
    #   network-object 2001:db8:3::/64
    # object-group service test_og_service
    #   service-object tcp-udp

    - name: Parse the commands for provided configuration
      cisco.asa.asa_ogs:
        running_config: "{{ lookup('file', 'parsed.cfg') }}"
        state: parsed

    # Module Execution Result:
    # ------------------------
    #
    # "parsed": [
    #         {
    #             "object_groups": [
    #                 {
    #                     "name": "test_network_og"
    #                 },
    #                 {
    #                     "description": "test_og_network",
    #                     "name": "test_og_network",
    #                     "network_object": {
    #                         "host": [
    #                             "192.0.2.2"
    #                         ]
    #                     }
    #                 }
    #             ],
    #             "object_type": "network"
    #         },
    #         {
    #             "object_groups": [
    #                 {
    #                     "name": "test_og_service",
    #                     "service_object": {
    #                         "protocol": [
    #                             "tcp-udp",
    #                             "ipinip"
    #                         ]
    #                     }
    #                 }
    #             ],
    #             "object_type": "service"
    #         }
    #     ]



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
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The configuration as structured data after module completion.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration as structured data prior to module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
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
                <td>always</td>
                <td>
                            <div>The set of commands pushed to the remote device</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;object-group network test_network_og&#x27;, &#x27;description test_network_og&#x27;, &#x27;network-object host 192.0.2.1&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Sumit Jaiswal (@justjais)
