# lxy
简单的机器人对话

<code>pip install openpyxl</code>

使用数据库为[强大的二次元聊天机器人词库2W+词条(不定期更新)](https://mirai.mamoe.net/topic/1829/%E5%BC%BA%E5%A4%A7%E7%9A%84%E4%BA%8C%E6%AC%A1%E5%85%83%E8%81%8A%E5%A4%A9%E6%9C%BA%E5%99%A8%E4%BA%BA%E8%AF%8D%E5%BA%932w-%E8%AF%8D%E6%9D%A1-%E4%B8%8D%E5%AE%9A%E6%9C%9F%E6%9B%B4%E6%96%B0?_=1686707986321)
需要把xls转换/重写到xlsx文件，否则无法读取

模糊匹配

手动设置强制替换

<code>match_dict = {
    "你在做什么": "你在干什么",
    "想吃掉你" : "吃掉你"
}</code>

无键随机返回失败语句

<code>dont_know = ['唔...', '奇怪，突然不想动脑子了！', '诶？什么呢...', '发生什么事了？', '嗯', '什么啦！']</code>

改一改就能接入一些bot的聊天了
