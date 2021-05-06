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
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from .._actions import AddGroups


def load_arguments(self, _):

    with self.argument_context('sshkey list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('sshkey show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('ssh_public_key_name', options_list=['--name', '-n', '--ssh-public-key-name'], type=str, help='The '
                   'name of the SSH public key.', id_part='name')

    with self.argument_context('sshkey create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('ssh_public_key_name', options_list=['--name', '-n', '--ssh-public-key-name'], type=str, help='The '
                   'name of the SSH public key.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('public_key', type=str, help='SSH public key used to authenticate to a virtual machine through ssh. '
                   'If this property is not initially provided when the resource is created, the publicKey property '
                   'will be populated when generateKeyPair is called. If the public key is provided upon resource '
                   'creation, the provided public key needs to be at least 2048-bit and in ssh-rsa format.')

    with self.argument_context('sshkey update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('ssh_public_key_name', options_list=['--name', '-n', '--ssh-public-key-name'], type=str, help='The '
                   'name of the SSH public key.', id_part='name')
        c.argument('tags', tags_type)
        c.argument('public_key', type=str, help='SSH public key used to authenticate to a virtual machine through ssh. '
                   'If this property is not initially provided when the resource is created, the publicKey property '
                   'will be populated when generateKeyPair is called. If the public key is provided upon resource '
                   'creation, the provided public key needs to be at least 2048-bit and in ssh-rsa format.')

    with self.argument_context('sshkey delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('ssh_public_key_name', options_list=['--name', '-n', '--ssh-public-key-name'], type=str, help='The '
                   'name of the SSH public key.', id_part='name')

    with self.argument_context('sig group-list') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), id_part='name')
        c.argument('shared_to', options_list=['--scope'], arg_type=get_enum_type(['tenant']), help='The query '
                   'parameter to decide what shared galleries to fetch when doing listing operations.')

    with self.argument_context('sig share update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('gallery_name', type=str, help='The name of the Shared Image Gallery.', id_part='name')
        c.argument('operation_type', arg_type=get_enum_type(['Add', 'Remove', 'Reset']), help='This property allows '
                   'you to specify the operation type of gallery sharing update. <br><br> Possible values are: '
                   '<br><br> **Add** <br><br> **Remove** <br><br> **Reset**')
        c.argument('groups', action=AddGroups, nargs='+', help='A list of sharing profile groups.')

    with self.argument_context('sig share image-definition list') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('gallery_unique_name', type=str, help='The unique name of the Shared Gallery.')
        c.argument('shared_to', options_list=['--scope'], arg_type=get_enum_type(['tenant']), help='The query '
                   'parameter to decide what shared galleries to fetch when doing listing operations.')

    with self.argument_context('sig share image-definition show') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), id_part='name')
        c.argument('gallery_unique_name', type=str, help='The unique name of the Shared Gallery.',
                   id_part='child_name_1')
        c.argument('gallery_image_name', options_list=['--gallery-image-definition', '-i'], type=str, help='The name '
                   'of the Shared Gallery Image Definition from which the Image Versions are to be listed.',
                   id_part='child_name_2')

    with self.argument_context('sig share image-version list') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('gallery_unique_name', type=str, help='The unique name of the Shared Gallery.')
        c.argument('gallery_image_name', options_list=['--gallery-image-definition', '-i'], type=str, help='The name '
                   'of the Shared Gallery Image Definition from which the Image Versions are to be listed.')
        c.argument('shared_to', options_list=['--scope'], arg_type=get_enum_type(['tenant']), help='The query '
                   'parameter to decide what shared galleries to fetch when doing listing operations.')

    with self.argument_context('sig share image-version show') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), id_part='name')
        c.argument('gallery_unique_name', type=str, help='The unique name of the Shared Gallery.',
                   id_part='child_name_1')
        c.argument('gallery_image_name', options_list=['--gallery-image-definition', '-i'], type=str, help='The name '
                   'of the Shared Gallery Image Definition from which the Image Versions are to be listed.',
                   id_part='child_name_2')
        c.argument('gallery_image_version_name', options_list=['--gallery-image-version', '-e'], type=str, help='The '
                   'name of the gallery image version to be created. Needs to follow semantic version name pattern: '
                   'The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. '
                   'Format: <MajorVersion>.<MinorVersion>.<Patch>', id_part='child_name_3')
