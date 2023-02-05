# import abc
# from dataclasses import dataclass, field
# from typing import Any
#
# from algoliasearch_django import raw_search
#
#
# @dataclass
# class SearchAdapter:
#     search_terms: str
#
#     @abc.abstractmethod
#     def execute(self):
#         ...
#
#
# @dataclass
# class SearchOilGasAdapter(SearchAdapter):
#     model: Any
#     params: dict = field(default_factory=dict)
#
#     def execute(self):
#         response = raw_search(self.model, self.search_terms, self.params)
#         return response
