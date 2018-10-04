import requests
import json

def get_recipe(cuisine):
    var_app_id = "dea5ff13"
    var_app_key = "3decd4e9347b4079ac601797ae8c2a66"

    search_key_word = cuisine
    var_from = "0"
    var_to = "10"
    
    # final_res = {}
    res = []

    response = requests.get('https://api.edamam.com/search?q='+search_key_word+'&app_id='+var_app_id+'&app_key='+var_app_key+'&from='+var_from+'&to='+var_to)
    jsonified_response = json.loads(response.text)
    # print(response.json())

    res.append(jsonified_response["hits"][1]["recipe"]["label"])
    res.append(jsonified_response["hits"][1]["recipe"]["shareAs"])
    res.append(jsonified_response["hits"][1]["recipe"]["calories"])
    res.append(jsonified_response["hits"][1]["recipe"]["ingredientLines"])


    # for i in range(0, 6):
    #     final_res.update({
    #             "Recipe "+str(i+1) :  jsonified_response["hits"][i]["recipe"]["shareAs"],
    #             "Recipe "+str(i+1) :  jsonified_response["hits"][i]["recipe"]["ingredientLines"]

    #     })
    return res
