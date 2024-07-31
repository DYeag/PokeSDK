from .common import *


class Generation:
    base_url: str

    def __init__(self, url) -> None:
        self.base_url = url + 'generation/'