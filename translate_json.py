import json

def translate(input_json_path, output_json_path):
    input_json = json.load(open(input_json_path))
    output_json = json.load(open(output_json_path))

    output_json['first_slide']['image_path'] = input_json['ProductPhoto']
    output_json['first_slide']['title'] = input_json['ProductName']
    output_json['first_slide']['subtitle'] = input_json['ProductFunc']

    output_json['second_slide']["text_1_2"] = input_json['MarketName']
    output_json['second_slide']["text_2_1"] = input_json['MarketDesc']
    output_json['second_slide']["text_2_2"] = input_json['ProductDesc']

    output_json['third_slide']["text_1"] = input_json['CompetitorsDesc']
    output_json['third_slide']["text_2"] = input_json['ProductUnic']
    output_json['third_slide']["text_3"] = input_json['ProductBest']


    output_json['fourth_slide']["years"]["2020"]["выручка"] = input_json['netprofit2020']
    output_json['fourth_slide']["years"]["2020"]["прибыль"] = input_json['income2020']

    output_json['fourth_slide']["years"]["2021"]["выручка"] = input_json['netprofit2021']
    output_json['fourth_slide']["years"]["2021"]["прибыль"] = input_json['income2021']

    output_json['fourth_slide']["years"]["2022"]["выручка"] = input_json['netprofit2022']
    output_json['fourth_slide']["years"]["2022"]["прибыль"] = input_json['income2022']

    output_json['fourth_slide']["years"]["2023"]["выручка"] = input_json['netprofit2023']
    output_json['fourth_slide']["years"]["2023"]["прибыль"] = input_json['income2023']

    output_json['fourth_slide']["years"]["2024"]["выручка"] = input_json['netprofit2024']
    output_json['fourth_slide']["years"]["2024"]["прибыль"] = input_json['income2024']

    output_json['fifth_slide']["text_1"] = input_json['InvestmentPlans']
    output_json['fifth_slide']["text_2"] = input_json['InvestmentGoal']

    output_json["sixth_slide"]["members"] = {

    input_json['fio1'] : {
            "position": input_json["job1"],
            "experience" : input_json["experience1"]
        },
    input_json['fio2'] : {
            "position": input_json["job2"],
            "experience" : input_json["experience3"]
        },
    input_json['fio3'] : {
            "position": input_json["job3"],
            "experience" : input_json["experience3"]
        },
    input_json['fio4'] : {
            "position": input_json["job4"],
            "experience" : input_json["experience4"]
        },
    input_json['fio5'] : {
            "position": input_json["job5"],
            "experience" : input_json["experience5"]
        },
    }

    output_json["seventh_slide"]["name"] = input_json["AuthorName"]
    output_json["seventh_slide"]["number"] = input_json["AuthorPhone"]
    output_json["seventh_slide"]["email"] = input_json["AuthorEmail"]
    output_json["seventh_slide"]["telegram"] = input_json["AuthorTelegram"]

    return output_json