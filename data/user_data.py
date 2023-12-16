from data_models.user_model import UserModelRequest
from data_models.user_list_model import UserListModelRequest
import random

#   create user
data = [UserModelRequest(first_name="Иван", last_name="Иванов", company_id=1),
        UserModelRequest(first_name="Petr", last_name="Andreeev", company_id=None)]
invalid_data1 = [UserModelRequest(first_name="Анна", last_name=None, company_id=1)]
invalid_data2 = [UserModelRequest(first_name="Анна", last_name="Иванова", company_id=0)]
invalid_data3 = [UserModelRequest(first_name="Анна", last_name="Иванова", company_id=4)]

#   get users list
list_data = [UserListModelRequest(limit=2, offset=0),
             UserListModelRequest(limit=-3, offset=0),
             UserListModelRequest(limit=None, offset=0)]

#   get one user
invalid_user_ids = [-1, 0, 999999999999]

#   update user
update_data = [(data[0], UserModelRequest(first_name="Astra", last_name="None", company_id=2)),
               (data[1], UserModelRequest(first_name="Nobody", last_name="Nothing", company_id=None))]
invalid_update_data = [(data[0], UserModelRequest(first_name="Astra", last_name=None, company_id=2)),
                       (data[1], UserModelRequest(first_name="Nobody", last_name="Nothing", company_id=9))]
invalid_update_data2 = [(0, UserModelRequest(first_name="Astra", last_name="None", company_id=2)),
                        (99999999, UserModelRequest(first_name="Nobody", last_name="Nothing", company_id=None))]
#   delete user
del_user_id = [random.randint(2000, 3000)]
invalid_del_user_id = [0, 99999999]
