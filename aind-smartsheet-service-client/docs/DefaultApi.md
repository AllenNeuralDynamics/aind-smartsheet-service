# aind_smartsheet_service_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_funding**](DefaultApi.md#get_funding) | **GET** /funding | Get Funding
[**get_perfusions**](DefaultApi.md#get_perfusions) | **GET** /perfusions | Get Perfusions
[**get_project_names**](DefaultApi.md#get_project_names) | **GET** /project_names | Get Project Names
[**get_protocols**](DefaultApi.md#get_protocols) | **GET** /protocols | Get Protocols


# **get_funding**
> List[FundingModel] get_funding(project_name=project_name, subproject=subproject)

Get Funding

## Funding
Returns funding information for a project_name and subproject.

### Example


```python
import aind_smartsheet_service_client
from aind_smartsheet_service_client.models.funding_model import FundingModel
from aind_smartsheet_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_smartsheet_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aind_smartsheet_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_smartsheet_service_client.DefaultApi(api_client)
    project_name = 'Discovery-Neuromodulator circuit dynamics during foraging' # str |  (optional)
    subproject = 'Subproject 2 Molecular Anatomy Cell Types' # str |  (optional)

    try:
        # Get Funding
        api_response = api_instance.get_funding(project_name=project_name, subproject=subproject)
        print("The response of DefaultApi->get_funding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_funding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | [optional] 
 **subproject** | **str**|  | [optional] 

### Return type

[**List[FundingModel]**](FundingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_perfusions**
> List[PerfusionsModel] get_perfusions(subject_id=subject_id)

Get Perfusions

## Perfusions
Returns perfusions for a given subject_id.

### Example


```python
import aind_smartsheet_service_client
from aind_smartsheet_service_client.models.perfusions_model import PerfusionsModel
from aind_smartsheet_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_smartsheet_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aind_smartsheet_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_smartsheet_service_client.DefaultApi(api_client)
    subject_id = '689418' # str |  (optional)

    try:
        # Get Perfusions
        api_response = api_instance.get_perfusions(subject_id=subject_id)
        print("The response of DefaultApi->get_perfusions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_perfusions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**|  | [optional] 

### Return type

[**List[PerfusionsModel]**](PerfusionsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_names**
> List[Optional[str]] get_project_names()

Get Project Names

## Project Names
Returns a list of project names.

### Example


```python
import aind_smartsheet_service_client
from aind_smartsheet_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_smartsheet_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aind_smartsheet_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_smartsheet_service_client.DefaultApi(api_client)

    try:
        # Get Project Names
        api_response = api_instance.get_project_names()
        print("The response of DefaultApi->get_project_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_names: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Optional[str]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protocols**
> List[ProtocolsModel] get_protocols(protocol_name=protocol_name)

Get Protocols

## Protocols
Returns protocols given a name.

### Example


```python
import aind_smartsheet_service_client
from aind_smartsheet_service_client.models.protocols_model import ProtocolsModel
from aind_smartsheet_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_smartsheet_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aind_smartsheet_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_smartsheet_service_client.DefaultApi(api_client)
    protocol_name = 'Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain' # str |  (optional)

    try:
        # Get Protocols
        api_response = api_instance.get_protocols(protocol_name=protocol_name)
        print("The response of DefaultApi->get_protocols:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_protocols: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol_name** | **str**|  | [optional] 

### Return type

[**List[ProtocolsModel]**](ProtocolsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

