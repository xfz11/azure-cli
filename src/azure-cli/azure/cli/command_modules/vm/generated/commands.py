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
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from ..generated._client_factory import (
    cf_ssh_public_key,
    cf_gallery,
    cf_gallery_sharing_profile,
    cf_shared_gallery,
    cf_shared_gallery_image,
    cf_shared_gallery_image_version,
)


vm_ssh_public_key = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._ssh_public_keys_operations#SshPublicKeysOperations.{}',
    client_factory=cf_ssh_public_key,
)


vm_gallery = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._galleries_operations#GalleriesOperations.{}',
    client_factory=cf_gallery,
)


vm_gallery_sharing_profile = CliCommandType(
    operations_tmpl=(
        'azure.mgmt.compute.operations._gallery_sharing_profile_operations#GallerySharingProfileOperations.{}'
    ),
    client_factory=cf_gallery_sharing_profile,
)


vm_shared_gallery_image = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._shared_gallery_images_operations#SharedGalleryImagesOperations.{}',
    client_factory=cf_shared_gallery_image,
)


vm_shared_gallery_image_version = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._shared_gallery_image_versions_operations#SharedGalleryImageVersionsOperations.{}',
    client_factory=cf_shared_gallery_image_version,
)


def load_command_table(self, _):

    with self.command_group('sshkey', vm_ssh_public_key, client_factory=cf_ssh_public_key, is_experimental=True) as g:
        g.custom_command('list', 'sshkey_list')
        g.custom_show_command('show', 'sshkey_show')
        g.custom_command('create', 'sshkey_create')
        g.custom_command('update', 'sshkey_update')
        g.custom_command('delete', 'sshkey_delete', confirmation=True)

    with self.command_group('sig', vm_gallery, client_factory=cf_gallery, is_experimental=True) as g:
        g.custom_command('group-list', 'sig_group_list', client_factory=cf_shared_gallery)

    with self.command_group(
        'sig share', vm_gallery_sharing_profile, client_factory=cf_gallery_sharing_profile, is_experimental=True
    ) as g:
        g.custom_command('update', 'sig_share_update')

    with self.command_group(
        'sig share image-definition',
        vm_shared_gallery_image,
        client_factory=cf_shared_gallery_image,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'sig_share_image_definition_list')
        g.custom_show_command('show', 'sig_share_image_definition_show')

    with self.command_group(
        'sig share image-version',
        vm_shared_gallery_image_version,
        client_factory=cf_shared_gallery_image_version,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'sig_share_image_version_list')
        g.custom_show_command('show', 'sig_share_image_version_show')
