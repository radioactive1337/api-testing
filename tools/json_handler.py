import json


class JsonHandler:
    def update_json(self, json_data, key, new_value):
        if isinstance(json_data, dict):
            for k, v in json_data.items():
                if k == key:
                    json_data[k] = new_value
                elif isinstance(v, (dict, list)):
                    self.update_json(v, key, new_value)
        return json.dumps(json_data)

    def get_value_by_key(self, key, input_dict):
        if not isinstance(input_dict, dict):
            return "Error: input object is not a dict"
        for k, v in input_dict.items():
            if k == key:
                return v
            elif isinstance(v, (dict, list)):
                result = self.get_value_by_key(key, v)
                if result is not None:
                    return result
        return f"Error: Key '{key}' is not found"
