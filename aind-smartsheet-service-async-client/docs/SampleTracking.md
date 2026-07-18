# SampleTracking

Sample Tracking Sheet Information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_sample** | **str** |  | [optional] 
**screening_status** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**sample** | **str** |  | [optional] 
**genotype** | **str** |  | [optional] 
**processing_lead** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**project_description** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**age_of_injection** | **str** |  | [optional] 
**virus_dose** | **str** |  | [optional] 
**dcm_delipidation_start** | **str** |  | [optional] 
**dcm_delipidation_end** | **str** |  | [optional] 
**sbip_delipidation_start** | **str** |  | [optional] 
**sbip_delipidation_end** | **str** |  | [optional] 
**immuno_primary_ab_start_date** | **str** |  | [optional] 
**immuno_primary_antibody1** | **str** |  | [optional] 
**mass_of_primary_antibody1_used_per_brain_ug** | **str** |  | [optional] 
**primary_antibody1_catalog_num** | **str** |  | [optional] 
**primary_antibody1_lot_num** | **str** |  | [optional] 
**immuno_primary_antibody2** | **str** |  | [optional] 
**mass_of_primary_antibody2_used_per_brain_ug** | **str** |  | [optional] 
**primary_antibody2_catalog_num** | **str** |  | [optional] 
**primary_antibody2_lot_num** | **str** |  | [optional] 
**immuno_primary_antibody3** | **str** |  | [optional] 
**mass_of_primary_antibody3_used_per_brain_ug** | **str** |  | [optional] 
**primary_antibody3_catalog_num** | **str** |  | [optional] 
**primary_antibody3_lot_num** | **str** |  | [optional] 
**primary_antibody_rrid** | **str** |  | [optional] 
**immuno_secondary_ab_start_date** | **str** |  | [optional] 
**immuno_secondary_antibody1** | **str** |  | [optional] 
**mass_of_secondary_antibody1_used_per_brain_ug** | **str** |  | [optional] 
**secondary_antibody1_catalog_num** | **str** |  | [optional] 
**secondary_antibody1_lot_num** | **str** |  | [optional] 
**immuno_secondary_antibody2** | **str** |  | [optional] 
**mass_of_secondary_antibody2_used_per_brain_ug** | **str** |  | [optional] 
**secondary_antibody2_catalog_num** | **str** |  | [optional] 
**secondary_antibody2_lot_num** | **str** |  | [optional] 
**immuno_secondary_antibody3** | **str** |  | [optional] 
**mass_of_secondary_antibody3_used_per_brain_ug** | **str** |  | [optional] 
**secondary_antibody3_catalog_num** | **str** |  | [optional] 
**secondary_antibody3_lot_num** | **str** |  | [optional] 
**secondary_antibody_rrid** | **str** |  | [optional] 
**fluorophore1** | **str** |  | [optional] 
**fluorophore2** | **str** |  | [optional] 
**fluorophore3** | **str** |  | [optional] 
**fluorophore_t** | **str** |  | [optional] 
**gelation_mbs_start** | **str** |  | [optional] 
**gelation_mbs_end** | **str** |  | [optional] 
**gelation_ac_x_start** | **str** |  | [optional] 
**gelation_ac_x_end** | **str** |  | [optional] 
**gelation_pbs_wash_start** | **str** |  | [optional] 
**gelation_pbs_wash_end** | **str** |  | [optional] 
**gelation_stock_xva_044_equilibration_start** | **str** |  | [optional] 
**gelation_stock_xva_044_equilibration_end** | **str** |  | [optional] 
**gelation_prok_rt_start** | **str** |  | [optional] 
**gelation_prok_rt_end** | **str** |  | [optional] 
**duration_days** | **str** |  | [optional] 
**gelation_add_l_prok_37c_start** | **str** |  | [optional] 
**gelation_add_l_prok_37c_end** | **str** |  | [optional] 
**duration_days_gelation_add_l_prok_37c** | **str** |  | [optional] 
**pbs_wash_start** | **str** |  | [optional] 
**pbs_wash_end** | **str** |  | [optional] 
**date_of_storage_in_pbs_az_0_05_4c** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**notes_ii** | **str** |  | [optional] 
**notes_iii** | **str** |  | [optional] 

## Example

```python
from aind_smartsheet_service_async_client.models.sample_tracking import SampleTracking

# TODO update the JSON string below
json = "{}"
# create an instance of SampleTracking from a JSON string
sample_tracking_instance = SampleTracking.from_json(json)
# print the JSON string representation of the object
print(SampleTracking.to_json())

# convert the object into a dict
sample_tracking_dict = sample_tracking_instance.to_dict()
# create an instance of SampleTracking from a dict
sample_tracking_from_dict = SampleTracking.from_dict(sample_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


