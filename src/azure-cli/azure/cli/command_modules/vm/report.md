# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az vm|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az vm` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az sshkey|SshPublicKeys|[commands](#CommandsInSshPublicKeys)|
|az sig|GalleryImages|[commands](#CommandsInGalleryImages)|
|az sig image-definition|SharedGalleryImages|[commands](#CommandsInSharedGalleryImages)|
|az sig image-version|SharedGalleryImageVersions|[commands](#CommandsInSharedGalleryImageVersions)|

## COMMANDS
### <a name="CommandsInGalleryImages">Commands in `az sig` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sig update](#GalleryImagesUpdate)|Update|[Parameters](#ParametersGalleryImagesUpdate)|[Example](#ExamplesGalleryImagesUpdate)|
|[az sig group-list](#GalleryImagesList)|List|[Parameters](#ParametersGalleryImagesList)|[Example](#ExamplesGalleryImagesList)|
|[az sig share](#GalleryImagesUpdate)|Update|[Parameters](#ParametersGalleryImagesUpdate)|[Example](#ExamplesGalleryImagesUpdate)|

### <a name="CommandsInSharedGalleryImages">Commands in `az sig image-definition` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sig image-definition list](#SharedGalleryImagesList)|List|[Parameters](#ParametersSharedGalleryImagesList)|[Example](#ExamplesSharedGalleryImagesList)|
|[az sig image-definition show](#SharedGalleryImagesGet)|Get|[Parameters](#ParametersSharedGalleryImagesGet)|[Example](#ExamplesSharedGalleryImagesGet)|

### <a name="CommandsInSharedGalleryImageVersions">Commands in `az sig image-version` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sig image-version list](#SharedGalleryImageVersionsList)|List|[Parameters](#ParametersSharedGalleryImageVersionsList)|[Example](#ExamplesSharedGalleryImageVersionsList)|
|[az sig image-version show](#SharedGalleryImageVersionsGet)|Get|[Parameters](#ParametersSharedGalleryImageVersionsGet)|[Example](#ExamplesSharedGalleryImageVersionsGet)|

### <a name="CommandsInSshPublicKeys">Commands in `az sshkey` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sshkey list](#SshPublicKeysListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersSshPublicKeysListByResourceGroup)|Not Found|
|[az sshkey list](#SshPublicKeysListBySubscription)|ListBySubscription|[Parameters](#ParametersSshPublicKeysListBySubscription)|Not Found|
|[az sshkey show](#SshPublicKeysGet)|Get|[Parameters](#ParametersSshPublicKeysGet)|[Example](#ExamplesSshPublicKeysGet)|
|[az sshkey create](#SshPublicKeysCreate)|Create|[Parameters](#ParametersSshPublicKeysCreate)|[Example](#ExamplesSshPublicKeysCreate)|
|[az sshkey update](#SshPublicKeysUpdate)|Update|[Parameters](#ParametersSshPublicKeysUpdate)|Not Found|
|[az sshkey delete](#SshPublicKeysDelete)|Delete|[Parameters](#ParametersSshPublicKeysDelete)|Not Found|


## COMMAND DETAILS

### group `az sig`
#### <a name="GalleryImagesUpdate">Command `az sig update`</a>

##### <a name="ExamplesGalleryImagesUpdate">Example</a>
```
az sig update --hyper-v-generation "V1" --identifier offer="myOfferName" publisher="myPublisherName" sku="mySkuName" \
--os-state "Generalized" --os-type "Windows" --name "myGalleryImageName" --gallery-name "myGalleryName" \
--resource-group "myResourceGroup"
```
##### <a name="ParametersGalleryImagesUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--gallery-name**|string|The name of the Shared Image Gallery in which the Image Definition is to be updated.|gallery_name|galleryName|
|**--gallery-image-name**|string|The name of the gallery image definition to be updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.|gallery_image_name|galleryImageName|
|**--tags**|dictionary|Resource tags|tags|tags|
|**--description**|string|The description of this gallery image definition resource. This property is updatable.|description|description|
|**--eula**|string|The Eula agreement for the gallery image definition.|eula|eula|
|**--privacy-statement-uri**|string|The privacy statement uri.|privacy_statement_uri|privacyStatementUri|
|**--release-note-uri**|string|The release note uri.|release_note_uri|releaseNoteUri|
|**--os-type**|sealed-choice|This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. <br><br> Possible values are: <br><br> **Windows** <br><br> **Linux**|os_type|osType|
|**--os-state**|sealed-choice|This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'.|os_state|osState|
|**--hyper-v-generation**|choice|The hypervisor generation of the Virtual Machine. Applicable to OS disks only.|hyper_v_generation|hyperVGeneration|
|**--end-of-life-date**|date-time|The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable.|end_of_life_date|endOfLifeDate|
|**--identifier**|object|This is the gallery image definition identifier.|identifier|identifier|
|**--disallowed**|object|Describes the disallowed disk types.|disallowed|disallowed|
|**--purchase-plan**|object|Describes the gallery image definition purchase plan. This is used by marketplace images.|purchase_plan|purchasePlan|
|**--features**|array|A list of gallery image features.|features|features|
|**--v-cp-us**|object|Describes the resource range.|v_cp_us|vCPUs|
|**--memory**|object|Describes the resource range.|memory|memory|

#### <a name="GalleryImagesList">Command `az sig group-list`</a>

##### <a name="ExamplesGalleryImagesList">Example</a>
```
az sig group-list --location "myLocation"
```
##### <a name="ParametersGalleryImagesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Resource location.|location|location|

#### <a name="GalleryImagesUpdate">Command `az sig share`</a>

##### <a name="ExamplesGalleryImagesUpdate">Example</a>
```
az sig share --gallery-name "myGalleryName" --resource-group "myResourceGroup" --groups type="Subscriptions" \
ids="34a4ab42-0d72-47d9-bd1a-aed207386dac" ids="380fd389-260b-41aa-bad9-0a83108c370b" --groups type="AADTenants" \
ids="c24c76aa-8897-4027-9b03-8f7928b54ff6" --operation-type "Add"
```
##### <a name="ExamplesGalleryImagesUpdate">Example</a>
```
az sig share --gallery-name "myGalleryName" --resource-group "myResourceGroup" --operation-type "Reset"
```
##### <a name="ParametersGalleryImagesUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--gallery-name**|string|The name of the Shared Image Gallery.|gallery_name|galleryName|
|**--operation-type**|choice|This property allows you to specify the operation type of gallery sharing update. <br><br> Possible values are: <br><br> **Add** <br><br> **Remove** <br><br> **Reset**|operation_type|operationType|
|**--groups**|array|A list of sharing profile groups.|groups|groups|

### group `az sig image-definition`
#### <a name="SharedGalleryImagesList">Command `az sig image-definition list`</a>

##### <a name="ExamplesSharedGalleryImagesList">Example</a>
```
az sig image-definition list --gallery-unique-name "galleryUniqueName" --location "myLocation"
```
##### <a name="ParametersSharedGalleryImagesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Resource location.|location|location|
|**--gallery-unique-name**|string|The unique name of the Shared Gallery.|gallery_unique_name|galleryUniqueName|

#### <a name="SharedGalleryImagesGet">Command `az sig image-definition show`</a>

##### <a name="ExamplesSharedGalleryImagesGet">Example</a>
```
az sig image-definition show --gallery-image-name "myGalleryImageName" --gallery-unique-name "galleryUniqueName" \
--location "myLocation"
```
##### <a name="ParametersSharedGalleryImagesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Resource location.|location|location|
|**--gallery-unique-name**|string|The unique name of the Shared Gallery.|gallery_unique_name|galleryUniqueName|
|**--gallery-image-name**|string|The name of the Shared Gallery Image Definition from which the Image Versions are to be listed.|gallery_image_name|galleryImageName|

### group `az sig image-version`
#### <a name="SharedGalleryImageVersionsList">Command `az sig image-version list`</a>

##### <a name="ExamplesSharedGalleryImageVersionsList">Example</a>
```
az sig image-version list --gallery-image-name "myGalleryImageName" --gallery-unique-name "galleryUniqueName" \
--location "myLocation"
```
##### <a name="ParametersSharedGalleryImageVersionsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Resource location.|location|location|
|**--gallery-unique-name**|string|The unique name of the Shared Gallery.|gallery_unique_name|galleryUniqueName|
|**--gallery-image-name**|string|The name of the Shared Gallery Image Definition from which the Image Versions are to be listed.|gallery_image_name|galleryImageName|

#### <a name="SharedGalleryImageVersionsGet">Command `az sig image-version show`</a>

##### <a name="ExamplesSharedGalleryImageVersionsGet">Example</a>
```
az sig image-version show --gallery-image-name "myGalleryImageName" --gallery-image-version-name \
"myGalleryImageVersionName" --gallery-unique-name "galleryUniqueName" --location "myLocation"
```
##### <a name="ParametersSharedGalleryImageVersionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Resource location.|location|location|
|**--gallery-unique-name**|string|The unique name of the Shared Gallery.|gallery_unique_name|galleryUniqueName|
|**--gallery-image-name**|string|The name of the Shared Gallery Image Definition from which the Image Versions are to be listed.|gallery_image_name|galleryImageName|
|**--gallery-image-version-name**|string|The name of the gallery image version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>|gallery_image_version_name|galleryImageVersionName|

### group `az sshkey`
#### <a name="SshPublicKeysListByResourceGroup">Command `az sshkey list`</a>

##### <a name="ParametersSshPublicKeysListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|

#### <a name="SshPublicKeysListBySubscription">Command `az sshkey list`</a>

##### <a name="ParametersSshPublicKeysListBySubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="SshPublicKeysGet">Command `az sshkey show`</a>

##### <a name="ExamplesSshPublicKeysGet">Example</a>
```
az sshkey show --resource-group "myResourceGroup" --name "mySshPublicKeyName"
```
##### <a name="ParametersSshPublicKeysGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--ssh-public-key-name**|string|The name of the SSH public key.|ssh_public_key_name|sshPublicKeyName|

#### <a name="SshPublicKeysCreate">Command `az sshkey create`</a>

##### <a name="ExamplesSshPublicKeysCreate">Example</a>
```
az sshkey create --location "westus" --public-key "{ssh-rsa public key}" --resource-group "myResourceGroup" --name \
"mySshPublicKeyName"
```
##### <a name="ParametersSshPublicKeysCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--ssh-public-key-name**|string|The name of the SSH public key.|ssh_public_key_name|sshPublicKeyName|
|**--location**|string|Resource location|location|location|
|**--tags**|dictionary|Resource tags|tags|tags|
|**--public-key**|string|SSH public key used to authenticate to a virtual machine through ssh. If this property is not initially provided when the resource is created, the publicKey property will be populated when generateKeyPair is called. If the public key is provided upon resource creation, the provided public key needs to be at least 2048-bit and in ssh-rsa format.|public_key|publicKey|

#### <a name="SshPublicKeysUpdate">Command `az sshkey update`</a>

##### <a name="ParametersSshPublicKeysUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--ssh-public-key-name**|string|The name of the SSH public key.|ssh_public_key_name|sshPublicKeyName|
|**--tags**|dictionary|Resource tags|tags|tags|
|**--public-key**|string|SSH public key used to authenticate to a virtual machine through ssh. If this property is not initially provided when the resource is created, the publicKey property will be populated when generateKeyPair is called. If the public key is provided upon resource creation, the provided public key needs to be at least 2048-bit and in ssh-rsa format.|public_key|publicKey|

#### <a name="SshPublicKeysDelete">Command `az sshkey delete`</a>

##### <a name="ParametersSshPublicKeysDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--ssh-public-key-name**|string|The name of the SSH public key.|ssh_public_key_name|sshPublicKeyName|
