from Infra.Api_wrapper import APIWrapper
from Logic.Utils import *
import os

class Store_Search_API:

    def __init__(self):
        self.my_api = APIWrapper()
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = read_json(os.path.join(cur_dir, "API_Configs", "Store_Search_API.json"))
        self.URL = self._config['url']
        # self.default_params = curr_config['params']


    def prepair_url_params(self, input_):
        params_dict = {}
        for key in input_.keys():
            params = self._config[key]
            params_dict[params] = input_[key]
        return params_dict

    def get_search_result(self, search_term, **extra):
        url = f"{self.URL}?term={search_term}"
        if extra:
            params_dict = self.prepair_url_params(extra)
            url = add_query_Parameters_to_api_request(url, params_dict)
        result = self.my_api.api_get_request(url)
        return result.json()

    def get_names_of_found_serach_apps(self,search_result):
        result = search_result['items']
        ans_ = []
        for app in result:
            ans_.append(app['name'])
        return ans_

    def get_app_id_from_app_details(self,search_result):
        result = search_result['items']
        ans_ = []
        for app in result:
            ans_.append(str(app['id']))
        return ans_



