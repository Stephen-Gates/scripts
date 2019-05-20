import json 
import requests 
import pandas as pd

api_token = 'JgkJgW5WePSRRGqwE9uVdbQ2KUpGCJaFhRaK5b5S'
auth_url = 'https://app.leanix.net/services/mtm/v1/oauth2/token' 
request_url = 'https://svc.leanix.net/services/mtm/v1/workspaces/3eb07b2e-7ae1-4388-8a17-618ef89388a8/users?page=0' 

# Get the bearer token - see https://dev.leanix.net/v4.0/docs/authentication
response = requests.post(auth_url, auth=('apitoken', api_token),
                         data={'grant_type': 'client_credentials'})
response.raise_for_status() 
access_token = response.json()['access_token']
auth_header = 'Bearer ' + access_token
header = {'Authorization': auth_header}

# General function to call GraphQL given a query
def call():
  response = requests.get(url=request_url, headers=header)
  response.raise_for_status()
  return response.json()

for user in call()['data']:
  print (user['id'] + " " + user['userName'])

