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
    cf_virtual_machine,
    cf_virtual_machine_scale_set,
    cf_virtual_machine_scale_set_vm_extension,
    cf_virtual_machine_scale_set_vms,
    cf_virtual_machine_scale_set_vm_run_command,
    cf_disk_access,
    cf_disk_restore_point,
    cf_gallery_application,
    cf_gallery_application_version,
    cf_cloud_service_role_instance,
    cf_cloud_service_role,
    cf_cloud_service,
    cf_cloud_service_update_domain,
)


vm_ssh_public_key = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._ssh_public_keys_operations#SshPublicKeysOperations.{}',
    client_factory=cf_ssh_public_key,
)


vm_virtual_machine = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._virtual_machines_operations#VirtualMachinesOperations.{}',
    client_factory=cf_virtual_machine,
)


vm_virtual_machine_scale_set = CliCommandType(
    operations_tmpl=(
        'azure.mgmt.compute.operations._virtual_machine_scale_sets_operations#VirtualMachineScaleSetsOperations.{}'
    ),
    client_factory=cf_virtual_machine_scale_set,
)


vm_virtual_machine_scale_set_vm_extension = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._virtual_machine_scale_set_vm_extensions_operations#VirtualMachineScaleSetVmExtensionsOperations.{}',
    client_factory=cf_virtual_machine_scale_set_vm_extension,
)


vm_virtual_machine_scale_set_vms = CliCommandType(
    operations_tmpl=(
        'azure.mgmt.compute.operations._virtual_machine_scale_set_vms_operations#VirtualMachineScaleSetVMsOperations.{}'
    ),
    client_factory=cf_virtual_machine_scale_set_vms,
)


vm_virtual_machine_scale_set_vm_run_command = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._virtual_machine_scale_set_vm_run_commands_operations#VirtualMachineScaleSetVmRunCommandsOperations.{}',
    client_factory=cf_virtual_machine_scale_set_vm_run_command,
)


vm_disk_access = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._disk_accesses_operations#DiskAccessesOperations.{}',
    client_factory=cf_disk_access,
)


vm_disk_restore_point = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._disk_restore_point_operations#DiskRestorePointOperations.{}',
    client_factory=cf_disk_restore_point,
)


vm_gallery_application = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._gallery_applications_operations#GalleryApplicationsOperations.{}',
    client_factory=cf_gallery_application,
)


vm_gallery_application_version = CliCommandType(
    operations_tmpl=(
        'azure.mgmt.compute.operations._gallery_application_versions_operations#GalleryApplicationVersionsOperations.{}'
    ),
    client_factory=cf_gallery_application_version,
)


vm_cloud_service_role_instance = CliCommandType(
    operations_tmpl=(
        'azure.mgmt.compute.operations._cloud_service_role_instances_operations#CloudServiceRoleInstancesOperations.{}'
    ),
    client_factory=cf_cloud_service_role_instance,
)


vm_cloud_service_role = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._cloud_service_roles_operations#CloudServiceRolesOperations.{}',
    client_factory=cf_cloud_service_role,
)


vm_cloud_service = CliCommandType(
    operations_tmpl='azure.mgmt.compute.operations._cloud_services_operations#CloudServicesOperations.{}',
    client_factory=cf_cloud_service,
)


vm_cloud_service_update_domain = CliCommandType(
    operations_tmpl=(
        'azure.mgmt.compute.operations._cloud_services_update_domain_operations#CloudServicesUpdateDomainOperations.{}'
    ),
    client_factory=cf_cloud_service_update_domain,
)


def load_command_table(self, _):

    with self.command_group('sshkey', vm_ssh_public_key, client_factory=cf_ssh_public_key) as g:
        g.custom_command('list', 'sshkey_list')
        g.custom_show_command('show', 'sshkey_show')
        g.custom_command('create', 'sshkey_create')
        g.custom_command('update', 'sshkey_update')
        g.custom_command('delete', 'sshkey_delete', confirmation=True)

    with self.command_group('vm virtual-machine', vm_virtual_machine, client_factory=cf_virtual_machine) as g:
        g.custom_command('install-patch', 'vm_virtual_machine_install_patch')
        g.custom_command('reimage', 'vm_virtual_machine_reimage')

    with self.command_group(
        'vm virtual-machine-scale-set', vm_virtual_machine_scale_set, client_factory=cf_virtual_machine_scale_set
    ) as g:
        g.custom_command(
            'force-recovery-service-fabric-platform-update-domain-walk',
            'vm_virtual_machine_scale_set_force_recovery_service_fabric_platform_update_domain_walk',
        )
        g.custom_command('redeploy', 'vm_virtual_machine_scale_set_redeploy')
        g.custom_command('reimage-all', 'vm_virtual_machine_scale_set_reimage_all')

    with self.command_group(
        'vm virtual-machine-scale-set-vm-extension',
        vm_virtual_machine_scale_set_vm_extension,
        client_factory=cf_virtual_machine_scale_set_vm_extension,
    ) as g:
        g.custom_command('list', 'vm_virtual_machine_scale_set_vm_extension_list')
        g.custom_show_command('show', 'vm_virtual_machine_scale_set_vm_extension_show')
        g.custom_command('create', 'vm_virtual_machine_scale_set_vm_extension_create', supports_no_wait=True)
        g.custom_wait_command('wait', 'vm_virtual_machine_scale_set_vm_extension_show')

    with self.command_group(
        'vm virtual-machine-scale-set-v-ms',
        vm_virtual_machine_scale_set_vms,
        client_factory=cf_virtual_machine_scale_set_vms,
    ) as g:
        g.custom_command('redeploy', 'vm_virtual_machine_scale_set_v_ms_redeploy')
        g.custom_command('reimage-all', 'vm_virtual_machine_scale_set_v_ms_reimage_all')
        g.custom_command(
            'retrieve-boot-diagnostic-data', 'vm_virtual_machine_scale_set_v_ms_retrieve_boot_diagnostic_data'
        )

    with self.command_group(
        'vm virtual-machine-scale-set-vm-run-command',
        vm_virtual_machine_scale_set_vm_run_command,
        client_factory=cf_virtual_machine_scale_set_vm_run_command,
    ) as g:
        g.custom_command('list', 'vm_virtual_machine_scale_set_vm_run_command_list')

    with self.command_group('vm disk-access', vm_disk_access, client_factory=cf_disk_access) as g:
        g.custom_command('delete-a-private-endpoint-connection', 'vm_disk_access_delete_a_private_endpoint_connection')
        g.custom_command('list-private-endpoint-connection', 'vm_disk_access_list_private_endpoint_connection')
        g.custom_command('show-private-link-resource', 'vm_disk_access_show_private_link_resource')

    with self.command_group('vm disk-restore-point', vm_disk_restore_point, client_factory=cf_disk_restore_point) as g:
        g.custom_show_command('show', 'vm_disk_restore_point_show')

    with self.command_group(
        'vm gallery-application', vm_gallery_application, client_factory=cf_gallery_application
    ) as g:
        g.custom_command('list', 'vm_gallery_application_list')
        g.custom_show_command('show', 'vm_gallery_application_show')
        g.custom_command('create', 'vm_gallery_application_create', supports_no_wait=True)
        g.custom_command('delete', 'vm_gallery_application_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'vm_gallery_application_show')

    with self.command_group(
        'vm gallery-application-version', vm_gallery_application_version, client_factory=cf_gallery_application_version
    ) as g:
        g.custom_command('list', 'vm_gallery_application_version_list')

    with self.command_group(
        'vm cloud-service-role-instance', vm_cloud_service_role_instance, client_factory=cf_cloud_service_role_instance
    ) as g:
        g.custom_command('list', 'vm_cloud_service_role_instance_list')
        g.custom_show_command('show', 'vm_cloud_service_role_instance_show')
        g.custom_command('reimage', 'vm_cloud_service_role_instance_reimage', supports_no_wait=True)
        g.custom_command('restart', 'vm_cloud_service_role_instance_restart', supports_no_wait=True)
        g.custom_command('show-instance-view', 'vm_cloud_service_role_instance_show_instance_view')
        g.custom_command('show-remote-desktop-file', 'vm_cloud_service_role_instance_show_remote_desktop_file')
        g.custom_wait_command('wait', 'vm_cloud_service_role_instance_show')

    with self.command_group('vm cloud-service-role', vm_cloud_service_role, client_factory=cf_cloud_service_role) as g:
        g.custom_command('list', 'vm_cloud_service_role_list')
        g.custom_show_command('show', 'vm_cloud_service_role_show')

    with self.command_group('vm cloud-service', vm_cloud_service, client_factory=cf_cloud_service) as g:
        g.custom_command('list', 'vm_cloud_service_list')
        g.custom_show_command('show', 'vm_cloud_service_show')
        g.custom_command('create', 'vm_cloud_service_create', supports_no_wait=True)
        g.custom_command('delete', 'vm_cloud_service_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('delete-instance', 'vm_cloud_service_delete_instance', supports_no_wait=True)
        g.custom_command('list-all', 'vm_cloud_service_list_all')
        g.custom_command('power-off', 'vm_cloud_service_power_off', supports_no_wait=True)
        g.custom_command('restart', 'vm_cloud_service_restart', supports_no_wait=True)
        g.custom_command('show-instance-view', 'vm_cloud_service_show_instance_view')
        g.custom_command('start', 'vm_cloud_service_start', supports_no_wait=True)
        g.custom_wait_command('wait', 'vm_cloud_service_show')

    with self.command_group(
        'vm cloud-service-update-domain', vm_cloud_service_update_domain, client_factory=cf_cloud_service_update_domain
    ) as g:
        g.custom_command('list-update-domain', 'vm_cloud_service_update_domain_list_update_domain')
        g.custom_command('show-update-domain', 'vm_cloud_service_update_domain_show_update_domain')
        g.custom_command('walk-update-domain', 'vm_cloud_service_update_domain_walk_update_domain')
