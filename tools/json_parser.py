def get_data(keys: list | str, data: dict | list):
    # body = data
    for key in keys:
        try:
            data = data[key]
            if data is None:
                return {}
        except Exception:
            raise Exception(f"there is no data {key}")
    return data
