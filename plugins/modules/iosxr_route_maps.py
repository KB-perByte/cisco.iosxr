#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for iosxr_route_maps
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
---
module: iosxr_route_maps
short_description: Resource module to configure route maps.
description:
  - This module configures and manages the attributes of Route maps on Cisco IOSXR.
version_added: 10.2.0
author: Sagar Paul (@KB-perByte)
notes:
  - Tested against Cisco IOS-XR 7.2.2.
  - This module works with connection C(network_cli).
options:
  config:
    description: A list of configurations for route policy.
    type: list
    elements: dict
    suboptions:
      name:
        description: Name of the route policy.
        type: str
      global: &global
        description: A list of global configurations for route policy.
        type: dict
        suboptions:
          add: &add
            description: Add offset to the existing value
            type: dict
            suboptions:
              eigrp_metric:
                description: EIGRP metric attribute
                type: dict
                suboptions:
                  bandwidth:
                    description: <0-4294967295> Bandwidth in Kbits per second
                    type: int
                  delay:
                    description: <0-4294967295> Delay metric in 10 microsecond units
                    type: int
                  reliability:
                    description: <0-255> Reliability metric where 255 is 100% reliable
                    type: int
                  effective_bandwith:
                    type: int
                    description: <0-255> Effective bandwidth metric (Loading) where 255 is 100% loaded
                  max_transmission:
                    description: <0-65535> Maximum Transmission Unit metric of the path
                    type: int
              rip_metric:
                description: <0-16> RIP metric attribute
                type: int
          apply: &apply
            description: Apply a route policy
            type: list
            elements: dict
            suboptions:
              route_policy:
                type: str
                description: Apply a specific route policy
              route_policy_input:
                type: str
                description: ipv4/ ipv6 / name-string
          drop: &drop
            type: bool
            description: Reject this route with no further processing
          pass: &pass
            type: bool
            description: Pass this route for further processing
          prepend: &prepend
            description: Prepend to BGP AS-path
            type: dict
            suboptions:
              number_of_times:
                type: int
                description: number of times to prepend
              as_path:
                type: int
                description: <1-4294967295> 32-bit decimal number/ 16-bit decimal number as-path
              most_recent:
                type: bool
                description: Most recent Autonomous System Number
              own_as:
                type: bool
                description: Local Autonomous System Number
          suppress_route: &suppess
            type: bool
            description: Suppress specific routes when aggregating
          unsuppress_route: &unsuppess
            type: bool
            description: Unsuppress specific aggregated routes
          remove: &remove
            description: Remove all private-as entries
            type: dict
            suboptions:
              set:
                type: bool
                description: Remove all private-as entries (remove as-path private-as)
              entire_aspath:
                type: bool
                description: Remove private-AS from entire aspath
          set: &set
            description: Set a route attribute
            type: dict
            suboptions:
              administrative_distance:
                description: Administrative Distance of the prefix, <1-255> 8 bit decimal numbe
                type: int
              aigp_metric:
                description: AIGP metric attribute
                type: dict
                suboptions:
                  icrement:
                    type: bool
                    description: "+ Increment the attribute with specified value"
                  decrement:
                    description: "- Decrement the attribute by specified value"
                    type: bool
                  metric_number:
                    description: <0-4294967295>  32-bit decimal number
                    type: int
                  igp_cost:
                    description: Internal routing protocol cost
                    type: bool
              attribute_set: # set attribute-set name-string 2232
                description: TE attribute-set name <0-4294967295> 32-bit decimal number
                type: str
              c_multicast_routing:
                description: Multicast Customer routing type
                type: dict
                suboptions:
                  bgp:
                    type: bool
                    description: BGP customer-multicast routing
                  pim:
                    type: bool
                    description: PIM customer-multicast routing
              community:
                description: BGP community attribute
                type: dict
                suboptions:
                  community_name:
                    type: str
                    description: Community set name
                  additive:
                    type: bool
                    description: Add to the existing community
              core_tree:
                description: Multicast Distribution Tree type
                type: dict
                suboptions:
                  ingress_replication:
                    type: bool
                    description: Ingress Replication core segment
                  ingress_replication_default:
                    type: bool
                    description: Ingress Replication Default MDT core
                  ingress_replication_partitioned:
                    type: bool
                    description: Ingress Replication Partitioned MDT core
                  mldp:
                    type: bool
                    description: MLDP core segment
                  mldp_default:
                    type: bool
                    description: MLDP Default MDT core
                  mldp_inband:
                    type: bool
                    description: MLDP Inband core
                  mldp_partitioned_mp2mp:
                    type: bool
                    description: MLDP Partitioned MP2MP MDT core
                  mldp_partitioned_p2mp:
                    type: bool
                    description: MLDP Partitioned P2MP MDT core
                  p2mp_te:
                    type: bool
                    description: P2MP TE core segment
                  p2mp_te_default:
                    type: bool
                    description: P2MP TE Default MDT core
                  p2mp_te_partitioned:
                    type: bool
                    description: P2MP TE Partitioned MDT core
                  pim_default:
                    type: bool
                    description: PIM Default MDT core
                  sr_p2mp:
                    type: bool
                    description: Segment-Routing P2MP core
              dampening:
                description: BGP route flap dampening parameters
                type: dict
                suboptions:
                  halflife:
                    type: int
                    description: Dampening penalty half-life, <1-45> Half-life time for penalty, default 15
                  max_suppress:
                    type: int
                    description: Maximum dampening penalty, <1-255> Maximum dampening penalty time, default 60
                  reuse:
                    type: int
                    description: Penalty before reusing suppressed route, <1-20000> Dampening reuse threshold, default 750
                  suppress:
                    type: int
                    description: Dampening penalty to start suppressing a route, <1-20000>  Suppress penalty threshold, default 2000
              downstream_core_tree:
                description: BGP I-PMSI/S-PMSI core tree type
                type: dict
                suboptions:
                  ingress_replication:
                    type: bool
                    description: Ingress Replication core segment
                  mldp:
                    type: bool
                    description: MLDP core segment
                  p2mp_te:
                    type: bool
                    description: P2MP TE core segment
                  sr_p2mp:
                    type: bool
                    description: Segment-Routing P2MP core
              eigrp_metric:
                description: EIGRP metric attribute
                type: dict
                suboptions:
                  bandwidth:
                    description: <0-4294967295> Bandwidth in Kbits per second
                    type: int
                  delay:
                    description: <0-4294967295> Delay metric in 10 microsecond units
                    type: int
                  reliability:
                    description: <0-255> Reliability metric where 255 is 100% reliable
                    type: int
                  effective_bandwith:
                    type: int
                    description: <0-255> Effective bandwidth metric (Loading) where 255 is 100% loaded
                  max_transmission:
                    description: <0-65535> Maximum Transmission Unit metric of the path
                    type: int
              fallback_vrf_lookup:
                description: fallback vrf look-up
                type: bool
              flow_tag:
                description: flow tag value for PBR BGP flow-tag, <1-63> 6 bit decimal number starting from 1
                type: int
              forward_class:
                description: Forward class (default value 0), <1-7> 3 bit decimal number starting from 1
                type: int
              ip_precedence:
                description: IP Precedence to classify packets, <1-7> 3 bit decimal number starting from 1
                type: int
              isis_metric:
                description: IS-IS metric attribute, <0-16777215> 24 bit decimal number
                type: int
              label:
                description: Set BGP label value, <0-1048575> 20 bit decimal number
                type: int
              label_index:
                description: Set Segment Routing label-index value, <0-1048575>  20 bit decimal number
                type: int
              label_mode:
                description: Set BGP label-mode value
                type: dict
                suboptions:
                  per_ce:
                    type: bool
                    description: Set the label mode to per-ce
                  per_prefix:
                    type: bool
                    description: Set the label mode to per-prefix
                  per_vrf:
                    type: bool
                    description: Set the label mode to per-vrf
              large_community:
                description: BGP large community attribute
                type: str
              level:
                description: Where to import route
                type: dict
                suboptions:
                  level_1:
                    type: bool
                    description: IS-IS level-1 routes
                  level_1_2:
                    type: bool
                    description: IS-IS level-1 and level-2 routes
                  level_2:
                    type: bool
                    description: IS-IS level-2 routes
              load_balance:
                description: Load-balance for ECMP ecmp-consistent
                type: bool
              lsm_root:
                description: Label Switched Multicast Root address
                type: str
              metric_type:
                description: Type of metric for destination routing protocol
                type: dict
                suboptions:
                  external:
                    type: bool
                    description: ISIS external metric-type
                  internal:
                    type: bool
                    description: ISIS internal metric-type
                  rib_metric_as_external:
                    type: bool
                    description: Use RIB metric and set ISIS external metric-type
                  rib_metric_as_internal:
                    type: bool
                    description: Use RIB metric and set ISIS internal metric-type
                  type_1:
                    type: bool
                    description: OSPF type-1 route
                  type_2:
                    type: bool
                    description: OSPF type-2 route
              mpls:
                description: MPLS traffic-eng attributeset name-string
                type: str
              next_hop:
                description: Next hop address specified in this route
                type: dict
                suboptions:
                  address:
                    type: str
                    description: next hop address
              origin:
                description: BGP origin code
                type: dict
                suboptions:
                  egp:
                    type: bool
                    description: ISIS external metric-type
                  igp:
                    type: bool
                    description: ISIS internal metric-type
                  rincomplete:
                    type: bool
                    description: Use RIB metric and set ISIS external metric-type
              ospf_metric:
                description: OSPF metric attribute
                type: int
              path_color:
                description: BGP Path Color for RIB (path-color external-reach)
                type: bool
              qos_group:
                description: QoS Group to classify packets
                type: int
              rib_metric:
                description: RIB metric for table-policy
                type: int
              rip_metric:
                description: RIP metric attribute
                type: int
              rip_tag:
                description: RIP Route tag attribute
                type: int
              rt_set:
                description: Limit on routes with paths with an RT-set
                type: int
              s_pmsi:
                description: S-PMSI Advertisement type (star-g)
                type: bool
              spf_priority:
                description: OSPF SPF priority
                type: dict
                suboptions:
                  critical:
                    type: bool
                    description: Critical priority
                  high:
                    type: bool
                    description: High priority
                  medium:
                    type: bool
                    description: Medium priority
              static_p2mp_te:
                description: Static P2MP-TE tunnel
                type: str
              tag:
                description: Route tag attribute
                type: int
              traffic_index:
                description: Traffic-index for BGP policy accounting
                type: dict
                suboptions:
                  index_number:
                    type: int
                    description: 6 bit decimal number starting from 1 <1-63>
                  ignore:
                    type: bool
                    description: Remove any traffic-index setting
              upstream_core_tree:
                description: BGP Leaf AD core tree type
                type: dict
                suboptions:
                  ingress_replication:
                    type: bool
                    description: Ingress Replication core segment
                  mldp:
                    type: bool
                    description: MLDP core segment
                  p2mp_te:
                    type: bool
                    description: P2MP TE core segment
                  sr_p2mp:
                    type: bool
                    description: Segment-Routing P2MP core
              vpn_distinguisher:
                description: BGP VPN distinguisher (VD) attribute
                type: int
              weight:
                description: Weight attribute for route selection
                type: int
      if: &ifcondition
        description: A list of configurations for route policy. Automatically considers then at last
        type: dict
        suboptions:
          conditions:
            type: list
            elements: dict
            suboptions:
              aigp_metric:
                description: AIGP metric attribute
                type: dict
                suboptions:
                  match:
                    description: Match criteria
                    choices:
                      - eq
                      - ge
                      - is
                      - le
                    type: str
                  input_number:
                    type: int
                    description: <0-4294967295> 32-bit decimal number
                  combine_condition: &combine_condition
                    description: Combine conditions with Boolean AND / OR
                    choices:
                      - and
                      - or
                    type: str
              as_path:
                description: BGP AS-path attribute
                type: dict
                suboptions:
                  input_name:
                    description: AS-path attribute (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              community:
                description: BGP community attribute
                type: dict
                suboptions:
                  match:
                    description: community match options
                    choices:
                      - is-empty
                      - matches-any
                      - matches-every
                      - matches-within
                    type: str
                  input_name:
                    description: community input and requires a match input (supports matches-any/matches-every/matches-within member or set)
                    type: str
                  combine_condition: *combine_condition
              community_length:
                description: BGP community length attribute
                type: dict
                suboptions:
                  match:
                    description: Match criteria
                    choices:
                      - eq
                      - ge
                      - is
                      - le
                    type: str
                  input_number:
                    type: int
                    description: <0-65535> 16-bit decimal number
                  combine_condition: *combine_condition
              destination:
                description: Destination address in the route
                type: dict
                suboptions:
                  match:
                    description: BGP extended community attribute, BGP Route Target (RT) extended community
                    choices:
                      - in
                      - is-backup-path
                      - is-best-external
                      - is-best-path
                      - is-multi-path
                      - longer-than
                      - or-longer
                    type: str
                  destination_name:
                    description: destination input and requires a match input (supports in/longer-than/or-longer member or set)
                    type: str
                  combine_condition: *combine_condition
              destination_prefix:
                description: destination address of flowspec NLRI
                type: dict
                suboptions:
                  input_name:
                    description: destination address of flowspec NLRI (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              esi:
                description: Ethernet Segment Identifier
                type: dict
                suboptions:
                  input_name:
                    description: Ethernet Segment Identifier (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              etag:
                description: Ethernet tag attribute
                type: dict
                suboptions:
                  input_name:
                    description: Ethernet tag attribute (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              evpn_gateway:
                description: Router's Gateway IP address
                type: dict
                suboptions:
                  input_name:
                    description: Router's Gateway IP address (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              evpn_originator:
                description: Originating Router's IP address
                type: dict
                suboptions:
                  input_name:
                    description: Originating Router's IP address (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              evpn_route_type:
                description: specifies EVPN route type
                type: dict
                suboptions:
                  input_number:
                    description: specifies EVPN route type, <1-5> 3 bit decimal number starting from 1 (supports is Exact Match)
                    type: int
                  combine_condition: *combine_condition
              extcommunity_color:
                description: BGP extended community attribute, BGP Color extended community
                type: dict
                suboptions:
                  match:
                    description: extcommunity color match options
                    choices:
                      - is-empty
                      - matches-any
                      - matches-every
                      - matches-within
                    type: str
                  community_name:
                    description: extcommunity input and requires a match input (supports matches-any/matches-every/matches-within member or set)
                    type: str
                  combine_condition: *combine_condition
              extcommunity_rt:
                description: BGP extended community attribute, BGP Route Target (RT) extended community
                type: dict
                suboptions:
                  match:
                    description: extcommunity rt match options
                    choices:
                      - is-empty
                      - matches-any
                      - matches-every
                      - matches-within
                    type: str
                  community_name:
                    description: extcommunity input and requires a match input (supports matches-any/matches-every/matches-within member or set)
                    type: str
                  combine_condition: *combine_condition
              extcommunity_seg_nh:
                description: BGP extended community attribute, P2MP Segmented Nexthop extended community
                type: dict
                suboptions:
                  match:
                    description: extcommunity seg nh match options
                    choices:
                      - is-empty
                      - matches-any
                      - matches-every
                      - matches-within
                    type: str
                  community_name:
                    description: extcommunity input and requires a match input (supports matches-any/matches-every/matches-within member or set)
                    type: str
                  combine_condition: *combine_condition
              extcommunity_soo:
                description: BGP extended community attribute, BGP Site of Origin (SoO) extended community
                type: dict
                suboptions:
                  match:
                    description: extcommunity soo match options
                    choices:
                      - is-empty
                      - matches-any
                      - matches-every
                      - matches-within
                    type: str
                  community_name:
                    description: extcommunity input and requires a match input (supports matches-any/matches-every/matches-within member or set)
                    type: str
                  combine_condition: *combine_condition
              i_pmsi_present:
                description: BGP I-PMSI Route present
                type: dict
                suboptions:
                  set:
                    description: Enable BGP I-PMSI Route present
                    type: bool
                  combine_condition: *combine_condition
              large_community:
                description: BGP large community attribute (supports is Exact Match)
                type: dict
                suboptions:
                  match:
                    description: large-community color match options
                    choices:
                      - is-empty
                      - matches-any
                      - matches-every
                      - matches-within
                    type: str
                  community_name:
                    description: large-community input and requires a match input (supports matches-any/matches-every/matches-within member or set)
                    type: str
                  combine_condition: *combine_condition
              local_preference:
                description: BGP local-preference attribute
                type: dict
                suboptions:
                  match:
                    description: Match criteria
                    choices:
                      - eq
                      - ge
                      - is
                      - le
                    type: str
                  input_number:
                    type: int
                    description: <0-4294967295> 32-bit decimal number
                  combine_condition: *combine_condition
              mac:
                description: MAC Address in the route
                type: dict
                suboptions:
                  input_name:
                    description: MAC Address in the route (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              med:
                description: BGP Multi-Exit-Discriminator attribute
                type: dict
                suboptions:
                  match:
                    description: Match criteria
                    choices:
                      - eq
                      - ge
                      - is
                      - le
                    type: str
                  input_number:
                    type: int
                    description: <0-4294967295> 32-bit decimal number
                  combine_condition: *combine_condition
              next_hop:
                description: Next hop address specified in this route
                type: dict
                suboptions:
                  input_name:
                    description: Next hop address specified in this route (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              orf_prefix:
                description: Specify BGP outbound route filter
                type: dict
                suboptions:
                  input_name:
                    description: Specify BGP outbound route filter (ORF) (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              origin:
                description: Specify BGP outbound route filter
                type: dict
                suboptions:
                  input_choice:
                    description: BGP origin code (supports is Exact Match)
                    choices:
                      - ebgp
                      - ibgp
                      - incomplete
                    type: str
                  combine_condition: *combine_condition
              path_type:
                description: BGP path type
                type: dict
                suboptions:
                  input_choice:
                    description: BGP path type (supports is Exact Match)
                    choices:
                      - ebgp
                      - ibgp
                    type: str
                  combine_condition: *combine_condition
              protocol:
                description: Protocol installing the route
                type: dict
                suboptions:
                  input_choice:
                    description: Protocol installing the route (supports is Exact Match)
                    choices:
                      - bgp
                      - connected
                      - eigrp
                      - isis
                      - ospf
                      - ospfv3
                      - rip
                      - static
                    type: str
                  combine_condition: *combine_condition
              rd:
                description: BGP VPN route-distinguisher (RD) attribute
                type: dict
                suboptions:
                  input_name:
                    description: BGP VPN route-distinguisher (RD) attribute (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              rib_has_route:
                description: Look in the rib for a route
                type: dict
                suboptions:
                  input_name:
                    description: Look in the rib for a route (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              rib_metric:
                description: RIB metric for table-policy
                type: dict
                suboptions:
                  match:
                    description: Match criteria
                    choices:
                      - eq
                      - ge
                      - is
                      - le
                    type: str
                  input_number:
                    type: int
                    description: <0-4294967295> 32-bit decimal number
                  combine_condition: *combine_condition
              route_aggregated:
                description: Check whether route is aggregated
                type: dict
                suboptions:
                  set:
                    description: Enable whether route is aggregated
                    type: bool
                  combine_condition: *combine_condition
              route_has_label:
                description: MPLS label set in the route
                type: dict
                suboptions:
                  set:
                    description: Enable MPLS label set in the route
                    type: bool
                  combine_condition: *combine_condition
              route_has_vrf_ri:
                description: RIB route has VRF Route-Import Extended Community
                type: dict
                suboptions:
                  set:
                    description: Enable MPLS label set in the route
                    type: bool
                  combine_condition: *combine_condition
              route_type:
                description: Type of route (support is Exact Match)
                type: dict
                suboptions:
                  input_choice:
                    description: Choose type of route
                    choices:
                      - interarea
                      - internal
                      - level-1
                      - level-1-2
                      - level-2
                      - local
                      - ospf-external-type-1
                      - ospf-external-type-2
                      - ospf-inter-area
                      - ospf-intra-area
                      - ospf-nssa-type-1
                      - ospf-nssa-type-2
                      - type-1
                      - type-2
                    type: str
                  combine_condition: *combine_condition
              source:
                description: Advertising source address of route
                type: dict
                suboptions:
                  input_name:
                    description: Advertising source address of route (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              source_prefix:
                description: Advertising source address of flowspec NLRI
                type: dict
                suboptions:
                  input_name:
                    description: Advertising source address of flowspec NLRI (supports in member or set)
                    type: str
                  combine_condition: *combine_condition
              tag:
                description: Route tag attribute
                type: dict
                suboptions:
                  match:
                    description: Match criteria
                    choices:
                      - eq
                      - ge
                      - in
                      - is
                      - le
                    type: str
                  input_number:
                    type: int
                    description: <0-4294967295> 32-bit decimal number
                  combine_condition: *combine_condition
              validation_state:
                description: Validation-State (supports is Exact Match)
                type: dict
                suboptions:
                  input_choice:
                    description: Choose Validation-State
                    choices:
                      - invalid
                      - not-found
                      - valid
                    type: str
                  combine_condition: *combine_condition
              vpn_distinguisher:
                description: BGP VPN distinguisher (VD) attribute
                type: dict
                suboptions:
                  input_number:
                    description: BGP VPN distinguisher (VD) attribute (supports is Exact Match)
                    type: int
                  combine_condition: *combine_condition
          add: *add
          apply: *apply
          drop: *drop
          pass: *pass
          prepend: *prepend
          suppress_route: *suppess
          unsuppress_route: *unsuppess
          remove: *remove
          set: *set
      elif: *ifcondition
      else:
        description: A list of configurations for route policy. Automatically considers then at last
        type: dict
        suboptions:
          global: *global
          if_of_else: *ifcondition
          else_of_else:
            description: A list of configurations for route policy. Automatically considers then at last
            type: dict
            suboptions:
              add: *add
              apply: *apply
              drop: *drop
              pass: *pass
              prepend: *prepend
              suppress_route: *suppess
              unsuppress_route: *unsuppess
              remove: *remove
              set: *set
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be and aggregate of the output received from the IOS XR
        device by executing the command B(show running-config route-policy <policy_name>)
        for per route-policy.
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
      - The state the configuration should be left in
      - The states I(rendered), I(gathered) and I(parsed) does not perform any change
        on the device.
      - The state I(rendered) will transform the configuration in C(config) option to
        platform specific CLI commands which will be returned in the I(rendered) key
        within the result. For state I(rendered) active connection to remote host is
        not required.
      - The state I(gathered) will fetch the running configuration from device and
        transform it into structured data in the format as per the resource module
        argspec and the value is returned in the I(gathered) key within the result.
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into JSON format as per the resource module parameters and the
        value is returned in the I(parsed) key within the result. The value of
        C(running_config) option should be the aggregate of the output of
        command I(show running-config route-policy <policy_name>) that gives individual
        route-policy details and executed on device.
        For state I(parsed) active connection to remote host is not required.
    type: str
    choices:
      - merged
      - replaced
      - overridden
      - deleted
      - rendered
      - gathered
      - parsed
    default: merged
"""

EXAMPLES = """

"""

RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
after:
  description: The resulting configuration after module execution.
  returned: when changed
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
commands:
  description: The set of commands pushed to the remote device.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: list
  sample:
    - sample command 1
    - sample command 2
    - sample command 3
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - sample command 1
    - sample command 2
    - sample command 3
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.route_maps.route_maps import (
    Route_mapsArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.route_maps.route_maps import (
    Route_maps,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Route_mapsArgs.argument_spec,
        mutually_exclusive=[["config", "running_config"]],
        required_if=[
            ["state", "merged", ["config"]],
            ["state", "replaced", ["config"]],
            ["state", "overridden", ["config"]],
            ["state", "rendered", ["config"]],
            ["state", "parsed", ["running_config"]],
        ],
        supports_check_mode=True,
    )

    result = Route_maps(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
