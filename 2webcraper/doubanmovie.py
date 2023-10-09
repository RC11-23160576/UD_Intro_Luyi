import requests
import json
import xlwings as xw


if  __name__ == "__main__":

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    url= "https://movie.douban.com/j/chart/top_list"

    movies = input('Please enter the type you want to know:')
    start_num = input("please enter start num:")
    limit_num = input("please enter limit num:")

    param = {
        'type': '3',
        'interval_id': '100:90',
        'action':'',
        'start': start_num,
        'limit': limit_num,
    }

    response = requests.get(url=url, params=param,headers = headers)
    # print(response.text)
    # ps_name = json.loads(response.text).get('ps_name')
    # print('\r\n',ps_name)

    dic_obj = response.json()
    # json_name = json.loads(dic_obj)
    app = xw.App(visible=False,add_book=False)
    wb = app.books.add()
    sht = wb.sheets['Sheet1']

    sht.range('A1').value ='序号'
    sht.range('B1').value ='排名'
    sht.range('C1').value ='名称'
    sht.range('D1').value ='评分'
    sht.range('E1').value ='上映日期'
    sht.range('F1').value ='国家'

    i=1
    for dic_item in dic_obj:
        print('cnt:',i,'title ',dic_item['title'],'\r\n')
        sht.range('A'+str(i+1)).value =i
        sht.range('B'+str(i+1)).value = dic_item['rank']
        sht.range('C'+str(i+1)).value = dic_item['title']
        sht.range('D'+str(i+1)).value = dic_item['rating'][0]
        sht.range('E'+str(i+1)).value = dic_item['release_date']
        sht.range('F'+str(i+1)).value = dic_item['regions'][0]
        i +=1
    wb.save(r'D:\movie.xls')
    wb.close()
    app.quit()
