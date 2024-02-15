import string
import random
from flask import redirect

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for i in range(6))
        return short_url

    def shorten_url(self, long_url):
        if long_url in self.url_mapping.values():
            for short, url in self.url_mapping.items():
                if url == long_url:
                    return short

        short_url = self.generate_short_url()
        while short_url in self.url_mapping:
            short_url = self.generate_short_url()

        self.url_mapping[short_url] = long_url
        return short_url

    def expand_url(self, short_url):
        return self.url_mapping.get(short_url)
