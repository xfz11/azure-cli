# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    get_enum_type,
    resource_group_name_type
)


def load_arguments(self, _):

    with self.argument_context('sshkey generate') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('ssh_public_key_name', options_list=['--name', '-n', '--ssh-public-key-name'], type=str, help='The '
                   'name of the SSH public key.', id_part='name')

    with self.argument_context('sig group-list') as c:
        c.argument('shared_to', options_list=['--scope'], arg_type=get_enum_type(['tenant', 'subscription']),
                   help='The query parameter to decide what shared galleries to fetch when doing listing operations.',
                   default='subscription')

    for scope in ['sig share add', 'sig share remove']:
        with self.argument_context(scope) as c:
            c.argument('resource_group_name', resource_group_name_type)
            c.argument('gallery_name', type=str, help='The name of the Shared Image Gallery.', id_part='name')
            c.argument('subscription_ids', nargs='+', help='A list of subscription ids to share the gallery.')
            c.argument('tenant_ids', nargs='+', help='A list of tenant ids to share the gallery.')

    with self.argument_context('sig share add') as c:
        c.argument('op_type', default='Add', deprecate_info=c.deprecate(hide=True),
                   help='distinguish add operation and remove operation')

    with self.argument_context('sig share remove') as c:
        c.argument('op_type', default='Remove', deprecate_info=c.deprecate(hide=True),
                   help='distinguish add operation and remove operation')

    with self.argument_context('sig share reset') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('gallery_name', type=str, help='The name of the Shared Image Gallery.', id_part='name')

    with self.argument_context('sig share image-definition list') as c:
        c.argument('shared_to', options_list=['--scope'], arg_type=get_enum_type(['tenant', 'subscription']),
                   help='The query parameter to decide what shared galleries to fetch when doing listing operations.',
                   default='subscription')

    with self.argument_context('sig share image-version list') as c:
        c.argument('shared_to', options_list=['--scope'], arg_type=get_enum_type(['tenant', 'subscription']),
                   help='The query parameter to decide what shared galleries to fetch when doing listing operations.',
                   default='subscription')
