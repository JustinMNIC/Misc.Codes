"""Write a module in which the process_data function takes the path to a json file with data about the site's customers 
(example file in data_hw2.json) and the path to the output json file. 
The process_data function writes statistics to this generic json: the percentage of each age category's audience 0-18-25-45-60+, 
and the percentage of customers who have been online: less than two days, a week, a month, six months, and more than six months ago. 
Put the homework and its tests in a separate hw2 folder. The tests use different json files. 
In workflows, separate jobs for linter tests of different homers, 
separate jobs for tests of different homers (the goal is to have them displayed as separate checkboxes in actions).

{
    "user1": {
        "region": "Saint-Petersburg",
        "registered": "2012-12-24",
        "last_login": "2023-10-01",
        "email": "user@yandex.ru",
        "age": 36
    },
    "user2": {
        "region": "Sochi",
        "registered": "2022-10-30",
        "last_login": "2022-11-21",
        "email": "user2@gmail.com",
        "age": 18
    }
}

"""

import json 
import time

def process_data(json_input_path, json_output_path):
    
    imported_data = json.load(open(json_input_path, "r"))
    
    report = {
        "total_users": len(imported_data),
        "age": {"0-18": 0, "18-25": 0, "25-45": 0, "45-60": 0, "60+": 0},
        "online": {"less than two days": 0, "a week": 0, "a month": 0, "six months": 0, "more than six months": 0}
        }
    for user, user_data in imported_data.items():
        age = user_data["age"]
        if age <= 18:
            report["age"]["0-18"] += 1
        elif age <= 25:
            report["age"]["18-25"] += 1
        elif age <= 45:
            report["age"]["25-45"] += 1
        elif age <= 60:
            report["age"]["45-60"] += 1
        else:
            report["age"]["60+"] += 1
            
        last_login = time.strptime(user_data["last_login"], "%Y-%m-%d")
        current_date = time.strptime(time.strftime("%Y-%m-%d"), "%Y-%m-%d")
        time_difference = time.mktime(current_date) - time.mktime(last_login)
        
        if time_difference <= 2*24*60*60:
            report["online"]["less than two days"] += 1
        elif time_difference <= 7*24*60*60:
            report["online"]["a week"] += 1
        elif time_difference <= 30*24*60*60: # I'm assuming a month has 30 days
            report["online"]["a month"] += 1
        elif time_difference <= 6*30*24*60*60:
            report["online"]["six months"] += 1
        else:
            report["online"]["more than six months"] += 1
    
    for age_category, age_category_count in report["age"].items():
        report["age"][age_category] = age_category_count / len(imported_data) * 100
        
    for online_category, online_category_count in report["online"].items():
        report["online"][online_category] = online_category_count / len(imported_data) * 100
    
    output_statistics = {}
    output_statistics[time.strftime("%d/%m/%Y %H:%M:%S")] = report
    
    try:
        with open(json_output_path, "r") as file:
            data = json.load(file)
            data.update(output_statistics)
        with open(json_output_path, "w") as file:
            json.dump(data, file, indent=4)
    except:
        with open(json_output_path, "w") as file:
            json.dump(output_statistics, file, indent=4)
    
process_data(json_input_path="input_data_hw2.json" , json_output_path="output_data_hw2.json")