from .common import *


class Pokemon:
    base_url: str

    def __init__(self, url) -> None:
        self.base_url = url + 'pokemon/'

    def get_info(self, id_or_name):
        data = get_request(f'{self.base_url}{id_or_name}')
        print(data)

    def get_location_areas(self, id_or_name):
        data = get_request(f'{self.base_url}{id_or_name}/encounters')
        print(data)
