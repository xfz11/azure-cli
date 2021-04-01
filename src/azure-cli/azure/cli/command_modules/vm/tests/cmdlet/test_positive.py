# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.testsdk import ScenarioTest


# Test class for Scenario
class PositiveTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(PositiveTest, self).__init__(*args, **kwargs)

    # EXAMPLE: /SshPublicKeys/get/Get an ssh public key.
    def test_show(self):
        self.cmd('az sshkey show '
                 '--resource-group "myResourceGroup" '
                 '--name "mySshPublicKeyName"')

    # EXAMPLE: /SshPublicKeys/put/Create a new SSH public key resource.
    def test_create(self):
        self.cmd('az sshkey create '
                 '--location "westus" '
                 '--public-key "{{ssh-rsa public key}}" '
                 '--resource-group "myResourceGroup" '
                 '--name "mySshPublicKeyName"')

    # EXAMPLE: /VirtualMachines/post/Install patch state of a virtual machine.
    def test_virtual_machine_install_patch(self):
        self.cmd('az vm virtual-machine install-patch '
                 '--maximum-duration "PT4H" '
                 '--reboot-setting "IfRequired" '
                 '--windows-parameters classifications-to-include="Critical" classifications-to-include="Security" max-patch-publish-date="2020-11-19T02:36:43.0539904+00:00" '
                 '--resource-group "myResourceGroupName" '
                 '--name "myVMName"')

    # EXAMPLE: /VirtualMachines/post/Reimage a Virtual Machine.
    def test_virtual_machine_reimage(self):
        self.cmd('az vm virtual-machine reimage '
                 '--temp-disk true '
                 '--resource-group "myResourceGroup" '
                 '--name "myVMName"')

    # EXAMPLE: /VirtualMachineScaleSetVMExtensions/get/List extensions in Vmss instance.
    def test_virtual_machine_scale_set_vm_extension_list(self):
        self.cmd('az vm virtual-machine-scale-set-vm-extension list '
                 '--instance-id "0" '
                 '--resource-group "myResourceGroup" '
                 '--vm-scale-set-name "myvmScaleSet"')

    # EXAMPLE: /VirtualMachineScaleSetVMExtensions/get/Get VirtualMachineScaleSet VM extension.
    def test_virtual_machine_scale_set_vm_extension_show(self):
        self.cmd('az vm virtual-machine-scale-set-vm-extension show '
                 '--instance-id "0" '
                 '--resource-group "myResourceGroup" '
                 '--vm-extension-name "myVMExtension" '
                 '--vm-scale-set-name "myvmScaleSet"')

    # EXAMPLE: /VirtualMachineScaleSetVMExtensions/put/Create VirtualMachineScaleSet VM extension.
    def test_virtual_machine_scale_set_vm_extension_create(self):
        self.cmd('az vm virtual-machine-scale-set-vm-extension create '
                 '--type-properties-type "extType" '
                 '--auto-upgrade-minor-version true '
                 '--publisher "extPublisher" '
                 '--settings "{{\\"UserName\\":\\"xyz@microsoft.com\\"}}" '
                 '--type-handler-version "1.2" '
                 '--instance-id "0" '
                 '--resource-group "myResourceGroup" '
                 '--vm-extension-name "myVMExtension" '
                 '--vm-scale-set-name "myvmScaleSet"')

    # EXAMPLE: /VirtualMachineScaleSetVMs/post/RetrieveBootDiagnosticsData of a virtual machine.
    def test_virtual_machine_scale(self):
        self.cmd('az vm virtual-machine-scale-set-v-ms retrieve-boot-diagnostic-data '
                 '--instance-id "0" '
                 '--resource-group "ResourceGroup" '
                 '--sas-uri-expiration-time-in-minutes 60 '
                 '--vm-scale-set-name "myvmScaleSet"')

    # EXAMPLE: /VirtualMachineScaleSetVMRunCommands/get/List run commands in Vmss instance.
    def test_virtual_machine_scale_set_vm_run_command_list(self):
        self.cmd('az vm virtual-machine-scale-set-vm-run-command list '
                 '--instance-id "0" '
                 '--resource-group "myResourceGroup" '
                 '--vm-scale-set-name "myvmScaleSet"')

    # EXAMPLE: /DiskAccesses/delete/Delete a private endpoint connection under a disk access resource.
    def test_disk_access_delete(self):
        self.cmd('az vm disk-access delete-a-private-endpoint-connection -y '
                 '--name "myDiskAccess" '
                 '--private-endpoint-connection-name "myPrivateEndpointConnection" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /DiskAccesses/get/Get information about a private endpoint connection under a disk access resource.
    def test_disk_access_list_private_endpoint_connection(self):
        self.cmd('az vm disk-access list-private-endpoint-connection '
                 '--name "myDiskAccess" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /DiskAccesses/get/List all possible private link resources under disk access resource.
    def test_disk_access_show_private_link_resource(self):
        self.cmd('az vm disk-access show-private-link-resource '
                 '--name "myDiskAccess" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /DiskRestorePoint/get/Get an incremental disk restorePoint resource.
    def test_disk_restore_point_show(self):
        self.cmd('az vm disk-restore-point show '
                 '--name "TestDisk45ceb03433006d1baee0_b70cd924-3362-4a80-93c2-9415eaa12745" '
                 '--resource-group "myResourceGroup" '
                 '--restore-point-collection-name "rpc" '
                 '--vm-restore-point-name "vmrp"')

    # EXAMPLE: /GalleryApplications/get/List gallery Applications in a gallery.
    def test_gallery_application_list(self):
        self.cmd('az vm gallery-application list '
                 '--gallery-name "myGalleryName" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /GalleryApplications/get/Get a gallery Application.
    def test_gallery_application_show(self):
        self.cmd('az vm gallery-application show '
                 '--name "myGalleryApplicationName" '
                 '--gallery-name "myGalleryName" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /GalleryApplications/put/Create or update a simple gallery Application.
    def test_gallery_application_create(self):
        self.cmd('az vm gallery-application create '
                 '--location "West US" '
                 '--description "This is the gallery application description." '
                 '--eula "This is the gallery application EULA." '
                 '--privacy-statement-uri "myPrivacyStatementUri}}" '
                 '--release-note-uri "myReleaseNoteUri" '
                 '--supported-os-type "Windows" '
                 '--name "myGalleryApplicationName" '
                 '--gallery-name "myGalleryName" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /GalleryApplications/delete/Delete a gallery Application.
    def test_gallery_application_delete(self):
        self.cmd('az vm gallery-application delete -y '
                 '--name "myGalleryApplicationName" '
                 '--gallery-name "myGalleryName" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /GalleryApplicationVersions/get/List gallery Application Versions in a gallery Application Definition.
    def test_gallery_application_version_list(self):
        self.cmd('az vm gallery-application-version list '
                 '--gallery-application-name "myGalleryApplicationName" '
                 '--gallery-name "myGalleryName" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /CloudServiceRoleInstances/get/List Role Instances in a Cloud Service
    def test_cloud_service_role_instance_list(self):
        self.cmd('az vm cloud-service-role-instance list '
                 '--cloud-service-name "{{cs-name}}" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServiceRoleInstances/get/Get Cloud Service Role Instance
    def test_cloud_service_role_instance_show(self):
        self.cmd('az vm cloud-service-role-instance show '
                 '--cloud-service-name "{{cs-name}}" '
                 '--resource-group "ConstosoRG" '
                 '--role-instance-name "{roleInstance-name}"')

    # EXAMPLE: /CloudServiceRoleInstances/post/Reimage Cloud Service Role Instance
    def test_cloud_service_role_instance_reimage(self):
        self.cmd('az vm cloud-service-role-instance reimage '
                 '--cloud-service-name "{{cs-name}}" '
                 '--resource-group "ConstosoRG" '
                 '--role-instance-name "{roleInstance-name}"')

    # EXAMPLE: /CloudServiceRoleInstances/post/Restart Cloud Service Role Instance
    def test_cloud_service_role_instance_restart(self):
        self.cmd('az vm cloud-service-role-instance restart '
                 '--cloud-service-name "{{cs-name}}" '
                 '--resource-group "ConstosoRG" '
                 '--role-instance-name "{roleInstance-name}"')

    # EXAMPLE: /CloudServiceRoleInstances/get/Get Instance View of Cloud Service Role Instance
    def test_cloud_service_role(self):
        self.cmd('az vm cloud-service-role-instance show-instance-view '
                 '--cloud-service-name "{{cs-name}}" '
                 '--resource-group "ConstosoRG" '
                 '--role-instance-name "{roleInstance-name}"')

    # EXAMPLE: /CloudServiceRoles/get/List Roles in a Cloud Service
    def test_cloud_service_role_list(self):
        self.cmd('az vm cloud-service-role list '
                 '--cloud-service-name "{{cs-name}}" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServiceRoles/get/Get Cloud Service Role
    def test_cloud_service_role_show(self):
        self.cmd('az vm cloud-service-role show '
                 '--cloud-service-name "{{cs-name}}" '
                 '--resource-group "ConstosoRG" '
                 '--role-name "{role-name}"')

    # EXAMPLE: /CloudServices/get/List Cloud Services in a Resource Group
    def test_cloud_service_list(self):
        self.cmd('az vm cloud-service list '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/get/Get Cloud Service with Multiple Roles and RDP Extension
    def test_cloud_service_show(self):
        self.cmd('az vm cloud-service show '
                 '--name "{{cs-name}}" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/put/Create New Cloud Service with Multiple Roles
    def test_cloud_service_create(self):
        self.cmd('az vm cloud-service create '
                 '--name "{{cs-name}}" '
                 '--location "westus" '
                 '--configuration "{{ServiceConfiguration}}" '
                 '--load-balancer-configurations "[{{\\"name\\":\\"contosolb\\",\\"properties\\":{{\\"frontendIPConfigurations\\":[{{\\"name\\":\\"contosofe\\",\\"properties\\":{{\\"publicIPAddress\\":{{\\"id\\":\\"/subscriptions/{{subscription-id}}/resourceGroups/ConstosoRG/providers/Microsoft.Network/publicIPAddresses/contosopublicip\\"}}}}}}]}}}}]" '
                 '--package-url "{{PackageUrl}}" '
                 '--roles "[{{\\"name\\":\\"ContosoFrontend\\",\\"sku\\":{{\\"name\\":\\"Standard_D1_v2\\",\\"capacity\\":1,\\"tier\\":\\"Standard\\"}}}},{{\\"name\\":\\"ContosoBackend\\",\\"sku\\":{{\\"name\\":\\"Standard_D1_v2\\",\\"capacity\\":1,\\"tier\\":\\"Standard\\"}}}}]" '
                 '--upgrade-mode "Auto" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/put/Create New Cloud Service with Single Role
    def test_cloud_service_create2(self):
        self.cmd('az vm cloud-service create '
                 '--name "{{cs-name}}" '
                 '--location "westus" '
                 '--configuration "{{ServiceConfiguration}}" '
                 '--load-balancer-configurations "[{{\\"name\\":\\"myLoadBalancer\\",\\"properties\\":{{\\"frontendIPConfigurations\\":[{{\\"name\\":\\"myfe\\",\\"properties\\":{{\\"publicIPAddress\\":{{\\"id\\":\\"/subscriptions/{{subscription-id}}/resourceGroups/ConstosoRG/providers/Microsoft.Network/publicIPAddresses/myPublicIP\\"}}}}}}]}}}}]" '
                 '--package-url "{{PackageUrl}}" '
                 '--roles "[{{\\"name\\":\\"ContosoFrontend\\",\\"sku\\":{{\\"name\\":\\"Standard_D1_v2\\",\\"capacity\\":1,\\"tier\\":\\"Standard\\"}}}}]" '
                 '--upgrade-mode "Auto" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/put/Create New Cloud Service with Single Role and Certificate from Key Vault
    def test_cloud_service_create3(self):
        self.cmd('az vm cloud-service create '
                 '--name "{{cs-name}}" '
                 '--location "westus" '
                 '--configuration "{{ServiceConfiguration}}" '
                 '--load-balancer-configurations "[{{\\"name\\":\\"contosolb\\",\\"properties\\":{{\\"frontendIPConfigurations\\":[{{\\"name\\":\\"contosofe\\",\\"properties\\":{{\\"publicIPAddress\\":{{\\"id\\":\\"/subscriptions/{{subscription-id}}/resourceGroups/ConstosoRG/providers/Microsoft.Network/publicIPAddresses/contosopublicip\\"}}}}}}]}}}}]" '
                 '--secrets "[{{\\"sourceVault\\":{{\\"id\\":\\"/subscriptions/{{subscription-id}}/resourceGroups/ConstosoRG/providers/Microsoft.KeyVault/vaults/{{keyvault-name}}\\"}},\\"vaultCertificates\\":[{{\\"certificateUrl\\":\\"https://{{keyvault-name}}.vault.azure.net:443/secrets/ContosoCertificate/{{secret-id}}\\"}}]}}]" '
                 '--package-url "{{PackageUrl}}" '
                 '--roles "[{{\\"name\\":\\"ContosoFrontend\\",\\"sku\\":{{\\"name\\":\\"Standard_D1_v2\\",\\"capacity\\":1,\\"tier\\":\\"Standard\\"}}}}]" '
                 '--upgrade-mode "Auto" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/put/Create New Cloud Service with Single Role and RDP Extension
    def test_cloud_service_create4(self):
        self.cmd('az vm cloud-service create '
                 '--name "{{cs-name}}" '
                 '--location "westus" '
                 '--configuration "{{ServiceConfiguration}}" '
                 '--extensions "[{{\\"name\\":\\"RDPExtension\\",\\"properties\\":{{\\"type\\":\\"RDP\\",\\"autoUpgradeMinorVersion\\":false,\\"protectedSettings\\":\\"<PrivateConfig><Password>{{password}}</Password></PrivateConfig>\\",\\"publisher\\":\\"Microsoft.Windows.Azure.Extensions\\",\\"settings\\":\\"<PublicConfig><UserName>UserAzure</UserName><Expiration>10/22/2021 15:05:45</Expiration></PublicConfig>\\",\\"typeHandlerVersion\\":\\"1.2.1\\"}}}}]" '
                 '--load-balancer-configurations "[{{\\"name\\":\\"contosolb\\",\\"properties\\":{{\\"frontendIPConfigurations\\":[{{\\"name\\":\\"contosofe\\",\\"properties\\":{{\\"publicIPAddress\\":{{\\"id\\":\\"/subscriptions/{{subscription-id}}/resourceGroups/ConstosoRG/providers/Microsoft.Network/publicIPAddresses/contosopublicip\\"}}}}}}]}}}}]" '
                 '--package-url "{{PackageUrl}}" '
                 '--roles "[{{\\"name\\":\\"ContosoFrontend\\",\\"sku\\":{{\\"name\\":\\"Standard_D1_v2\\",\\"capacity\\":1,\\"tier\\":\\"Standard\\"}}}}]" '
                 '--upgrade-mode "Auto" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/delete/Delete Cloud Service
    def test_cloud_service_delete(self):
        self.cmd('az vm cloud-service delete -y '
                 '--name "{{cs-name}}" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/post/Delete Cloud Service Role Instances
    def test_cloud_service_delete_instance(self):
        self.cmd('az vm cloud-service delete-instance '
                 '--name "{{cs-name}}" '
                 '--role-instances "ContosoFrontend_IN_0" "ContosoBackend_IN_1" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/get/List Cloud Services in a Subscription
    def test_cloud_service_list_all(self):
        self.cmd('az vm cloud-service list-all')

    # EXAMPLE: /CloudServices/post/Stop or PowerOff Cloud Service
    def test_cloud_service_power_off(self):
        self.cmd('az vm cloud-service power-off '
                 '--name "{{cs-name}}" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/post/Restart Cloud Service Role Instances
    def test_cloud_service_restart(self):
        self.cmd('az vm cloud-service restart '
                 '--name "{{cs-name}}" '
                 '--role-instances "ContosoFrontend_IN_0" "ContosoBackend_IN_1" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/get/Get Cloud Service Instance View with Multiple Roles
    def test_cloud_service_show_instance_view(self):
        self.cmd('az vm cloud-service show-instance-view '
                 '--name "{{cs-name}}" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServices/post/Start Cloud Service
    def test_cloud_service_start(self):
        self.cmd('az vm cloud-service start '
                 '--name "{{cs-name}}" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServicesUpdateDomain/get/List Update Domains in Cloud Service
    def test_cloud_service_update3(self):
        self.cmd('az vm cloud-service-update-domain list-update-domain '
                 '--cloud-service-name "{{cs-name}}" '
                 '--resource-group "ConstosoRG"')

    # EXAMPLE: /CloudServicesUpdateDomain/get/Get Cloud Service Update Domain
    def test_cloud_service_update2(self):
        self.cmd('az vm cloud-service-update-domain show-update-domain '
                 '--cloud-service-name "{{cs-name}}" '
                 '--resource-group "ConstosoRG" '
                 '--update-domain 1')

    # EXAMPLE: /CloudServicesUpdateDomain/put/Update Cloud Service to specified Domain
    def test_cloud_service_update(self):
        self.cmd('az vm cloud-service-update-domain walk-update-domain '
                 '--cloud-service-name "{{cs-name}}" '
                 '--resource-group "ConstosoRG" '
                 '--update-domain 1')
