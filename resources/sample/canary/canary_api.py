from resources.common.api_base import ApiBase

class CanaryApi(ApiBase):

    def __init__(self):
        super().__init__()  # Initialize the parent class
        with open("resources\\sample\\canary\\canary.properties", 'rb') as read_prop:
            self._api_properties.load(read_prop)
        self.add_to_headers_list("Content-Type", self._api_properties.get("Content-Type").data)

    def canary_test_get(self):
        self.construct_api()
        self.call_get_api()