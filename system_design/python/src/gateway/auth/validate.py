import os, requests

'''
Flow:
    - User logs in and gets a JWT token
    - User will start using that JWT token to access our service endpoints
    - This method will verify that JWT token which comes in the header of every request
'''
def token(request):
    if not "Authorization" in request.headers:
        return None, ("Missing credentials to access service!", 401)
    
    token = request.headers["Authorization"]
    if not token:
        return None, ("Missing credentials to access service!!", 401)
    
    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
        headers = {"Authorization": token},
    )

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (f"Error in response: {response.text}", response.status_code)
        