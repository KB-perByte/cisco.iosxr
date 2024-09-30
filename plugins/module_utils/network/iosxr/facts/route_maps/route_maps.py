# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The iosxr route_maps fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

import re

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.route_maps.route_maps import (
    Route_mapsArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.route_maps import (
    Route_mapsName,
    Route_mapsTemplate,
)


class Route_mapsFacts(object):
    """The iosxr route_maps facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Route_mapsArgs.argument_spec

    def get_policynames(self, connection):
        return connection.get("show running-config | include route-policy")

    def parse_route_policy(self, route_policy):
        result = {}
        lines = route_policy.splitlines()
        current_key = None
        current_value = []
        store_global = True
        global_value = []

        def process_else(else_line):
            else_result = {}
            else_current_key = None
            else_current_value = []
            else_store_global = True
            else_global_value = []

            for line in else_line:
                line = line.strip()
                if line.startswith("if ") or line.startswith("elseif ") or line.startswith("else"):
                    else_store_global = False
                    if else_current_key:
                        else_result[else_current_key] = else_current_value
                    else_current_key = line
                    else_current_value = []
                else:
                    else_current_value.append(line)

                if else_store_global:
                    else_global_value.append(line)

                if else_global_value:
                    else_result["global"] = else_global_value

            if else_current_key:
                else_result[else_current_key] = else_current_value

            return else_result

        for idx, line in enumerate(lines):
            line = line.strip()

            if line.startswith("if ") or line.startswith("elseif "):
                store_global = False
                if current_key:
                    result[current_key] = current_value
                current_key = line
                current_value = []
            else:
                current_value.append(line)

            if not (line.startswith("if ") or line.startswith("elseif ")) and line.startswith(
                "else",
            ):
                else_data = process_else(lines[idx + 1 : :])
                break

            if store_global:
                global_value.append(line)

        # Add the last block
        if current_key:
            result[current_key] = current_value

        if else_data:
            result["else"] = else_data

        if global_value:
            result["global"] = global_value

        return result

    def get_policy_config(self, connection, name):
        policy_data = connection.get(f"show running-config route-policy {name}")

        policy_map = self.parse_route_policy(policy_data)

        route_maps_parser = Route_mapsTemplate(lines=policy_data.splitlines(), module=self._module)
        objs = list(route_maps_parser.parse().values())
        return objs

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for Route_maps network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []
        policy_list = []

        if not data:
            data = self.get_policynames(connection=connection)

        # parse native config using the Route_maps template
        route_maps_parser = Route_mapsName(lines=data.splitlines(), module=self._module)
        objs = list(route_maps_parser.parse().values())

        for policies in objs:
            policy_list.append(self.get_policy_config(connection=connection, name=policies))

        ansible_facts["ansible_network_resources"].pop("route_maps", None)

        params = utils.remove_empties(
            route_maps_parser.validate_config(self.argument_spec, {"config": objs}, redact=True),
        )

        facts["route_maps"] = params["config"]
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts