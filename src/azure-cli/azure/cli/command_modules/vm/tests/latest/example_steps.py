# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /Galleries/get/Get a gallery.
@try_manual
def step_group_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az sig group-list '
             '--location "myLocation"',
             checks=checks)


# EXAMPLE: /GallerySharingProfile/get/Get a gallery.
@try_manual
def step_share_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az sig share show '
             '--gallery-unique-name "galleryUniqueName" '
             '--location "myLocation"',
             checks=checks)


# EXAMPLE: /GallerySharingProfile/post/Add sharing id to the sharing profile of a gallery.
@try_manual
def step_share_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az sig share update '
             '--gallery-name "{myGallery}" '
             '--resource-group "{rg}" '
             '--groups type="Subscriptions" ids="34a4ab42-0d72-47d9-bd1a-aed207386dac" ids="380fd389-260b-41aa-bad9-0a8'
             '3108c370b" '
             '--groups type="AADTenants" ids="c24c76aa-8897-4027-9b03-8f7928b54ff6" '
             '--operation-type "Add"',
             checks=checks)


# EXAMPLE: /GallerySharingProfile/post/reset sharing profile of a gallery.
@try_manual
def step_share_update2(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az sig share update '
             '--gallery-name "{myGallery}" '
             '--resource-group "{rg}" '
             '--operation-type "Reset"',
             checks=checks)


# EXAMPLE: /SharedGalleryImages/get/Get a gallery.
@try_manual
def step_share_image_definition_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az sig share image-definition list '
             '--gallery-unique-name "galleryUniqueName" '
             '--location "myLocation"',
             checks=checks)


# EXAMPLE: /SharedGalleryImageVersions/get/Get a gallery.
@try_manual
def step_share_image_version_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az sig share image-version list '
             '--gallery-image-definition "myGalleryImageName" '
             '--gallery-unique-name "galleryUniqueName" '
             '--location "myLocation"',
             checks=checks)


# EXAMPLE: /SshPublicKeys/put/Create a new SSH public key resource.
@try_manual
def step_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az sshkey create '
             '--location "westus" '
             '--public-key "{{ssh-rsa public key}}" '
             '--resource-group "{rg}" '
             '--name "{mySshPublicKey}"',
             checks=checks)


# EXAMPLE: /SshPublicKeys/get/Get an ssh public key.
@try_manual
def step_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az sshkey show '
             '--resource-group "{rg}" '
             '--name "{mySshPublicKey}"',
             checks=checks)
