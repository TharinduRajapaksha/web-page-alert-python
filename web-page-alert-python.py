import requests
import json


def lambda_handler(event, context):
    ########################### Check web page status and get the HTTP request response code #####################################
    url = 'https://byitholdings.com/' # Default URL if none provide
    response = requests.get(url)
    print(response)
    status_code = response.status_code
    print(status_code)
    
    ############################## Send message to Google Chat webhook #####################################

    webhook_url = "https://chat.googleapis.com/v1/spaces/AAAAlHaneYM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=rammRFetJsfPcv2uXyQVBOxU2bsZwJS11jBzmi127j4"

    webhook_url = "https://chat.googleapis.com/v1/spaces/AAAAlHaneYM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=rammRFetJsfPcv2uXyQVBOxU2bsZwJS11jBzmi127j4"

    if 500 <= status_code < 600:
        message = {
            "message": f"Alert! The web page {url} is down. HTTP Status Code: {status_code}"
        }
        response = requests.post(
        webhook_url,
        data=json.dumps(message),
        headers={'Content-Type': 'application/json'}
        )
    else:
        print("Web page up and running with status code - ",status_code)

