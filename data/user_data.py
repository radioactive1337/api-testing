from data_models.create_user_model import CreateUserModelRequest

#       request data
data = [CreateUserModelRequest(first_name="Иван", last_name="Иванов", company_id=1),
        CreateUserModelRequest(first_name="Petr", last_name="Andreeev", company_id=None)]

invalid_data1 = [CreateUserModelRequest(first_name="Анна", last_name=None, company_id=1)]

invalid_data2 = [CreateUserModelRequest(first_name="Анна", last_name="Иванова", company_id=0)]

invalid_data3 = [CreateUserModelRequest(first_name="Анна", last_name="Иванова", company_id=4)]
