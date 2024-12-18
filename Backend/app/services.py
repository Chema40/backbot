import requests
from app.config import settings

def contact_method():
    try:
        response = requests.get(settings.contact_method_url)
        api_response = response.json()
    
    except requests.RequestException as e:
        print(f"Error contacting backend: {str(e)}")
    
    return response.status_code, api_response
