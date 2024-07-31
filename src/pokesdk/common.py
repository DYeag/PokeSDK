import requests


def get_request(url: str):
    """
    Generic get Request, catches errors, passes on successes
    :return:
    """

    response = requests.get(url=url)
    if response.status_code >= 200 and response.status_code < 300:
        print(f'Good Status Code: {response.status_code}')
    else:
        print(f'Bad Status Code: {response.status_code}')
        print(response.json())

    return response.json()