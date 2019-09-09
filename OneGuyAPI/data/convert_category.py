# import json
#
# def get_category(categorys):
#     sub_str = ''
#     for category in all_category:
#         id = category['CategoryId']
#         code = category['CategoryName']
#         if name == '全部':
#             continue
#         name = category['Grade']
#         picture_pul = category['PictureUrl']
#         parent_id = category['PriorID']
#
#         sub_str += "('%s','%s','%s',%s,'%s','%s'),\n"%(id,name,code,grade,picture_url,parent_id)
#
#
#         if category['Childs']:
#             sub_str += get_category(category['Childs'])
#
#     return sub_str
#
#
# with open('category.json') as f:
#     catgory_dict = json.load(f)
#     all_category = catgory_dict['Data']['CategoryList']
#     sql = 'insert into t_category(id,code,name,.,.,.) values'
#     sub_str = get_category(all_category)
#     with open('category.sql','w',encoding='utf-8') as sql_f:
#         sql.write()
