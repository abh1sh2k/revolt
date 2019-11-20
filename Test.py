import json
if __name__ == "__main__":
    with open('input.json', 'r') as content_file:
        content = content_file.read()
        read_json = json.loads(content)
        whole_json = {}
        for js in read_json:
            country = js["country"]
            city = js["city"]
            currency = js["currency"]
            amount = js["amount"]
            #print city , country , amount , currency
            city_json = [{'amount': amount}]

            if not currency in whole_json:
                whole_json[currency] = {}
            if not country in whole_json[currency]:
                whole_json[currency][country] = {}
            if not city in whole_json[currency][country]:
                whole_json[currency][country][city] = {}

            whole_json[currency][country][city]= city_json
        new_json = json.dumps(whole_json)
        print new_json
