# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from ..generated._client_factory import cf_express_route_circuit_connection

    network_express_route_circuit_connection = CliCommandType(
        operations_tmpl='azure.mgmt.network.operations._express_route_circuit_connections_operations#ExpressRouteCircuitConnectionsOperations.{}',
        client_factory=cf_express_route_circuit_connection,
    )
    with self.command_group(
        'network express-route-circuit-connection',
        network_express_route_circuit_connection,
        client_factory=cf_express_route_circuit_connection,
    ) as g:
        g.custom_command('list', 'network_express_route_circuit_connection_list')

    from ..generated._client_factory import cf_express_route_circuit

    network_express_route_circuit = CliCommandType(
        operations_tmpl=(
            'azure.mgmt.network.operations._express_route_circuits_operations#ExpressRouteCircuitsOperations.{}'
        ),
        client_factory=cf_express_route_circuit,
    )
    with self.command_group(
        'network express-route-circuit', network_express_route_circuit, client_factory=cf_express_route_circuit
    ) as g:
        g.custom_command('list-route-table-summary', 'network_express_route_circuit_list_route_table_summary')
        g.custom_command('show-peering-stat', 'network_express_route_circuit_show_peering_stat')

    with self.command_group('network', is_experimental=True):
        pass
