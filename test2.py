import python_http_client
import json
python_http_client.client = python_http_client.Client('138.199.50.138') # IP address of the server
response = python_http_client.client.get('/api/v1/health')
print(json.loads(response.text))