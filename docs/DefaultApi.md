# blockmarkets.DefaultApi

All URIs are relative to *https://api.blockmarkets.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**benchmark_rate**](DefaultApi.md#benchmark_rate) | **GET** /v1/rates/benchmark/{symbol} | Returns the latest available benchmark rates for a specific asset.
[**benchmark_rate_history**](DefaultApi.md#benchmark_rate_history) | **GET** /v1/rates/benchmark/{symbol}/history | Returns historical benchmark rates for an asset. Requires premium subscription.
[**list_asset_markets**](DefaultApi.md#list_asset_markets) | **GET** /v1/assets/{symbol} | Returns a list of all markets (base and quote) for a specific asset.
[**list_assets**](DefaultApi.md#list_assets) | **GET** /v1/assets | Returns a list of supported assets.
[**list_benchmark_rates**](DefaultApi.md#list_benchmark_rates) | **GET** /v1/rates/benchmark | Returns a list of supported USD benchmark rates.
[**list_exchange_markets**](DefaultApi.md#list_exchange_markets) | **GET** /v1/exchanges/{exchange} | Returns a list of markets for a specific exchange.
[**list_exchanges**](DefaultApi.md#list_exchanges) | **GET** /v1/exchanges | Returns a list of supported exchanges.
[**list_markets**](DefaultApi.md#list_markets) | **GET** /v1/markets | Returns a list of supported markets.
[**list_pair_markets**](DefaultApi.md#list_pair_markets) | **GET** /v1/pairs/{pair} | Returns a list of markets for a specific asset pair.
[**list_pairs**](DefaultApi.md#list_pairs) | **GET** /v1/pairs | Returns a list of supported asset pairs.
[**list_spot_rates**](DefaultApi.md#list_spot_rates) | **GET** /v1/rates/spot | Returns a list of supported USD spot rates.
[**market_book**](DefaultApi.md#market_book) | **GET** /v1/markets/{exchange}/{pair}/book | Returns the top 50 bids and asks from the current order book for a market pair. Requires premium subscription.
[**market_ohlcv**](DefaultApi.md#market_ohlcv) | **GET** /v1/markets/{exchange}/{pair}/ohlcv | Returns OHLCV history for a market pair.
[**market_ticker**](DefaultApi.md#market_ticker) | **GET** /v1/markets/{exchange}/{pair} | Returns the latest ticker for a market pair.
[**market_trades**](DefaultApi.md#market_trades) | **GET** /v1/markets/{exchange}/{pair}/trades | Returns trades for a market pair. Requires premium subscription.
[**spot_rate**](DefaultApi.md#spot_rate) | **GET** /v1/rates/spot/{symbol} | Returns the last USD spot rate for an asset.
[**spot_rate_history**](DefaultApi.md#spot_rate_history) | **GET** /v1/rates/spot/{symbol}/history | Returns historical spot rates for an asset. Requires premium subscription.
[**spot_rate_ohlcv**](DefaultApi.md#spot_rate_ohlcv) | **GET** /v1/rates/spot/{symbol}/ohlcv | Returns the OHLCV history for a spot rate.


# **benchmark_rate**
> Empty benchmark_rate(symbol)

Returns the latest available benchmark rates for a specific asset.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
symbol = 'symbol_example' # str | The asset symbol (see /assets)

try:
    # Returns the latest available benchmark rates for a specific asset.
    api_response = api_instance.benchmark_rate(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->benchmark_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The asset symbol (see /assets) | 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **benchmark_rate_history**
> Empty benchmark_rate_history(symbol, close=close)

Returns historical benchmark rates for an asset. Requires premium subscription.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
symbol = 'symbol_example' # str | The asset symbol (see /assets)
close = 'close_example' # str | The closing time. Options - 4pm-gmt-close, 4pm-est-close, 0-utc-close (optional)

try:
    # Returns historical benchmark rates for an asset. Requires premium subscription.
    api_response = api_instance.benchmark_rate_history(symbol, close=close)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->benchmark_rate_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The asset symbol (see /assets) | 
 **close** | **str**| The closing time. Options - 4pm-gmt-close, 4pm-est-close, 0-utc-close | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_asset_markets**
> Empty list_asset_markets(symbol)

Returns a list of all markets (base and quote) for a specific asset.

### Example
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blockmarkets.DefaultApi()
symbol = 'symbol_example' # str | The asset symbol (see /assets)

try:
    # Returns a list of all markets (base and quote) for a specific asset.
    api_response = api_instance.list_asset_markets(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_asset_markets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The asset symbol (see /assets) | 

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets**
> Empty list_assets()

Returns a list of supported assets.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))

try:
    # Returns a list of supported assets.
    api_response = api_instance.list_assets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_assets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_benchmark_rates**
> Empty list_benchmark_rates()

Returns a list of supported USD benchmark rates.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))

try:
    # Returns a list of supported USD benchmark rates.
    api_response = api_instance.list_benchmark_rates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_benchmark_rates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_exchange_markets**
> Empty list_exchange_markets(exchange)

Returns a list of markets for a specific exchange.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
exchange = 'exchange_example' # str | The 4-char exchange code (see /exchanges)

try:
    # Returns a list of markets for a specific exchange.
    api_response = api_instance.list_exchange_markets(exchange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_exchange_markets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| The 4-char exchange code (see /exchanges) | 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_exchanges**
> Empty list_exchanges()

Returns a list of supported exchanges.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))

try:
    # Returns a list of supported exchanges.
    api_response = api_instance.list_exchanges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_exchanges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_markets**
> Empty list_markets()

Returns a list of supported markets.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))

try:
    # Returns a list of supported markets.
    api_response = api_instance.list_markets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_markets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pair_markets**
> Empty list_pair_markets(pair)

Returns a list of markets for a specific asset pair.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
pair = 'pair_example' # str | The asset pair (see /pairs)

try:
    # Returns a list of markets for a specific asset pair.
    api_response = api_instance.list_pair_markets(pair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_pair_markets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| The asset pair (see /pairs) | 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pairs**
> Empty list_pairs()

Returns a list of supported asset pairs.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))

try:
    # Returns a list of supported asset pairs.
    api_response = api_instance.list_pairs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_pairs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_spot_rates**
> Empty list_spot_rates()

Returns a list of supported USD spot rates.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))

try:
    # Returns a list of supported USD spot rates.
    api_response = api_instance.list_spot_rates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_spot_rates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_book**
> Empty market_book(exchange, pair)

Returns the top 50 bids and asks from the current order book for a market pair. Requires premium subscription.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
exchange = 'exchange_example' # str | The 4-char exchange code (see /exchanges)
pair = 'pair_example' # str | The asset pair (see /pairs)

try:
    # Returns the top 50 bids and asks from the current order book for a market pair. Requires premium subscription.
    api_response = api_instance.market_book(exchange, pair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->market_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| The 4-char exchange code (see /exchanges) | 
 **pair** | **str**| The asset pair (see /pairs) | 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_ohlcv**
> Empty market_ohlcv(exchange, pair, limit=limit, interval=interval, start=start, end=end)

Returns OHLCV history for a market pair.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
exchange = 'exchange_example' # str | The 4-char exchange code (see /exchanges)
pair = 'pair_example' # str | The asset pair (see /pairs)
limit = 56 # int | Number of records to retrieve (default=100, max=1000) (optional)
interval = 56 # int | Interval period in minutes. Supported - 1,3,5,15,30,60,1440 (default=1440) (optional)
start = 'start_example' # str | Start datetime in ISO 8601 (optional)
end = 'end_example' # str | End datetime in ISO 8601 (optional)

try:
    # Returns OHLCV history for a market pair.
    api_response = api_instance.market_ohlcv(exchange, pair, limit=limit, interval=interval, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->market_ohlcv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| The 4-char exchange code (see /exchanges) | 
 **pair** | **str**| The asset pair (see /pairs) | 
 **limit** | **int**| Number of records to retrieve (default&#x3D;100, max&#x3D;1000) | [optional] 
 **interval** | **int**| Interval period in minutes. Supported - 1,3,5,15,30,60,1440 (default&#x3D;1440) | [optional] 
 **start** | **str**| Start datetime in ISO 8601 | [optional] 
 **end** | **str**| End datetime in ISO 8601 | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_ticker**
> Empty market_ticker(exchange, pair)

Returns the latest ticker for a market pair.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
exchange = 'exchange_example' # str | The 4-char exchange code (see /exchanges)
pair = 'pair_example' # str | The asset pair (see /pairs)

try:
    # Returns the latest ticker for a market pair.
    api_response = api_instance.market_ticker(exchange, pair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->market_ticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| The 4-char exchange code (see /exchanges) | 
 **pair** | **str**| The asset pair (see /pairs) | 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_trades**
> Empty market_trades(exchange, pair, limit=limit, start=start, end=end)

Returns trades for a market pair. Requires premium subscription.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
exchange = 'exchange_example' # str | The 4-char exchange code (see /exchanges)
pair = 'pair_example' # str | The asset pair (see /pairs)
limit = 56 # int | Number of records to retrieve (default=100, max=1000) (optional)
start = 'start_example' # str | Start datetime in ISO 8601 (optional)
end = 'end_example' # str | End datetime in ISO 8601 (optional)

try:
    # Returns trades for a market pair. Requires premium subscription.
    api_response = api_instance.market_trades(exchange, pair, limit=limit, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->market_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| The 4-char exchange code (see /exchanges) | 
 **pair** | **str**| The asset pair (see /pairs) | 
 **limit** | **int**| Number of records to retrieve (default&#x3D;100, max&#x3D;1000) | [optional] 
 **start** | **str**| Start datetime in ISO 8601 | [optional] 
 **end** | **str**| End datetime in ISO 8601 | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spot_rate**
> Empty spot_rate(symbol)

Returns the last USD spot rate for an asset.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
symbol = 'symbol_example' # str | The asset symbol (see /assets)

try:
    # Returns the last USD spot rate for an asset.
    api_response = api_instance.spot_rate(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->spot_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The asset symbol (see /assets) | 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spot_rate_history**
> Empty spot_rate_history(symbol, limit=limit, start=start, end=end)

Returns historical spot rates for an asset. Requires premium subscription.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
symbol = 'symbol_example' # str | The asset symbol (see /assets)
limit = 56 # int | Number of records to retrieve (default=100, max=1000) (optional)
start = 'start_example' # str | Start datetime in ISO 8601 (optional)
end = 'end_example' # str | End datetime in ISO 8601 (optional)

try:
    # Returns historical spot rates for an asset. Requires premium subscription.
    api_response = api_instance.spot_rate_history(symbol, limit=limit, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->spot_rate_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The asset symbol (see /assets) | 
 **limit** | **int**| Number of records to retrieve (default&#x3D;100, max&#x3D;1000) | [optional] 
 **start** | **str**| Start datetime in ISO 8601 | [optional] 
 **end** | **str**| End datetime in ISO 8601 | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spot_rate_ohlcv**
> Empty spot_rate_ohlcv(symbol, limit=limit, interval=interval, start=start, end=end)

Returns the OHLCV history for a spot rate.

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import blockmarkets
from blockmarkets.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = blockmarkets.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = blockmarkets.DefaultApi(blockmarkets.ApiClient(configuration))
symbol = 'symbol_example' # str | The asset symbol (see /assets)
limit = 56 # int | Number of records to retrieve (default=100, max=1000) (optional)
interval = 56 # int | Interval period in minutes. Supported -  1,3,5,15,30,60,1440 (default=1440) (optional)
start = 'start_example' # str | Start datetime in ISO 8601 (optional)
end = 'end_example' # str | End datetime in ISO 8601 (optional)

try:
    # Returns the OHLCV history for a spot rate.
    api_response = api_instance.spot_rate_ohlcv(symbol, limit=limit, interval=interval, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->spot_rate_ohlcv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The asset symbol (see /assets) | 
 **limit** | **int**| Number of records to retrieve (default&#x3D;100, max&#x3D;1000) | [optional] 
 **interval** | **int**| Interval period in minutes. Supported -  1,3,5,15,30,60,1440 (default&#x3D;1440) | [optional] 
 **start** | **str**| Start datetime in ISO 8601 | [optional] 
 **end** | **str**| End datetime in ISO 8601 | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

