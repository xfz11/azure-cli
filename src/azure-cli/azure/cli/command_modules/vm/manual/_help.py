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

from knack.help_files import helps


helps['sshkey'] = """
    type: group
    short-summary: Manage ssh public key with vm
"""

helps['sshkey list'] = """
    type: command
    short-summary: "List all of the SSH public keys."
"""

helps['sshkey show'] = """
    type: command
    short-summary: "Retrieve information about an SSH public key."
    examples:
      - name: Get an ssh public key.
        text: |-
               az sshkey show --resource-group "myResourceGroup" --name "mySshPublicKeyName"
"""

helps['sshkey create'] = """
    type: command
    short-summary: "Create a new SSH public key resource."
    examples:
      - name: Create a new SSH public key resource.
        text: |-
               az sshkey create --location "westus" --public-key "{ssh-rsa public key}" --resource-group \
"myResourceGroup" --name "mySshPublicKeyName"
      - name: Create a new SSH public key resource using public key in a file.
        text: |-
               az sshkey create --location "westus" --public-key "@filename" --resource-group \
"myResourceGroup" --name "mySshPublicKeyName"
      - name: Create a new SSH public key resource with auto-generated value.
        text: |-
               az sshkey create --location "westus" --resource-group "myResourceGroup" --name "mySshPublicKeyName"
"""

helps['sshkey update'] = """
    type: command
    short-summary: "Update an SSH public key resource."
"""

helps['sshkey delete'] = """
    type: command
    short-summary: "Delete an SSH public key."
"""

helps['sig share wait'] = """
type: command
short-summary: wait for shared gallery get related operation
"""

helps['sig share update'] = """
    type: command
    short-summary: "Update sharing profile of a gallery."
    parameters:
      - name: --groups
        short-summary: "A list of sharing profile groups."
        long-summary: |
            Usage: --groups type=XX ids=XX

            type: This property allows you to specify the type of sharing group.
            ids: A list of subscription/tenant ids the gallery is aimed to be shared to.

            Multiple actions can be specified by using more than one --groups argument.
    examples:
      - name: Add sharing id to the sharing profile of a gallery.
        text: |-
               az sig share update --gallery-name "myGalleryName" --resource-group "myResourceGroup" --groups \
type="Subscriptions" ids="34a4ab42-0d72-47d9-bd1a-aed207386dac" ids="380fd389-260b-41aa-bad9-0a83108c370b" --groups \
type="AADTenants" ids="c24c76aa-8897-4027-9b03-8f7928b54ff6" --operation-type "Add"
      - name: reset sharing profile of a gallery.
        text: |-
               az sig share update --gallery-name "myGalleryName" --resource-group "myResourceGroup" --operation-type \
"Reset"
"""
