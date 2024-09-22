import json
import os
from typing import Dict


class DistrictNotFoundException(Exception):
    """Exception to be raised if correct district is not provided by user"""

    pass


class DistrictNotProvidedException(Exception):
    """Exception to be raised if district is not provided by user"""

    pass


class MunicipalityNotFoundException(Exception):
    """Exception to be raised if municipality is not found"""

    pass


class NepalMunicipality:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "data", "data.json")
    ALL_MUNICIPALITIES_PATH = os.path.join(
        BASE_DIR, "data", "all_nepal_municipalities.json"
    )

    def __init__(self, district_name: str = None):
        self.municipality_name = None
        self._district_name = district_name
        self._data = self._load_json(self.DATA_PATH)

    @staticmethod
    def _load_json(file_path: str) -> list[Dict]:
        with open(file_path, "r") as f:
            return json.load(f)

    def all_municipalities(self):
        """
        Use this to get list of all municipalities of specific district
        provided from class instance if district is none You will get None as return Value
        """
        if self._district_name is not None:
            for items in self._data:
                if self._district_name in self.all_districts():
                    if items.get(self._district_name) is not None:
                        return items.get(self._district_name)
                else:
                    raise DistrictNotFoundException(
                        "District not found for following text, please check "
                        "district spelling."
                    )
        raise DistrictNotProvidedException(
            "District not provided please provide district name."
        )

    @classmethod
    def municipalities(cls, district_name: str = None):
        """
        Use this method to get a list of all municipalities in a specific district.
        :param district_name: The name of the district. If None, use the instance's district name.
        :return: A list of municipalities in the specified district.
        """
        # Check if this is an instance method call
        if not isinstance(cls, type):
            # This is an instance method call
            district_name = district_name or cls._district_name

        # If district_name is still None, raise the exception
        if district_name is None:
            raise DistrictNotProvidedException(
                "District not provided. Please provide a district name."
            )

        data = cls._load_json(cls.DATA_PATH)
        districts = cls.all_districts()

        if district_name not in districts:
            raise DistrictNotFoundException(
                f"District '{district_name}' not found. Please check the spelling."
            )

        for item in data:
            if district_name in item:
                return item[district_name]

        raise DistrictNotFoundException(
            f"Municipalities for district '{district_name}' could not be found."
        )

    @classmethod
    def all_districts(cls, province_name: str = None) -> list[str]:
        """Use this method to get a list of all districts of Nepal."""
        data = cls._load_json(cls.DATA_PATH)
        muni_data = cls._load_json(cls.ALL_MUNICIPALITIES_PATH)
        all_districts: list = [list(item.keys())[0] for item in data]
        if province_name:
            filtered_entries = [e for e in muni_data if e["province"] == province_name]
            all_districts = list(set([entry["district"] for entry in filtered_entries]))
        return all_districts

    @classmethod
    def districts(cls, province_name: str = None) -> list[str]:
        """Use this method to get a list of all districts of Nepal."""
        data = cls._load_json(cls.DATA_PATH)
        muni_data = cls._load_json(cls.ALL_MUNICIPALITIES_PATH)
        all_districts: list = [list(item.keys())[0] for item in data]
        if province_name:
            filtered_entries = [e for e in muni_data if e["province"] == province_name]
            all_districts = list(set([entry["district"] for entry in filtered_entries]))
        return all_districts

    @classmethod
    def all_data_info(cls, municipality_name: str = None) -> Dict[str, str]:
        """
        Use this method to get the details of a specific municipality, such as its district, province, and province number.
        :param municipality_name: The name of the municipality.
        :return: A dictionary with details about the municipality.
        """
        data = cls._load_json(cls.ALL_MUNICIPALITIES_PATH)

        province_mapping = {
            "Koshi": "Province 1",
            "Madhesh": "Province 2",
            "Bagmati": "Province 3",
            "Gandaki": "Province 4",
            "Lumbini": "Province 5",
            "Karnali": "Province 6",
            "Sudurpashchim": "Province 7",
        }

        for item in data:
            if item["name"].lower() == municipality_name.lower():
                return {
                    "municipality": item["name"],
                    "district": item["district"],
                    "province": item["province"],
                    "province_no": province_mapping.get(item["province"], "Unknown"),
                    "country": item["country"],
                }

        raise MunicipalityNotFoundException(
            f"No matching info for provided municipality '{municipality_name}'. "
            "Please check the spelling or try another name."
        )


if __name__ == "__main__":
    print(NepalMunicipality.all_data_info("Kathmandu"))
