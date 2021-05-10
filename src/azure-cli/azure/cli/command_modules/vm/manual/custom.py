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

from azure.cli.core.azclierror import ValidationError


def sshkey_create(client,
                  resource_group_name,
                  ssh_public_key_name,
                  location,
                  tags=None,
                  public_key=None):
    parameters = {
        'location': location,
        'tags': tags,
        'public_key': public_key
    }
    client.create(resource_group_name=resource_group_name,
                  ssh_public_key_name=ssh_public_key_name,
                  parameters=parameters)
    if public_key is None:  # Generate one if public key is None
        client.generate_key_pair(resource_group_name=resource_group_name,
                                 ssh_public_key_name=ssh_public_key_name)
    return client.get(resource_group_name=resource_group_name,
                      ssh_public_key_name=ssh_public_key_name)


def sig_group_list(client,
                   location,
                   shared_to=None):
    if shared_to == 'subscription':
        shared_to = None
    return client.list(location=location,
                       shared_to=shared_to)


def sig_share_update(cmd, client, resource_group_name, gallery_name, subscription_ids=None, tenant_ids=None,
                     op_type=None):
    SharingProfileGroup, SharingUpdate, SharingProfileGroupTypes = cmd.get_models(
        'SharingProfileGroup', 'SharingUpdate', 'SharingProfileGroupTypes')
    if subscription_ids is None and tenant_ids is None:
        raise ValidationError('At least one of subscription ids or tenant ids must be provided')
    groups = []
    if subscription_ids:
        groups.append(SharingProfileGroup(type=SharingProfileGroupTypes.SUBSCRIPTIONS, ids=subscription_ids))
    if tenant_ids:
        groups.append(SharingProfileGroup(type=SharingProfileGroupTypes.AAD_TENANTS, ids=tenant_ids))
    sharing_update = SharingUpdate(operation_type=op_type, groups=groups)
    return client.begin_update(resource_group_name=resource_group_name,
                               gallery_name=gallery_name,
                               sharing_update=sharing_update)


def sig_share_reset(cmd, client, resource_group_name, gallery_name):
    SharingUpdate, SharingUpdateOperationTypes = cmd.get_models('SharingUpdate', 'SharingUpdateOperationTypes')
    sharing_update = SharingUpdate(operation_type=SharingUpdateOperationTypes.RESET)
    return client.begin_update(resource_group_name=resource_group_name,
                               gallery_name=gallery_name,
                               sharing_update=sharing_update)


def sig_share_image_definition_list(client,
                                    location,
                                    gallery_unique_name,
                                    shared_to=None):
    if shared_to == 'subscription':
        shared_to = None
    return client.list(location=location,
                       gallery_unique_name=gallery_unique_name,
                       shared_to=shared_to)


def sig_share_image_version_list(client,
                                 location,
                                 gallery_unique_name,
                                 gallery_image_name,
                                 shared_to=None):
    if shared_to == 'subscription':
        shared_to = None
    return client.list(location=location,
                       gallery_unique_name=gallery_unique_name,
                       gallery_image_name=gallery_image_name,
                       shared_to=shared_to)
