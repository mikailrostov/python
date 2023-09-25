import json
import requests
import boto3

def extract_gps_data(url):
    # Make a GET request to the GPS data endpoint
    response = requests.get(url)
    
    # Extract the GPS data from the response
    gps_data = json.loads(response.text)

    return gps_data

def supply_to_apigateway(api_endpoint, gps_data):
    # Create an AWS API Gateway client
    apigateway_client = boto3.client('apigateway')
    
    # Prepare the request parameters
    restapi_id = '<Your API Gateway Rest API ID>'
    stage_name = '<Your API Gateway Stage Name>'
    
    # Create a POST request to supply GPS data to API Gateway
    request = {
        'body': json.dumps(gps_data)
    }
    
    # Send the POST request to the API Gateway endpoint
    response = apigateway_client.test_invoke_method(
        restApiId=restapi_id,
        resourceId=api_endpoint,
        httpMethod='POST',
        pathWithQueryString='/{}/{}'.format(stage_name, api_endpoint),
        body=json.dumps(request)
    )
    
    print('API Gateway response:', response)
    
# Define the endpoint URL (replace with your actual endpoint)
endpoint_url = '<Your GPS data endpoint URL>'

# Define the API Gateway endpoint (replace with your actual API Gateway endpoint)
api_gateway_endpoint = '<Your API Gateway endpoint>'

# Extract GPS data
gps_data = extract_gps_data(endpoint_url)

# Supply GPS data to API Gateway
supply_to_apigateway(api_gateway_endpoint, gps_data)
