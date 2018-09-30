
# ---coding:utf-8---
import decimal
import sys
import os
import base64
import subprocess
import random
from robot.api import logger
from rediscluster.client import StrictRedisCluster

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import *
import string
import yaml
reload(sys)

sys.setdefaultencoding('utf8')


#
# def get_sum_of_list(list_):
#     float_sum = 0.00
#     for index in list_:
#         float_index = float(index)
#         float_sum += float_index
#     return decimal.Decimal('%0.2f' % float_sum)
#
#
#
# aa = get_sum_of_list([1.114,2.2222])
# print(aa)




# def return_random():
#     random_value = random.randint(100000000, 199999999)
#     return random_value
#
# aa = return_random()
# print(aa)



# def remove_comma(list_):
#     return_list = []
#     for index in list_:
#         index_re1 = index.replace(',', '')
#         index_re1 = index_re1.replace('¥', '')
#         return_list.append(index_re1)
#     return return_list
#
# aa = remove_comma(["1,234.00¥","22.0¥"])
# print(aa)

# def remove_comma_string(arg_str):
#     arg_str = str(arg_str)
#     arg_str1 = arg_str.replace(',', '')
#     arg_str1 = arg_str1.replace('¥', '')
#     arg_str1 = arg_str1.replace('￥', '')
#     float_return = float(arg_str1)
#     return decimal.Decimal('%0.2f' % float_return)
#
# aa = remove_comma_string('1,234.1155¥￥')
# print(aa)

# def remove_special_char_string(str_):
#     str1 = str_.replace('@', '')
#     str2 = str1.replace('&', '')
#     return str2
#
# aa = remove_special_char_string("abd@dd&eeff")
# print (aa)

# def remove_special_char(str_, remove_char):
#     str1 = str_.replace(remove_char, '')
#     return str1
#
# aa = remove_special_char("d@f#4$6%7*8+","+")
# print(aa)
#
# def correct_verify_code_format(s):
#     arg1 = s.replace('><', 'X')
#     arg2 = arg1.replace(']', 'J')
#     arg3 = arg2.replace('$', 'S')
#     arg4 = arg3.replace('\/', 'V')
#     arg5 = arg4.replace('’', '')
#     return arg5.replace(' ', '')

# aa = correct_verify_code_format("aa><]$\/’w w w")
# print(aa)
#
# def construct_locator_var(locator, *args):
#     """This is an alternative solution for constructing the dynamic locators
#     args can accept multiple values.
#     locator-dynamic locator that contains the variables as <var>
#     """
#     if locator is None:
#         raise AssertionError("Cannot construct the full locator when the input locator not exist")
#     try:
#         for each in args:
#             locator = locator.replace('<var>', str(each), 1)
#     except StandardError:
#         raise StandardError("Please provide the parameters needed")
#     return locator
#
#
# aa = construct_locator_var("da<var>",["bb","cc",11,22])
# print(aa)

#
# def find_substring(full_str, sub_str):
#     index = full_str.find(sub_str)
#     if index == -1:
#         return 'False'
#     else:
#         return 'True'
#
# aa = find_substring("ajkdshjahsdhfaks","ash")
# print(aa)

#
# def element_in_list(list_, value):
#     if value in list_:
#         return 'True'
#     else:
#         return 'False'
#
# aa = element_in_list([1,2,3,4,"a","b"],"aa")
# print (aa)

# def get_average_of_list(list_number):
#     sum_ = 0
#     for i in list_number:
#         sum_ += i
#     average = sum_ / len(list_number)
#     return average
#
# aa = get_average_of_list([4,4.9,5,7,8])
# print(aa)
#
# def convert_to_float_currency(arg1):
#     return_float = float(arg1)
#     return decimal.Decimal('%0.2f' % return_float)
#
# aa = convert_to_float_currency("1.2356333")
# print(aa)
#
#
# def get_type(arg0):
#     if arg0 is not None:
#         return_type = type(arg0)
#         print str(return_type)[7:-2]
#     else:
#         return 'none'
#
# aa = get_type({"ss":"sss"})
# #print(aa)

#
# def remove_space(arg_str):
#     arg_str = str(arg_str)
#     arg1 = arg_str.replace(' ', '')
#     return arg1
#
# aa = remove_space("aa dd ff gg kk")
# print (aa)


#
# def get_random_int(lower_int, upper_int):
#     return random.randint(int(lower_int), int(upper_int))
#
# aa = get_random_int(1,10)
# print(aa)


#
# def remove_quotation_mark(arg_str):
#     return_str = str(arg_str)
#     return_str = return_str.replace('"', '')
#     return_str = return_str.replace('“', '')
#     return return_str
#
# aa = remove_quotation_mark('aaass“素素”"ss"')
# print(aa)

#
# def get_lists_minus(arg_list_more, arg_list_less):
#     return list(set(arg_list_more).difference(set(arg_list_less)))
#
# aa = get_lists_minus([11,22,33,44,55,66,77],[22,33,66,99])
# print(aa)

# def validate_currency_format(arg_string):
#     currency_symbol_1 = '￥'
#     # currency_Symbol_2 = '¥'
#     currency_symbol_1 = currency_symbol_1.decode('utf-8')
#     arg_string = arg_string.decode('utf-8')
#     if str(arg_string[0]) != str(currency_symbol_1):
#         logger.info("this is invalid currency symbol", True, False)
#         raise AssertionError("this is invalid currency symbol :" + arg_string[0])
#     else:
#         print(str(arg_string[0]))
#         print (str(currency_symbol_1))
#     number_arg_string = arg_string[1:]
#     if type(eval(number_arg_string)) != type(1.00):
#         raise AssertionError("this is invalid currency number type :" + number_arg_string)
#     else:
#         print(eval(number_arg_string))
#         print(type(eval(number_arg_string)))
#         print(type(1.00))
#     if arg_string[-3] != '.':
#         raise AssertionError("this is invalid currency number value :" + number_arg_string)
#
# aa = validate_currency_format("￥111.22+11.00")
# print (aa)

#
# def sort_list_by_dict_value(list_, dict_key):
#     return sorted(list_, key=lambda dic: dic[dict_key])
#
# aa = sort_list_by_dict_value([("a",11),("s",3),("d",12),("f",7)],1)
# print(aa)

#
# def convert_base64_to_image(path, base_code):
#     img_data = base64.b64decode(base_code)
#     path = path + 'code.jpg'
#     file = open(path, 'wb')
#     file.write(img_data)
#     file.close()
#     return path
#
# aa =  convert_base64_to_image("E:\SoftWare\JetBrains\PycharmProjects\\",r"ztLKx9fWt/u0rg==")
# print(aa)

#
# def image_to_string(img, cleanup, plus=''):
#     # cleanup为True则识别完成后删除生成的文本文件
#     # plus参数为给tesseract的附加高级参数
#     subprocess.check_output('tesseract ' + img + ' ' +
#                             img + ' ' + plus, shell=True)  # 生成同名txt文件
#     text = ''
#     cleanup = cleanup.encode('utf-8')
#     with open(img + '.txt', 'r') as f:
#         text = f.read().strip()
#         text = correct_verify_code_format(text)
#     if cleanup == 'True':
#         os.remove(img + '.txt')
#         os.remove(img)
#     print(text.path())
#     return text
# aa = image_to_string("aaa",False)

#
# def get_sms_code(mobile, env='qa2', mode='r'):
#     # env值 qa2为test环境 stage为stage环境；mode值 r为注册手机号码获取验证码 f为找回密码获取验证码
#     if env.lower() != 'qa2' and env.lower() != 'stage':
#         return None
#     if mode.lower() != 'r' and mode.lower() != 'f' and mode.lower() != 'm':
#         return None
#     if mode == 'r':
#         sms_mode = 'SOA:MYACCOUNT:SMSCODE:1001:' + mobile
#     elif mode == 'f':
#         sms_mode = 'SOA:MYACCOUNT:SMSCODE:1002:' + mobile
#     elif mode == 'm':
#         sms_mode = 'SOA:MYACCOUNT:SMSCODE:1005:' + mobile
#     if env.lower() == 'qa2':
#         # Set redis db to QA2
#         redis_db = [{'host': '10.157.26.84', 'port': 6379}, {'host': '10.157.26.85', 'port': 6379},
#                     {'host': '10.157.26.86', 'port': 6379}, {'host': '10.157.26.87', 'port': 6379},
#                     {'host': '10.157.26.88', 'port': 6379}]
#     else:
#         # Set redis db to Stage
#         redis_db = [{'host': '10.157.24.45', 'port': 6379}, {'host': '10.157.24.46', 'port': 6379},
#                     {'host': '10.157.24.47', 'port': 6379}, {'host': '10.157.24.54', 'port': 6379},
#                     {'host': '10.157.24.55', 'port': 6379}]
#     try:
#         redisconn = StrictRedisCluster(startup_nodes=redis_db)
#         print redisconn.mget(smscode)
#         sms = redisconn.mget(sms_mode)
#         if sms[0]:
#             sms = filter(lambda ch: ch in '0123456789', sms[0])
#             return sms
#         else:
#             print
#             'can not find smscode'
#             return 'can not find smscode'
#     except Exception as e:
#         print
#         "Connect Redis node error:", e
#
#         # print get_Type(34)
#         # print test_string('javascript:this.src='/_ui/desktop/theme-blue/images/nopic-178-242.jpg';')
# aa = get_sms_code('18817943321',"stage","r")
# print(aa)

# def convert_yml_to_dict(filename):
#     f = open(filename)
#     y = yaml.load(f)
#     return y
#
# aa = convert_yml_to_dict("E:\SoftWare\JetBrains\PycharmProjects\RobotFramework\yml.yml")
# print(aa)


def compare_sub_dicts(dict_mast, dict_sub):
    result = True
    for key in dict_sub:
        if dict_sub[key] != dict_mast[key]:
            result = False
    return result


def compare_sub_dicts2(dict_mast, dict_sub):
    print (dict_mast)
    dict_mast_str = str(dict_mast)
#    dict_mast_str = dict_mast_str.replace("null","None")
#    dict_mast = eval(dict_mast_str)
    print (dict_mast_str)
    result = True
    for key in dict_sub:
        print(type(dict_sub[key]),dict_sub[key],type(dict_mast[key]),dict_mast[key])
        if dict_sub[key] != dict_mast[key]:
            result = False
    print(result)
    return result


