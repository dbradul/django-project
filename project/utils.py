import requests
import json


def format_records(lst):
    if len(lst) == 0:
        return 'Emtpy recordset'
    return '<br>'.join(str(elem) for elem in lst)


def email_validator(email):
    url = 'https://api.usebouncer.com/v1/email/verify'
    api_key = 'spLNRJEwMS8Q1vQm9JkDRhYs2AldHVWZwqpbugWC'

    params = {'email': email, 'timeout': 10}
    headers = {'x-api-key': api_key}

    response = requests.get(url, params=params, headers=headers)
    response = json.loads(response.content)
    print(response)
    try:
        if response['status'] == 'deliverable':
            return True
    except Exception:
        pass
    return False
