import json

def get_category(categorys):
    sub_str = ""
    for category in categorys:
        id = category['CategoryId']
        code = category['CategoryCode']
        name = category['CategoryName']
        if name == '全部':
            continue

        grade = category['Grade']
        picture_url = category['PictureUrl']
        parent_id = category['PriorId']

        sub_str += "('%s','%s','%s',%s,'%s','%s'),\n"%(id,name,code,grade,picture_url,parent_id)
        if category['Childs']:
            sub_str += get_category(category['Childs'])

    return sub_str


with open('category.json') as f:
    category_dict = json.load(f)
    all_category = category_dict['Data']['CategoryList']
