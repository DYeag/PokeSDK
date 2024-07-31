import requests
from .interface import *


def get_request(client: requests.Session, url: str):
    """
    Generic get Request, catches errors, passes on successes
    :return:
    """
    response = client.get(url=url)
    response.raise_for_status()
    return GenericResource(response.json())


def get_paged_request(client: requests.Session, url: str, limit: int):
    """
    Generic get Request with pagionation, catches errors, passes on successes
    :return:
    """
    ret = []
    next_url = f'{url}?limit={limit}&offset=0'

    while next_url:
        response = client.get(next_url)
        response.raise_for_status()

        data = response.json()

        for each in data['results']:
            ret.append(GenericResource(each))
        next_url = data['next']

    return ret
