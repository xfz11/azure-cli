# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network route-table route show",
)
class Show(AAZCommand):
    """Get the details of a route in a route table.

    :example: Get the details of a route in a route table.
        az network route-table route show -g MyResourceGroup --route-table-name MyRouteTable -n MyRoute -o table
    """

    _aaz_info = {
        "version": "2017-10-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/routetables/{}/routes/{}", "2017-10-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Route name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.route_table_name = AAZStrArg(
            options=["--route-table-name"],
            help="Route table name.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.RoutesGet(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class RoutesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeTables/{routeTableName}/routes/{routeName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "routeName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "routeTableName", self.ctx.args.route_table_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2017-10-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType()
            _schema_on_200.id = AAZStrType()
            _schema_on_200.name = AAZStrType()
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.properties
            properties.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            properties.next_hop_ip_address = AAZStrType(
                serialized_name="nextHopIpAddress",
            )
            properties.next_hop_type = AAZStrType(
                serialized_name="nextHopType",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )

            return cls._schema_on_200


__all__ = ["Show"]
