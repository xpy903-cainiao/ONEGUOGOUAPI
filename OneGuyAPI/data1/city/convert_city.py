import json


def get_city(citys):
    a = ""
    for i in range(3, len(citys)):
        for x in citys:
            id = i
            city_name = x['CityList'][0]['AreaName']
            is_hot = x['CityList'][0]['Grade']
            py_name = x['CityList'][0]['FirstLetter']
            a += "(%s,'%s','%s','%s'),\n" % (id, city_name, is_hot, py_name)
    return a


with open('city.json', encoding='utf-8') as f:
    city_dict = json.load(f)
    all = city_dict['Data']['CityList']
    print(type(all))
    # print(city_dict)

    sql = 'INSERT INTO t_city(city_id,city_name,is_hot,py_name) VALUES '

    a = get_city(all)

    with open('city.sql', 'w', encoding='utf-8') as sql_f:
        sql_f.write(sql + '\n' + a)
