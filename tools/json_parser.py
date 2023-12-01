def get_data(keys: list | str, data: dict | list):
    for key in keys:
        try:
            if key in data:
                return data[key]
        except Exception:
            raise Exception(f"there is no data {key}")
    return data





# def get_data(keys: list | str, data: dict | list):
#     for key in keys:
#         try:
#             data = data[key]
#             if data is None:
#                 return {}
#         except Exception:
#             raise Exception(f"there is no data {key}")
#     return data