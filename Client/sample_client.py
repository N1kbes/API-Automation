from requests import request


class SampleClient:
    base_url = "https://api.sampleapis.com/avatar"

    @staticmethod
    def get_avatar(url):
        url = f"{SampleClient.base_url}{url}"
        return request("Get", url)
