from data_models.user_model import UserModel
from data_models.user_list_model import UserListModel
import random

#   create user
data = [UserModel(first_name="Иван", last_name="Иванов", company_id=1),
        UserModel(first_name="Petr", last_name="Andreeev", company_id=None)]

invalid_data1 = [UserModel(first_name="Анна", last_name=None, company_id=1)]

invalid_data2 = [UserModel(first_name="Анна", last_name="Иванова", company_id=0)]

invalid_data3 = [UserModel(first_name="Анна", last_name="Иванова", company_id=4)]

#   get users list
list_data = [UserListModel(limit=2, offset=0),
             UserListModel(limit=-3, offset=0),
             UserListModel(limit=None, offset=0)]

#   get one user
user_ids = [68, 3012]

invalid_user_ids = [-1, 0, 99999999999]

#   update user
update_data = [(68, UserModel(first_name="Astra", last_name="None", company_id=2)),
               (72, UserModel(first_name="Nobody", last_name="Nothing", company_id=None))]

invalid_update_data = [(0, UserModel(first_name="Astra", last_name="None", company_id=2)),
                       (72, UserModel(first_name="Nobody", last_name="Nothing", company_id=9))]

#   delete user
del_user_id = [random.randint(2000, 3000)]

invalid_del_user_id = [0, 99999999]
