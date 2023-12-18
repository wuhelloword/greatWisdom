import time
from datetime import datetime, timedelta
from matplotlib import pyplot as plt

def get_max(num_list, operator):
    """
    筛除None值返回列表中的最大值
    :param num_list:
    :param operator: 如果是>,则求列表的最大值，如果是<则求列表的最小值
    :return:
    """
    result = None
    for i in num_list:
        if isinstance(i, (float, int)):
            if result is None:
                result = i
            if operator == ">":
                if i > result:
                    result = i
            if operator == "<":
                if i < result:
                    result = i
    return result

def get_date():
    """获取当天往前31天的日期"""
    # 获取当前日期
    current_date = datetime.now().date()
    current_date = datetime.now().replace(microsecond=0).date()
    print(current_date)
    # 获取近30天的日期
    dates = [current_date - timedelta(days=i) for i in range(31)]
    datas = dates[::-1]
    for i in datas:
        print(i)


def get_time():
    """获取当前时间往前24小时"""
    s = datetime.now().hour
    l = []
    # l = [for i in range(s, s+24)]
    for i in range(s - 1, s + 23):
        # print(i % 24)
        l.insert(-1, i % 24)
    print(l)

def get_not_digitar():
    import re
    result = re.findall(r"[^0123456789.]", '1h2.0')
    print(result)

def format_time():
    print(datetime.now().strftime("%#m.%d"))


def shabebe():
    import requests

    # try:
    result = requests.get(url='http://10.197.24.123:8000/Wins/jiaban/?id=F1241948')
    print(result.status_code)
    print(result.content.decode('utf-8'))
        # time.sleep(2)
    # except:
    #     pass

# class CommonFlag(object):
#     """
#     ui参数，将选项的字符串值根据逻辑转为Bool类型
#     """
#     if_fa = None
#     delete_retest = None
#     ui_apple_pass = None
#
#     @classmethod
#     def set_flag(cls, ui_param: UiParam):
#         if cls.if_fa is None or cls.delete_retest is None or cls.ui_apple_pass is None:
#             _check_value = lambda v, key_value: isinstance(v, str) and v.lower() == key_value
#             if _check_value(ui_param.re_test_data, 'no'):
#                 cls.delete_retest = True
#                 cls.if_fa = False
#             elif _check_value(ui_param.re_test_data, 'all'):
#                 cls.delete_retest = False
#                 cls.if_fa = False
#             else:
#                 cls.delete_retest = False
#                 cls.if_fa = True
#
#             if _check_value(ui_param.apple_pass, 'y'):
#                 cls.ui_apple_pass = True
#             else:
#                 cls.ui_apple_pass = True
#
#     @classmethod
#     def get_time_distance(cls, ui_param: UiParam):
#         """
#         @note: This is for FA situation, which won't be used that much
#         """
#         if ui_param.keep_fa_time:
#             return ui_param.keep_fa_time * 3600
#         else:
#             cls.if_fa = False
#             msg = "U had chosen FA, but forgot to fill in the FA Time..."
#             print(msg + ' then the if_fa  is set to False !')
#             MessagePushServer.gui_print(msg, color='black')




if __name__ == '__main__':
    pass
    # print(get_max([None, 1, 3, 2], "<"))
    # get_date()
    # get_time()
    # shabebe()



    # 创建一个带有单个值的数据
    x = [0]  # x 坐标值
    y = [5]  # y 坐标值

    # 绘制点
    plt.plot(x, y, marker='o')

    # 显示图形
    plt.show()







