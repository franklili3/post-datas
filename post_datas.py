import datetime
import requests
import pandas as pd
import numpy as np
import pandas as pd
import json

import os
# Initialize variables
last_date_dt = datetime.datetime(2021, 1, 1)  # Example value, replace with actual value
last_date_str = '2021-01-01'  # Example value, replace with actual value

# Initialize logger


home_url = 'https://pocketbase-5umc.onrender.com' #'http://127.0.0.1:8090/'
auth_path = '/api/admins/auth-with-password'
auth_url = home_url + auth_path
username = os.environ.get('admin_username')
#print('admin_username: ', username)

password = os.environ.get('admin_password')
# json.dumps 将python数据结构转换为JSON
data1 = json.dumps({"identity": username, "password": password})
# Content-Type 请求的HTTP内容类型 application/json 将数据已json形式发给服务器
header1 = {"Content-Type": "application/json"}
try:
    response1 = requests.post(auth_url, data=data1, headers=header1)
    if response1.status_code != 200:
        print(f"1 Failed to authenticate: {response1.status_code} - {response1.text}")
        raise Exception("1 Authentication failed")
    response1_json = response1.json()
    response1_str = str(response1_json)
    #print('html: ', html)
    #print('response1_str: {}'.format(response1_str[0:100]))
    # html.json JSON 响应内容，提取token值
    if response1_json['token']:
        token = response1_json['token']
except Exception as e:
    print(f"An error occurred: {e}")
    raise
header2 = {
    "Content-Type": "application/json",
       "Authorization": token
}

post_path2 = '/api/collections/bitcoin_strategy_backtest_cn_stock_performance/records'
bitcoin_strategy_backtest_cn_stock_performance = pd.read_csv("bitcoin_strategy_backtest_cn_stock_performance.csv")
for index, row in bitcoin_strategy_backtest_cn_stock_performance.iterrows():

    row_json2 = row.to_json()
    print('row_json: ', row_json2)
    row_json2_split = row_json2.split('}')
    data2 = row_json2_split[0] + '}'
    print('data2: ', data2)
    post_url = home_url + post_path2
    response2 = requests.post(post_url, headers=header2, data=data2)
    response2_json = response2.json()
    if response2.status_code == 200:
        print('post data success.')
    else:
        print(f"2 Failed to authenticate: {response2.status_code} - {response2.text}")
        raise Exception("2 Authentication failed")
'''
post_path3 = '/api/collections/bitcoin_strategy_backtest_cn_stock_performance/records'
bitcoin_strategy_backtest_cn_stock_performance = pd.read_csv("bitcoin_strategy_backtest_cn_stock_performance.csv")
for index, row in bitcoin_strategy_backtest_cn_stock_performance.iterrows():

    row_json3 = row.to_json()
    #print('row_json: ', row_json)
    row_json3_split = row_json3.split('}')
    data3 = row_json3_split[0] + '"}'
    #print('data: ', data)
    post_url = home_url + post_path3
    response3 = requests.post(post_url, headers=header2, data=data3)
    response3_json = response3.json()
    if response3.status_code == 200:
        logger.info('post data success.')
        print('post data success.')
    else:
        logger.error(f"3 Failed to authenticate: {response3.status_code} - {response3.text}")
        print(f"3 Failed to authenticate: {response3.status_code} - {response3.text}")
        raise Exception("3 Authentication failed")

post_path4 = '/api/collections/bitcoin_strategy_backtest_cn_stock_performance/records'
bitcoin_strategy_backtest_cn_stock_performance = pd.read_csv("bitcoin_strategy_backtest_cn_stock_performance.csv")
for index, row in bitcoin_strategy_backtest_cn_stock_performance.iterrows():

    row_json4 = row.to_json()
    #print('row_json: ', row_json)
    row_json4_split = row_json4.split('}')
    data4 = row_json4_split[0] + '"}'
    #print('data: ', data)
    post_url = home_url + post_path4
    response4 = requests.post(post_url, headers=header2, data=data4)
    response4_json = response4.json()
    if response4.status_code == 200:
        logger.info('post data success.')
        print('post data success.')
    else:
        logger.error(f"4 Failed to authenticate: {response4.status_code} - {response4.text}")
        print(f"4 Failed to authenticate: {response4.status_code} - {response4.text}")
        raise Exception("4 Authentication failed")
'''