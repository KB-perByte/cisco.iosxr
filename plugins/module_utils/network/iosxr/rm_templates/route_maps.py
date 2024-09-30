# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Route_maps parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class Route_mapsName(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Route_mapsName, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "name",
            "getval": re.compile(
                r"""
                ^route-policy\s(?P<name>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                '{{ name }}': '{{ name }}',
            },
            "shared": True,
        },
    ]
    # fmt: on


class Route_mapsConditionals(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Route_mapsConditionals, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "name",
            "getval": re.compile(
                r"""
                ^route-policy\s(?P<name>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                '{{ name }}': '{{ name }}',
            },
            "shared": True,
        },
        {
            "name": "conditions.aigp_metric",
            "getval": re.compile(
                r"""
                ^aigrp-metric
                (\s(?P<match>eq|ge|is|le))?
                (\s(?P<input_number>\d+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "aigp_metric": {
                        "match": "{{ match }}",
                        "input_number": "{{ input_number }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.as_path",
            "getval": re.compile(
                r"""
                ^as-path\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "aigp_metric": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.community",
            "getval": re.compile(
                r"""
                ^community
                (\s(?P<match>is-empty|matches-any|matches-every|matches-within))?
                (\s(?P<input_number>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "aigp_metric": {
                        "match": "{{ match }}",
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.destination",
            "getval": re.compile(
                r"""
                ^destination
                (\s(?P<match>in|is-backup-path|is-best-external|is-best-path|is-multi-path|longer-than|or-longer))?
                (\s(?P<destination_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "destination": {
                        "match": "{{ match }}",
                        "destination_name": "{{ destination_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.destination_prefix",
            "getval": re.compile(
                r"""
                ^destination-prefix\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "destination_prefix": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.esi",
            "getval": re.compile(
                r"""
                ^esi\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "esi": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.etag",
            "getval": re.compile(
                r"""
                ^etag\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "etag": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.evpn_gateway",
            "getval": re.compile(
                r"""
                ^evpn-gateway\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "evpn_gateway": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.evpn_originator",
            "getval": re.compile(
                r"""
                ^evpn-originator\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "evpn_originator": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.evpn_route_type",
            "getval": re.compile(
                r"""
                ^evpn-route-type\sis
                (\s(?P<input_name>\d+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "evpn_route_type": {
                        "input_number": "{{ input_number }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.extcommunity_color",
            "getval": re.compile(
                r"""
                ^extcommunity\scolor
                (\s(?P<match>is-empty|matches-any|matches-every|matches-within))?
                (\s(?P<community_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "extcommunity_color": {
                        "match": "{{ match }}",
                        "community_name": "{{ community_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.extcommunity_rt",
            "getval": re.compile(
                r"""
                ^extcommunity\srt
                (\s(?P<match>is-empty|matches-any|matches-every|matches-within))?
                (\s(?P<community_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "extcommunity_rt": {
                        "match": "{{ match }}",
                        "community_name": "{{ community_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.extcommunity_seg_nh",
            "getval": re.compile(
                r"""
                ^extcommunity\sseg-nh
                (\s(?P<match>is-empty|matches-any|matches-every|matches-within))?
                (\s(?P<community_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "extcommunity_seg_nh": {
                        "match": "{{ match }}",
                        "community_name": "{{ community_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.extcommunity_soo",
            "getval": re.compile(
                r"""
                ^extcommunity\ssoo
                (\s(?P<match>is-empty|matches-any|matches-every|matches-within))?
                (\s(?P<community_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "extcommunity_soo": {
                        "match": "{{ match }}",
                        "community_name": "{{ community_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.i_pmsi_present",
            "getval": re.compile(
                r"""
                ^i-pmsi-present
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "i_pmsi_present": {
                        "set": True,
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.large_community",
            "getval": re.compile(
                r"""
                ^large-community
                (\s(?P<match>is-empty|matches-any|matches-every|matches-within))?
                (\s(?P<community_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "large_community": {
                        "match": "{{ match }}",
                        "community_name": "{{ community_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.local_preference",
            "getval": re.compile(
                r"""
                ^local-preference
                (\s(?P<match>eq|ge|is|le))?
                (\s(?P<input_number>\d+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "local_preference": {
                        "match": "{{ match }}",
                        "input_number": "{{ input_number }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.mac",
            "getval": re.compile(
                r"""
                ^mac
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "mac": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.med",
            "getval": re.compile(
                r"""
                ^med
                (\s(?P<match>eq|ge|is|le))
                (\s(?P<input_number>\d+))
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "med": {
                        "match": "{{ match }}",
                        "input_number": "{{ input_number }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.next_hop",
            "getval": re.compile(
                r"""
                ^next-hop
                (\s(?P<input_name>\([^)]*\)|\S+))
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "next_hop": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.orf_prefix",
            "getval": re.compile(
                r"""
                ^orf\sprefix\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "orf_prefix": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.origin",
            "getval": re.compile(
                r"""
                ^origin\sis
                (\s(?P<input_choice>ebgp|ibgp|incomplete))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "origin": {
                        "input_choice": "{{ input_choice }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.path_type",
            "getval": re.compile(
                r"""
                ^path-type\sis
                (\s(?P<input_choice>ebgp|ibgp))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "path_type": {
                        "input_choice": "{{ input_choice }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.protocol",
            "getval": re.compile(
                r"""
                ^protocol\sis
                (\s(?P<input_choice>bgp|connected|eigrp|isis|ospf|ospfv3|rip|static))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "protocol": {
                        "input_choice": "{{ input_choice }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.rd",
            "getval": re.compile(
                r"""
                ^rd\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "rd": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.rib_has_route",
            "getval": re.compile(
                r"""
                ^rib-has-route\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "rib_has_route": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.rib_metric",
            "getval": re.compile(
                r"""
                ^rib-metric
                (\s(?P<match>eq|ge|is|le))
                (\s(?P<input_number>\d+))
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "rib_metric": {
                        "match": "{{ match }}",
                        "input_number": "{{ input_number }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.route_aggregated",
            "getval": re.compile(
                r"""
                ^route-aggregated
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "route_aggregated": {
                        "set": True,
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.route_has_label",
            "getval": re.compile(
                r"""
                ^route-has-label
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "route_has_label": {
                        "set": True,
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.route_has_vrf_ri",
            "getval": re.compile(
                r"""
                ^route-has-vrf-ri
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "route_has_vrf_ri": {
                        "set": True,
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.route_type",
            "getval": re.compile(
                r"""
                ^route-type\sis
                (\s(?P<input_choice>interarea|internal|level-1|level-1-2|level-2|local|ospf-external-type-1|ospf-external-type-2|ospf-inter-area|ospf-intra-area|ospf-nssa-type-1|ospf-nssa-type-2|type-1|type-2))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "route_type": {
                        "input_choice": "{{ input_choice }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.source",
            "getval": re.compile(
                r"""
                ^source\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "source": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.source_prefix",
            "getval": re.compile(
                r"""
                ^source-prefix\sin
                (\s(?P<input_name>\([^)]*\)|\S+))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "source": {
                        "input_name": "{{ input_name }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.tag",
            "getval": re.compile(
                r"""
                ^tag
                (\s(?P<match>eq|ge|is|le))
                (\s(?P<input_number>\d+))
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "tag": {
                        "match": "{{ match }}",
                        "input_number": "{{ input_number }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.validation_state",
            "getval": re.compile(
                r"""
                ^validation-state\sis
                (\s(?P<input_choice>invalid|not-found|valid))?
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "validation_state": {
                        "input_choice": "{{ input_choice }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
        {
            "name": "conditions.vpn_distinguisher",
            "getval": re.compile(
                r"""
                ^vpn-distinguisher\sis
                (\s(?P<input_number>\d+))
                (\s(?P<combine_condition>and|or|then))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "conditions": {
                    "vpn_distinguisher": {
                        "input_number": "{{ input_number }}",
                        "combine_condition": "{{ combine_condition }}",
                    },
                },
            },
        },
    ]
    # fmt: on


class Route_mapsTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Route_mapsTemplate, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "name",
            "getval": re.compile(
                r"""
                ^route-policy\s(?P<name>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                },
            },
            "shared": True,
        },
        {
            "name": "add.eigrp_metric",
            "getval": re.compile(
                r"""
                \s+add\seigrp-metric
                (\s(?P<bandwidth>\d+))?
                (\s(?P<delay>\d+))?
                (\s(?P<reliability>\d+))?
                (\s(?P<effective_bandwith>\d+))?
                (\s(?P<max_transmission>\d+))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                '{{ name }}': {
                    "add": {
                        "eigrp_metric": {
                            "bandwidth": "{{ bandwidth }}",
                            "delay": "{{ delay }}",
                            "reliability": "{{ reliability }}",
                            "effective_bandwith": "{{ effective_bandwith }}",
                            "max_transmission": "{{ max_transmission }}",
                        },
                    },
                },
            },
        },
        {
            "name": "add.rip_metric",
            "getval": re.compile(
                r"""
                \s+add\srip_metric
                (\s(?P<rip_metric>\d+))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                '{{ name }}': {
                    "add": {
                        "rip_metric": "{{ bandwidth }}",
                    },
                },
            },
        },
        {
            "name": "apply",
            "getval": re.compile(
                r"""
                \s+apply
                (\s(?P<route_policy>\S+))
                (\s(?P<route_policy_input>.+))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                '{{ name }}': {
                    "apply": [
                        {
                            "route_policy": "{{ route_policy }}",
                            "route_policy_input": "{{ route_policy_input }}",
                        },
                    ],
                },
            },
        },
        {
            "name": "drop",
            "getval": re.compile(
                r"""
                \s+drop
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "drop": True,
                },
            },
        },
        {
            "name": "pass",
            "getval": re.compile(
                r"""
                \s+pass
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "pass": True,
                },
            },
        },
        {
            "name": "prepend",
            "getval": re.compile(
                r"""
                \s+prepend
                (\sas-path\s(?P<as_path>\d+))?
                (\s(?P<most_recent>most-recent))?
                (\s(?P<own_as>own-as))?
                (\s(?P<number_of_times>\d+))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "prepend": {
                        "as_path": "{{ as_path }}",
                        "most_recent": "{{ not not most_recent }}",
                        "own_as": "{{ not not own_as }}",
                        "number_of_times": "{{ number_of_times }}",
                    },
                },
            },
        },
        {
            "name": "suppress_route",
            "getval": re.compile(
                r"""
                \s+suppress-route
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "suppress_route": True,
                },
            },
        },
        {
            "name": "unsuppress_route",
            "getval": re.compile(
                r"""
                \s+unsuppress-route
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "unsuppress_route": True,
                },
            },
        },
        {
            "name": "remove",
            "getval": re.compile(
                r"""
                \s+remove\sas-path
                (\s(?P<set>private-as))
                (\s(?P<entire_aspath>entire-aspath))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "remove": {
                        "set": True,
                        "as_path": "{{ as_path }}",
                    },
                },
            },
        },
        { # set starts
            "name": "set.administrative_distance",
            "getval": re.compile(
                r"""
                \s+set\sadministrative-distance
                (\s(?P<administrative_distance>\d+))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "administrative_distance": "{{ administrative_distance }}",
                    },
                },
            },
        },
        {
            "name": "set.aigp_metric",
            "getval": re.compile(
                r"""
                \s+set\saigp-metric
                (\s(?P<icrement>\+))?
                (\s(?P<decrement>\-))?
                (\s(?P<metric_number>\d+))?
                (\s(?P<igp_cost>igp-cost))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "aigp_metric": {
                            "icrement": "{{ not not icrement }}",
                            "decrement": "{{ not not decrement }}",
                            "metric_number": "{{ metric_number }}",
                            "igp_cost": "{{ not not igp_cost }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.attribute_set",
            "getval": re.compile(
                r"""
                \s+set\sattribute-set\sname-string
                (\s(?P<attribute_set>\d+))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "attribute_set": "{{ attribute_set }}",
                    },
                },
            },
        },
        {
            "name": "set.c_multicast_routing",
            "getval": re.compile(
                r"""
                \s+set\sc-multicast-routing
                (\s(?P<bgp>bgp))?
                (\s(?P<pim>pim))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "c_multicast_routing": {
                            "bgp": "{{ not not bgp }}",
                            "pim": "{{ not not pim }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.community",
            "getval": re.compile(
                r"""
                \s+set\scommunity
                (\s(?P<community_name>\S+))?
                (\s(?P<additive>additive))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "community": {
                            "community_name": "{{ community_name }}",
                            "additive": "{{ not not additive }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.core_tree",
            "getval": re.compile(
                r"""
                \s+set\score-tree
                (\s(?P<ingress_replication>ingress-replication))?
                (\s(?P<ingress_replication_default>ingress-replication-default))?
                (\s(?P<ingress_replication_partitioned>ingress-replication-partitioned))?
                (\s(?P<mldp>mldp))?
                (\s(?P<mldp_default>mldp-default))?
                (\s(?P<mldp_inband>mldp-inband))?
                (\s(?P<mldp_partitioned_mp2mp>mldp-partitioned-mp2mp))?
                (\s(?P<mldp_partitioned_p2mp>mldp-partitioned-p2mp))?
                (\s(?P<p2mp_te>p2mp-te))?
                (\s(?P<p2mp_te_default>p2mp-te-default))?
                (\s(?P<p2mp_te_partitioned>p2mp-te-partitioned))?
                (\s(?P<pim_default>pim-default))?
                (\s(?P<sr_p2mp>sr-p2mp))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "core_tree": {
                            "ingress_replication": "{{ not not ingress_replication }}",
                            "ingress_replication_default": "{{ not not ingress_replication_default }}",
                            "ingress_replication_partitioned": "{{ not not ingress_replication_partitioned }}",
                            "mldp": "{{ not not mldp }}",
                            "mldp_default": "{{ not not mldp_default }}",
                            "mldp_inband": "{{ not not mldp_inband }}",
                            "mldp_partitioned_mp2mp": "{{ not not mldp_partitioned_mp2mp }}",
                            "mldp_partitioned_p2mp": "{{ not not mldp_partitioned_p2mp }}",
                            "p2mp_te": "{{ not not p2mp_te }}",
                            "p2mp_te_default": "{{ not not p2mp_te_default }}",
                            "p2mp_te_partitioned": "{{ not not p2mp_te_partitioned }}",
                            "pim_default": "{{ not not pim_default }}",
                            "sr_p2mp": "{{ not not sr_p2mp }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.dampening",
            "getval": re.compile(
                r"""
                \s+set\sdampening
                (\s(?P<halflife>\d+))?
                (\s(?P<suppress>\d+))?
                (\s(?P<reuse>\d+))?
                (\s(?P<max_suppress>\d+))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "dampening": {
                            "halflife": "{{ halflife }}",
                            "max_suppress": "{{ max_suppress }}",
                            "reuse": "{{ reuse }}",
                            "suppress": "{{ suppress }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.downstream_core_tree",
            "getval": re.compile(
                r"""
                \s+set\sdownstream-core-tree
                (\s(?P<ingress_replication>ingress-replication))?
                (\s(?P<mldp>mldp))?
                (\s(?P<p2mp_te>p2mp-te))?
                (\s(?P<sr_p2mp>sr-p2mp))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "downstream_core_tree": {
                            "ingress_replication": "{{ not not ingress_replication }}",
                            "mldp": "{{ not not mldp }}",
                            "p2mp_te": "{{ not not p2mp_te }}",
                            "sr_p2mp": "{{ not not sr_p2mp }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.eigrp_metric",
            "getval": re.compile(
                r"""
                \s+set\seigrp-metric
                (\s(?P<bandwidth>\d+))?
                (\s(?P<delay>\d+))?
                (\s(?P<reliability>\d+))?
                (\s(?P<effective_bandwith>\d+))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "eigrp_metric": {
                            "bandwidth": "{{ bandwidth }}",
                            "delay": "{{ delay }}",
                            "reliability": "{{ reliability }}",
                            "effective_bandwith": "{{ effective_bandwith }}",
                            "max_transmission": "{{ max_transmission }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.fallback_vrf_lookup",
            "getval": re.compile(
                r"""
                \s+set\sfallback-vrf-lookup
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "fallback_vrf_lookup": True,
                    },
                },
            },
        },
        {
            "name": "set.flow_tag",
            "getval": re.compile(
                r"""
                \s+set\sflow-tag
                (\s(?P<flow_tag>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "flow_tag": "{{ flow_tag }}",
                    },
                },
            },
        },
        {
            "name": "set.forward_class",
            "getval": re.compile(
                r"""
                \s+set\sforward-class
                (\s(?P<flow_tag>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "forward_class": "{{ forward_class }}",
                    },
                },
            },
        },
        {
            "name": "set.ip_precedence",
            "getval": re.compile(
                r"""
                \s+set\sip-precedence
                (\s(?P<ip_precedence>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "ip_precedence": "{{ ip_precedence }}",
                    },
                },
            },
        },
        {
            "name": "set.isis_metric",
            "getval": re.compile(
                r"""
                \s+set\sisis-metric
                (\s(?P<isis_metric>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "isis_metric": "{{ isis_metric }}",
                    },
                },
            },
        },
        {
            "name": "set.label",
            "getval": re.compile(
                r"""
                \s+set\slabel
                (\s(?P<label>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "label": "{{ label }}",
                    },
                },
            },
        },
        {
            "name": "set.label_index",
            "getval": re.compile(
                r"""
                \s+set\slabel-index
                (\s(?P<label_index>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "label_index": "{{ label_index }}",
                    },
                },
            },
        },
        {
            "name": "set.label_mode",
            "getval": re.compile(
                r"""
                \s+set\slabel-mode
                (\s(?P<per_ce>per-ce))?
                (\s(?P<per_prefix>per-prefix))?
                (\s(?P<per_vrf>per-vrf))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "label_mode": {
                            "per_ce": "{{ not not per_ce }}",
                            "per_prefix": "{{ not not per_prefix }}",
                            "per_vrf": "{{ not not per_vrf }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.large_community",
            "getval": re.compile(
                r"""
                \s+set\slarge-community
                (\s(?P<large_community>.+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "large_community": "{{ large_community }}",
                    },
                },
            },
        },
        {
            "name": "set.level",
            "getval": re.compile(
                r"""
                \s+set\slevel
                (\s(?P<level_1>level-1))?
                (\s(?P<level_1_2>level-1-2))?
                (\s(?P<level_2>level-2))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "level": {
                            "level_1": "{{ not not level_1 }}",
                            "level_1_2": "{{ not not level_1_2 }}",
                            "level_2": "{{ not not level_2 }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.load_balance",
            "getval": re.compile(
                r"""
                \s+set\sload-balance\secmp-consistent
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "load_balance": True,
                    },
                },
            },
        },
        {
            "name": "set.lsm_root",
            "getval": re.compile(
                r"""
                \s+set\slsm-root
                (\s(?P<lsm_root>\S+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "lsm_root": "{{ lsm_root }}",
                    },
                },
            },
        },
        {
            "name": "set.metric_type",
            "getval": re.compile(
                r"""
                \s+set\smetric_type
                (\s(?P<external>external))?
                (\s(?P<internal>internal))?
                (\s(?P<rib_metric_as_external>rib-metric-as-external))?
                (\s(?P<rib_metric_as_internal>rib-metric-as-internal))?
                (\s(?P<type_1>type-1))?
                (\s(?P<type_2>type-2))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "metric_type": {
                            "external": "{{ not not external }}",
                            "internal": "{{ not not internal }}",
                            "rib_metric_as_external": "{{ not not rib_metric_as_external }}",
                            "rib_metric_as_internal": "{{ not not rib_metric_as_internal }}",
                            "type_1": "{{ not not type_1 }}",
                            "type_2": "{{ not not type_2 }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.mpls",
            "getval": re.compile(
                r"""
                \s+set\smpls\straffic-eng\sattributeset
                (\s(?P<mpls>\S+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "mpls": "{{ mpls }}",
                    },
                },
            },
        },
        {
            "name": "set.next_hop",
            "getval": re.compile(
                r"""
                \s+set\snext-hop
                (\s(?P<next_hop>\S+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "next_hop":{
                            "address": "{{ next_hop }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.origin",
            "getval": re.compile(
                r"""
                \s+set\sorigin
                (\s(?P<egp>egp))?
                (\s(?P<igp>igp))?
                (\s(?P<rincomplete>incomplete))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "origin": {
                            "egp": "{{ not not egp }}",
                            "igp": "{{ not not igp }}",
                            "rincomplete": "{{ not not rincomplete }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.ospf_metric",
            "getval": re.compile(
                r"""
                \s+set\sospf-metric
                (\s(?P<ospf_metric>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "ospf_metric": "{{ ospf_metric }}",
                    },
                },
            },
        },
        {
            "name": "set.path_color",
            "getval": re.compile(
                r"""
                \s+set\spath-color\sexternal-reach
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "path_color": True,
                    },
                },
            },
        },
        {
            "name": "set.qos_group",
            "getval": re.compile(
                r"""
                \s+set\sqos-group
                (\s(?P<qos_group>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "qos_group": "{{ qos_group }}",
                    },
                },
            },
        },
        {
            "name": "set.rib_metric",
            "getval": re.compile(
                r"""
                \s+set\srib-metric
                (\s(?P<rib_metric>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "rib_metric": "{{ rib_metric }}",
                    },
                },
            },
        },
        {
            "name": "set.rip_metric",
            "getval": re.compile(
                r"""
                \s+set\srip-metric
                (\s(?P<rip_metric>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "rip_metric": "{{ rip_metric }}",
                    },
                },
            },
        },
        {
            "name": "set.rip_tag",
            "getval": re.compile(
                r"""
                \s+set\srip-tag
                (\s(?P<rip_tag>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "rip_tag": "{{ rip_tag }}",
                    },
                },
            },
        },
        {
            "name": "set.rt_set",
            "getval": re.compile(
                r"""
                \s+set\srt-set
                (\s(?P<rt_set>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "rt_set": "{{ rt_set }}",
                    },
                },
            },
        },
        {
            "name": "set.s_pmsi",
            "getval": re.compile(
                r"""
                \s+set\ss-pmsi\sstart-g
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "s_pmsi": True,
                    },
                },
            },
        },
        {
            "name": "set.spf_priority",
            "getval": re.compile(
                r"""
                \s+set\sspf-priority
                (\s(?P<critical>critical))?
                (\s(?P<high>high))?
                (\s(?P<medium>medium))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "spf_priority": {
                            "critical": "{{ not not critical }}",
                            "high": "{{ not not high }}",
                            "medium": "{{ not not medium }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.static_p2mp_te",
            "getval": re.compile(
                r"""
                \s+set\sstatic-p2mp-te
                (\s(?P<static_p2mp_te>\S+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "static_p2mp_te": "{{ static_p2mp_te }}",
                    },
                },
            },
        },
        {
            "name": "set.tag",
            "getval": re.compile(
                r"""
                \s+set\stag
                (\s(?P<tag>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "tag": "{{ tag }}",
                    },
                },
            },
        },
        {
            "name": "set.traffic_index",
            "getval": re.compile(
                r"""
                \s+set\straffic-index
                (\s(?P<index_number>\d+))?
                (\s(?P<ignore>ignore))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "traffic_index": {
                            "index_number": "{{ index_number }}",
                            "ignore": "{{ not not ignore }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.upstream_core_tree",
            "getval": re.compile(
                r"""
                \s+set\supstream-core-tree
                (\s(?P<ingress_replication>ingress-replication))?
                (\s(?P<mldp>mldp))?
                (\s(?P<p2mp_te>p2mp-te))?
                (\s(?P<sr_p2mp>sr-p2mp))?
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "upstream_core_tree": {
                            "ingress_replication": "{{ not not ingress_replication }}",
                            "mldp": "{{ not not mldp }}",
                            "p2mp_te": "{{ not not p2mp_te }}",
                            "sr_p2mp": "{{ not not sr_p2mp }}",
                        },
                    },
                },
            },
        },
        {
            "name": "set.vpn_distinguisher",
            "getval": re.compile(
                r"""
                \s+set\svpn-distinguisher
                (\s(?P<vpn_distinguisher>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "vpn_distinguisher": "{{ vpn_distinguisher }}",
                    },
                },
            },
        },
        {
            "name": "set.weight",
            "getval": re.compile(
                r"""
                \s+set\sweight
                (\s(?P<weight>\d+))
                $""", re.VERBOSE,
            ),
            "setval": "",
            "result": {
                "{{ name }}": {
                    "set": {
                        "weight": "{{ weight }}",
                    },
                },
            },
        }, # set ends
    ]
    # fmt: on