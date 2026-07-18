# ImagingQueue

Imaging Queue Sheet Information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** |  | [optional] 
**sample** | **str** |  | [optional] 
**one_x_imaging_date** | **str** |  | [optional] 
**imaging_start_date** | **str** |  | [optional] 
**imaging_start_time** | **str** |  | [optional] 
**drop_off_date** | **str** |  | [optional] 
**imaging_end_date** | **str** |  | [optional] 
**imaging_end_time** | **str** |  | [optional] 
**imaging_buffer** | **str** |  | [optional] 
**microscope** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**genotype** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**fluorophore** | **str** |  | [optional] 
**signal_channel_s** | **str** |  | [optional] 
**auto_fluorescence_channel_s** | **str** |  | [optional] 
**focus_n_mm** | **str** |  | [optional] 
**etl_offset** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**notes_1** | **str** |  | [optional] 
**verified_mouse_tracker_for_metadata_intake** | **str** |  | [optional] 
**notes_on_missing_metadata** | **str** |  | [optional] 

## Example

```python
from aind_smartsheet_service_client.models.imaging_queue import ImagingQueue

# TODO update the JSON string below
json = "{}"
# create an instance of ImagingQueue from a JSON string
imaging_queue_instance = ImagingQueue.from_json(json)
# print the JSON string representation of the object
print(ImagingQueue.to_json())

# convert the object into a dict
imaging_queue_dict = imaging_queue_instance.to_dict()
# create an instance of ImagingQueue from a dict
imaging_queue_from_dict = ImagingQueue.from_dict(imaging_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


