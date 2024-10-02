from getgauge.python import step
from resources.common.api_base import ApiBase
from getgauge.python import data_store

class ApiBaseSteps(ApiBase):

    @step("I get a response message of: <message>")
    def status_message_returned(message):
        ApiBase.status_message_returned(data_store.scenario.response, message)

    @step("Then I expect a status code of: <code>")
    def status_code_returned(code):
        ApiBase.status_code_returned(data_store.scenario.response, code)