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

from azure.cli.core.commands import CliCommandType
from ..generated.commands import vm_shared_gallery_image, vm_shared_gallery_image_version, vm_gallery
from ..generated._client_factory import cf_shared_gallery_image_version, cf_shared_gallery_image, cf_gallery,\
    cf_shared_gallery


def load_command_table(self, _):

    from ..generated._client_factory import cf_ssh_public_key

    vm_ssh_public_key = CliCommandType(
        operations_tmpl='azure.mgmt.compute.operations._ssh_public_keys_operations#SshPublicKeysOperations.{}',
        client_factory=cf_ssh_public_key,
    )
    with self.command_group('sshkey', vm_ssh_public_key, client_factory=cf_ssh_public_key) as g:
        g.custom_command('create', 'sshkey_create')

    with self.command_group('sig', vm_gallery, client_factory=cf_gallery, is_experimental=True) as g:
        g.custom_command('group-list', 'sig_group_list', client_factory=cf_shared_gallery)

    with self.command_group('sig share image-definition', vm_shared_gallery_image,
                            client_factory=cf_shared_gallery_image, is_experimental=True) as g:
        g.custom_command('list', 'sig_share_image_definition_list')

    with self.command_group('sig share image-version', vm_shared_gallery_image_version,
                            client_factory=cf_shared_gallery_image_version, is_experimental=True) as g:
        g.custom_command('list', 'sig_share_image_version_list')
