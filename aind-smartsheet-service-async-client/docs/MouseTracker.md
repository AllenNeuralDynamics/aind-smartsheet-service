# MouseTracker

Mouse Tracker Sheet Information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num** | **int** |  | 
**ex_m_processing_status** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**mouse_id** | **str** |  | [optional] 
**sample_name** | **str** |  | [optional] 
**workflow** | **str** |  | [optional] 
**project_description** | **str** |  | [optional] 
**expression_time_days** | **str** |  | [optional] 
**pedigree** | **str** |  | [optional] 
**sex** | **str** |  | [optional] 
**dob** | **str** |  | [optional] 
**stx_injection_requested** | **str** |  | [optional] 
**ro_injection_requested** | **str** |  | [optional] 
**perfusion_requested** | **str** |  | [optional] 
**inj_details_tam_dose** | **str** |  | [optional] 
**tam_dosing_last_day** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**virus_mix_ro** | **str** |  | [optional] 
**virus_mix_total_volume_injected_ro_ul** | **str** |  | [optional] 
**virus_mix_vehicle_ro** | **str** |  | [optional] 
**virus1_injection_date** | **str** |  | [optional] 
**virus1_age_of_injection** | **str** |  | [optional] 
**virus1_injection_type** | **str** |  | [optional] 
**virus1** | **str** |  | [optional] 
**ai_p_num** | **str** |  | [optional] 
**virus1_id** | **str** |  | [optional] 
**virus1_stock_titer_gc_ml** | **str** |  | [optional] 
**working_titer_gc_ml** | **str** |  | [optional] 
**virus1_dose_gc** | **str** |  | [optional] 
**virus1_ap_mm** | **str** |  | [optional] 
**virus1_ml_mm** | **str** |  | [optional] 
**virus1_dv_mm** | **str** |  | [optional] 
**virus1_dv_b_mm** | **str** |  | [optional] 
**virus1_stereotaxic_volume_injected_nl** | **str** |  | [optional] 
**virus2_injection_date** | **str** |  | [optional] 
**virus2_age_of_injection** | **str** |  | [optional] 
**virus2_injection_type** | **str** |  | [optional] 
**virus2** | **str** |  | [optional] 
**virus2_ai_p_num** | **str** |  | [optional] 
**virus2_id** | **str** |  | [optional] 
**virus2_stock_titer_gc_ml** | **str** |  | [optional] 
**virus2_working_titer_gc_ml** | **str** |  | [optional] 
**virus2_dose_gc** | **str** |  | [optional] 
**virus2_effective_titer_gc_ml** | **str** |  | [optional] 
**virus2_ap_mm** | **str** |  | [optional] 
**virus2_ml_mm** | **str** |  | [optional] 
**virus2_dv_mm** | **str** |  | [optional] 
**virus2_dv_b_mm** | **str** |  | [optional] 
**virus2_stereotaxic_volume_injected_nl** | **str** |  | [optional] 
**virus3_injection_date** | **str** |  | [optional] 
**virus3_age_of_injection** | **str** |  | [optional] 
**virus3_injection_type** | **str** |  | [optional] 
**virus3** | **str** |  | [optional] 
**virus3_ai_p_num** | **str** |  | [optional] 
**virus3_id** | **str** |  | [optional] 
**virus3_stock_titer_gc_ml** | **str** |  | [optional] 
**virus3_dose_gc** | **str** |  | [optional] 
**virus3_effective_titer_gc_ml** | **str** |  | [optional] 
**virus3_ap_mm** | **str** |  | [optional] 
**virus3_ml_mm** | **str** |  | [optional] 
**virus3_dv_mm** | **str** |  | [optional] 
**virus3_dv_b_mm** | **str** |  | [optional] 
**virus3_stereotaxic_volume_injected_nl** | **str** |  | [optional] 
**virus4_injection_date** | **str** |  | [optional] 
**virus4_age_of_injection** | **str** |  | [optional] 
**virus4_injection_type** | **str** |  | [optional] 
**virus4** | **str** |  | [optional] 
**virus4_id** | **str** |  | [optional] 
**virus4_stock_titer_gc_ml** | **str** |  | [optional] 
**virus4_dose_gc** | **str** |  | [optional] 
**virus4_effective_titer_gc_ml** | **str** |  | [optional] 
**virus4_ap_mm** | **str** |  | [optional] 
**virus4_ml_mm** | **str** |  | [optional] 
**virus4_dv_mm** | **str** |  | [optional] 
**virus4_dv_b_mm** | **str** |  | [optional] 
**stereotaxic_volume_injected_nl** | **str** |  | [optional] 
**heparin_dose_u** | **str** |  | [optional] 
**perfused** | **str** |  | [optional] 
**perfusion_type** | **str** |  | [optional] 
**perfusion_date** | **str** |  | [optional] 
**age_of_perfusion** | **str** |  | [optional] 
**las_injection_notes** | **str** |  | [optional] 
**las_perfusion_dissection_notes** | **str** |  | [optional] 
**gross_anatomy_notes_pre_processing** | **str** |  | [optional] 
**other_notes** | **str** |  | [optional] 
**other_notes2** | **str** |  | [optional] 
**neuro_glancer_link** | **str** |  | [optional] 
**good_labeling_sparsity** | **str** |  | [optional] 
**target_area_of_interest** | **str** |  | [optional] 
**investigator** | **str** |  | [optional] 
**project_code** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**death_health_issues** | **str** |  | [optional] 

## Example

```python
from aind_smartsheet_service_async_client.models.mouse_tracker import MouseTracker

# TODO update the JSON string below
json = "{}"
# create an instance of MouseTracker from a JSON string
mouse_tracker_instance = MouseTracker.from_json(json)
# print the JSON string representation of the object
print(MouseTracker.to_json())

# convert the object into a dict
mouse_tracker_dict = mouse_tracker_instance.to_dict()
# create an instance of MouseTracker from a dict
mouse_tracker_from_dict = MouseTracker.from_dict(mouse_tracker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


