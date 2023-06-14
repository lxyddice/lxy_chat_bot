import openpyxl
import random
import time
import re
import os
from loguru import logger

def read_excel(filename, data):
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active

    for row in sheet.iter_rows(values_only=True):
        if len(row) >= 2:
            key = row[0]
            value = row[1]
            if key in data:
                data[key].append(value)
            else:
                data[key] = [value]

# 创建一个字典来保存所有xlsx文件的数据
all_data = {}

# 添加需要读取的xlsx文件
files = ['1.xlsx', '2.xlsx']

dont_know = ['唔...', '奇怪，突然不想动脑子了！', '诶？什么呢...', '发生什么事了？', '嗯', '什么啦！', '呃...']

# 读取每个文件的数据并合并到all_data字典中
for filename in files:
    read_excel(filename, all_data)

# 创建匹配字典
match_dict = {
    "你在做什么": "你在干什么",
    "想吃掉你" : "吃掉你"
}

logger.success("配置读取完毕")

while True:
    user_input = input('请输入键: ')

    if user_input == "":
        user_input = "再见"

    user_input = re.sub(r"[^\w\s]", "", user_input)

    # 匹配键并替换
    matched_key = match_dict.get(user_input)
    if matched_key:
        user_input = matched_key
    # 在字典中查找并随机输出值
    values = all_data.get(user_input)
    if values:
        random_value = random.choice(values)

        name = "lxy"  # 示例名称
        me = "冰晶"  # 示例个人称呼
        segments = random_value.split("{segment}")

        # 输出上半段
        for i, segment in enumerate(segments):
            segment = segment.replace("{name}", name).replace("{me}", me)
            logger.success(segment, end='', flush=True)  # 不换行输出并立即刷新缓冲区
            if i < len(segments) - 1:
                time.sleep(1.5)  # 等待1.5秒

        # 输出下半段换行
        # print()

    else:
            try:
                # 部分匹配大字典中的键并随机输出5项
                matched_keys = [key for key in all_data.keys() if user_input in key]
                if matched_keys:
                    random_keys = random.sample(matched_keys, min(5, len(matched_keys)))
                    for key in random_keys:
                        values = all_data[key]
                        random_value = random.choice(values)
                        segments = random_value.split("{segment}")

                        # 输出上半段
                        for i, segment in enumerate(segments):
                            segment = segment.replace("{name}", name).replace("{me}", me)
                            logger.success(segment, end='', flush=True)  # 不换行输出并立即刷新缓冲区
                            if i < len(segments) - 1:
                                time.sleep(1.5)  # 等待1.5秒

                        # 输出下半段换行
                        # print()
                else:
                    logger.success('键不存在或对应的值为空')
            except:
                logger.success(random.choice(dont_know))
    if user_input == "再见":
        os.system("pause")
        exit()
