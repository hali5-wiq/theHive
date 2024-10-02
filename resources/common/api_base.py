import json
import requests
from jproperties import Properties
from resources.common.helpers.date_maker import DateMaker
from resources.common.helpers.environment_selector import EnvironmentSelector
from resources.common.helpers.file_reader import FileReader
from resources.common.helpers.graphql_shell import GraphQlShell

class ApiBase:

    def __init__(self):
        self._file_reader = FileReader()
        self._api_properties = Properties()
        self._environment_selector = EnvironmentSelector()
        self._date_maker = DateMaker()
        self._graph_ql_shell = GraphQlShell()
        self._protocol = None
        self._port = None
        self._domain = None
        self._endpoint = None
        self._query = ""
        self._version = None
        self._response = None
        self._node = None
        self._headers = {}
        self._body = ""
        self._body_location = ""

    # Getter and setter for _file_reader
    @property
    def file_reader(self):
        return self._file_reader

    @file_reader.setter
    def file_reader(self, value):
        self._file_reader = value

    # Getter and setter for _api_properties
    @property
    def api_properties(self):
        return self._api_properties

    @api_properties.setter
    def api_properties(self, value):
        self._api_properties = value

    # Getter and setter for _environment_selector
    @property
    def environment_selector(self):
        return self._environment_selector

    @environment_selector.setter
    def environment_selector(self, value):
        self._environment_selector = value

    # Getter and setter for _date_maker
    @property
    def date_maker(self):
        return self._date_maker

    @date_maker.setter
    def date_maker(self, value):
        self._date_maker = value

    # Getter and setter for _graph_ql_shell
    @property
    def graph_ql_shell(self):
        return self._graph_ql_shell

    @graph_ql_shell.setter
    def graph_ql_shell(self, value):
        self._graph_ql_shell = value

    # Getter and setter for _protocol
    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        self._protocol = value

    # Getter and setter for _port
    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        self._port = value

    # Getter and setter for _domain
    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value

    # Getter and setter for _endpoint
    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value):
        self._endpoint = value

    # Getter and setter for _query
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value

    # Getter and setter for _version
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    # Getter and setter for _response
    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    # Getter and setter for _node
    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, value):
        self._node = value

    # Getter and setter for _headers
    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    # Getter and setter for _body
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value

    # Getter and setter for _body_location
    @property
    def body_location(self):
        return self._body_location

    @body_location.setter
    def body_location(self, value):
        self._body_location = value

    @body_location.setter
    def body_location(self, body_location):
        self._body_location = body_location

    def modify_first_found_payload_key_value(self, key, value):
        self.body = self.body.replace(key, value, 1)

    def add_body(self, body=None):
        if body is not None:
            self.body = body
        elif self.body_location:
            self.body = self.file_reader.read_file(self.body_location)

    def replace_all_key_value_in_payload(self, key, value):
        self.body = self.body.replace(key, value)

    def _construct_api(self):
        self.protocol = self._api_properties.get("protocol").data
        self.port = self._api_properties.get("port").data
        self.domain = self._api_properties.get("domain").data
        self.endpoint = self._api_properties.get("endpoint").data
        self.query = self._api_properties.get("query").data
        self.version = self._api_properties.get("version").data

    def construct_api(self):
        self._construct_api()
        self.add_body()

    def construct_api_with_body(self, body):
        self._construct_api()
        self.add_body(body)

    def construct_api_with_body_query(self, body, query):
        self._construct_api()
        self.query = query
        self.add_body(body)

    def construct_api_with_query(self, query):
        self._construct_api()
        self.query = query
        self.add_body()

    def call_post_api(self):
        self.response = requests.post(self._get_constructed_api_call(), headers=self.headers, data=self.body)

    def call_post_api_encoder_type(self, enc_type):
        self.response = requests.post(self._get_constructed_api_call(), headers=self.headers, data=self.body.encode(enc_type))

    def call_get_api(self):
        self.response = requests.get(self._get_constructed_api_call(), headers=self.headers, data=self.body)

    def call_patch_api(self):
        self.response = requests.patch(self._get_constructed_api_call(), headers=self.headers, data=self.body)

    def call_get_api_no_headers(self):
        self.response = requests.get(self._get_constructed_api_call(), data=self.body)

    def add_to_headers_list(self, key, value):
        self.headers[key] = value

    def status_code_returned(self, code):
        assert self.status_code == int(code), f"Expected status code {code}, but got {self.status_code}"

    def status_message_returned(self, message):
        assert self.reason == message, f"Expected status message '{message}', but got '{self.reason}'"

    def return_value_by_path(self, path):
        try:
            return self.response.json()[path]
        except KeyError:
            raise KeyError(f"Path '{path}' not found in response JSON: {self.response.json()}")

    def transform_json_payload_to_tree_node(self, payload):
        try:
            self.node = json.loads(payload)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON payload: {e}")

    def convert_pojo_to_json(self, payload):
        try:
            return json.dumps(payload)
        except TypeError as e:
            raise TypeError(f"Object not JSON serializable: {e}")

    def _get_constructed_api_call(self):
        return f"{self.protocol}{self.domain}{self.port}{self.version}{self.endpoint}{self.query}"