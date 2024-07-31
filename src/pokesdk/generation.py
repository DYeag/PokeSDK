from .common import *


class Generation:
    base_url: str
    client: requests.Session
    page_limit: int

    def __init__(self, url: str, client: requests.Session, page_limit: int):
        self.base_url = url + 'generation'
        self.client = client
        self.page_limit = page_limit

    def get_info(self, id_or_name: str = None):
        if id_or_name:
            data = get_request(self.client, f'{self.base_url}/{id_or_name}')
        else:
            data = get_paged_request(self.client, f'{self.base_url}', self.page_limit)

        return data