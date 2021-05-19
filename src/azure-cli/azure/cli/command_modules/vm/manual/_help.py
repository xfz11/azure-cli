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

helps['sig share'] = """
    type: group
    short-summary: Manage gallery sharing profile
"""

helps['sig share add'] = """
    type: command
    short-summary: "Update sharing profile of a gallery."
    examples:
      - name: Add sharing id to the sharing profile of a gallery.
        text: |-
               az sig share add --gallery-name "myGalleryName" --resource-group "myResourceGroup" \
--subscription-ids "34a4ab42-0d72-47d9-bd1a-aed207386dac" "380fd389-260b-41aa-bad9-0a83108c370b" \
--tenant-ids "c24c76aa-8897-4027-9b03-8f7928b54ff6"
"""

helps['sig share remove'] = """
    type: command
    short-summary: "Remove sharing profile of a gallery."
    examples:
      - name: Remove sharing ID to the sharing profile of a gallery.
        text: |-
               az sig share remove --gallery-name "myGalleryName" --resource-group "myResourceGroup" \
--subscription-ids "34a4ab42-0d72-47d9-bd1a-aed207386dac" "380fd389-260b-41aa-bad9-0a83108c370b" \
--tenant-ids "c24c76aa-8897-4027-9b03-8f7928b54ff6"
"""

helps['sig share reset'] = """
    type: command
    short-summary: "Reset sharing profile of a gallery."
    examples:
      - name: reset sharing profile of a gallery.
        text: |-
               az sig share reset --gallery-name "myGalleryName" --resource-group "myResourceGroup"
"""

helps['sig share wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of a shared gallery is met.
examples:
  - name: Place the CLI in a waiting state until the disk access is created with 'provisioningState' at 'Succeeded'.
    text: |
        az sig share wait --updated -g MyResourceGroup --gallery-name Gallery
"""

helps['sig shared-gallery list'] = """
    type: command
    short-summary: "List shared galleries by subscription id or tenant id."
    examples:
      - name: List shared galleries.
        text: |-
               az sig shared-gallery list --location "myLocation"
"""

helps['sig shared-image-definition list'] = """
    type: command
    short-summary: "List shared gallery images by subscription id or tenant id."
    examples:
      - name: List shared images.
        text: |-
               az sig shared-image-definition list --gallery-unique-name "galleryUniqueName" --location "myLocation"
"""

helps['sig shared-image-version list'] = """
    type: command
    short-summary: "List shared gallery image versions by subscription id or tenant id."
    examples:
      - name: List shared image versions.
        text: |-
               az sig shared-image-version list --gallery-image-definition "myGalleryImageName" --gallery-unique-name \
"galleryUniqueName" --location "myLocation"
"""
