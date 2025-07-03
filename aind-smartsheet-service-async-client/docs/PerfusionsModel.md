# PerfusionsModel

Expected model for the Perfusions SmartSheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_id** | **str** |  | [optional] 
**var_date** | **date** |  | [optional] 
**experimenter** | **str** |  | [optional] 
**iacuc_protocol** | **str** |  | [optional] 
**animal_weight_prior__g** | **str** |  | [optional] 
**output_specimen_id_s** | **str** |  | [optional] 
**postfix_solution** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from aind_smartsheet_service_async_client.models.perfusions_model import PerfusionsModel

# TODO update the JSON string below
json = "{}"
# create an instance of PerfusionsModel from a JSON string
perfusions_model_instance = PerfusionsModel.from_json(json)
# print the JSON string representation of the object
print(PerfusionsModel.to_json())

# convert the object into a dict
perfusions_model_dict = perfusions_model_instance.to_dict()
# create an instance of PerfusionsModel from a dict
perfusions_model_from_dict = PerfusionsModel.from_dict(perfusions_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


