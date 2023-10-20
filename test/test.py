import time
from datetime import datetime, timedelta

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



if __name__ == '__main__':
    pass
    # print(get_max([None, 1, 3, 2], "<"))
    # get_date()
    # get_time()
    shabebe()







