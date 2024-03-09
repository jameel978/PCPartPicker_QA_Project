from Infra.Api_wrapper import APIWrapper
from Logic.Utils import *
import os


class Advanced_search_API:

    def __init__(self):
        self.my_api = APIWrapper()
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = read_json(os.path.join(cur_dir, "API_Configs", "Advanced_search_API.json"))
        self.URL = self._config['url']

    def prepair_api_url(self, search_term):
        search_term = search_term.replace(" ","+")
        return f'{self.URL}?term={search_term}&json=1'

    def prepair_url_params(self, input_):
        params_dict = {}
        for key in input_.keys():
            params = self._config[key]
            if input_[key] == True:
                key = params.split("=")[0]
                val = params.split("=")[1]
                params_dict[key] = val
            else:
                params_dict[params] = input_[key]
        return params_dict

    def get_search_results(self, term, **extra):
        url = self.prepair_api_url(term)
        if extra:
            params_dict = self.prepair_url_params(extra)
            url = add_query_Parameters_to_api_request(url, params_dict)
        result = self.my_api.api_get_request(url)
        return result.json()

    def get_app_ids_from_search_results(self,result):
        items = result["items"]
        id_list = []
        for app in items:
            id_list.append(extract_idf_from_link(app['logo']))
        return id_list
