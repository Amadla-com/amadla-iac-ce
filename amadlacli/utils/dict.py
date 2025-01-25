"""
Amadla cli.

(C) 2024 Jean-Nicolas Boulay Desjardins (JNBD)
Released under MIT License

Dict utils.
"""

import copy
from collections import defaultdict


class DictUtils:
    """
    Dictionary utilities.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def merge_multilevel(d_to: dict, d_from: dict, inplace: bool = False) -> dict:
        """
        Merge two dictionaries and add missing components.
        :param d_to: dictionary
        :param d_from: dictionary
        :param inplace: boolean
        :return: dictionary
        """

        def fn(d_to: dict, d_from: dict):
            """
            Merge two dictionaries and add missing components.
            :param d_to: dictionary
            :param d_from: dictionary
            :return: dictionary
            """
            for k in d_from:
                if k in d_to:
                    if isinstance(d_to[k], dict):
                        d_to[k] = fn(d_to[k], d_from[k])
                else:
                    d_to[k] = d_from[k]
            return d_to

        if inplace:
            return fn(d_to, d_from)
        return fn(copy.deepcopy(d_to), d_from)

    @staticmethod
    def merge_first_level(d1, d2) -> dict:
        """
        Only merge the first level.
        :param d1: dictionary
        :param d2: dictionary
        :return: dictionary
        """
        dd = defaultdict(list)

        for d in (d1, d2):
            """
            Merge the first level of the dictionaries.
            :param d1: dictionary
            :d2: dictionary
            :return: dictionary
            """
            for key, value in d.items():
                if isinstance(value, list):
                    dd[key].extend(value)
                else:
                    dd[key].append(value)
        return dict(dd)

    @staticmethod
    def convert_to_dict_path(a: list | set | dict, schema: str) -> dict:
        """
        Convert list to dictionary.
        :param a: list to convert
        :param schema: schema to add to the dictionary
        :return: dictionary
        """

        def fn(a: list | set | dict) -> dict:
            """
            Recursive function for converting list to dictionary.
            :param a: list to convert
            :return: dictionary
            """
            new_d = {}
            p = ""
            for d in a:
                if len(new_d) == 0:
                    new_d = {d: {}}
                    p = d
                    if len(a) == 1:
                        new_d[d] = {"$schema": schema}
                else:
                    a.remove(p)
                    new_d[p] = fn(a)
            return new_d

        return fn(a)

    @staticmethod
    def binary_search(data: list[dict], search: str, key_name: str = "name"):
        """
        Search inside a list of dictionaries with the binary search algo.
        :param data: list of dictionaries
        :param search: string to search
        :param key_name: key name to search
        :return: index of the search string
        """

        def fn(arr, low, high, x):
            """
            Recursive function for binary search.
            :param arr: list of dictionaries
            :param low: low index
            :param high: high index
            :param x: string to search
            :return: index of the search string
            """

            if high >= low:
                mid = (high + low) // 2

                if arr[mid][key_name] == x:
                    return mid
                elif arr[mid][key_name] > x:
                    return fn(arr, low, mid - 1, x)
                else:
                    return fn(arr, mid + 1, high, x)

            else:
                return -1

        return fn(data, 0, len(data) - 1, search)

    @staticmethod
    def enum_to_dict(enum) -> dict:
        """
        Convert enum to dictionary.
        :param enum: enum
        :return: dictionary
        """
        return {e.name: e.value for e in enum}
