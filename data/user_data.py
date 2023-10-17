from data_models.user_model import UserModel
from data_models.user_list_model import UserListModel

#       request data
data = [UserModel(first_name="Иван", last_name="Иванов", company_id=1),
        UserModel(first_name="Petr", last_name="Andreeev", company_id=None)]

invalid_data1 = [UserModel(first_name="Анна", last_name=None, company_id=1)]

invalid_data2 = [UserModel(first_name="Анна", last_name="Иванова", company_id=0)]

invalid_data3 = [UserModel(first_name="Анна", last_name="Иванова", company_id=4)]

list_data = [UserListModel(limit=2, offset=0),
             UserListModel(limit=-3, offset=0),
             UserListModel(limit=None, offset=0)]
