# CrowdLabelApi.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availabilityAvailabilityPost**](DefaultApi.md#availabilityAvailabilityPost) | **POST** /availability | Availability
[**downloadResultsDownloadResultsGet**](DefaultApi.md#downloadResultsDownloadResultsGet) | **GET** /download_results | Download Results
[**faviconFaviconIcoGet**](DefaultApi.md#faviconFaviconIcoGet) | **GET** /favicon.ico | Favicon
[**getPagePageGet**](DefaultApi.md#getPagePageGet) | **GET** /{page} | Get Page
[**helloHelloPost**](DefaultApi.md#helloHelloPost) | **POST** /hello | Hello
[**indexGet**](DefaultApi.md#indexGet) | **GET** / | Index
[**loginLoginPost**](DefaultApi.md#loginLoginPost) | **POST** /login | Login
[**readItemsItemsGet**](DefaultApi.md#readItemsItemsGet) | **GET** /items/ | Read Items
[**readUsersMeUsersMeGet**](DefaultApi.md#readUsersMeUsersMeGet) | **GET** /users/me | Read Users Me
[**registerRegisterPost**](DefaultApi.md#registerRegisterPost) | **POST** /register | Register
[**uploadTaskUploadTaskPost**](DefaultApi.md#uploadTaskUploadTaskPost) | **POST** /upload_task | Upload Task
[**wrappertaskTaskIdGet**](DefaultApi.md#wrappertaskTaskIdGet) | **GET** /task/&lt;id&gt; | Wrappertask
[**wrappertasksTasksGet**](DefaultApi.md#wrappertasksTasksGet) | **GET** /tasks | Wrappertasks
[**wrapperuserUserUsernameGet**](DefaultApi.md#wrapperuserUserUsernameGet) | **GET** /user/&lt;username&gt; | Wrapperuser



## availabilityAvailabilityPost

> Availability availabilityAvailabilityPost(availability)

Availability

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
let availability = new CrowdLabelApi.Availability(); // Availability | 
apiInstance.availabilityAvailabilityPost(availability, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **availability** | [**Availability**](Availability.md)|  | 

### Return type

[**Availability**](Availability.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## downloadResultsDownloadResultsGet

> Object downloadResultsDownloadResultsGet()

Download Results

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
apiInstance.downloadResultsDownloadResultsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## faviconFaviconIcoGet

> faviconFaviconIcoGet()

Favicon

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
apiInstance.faviconFaviconIcoGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPagePageGet

> String getPagePageGet(page)

Get Page

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
let page = "page_example"; // String | 
apiInstance.getPagePageGet(page, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **String**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html, application/json


## helloHelloPost

> HelloResponse helloHelloPost(helloRequest)

Hello

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
let helloRequest = new CrowdLabelApi.HelloRequest(); // HelloRequest | 
apiInstance.helloHelloPost(helloRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helloRequest** | [**HelloRequest**](HelloRequest.md)|  | 

### Return type

[**HelloResponse**](HelloResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## indexGet

> String indexGet()

Index

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
apiInstance.indexGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html


## loginLoginPost

> JWT loginLoginPost(credentials)

Login

Successful login. Returns the &#x60;jwt&#x60; associated with the provided credentials.

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
let credentials = new CrowdLabelApi.Credentials(); // Credentials | 
apiInstance.loginLoginPost(credentials, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**Credentials**](Credentials.md)|  | 

### Return type

[**JWT**](JWT.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## readItemsItemsGet

> Object readItemsItemsGet()

Read Items

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.DefaultApi();
apiInstance.readItemsItemsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readUsersMeUsersMeGet

> Object readUsersMeUsersMeGet()

Read Users Me

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.DefaultApi();
apiInstance.readUsersMeUsersMeGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registerRegisterPost

> JWT registerRegisterPost(registration)

Register

Successful registration. Returns the &#x60;jwt&#x60; associated with the newly-created account

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
let registration = new CrowdLabelApi.Registration(); // Registration | 
apiInstance.registerRegisterPost(registration, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration** | [**Registration**](Registration.md)|  | 

### Return type

[**JWT**](JWT.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadTaskUploadTaskPost

> Object uploadTaskUploadTaskPost(data, inFile)

Upload Task

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
let data = "data_example"; // String | 
let inFile = "/path/to/file"; // File | 
apiInstance.uploadTaskUploadTaskPost(data, inFile, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **String**|  | 
 **inFile** | **File**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## wrappertaskTaskIdGet

> Object wrappertaskTaskIdGet(args, kwargs)

Wrappertask

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
let args = null; // Object | 
let kwargs = null; // Object | 
apiInstance.wrappertaskTaskIdGet(args, kwargs, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | [**Object**](.md)|  | 
 **kwargs** | [**Object**](.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wrappertasksTasksGet

> Object wrappertasksTasksGet(args, kwargs)

Wrappertasks

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
let args = null; // Object | 
let kwargs = null; // Object | 
apiInstance.wrappertasksTasksGet(args, kwargs, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | [**Object**](.md)|  | 
 **kwargs** | [**Object**](.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wrapperuserUserUsernameGet

> Object wrapperuserUserUsernameGet(args, kwargs)

Wrapperuser

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
let args = null; // Object | 
let kwargs = null; // Object | 
apiInstance.wrapperuserUserUsernameGet(args, kwargs, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | [**Object**](.md)|  | 
 **kwargs** | [**Object**](.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

