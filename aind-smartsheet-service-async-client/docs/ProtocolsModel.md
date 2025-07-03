# ProtocolsModel

Expected model for the Protocols SmartSheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol_type** | **str** |  | [optional] 
**procedure_name** | **str** |  | [optional] 
**protocol_name** | **str** |  | [optional] 
**doi** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**protocol_collection** | **bool** |  | [optional] 

## Example

```python
from aind_smartsheet_service_async_client.models.protocols_model import ProtocolsModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolsModel from a JSON string
protocols_model_instance = ProtocolsModel.from_json(json)
# print the JSON string representation of the object
print(ProtocolsModel.to_json())

# convert the object into a dict
protocols_model_dict = protocols_model_instance.to_dict()
# create an instance of ProtocolsModel from a dict
protocols_model_from_dict = ProtocolsModel.from_dict(protocols_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


