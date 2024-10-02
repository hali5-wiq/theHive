from getgauge.python import step
from resources.sample.canary.canary_api import CanaryApi
from getgauge.python import data_store

@step("Call canary get api")
def call_canary_get_api():
    ca = CanaryApi()
    ca.canary_test_get()
    data_store.scenario.response = ca.response