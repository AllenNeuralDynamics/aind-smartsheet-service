# ExaSPIMInfo

All exaSPIM Information for Specimen ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mouse_tracker_info** | [**List[MouseTracker]**](MouseTracker.md) |  | [optional] 
**sample_tracking_info** | [**List[SampleTracking]**](SampleTracking.md) |  | [optional] 
**imaging_queue_info** | [**List[ImagingQueue]**](ImagingQueue.md) |  | [optional] 
**qc_sheet_info** | [**List[QcSheet]**](QcSheet.md) |  | [optional] 

## Example

```python
from aind_smartsheet_service_async_client.models.exa_spim_info import ExaSPIMInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExaSPIMInfo from a JSON string
exa_spim_info_instance = ExaSPIMInfo.from_json(json)
# print the JSON string representation of the object
print(ExaSPIMInfo.to_json())

# convert the object into a dict
exa_spim_info_dict = exa_spim_info_instance.to_dict()
# create an instance of ExaSPIMInfo from a dict
exa_spim_info_from_dict = ExaSPIMInfo.from_dict(exa_spim_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


