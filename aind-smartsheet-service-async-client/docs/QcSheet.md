# QcSheet

QC Sheet Information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample** | **str** |  | [optional] 
**imaging_priority** | **str** |  | [optional] 
**date_sent_for_1x_imaging** | **str** |  | [optional] 
**date_of_tissue_processing_completion** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**genotype** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**project_description** | **str** |  | [optional] 
**perfusion_date** | **str** |  | [optional] 
**las_injection_notes** | **str** |  | [optional] 
**las_perfusion_dissection_notes** | **str** |  | [optional] 
**perfusion_dissection_quality_notes** | **str** |  | [optional] 
**perfusion_pass_fail** | **str** |  | [optional] 
**labeling_density_notes_olympus_mxv10** | **str** |  | [optional] 
**durotomy_tissue_damage_notes** | **str** |  | [optional] 
**immuno_gross_anatomy_notes** | **str** |  | [optional] 
**immuno_pass_fail** | **str** |  | [optional] 
**digestion_notes** | **str** |  | [optional] 
**digestion_pass_fail** | **str** |  | [optional] 
**special_notes** | **str** |  | [optional] 
**brain_size_at_1x_imaging** | **str** |  | [optional] 
**one_x_screening_link** | **str** |  | [optional] 
**investigator** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**surface_labeling** | **str** |  | [optional] 
**vascular_labeling** | **str** |  | [optional] 
**no_artifacts** | **str** |  | [optional] 
**targeted_sparsity** | **str** |  | [optional] 
**no_surface_labeling** | **str** |  | [optional] 
**no_vascular_labeling** | **str** |  | [optional] 
**targeted_sparsity_q** | **str** |  | [optional] 
**one_x_review_pass_fail** | **str** |  | [optional] 
**one_x_screening_notes_platform_lead** | **str** |  | [optional] 
**one_x_screening_notes_sample_processing_r_a** | **str** |  | [optional] 
**one_x_screening_notes_investigator** | **str** |  | [optional] 
**five_x_imaging_date** | **str** |  | [optional] 

## Example

```python
from aind_smartsheet_service_async_client.models.qc_sheet import QcSheet

# TODO update the JSON string below
json = "{}"
# create an instance of QcSheet from a JSON string
qc_sheet_instance = QcSheet.from_json(json)
# print the JSON string representation of the object
print(QcSheet.to_json())

# convert the object into a dict
qc_sheet_dict = qc_sheet_instance.to_dict()
# create an instance of QcSheet from a dict
qc_sheet_from_dict = QcSheet.from_dict(qc_sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


