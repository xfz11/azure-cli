## AZ

These settings apply only when `--az` is specified on the command line.

``` yaml $(az) && $(cloudservice)
tag: package-2020-10-01-preview-only
az:
  extensions: cloud-service
  namespace: azure.mgmt.compute
  package-name: azure-mgmt-compute
az-output-folder: $(azure-cli-extension-folder)/src/cloudservice
python-sdk-output-folder: $(az-output-folder)/azext_cloudservice/vendored_sdks/cloudservice
cli:
    cli-directive:
        - where:
            group: "*"
            op: "*"
          hidden: true
        - where:
            group: "CloudServiceRoleInstances"
            op: "*"
          hidden: false
        - where:
            group: "CloudServiceRoles"
            op: "*"
          hidden: false
        - where:
            group: "CloudServices"
            op: "*"
          hidden: false
        - where:
            group: "CloudServicesUpdateDomain"
            op: "*"
          hidden: false
directive:
  - where:
      group: cloud-service cloud-service-role-instance
    set:
      group: cloud-service role-instance
  - where:
      group: cloud-service cloud-service-role
    set:
      group: cloud-service role
  - where:
      group: cloud-service cloud-service-update-domain
    set:
      group: cloud-service update-domain
```

``` yaml $(az) && $(target-mode) == "core"
tag: package-2021-03-01
az:
  extensions: vm
  namespace: azure.mgmt.compute
  package-name: azure-mgmt-compute
az-output-folder: $(azure-cli-folder)/src/azure-cli/azure/cli/command_modules/vm
python-sdk-output-folder: "$(az-output-folder)/vendored_sdks/vm"
extension-mode: stable
compatible-level: track2
cli:
    cli-directive:
        - where:
            group: "*"
            op: "*"
          hidden: true
        - where:
            group: "SshPublicKeys"
            op: "*"
          hidden: false
        - where:
            group: "SshPublicKeys"
            op: "GenerateKeyPair"
          hidden: true
        - where:
            group: "*"
            op: "*"
            param: vmName
          alias: name
        - where:
            group: "Galleries"
            op: "Update"
          hidden: false
        - where:
            group: "GallerySharingProfile"
            op: "Update"
          hidden: false
        - where:
            group: "SharedGalleries"
            op: "*"
          hidden: false
        - where:
            group: "SharedGalleryImages"
            op: "*"
          hidden: false
        - where:
            group: "SharedGalleryImageVersions"
            op: "*"
          hidden: false
        - where:
            group: "*"
            op: "*"
            param: sharedTo
          alias: scope
directive: 
  - where: 
      group: vm sshpublickey
    set:
      group: sshkey
  - where: 
      group: vm gallerysharingprofile
    set:
      group: sig share
  - where: 
      group: vm sharedgallery
    set:
      group: sig share
  - where: 
      command: vm sharedgallery list
    set:
      command: sig group-list
  - where: 
      group: vm gallery
    set:
      group: sig
  - where: 
      group: vm sharedgalleryimages
    set:
      group: sig image-definition
  - where: 
      group: vm sharedgalleryimageversions
    set:
      group: sig image-version
```
