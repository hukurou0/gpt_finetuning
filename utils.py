from functions import available_functions

# 有効なfunctionが返ってきているかのチェックも行う
def get_function(response_message):
    ############ 引数とかが要件をを満たすかのチェック必要
    try:
        function_name = response_message["function_call"]["name"]
        function_to_call = available_functions[function_name]
        return function_to_call
    except:
        return False