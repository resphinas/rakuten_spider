# -*- coding: utf-8 -*-
"""
@Time ： 2022/1/7 14:30
@Auth ： wes
@File ：run.py
@IDE ：PyCharm
@email：2934218525@qq.com

"""
import time
import json
import re
import random
from tqdm import tqdm
import requests
import jsonpath
import utility.headers_config
from utility.generate_headers import change_headers_tool
from utility.tools import save_json_file,load_json_file
import csv
import utility
from fake_useragent import UserAgent
import json

COOKIES = """IS_CONNECTED=false; devdee=eyJhbGciOiJIUzM4NCJ9.eyJEZXZpY2VUb2tlbiI6IjVkNTQyM2M4MzExNjRmMzA5NjNiYjEzOGE4ZTM0OWQ0MTY0NjcwNzYxMjUwOSJ9.69_6PhXPk_YD_scvVlzeaJfkhDR8GTT1uuul2uV6s4CC_kAYJt-S3NPHoetQg2v6; pmcookies=0b23f9c0-eeb5-40d2-b8c1-7a9faacae89b; pm=country=249&trackingdate=2022-03-08+03:46:51.0&version=1_1; _mall_uuid=0b23f9c0-eeb5-40d2-b8c1-7a9faacae89b; atuserid={"name":"atuserid","val":"8de31e3e-2de1-42e3-8914-ac44303038a4","options":{"end":"2023-04-09T02:47:01.708Z","path":"/"}}; _#uid=1646707622519.888305223.7515187.5791.255391469.469; _#sess=1|20220308031702|1; _#srchist=62250:1:20220408024702; _#vdf=62250|1|20220408024702; pm_cnil_optin={"cnilopt":1}; didomi_token=eyJ1c2VyX2lkIjoiMTdmNjc2YzMtZGVhOC02MDM3LTlkZjUtZDNhYWY2ZjVhNmM0IiwiY3JlYXRlZCI6IjIwMjItMDMtMTBUMDE6NDY6MTguNTEwWiIsInVwZGF0ZWQiOiIyMDIyLTAzLTEwVDAxOjQ2OjE4LjUxMFoiLCJ2ZXJzaW9uIjoyLCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbImF1ZGllbmNlbS14ZWRlVTJnUSIsImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiLCJnZW9sb2NhdGlvbl9kYXRhIl19LCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpTSmVwYktqRzciLCJjOmNvbnRlbnRzcXVhcmUiLCJjOnRmMS1kaWdpdGFsLWZhY3RvcnkiLCJjOmZyYW5jZXR2LWZGcDN5VVhwIiwiYzppbnRvemV3ZS1XZlUyeHQ0TCIsImM6dGlueWNsdWVzLTNLaHBZTjZrIiwiYzp0d2VuZ2F0Y2YtMlh0UXdoV2YiLCJjOnBlcnNvbmFsaS1VRHpSQzJKbSIsImM6cmF0dGNmdjIteTZWTFgyUW4iLCJjOmF0aW50ZXJuZS1jV1FLSGVKWiIsImM6aGV5ZGF5LWFDcTRtTDJBIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIl19LCJhYyI6IkM2cUFHQUZrQW93THFnQUEuQzZxQUVBVVlGMVFBIn0=; euconsent-v2=CPVnHsAPVnHsAAHABBENCECsAP_AAH_AAAAAIltf_X__b3_j-_5_f_t0eY1P9_7_v-0zjhfdt-8N3f_X_L8X42M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6okVrzPsbk2cr7NKJ7PEmnMbO2dYGH9_n93TuZKY7______z_v-v_v____f_7-3_3__5_3---_e_V_99zLv9____39nP___9v-_9_____4IhgEmGpeQBdiWODJtGlUKIEYVhIdAKACigGFoisIHVwU7K4CfUELABCagIwIgQYgowYBAAIBAEhEQEgB4IBEARAIAAQAqwEIACNgEFgBYGAQACgGhYgRQBCBIQZHBUcpgQESLRQT2ViCUHexphCGWWAFAo_oqEBEoQQLAyEhYOY4AkBLhZIFmKF8gAAAAA.f_gAD_gAAAAA; _gcl_au=1.1.314531195.1646876779; __troRUID=d2c3fb02-8657-48ca-9faf-9105638ea07a; tinytrckr=r4wdzfslknswo96k4o4bc; atauthority={"name":"atauthority","val":{"authority_name":"default","visitor_mode":"optin"},"options":{"end":"2023-04-11T01:46:28.595Z","path":"/"}}; atidvisitor={"name":"atidvisitor","val":{"vrn":"-104628--104630-"},"options":{"path":"/","session":15724800,"end":15724800}}; rak_byr_prsnli=8107c88d-e4da-41ad-9c6b-457cdded3ab5; rgpd={"loadAds":false,"loadTracking":false,"loadCustomization":false}; _ra=1646883311772|e0fc7abb-d544-4027-b665-b2417bbc9aec; netotiate_vid=622971f01a9cb; _cs_c=3; _ga=GA1.2.870631674.1646899030; _fbp=fb.1.1647240365117.2112015572; tag_capping=true; __gads=ID=3fb64949d1f77366:T=1646876780:S=ALNI_MaBxSvnZxlsH5dbdZsM2y5_dwfscw; __troSYNC=1; mics_vid=26131369532; mics_lts=1648014436260; rak_land_91=1; kameleoonVisitorCode=_js_rduxkk092yo4a7x7; __trossion=1646876780_1800_18_d2c3fb02-8657-48ca-9faf-9105638ea07a:1648035261_d2c3fb02-8657-48ca-9faf-9105638ea07a:1648041190_1648041190_1_; _cs_id=633618f0-0723-a061-efa3-2c963eb12adf.1646876780.18.1648041191.1648041191.1.1681040780676; _cs_s=1.0.0.1648042991319; QueueITAccepted-SDFrts345E-V3_prodfullsite=EventId=prodfullsite&QueueId=00000000-0000-0000-0000-000000000000&RedirectType=disabled&IssueTime=1648041193&Hash=6edbb6ec2d979a6d4fc0bd1ea18b01ea0fb74fac1103e2b429dc781f3483e04a; cto_bundle=iz4eD185NGlJZVpUZ2lQRE1iR2hLRHBLaVhkOXZocWV3YVlpamlnNkdjV1NQVmhNNThBUTRweGlvaWR2YnZySnRjTUNIVnFsV3ZRZmkwcDVCZFlSbjR5T0pMZ0ZJMENXWXdyN2JwM2olMkI2V0VOZ2hYWk1Yb1VMTmVvOEZkc1BKcnlVdFlqWmx4YVd5RExsbVl6UDI5T3FpTDBKUSUzRCUzRA; datadome=mVub-WkIRDMfm3wQUa7kuFRTsag8lqAeUgwBYb~29qDTm990warv91foGG4ShHwprk~79BmCfXkzqjYHwE~4kvBYf38uRDwNKjeubRWxkpa7iChTQcAmzBfeLur.xg2"""
JSON_ROOT_FILE = "output/jsons/"
TOTAL_ID_NAME_FLAG_TABLE = "output/TOTAL_ID_NAME_FLAG_TABLE.csv"
TOTAL_ID_NAME_FLAG_JSON = "output/TOTAL_ID_NAME_FLAG_TABLE.json"
def get_cata_json():
    """
    通过requests请求 获取网页嵌套的含有品类逻辑的字典
    :return: dict
    """
    url = "https://fr.shopping.rakuten.com/restpublic/tech-web/menu"
    headers = """
    authority: fr.shopping.rakuten.com
method: GET
path: /restpublic/tech-web/menu
scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
cache-control: max-age=0
cookie: IS_CONNECTED=false; JSESSIONID=ED0874E86970386B3671A19084F1AAF3.tomcatfo-p004_synten_local_app; devdee=eyJhbGciOiJIUzM4NCJ9.eyJEZXZpY2VUb2tlbiI6IjVkNTQyM2M4MzExNjRmMzA5NjNiYjEzOGE4ZTM0OWQ0MTY0NjcwNzYxMjUwOSJ9.69_6PhXPk_YD_scvVlzeaJfkhDR8GTT1uuul2uV6s4CC_kAYJt-S3NPHoetQg2v6; pmcookies=0b23f9c0-eeb5-40d2-b8c1-7a9faacae89b; pm=country=249&trackingdate=2022-03-08+03%3A46%3A51.0&version=1_1; pm_session=%7B%22page_count%22%3A1%7D; _mall_uuid=0b23f9c0-eeb5-40d2-b8c1-7a9faacae89b; didomi_token=eyJ1c2VyX2lkIjoiMTdmNjc2YzMtZGVhOC02MDM3LTlkZjUtZDNhYWY2ZjVhNmM0IiwiY3JlYXRlZCI6IjIwMjItMDMtMDhUMDI6NDc6MDEuNDEwWiIsInVwZGF0ZWQiOiIyMDIyLTAzLTA4VDAyOjQ3OjAxLjQxMFoiLCJ2ZXJzaW9uIjpudWxsfQ==; rgpd=%22%257B%2522loadAds%2522%253Afalse%252C%2522loadTracking%2522%253Afalse%252C%2522loadCustomization%2522%253Afalse%257D%22; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%228de31e3e-2de1-42e3-8914-ac44303038a4%22%2C%22options%22%3A%7B%22end%22%3A%222023-04-09T02%3A47%3A01.708Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atauthority=%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22cnil%22%2C%22visitor_mode%22%3A%22exempt%22%7D%2C%22options%22%3A%7B%22end%22%3A%222023-04-09T02%3A47%3A01.712Z%22%2C%22path%22%3A%22%2F%22%7D%7D; _#uid=1646707622519.888305223.7515187.5791.255391469.469; _#sess=1%7C20220308031702%7C1; _#env=20220309024702; _#srchist=62250%3A1%3A20220408024702; _#vdf=62250%7C1%7C20220408024702; cto_bundle=MHcNlF8xJTJCbXpUc3plbVhRSXpJbGw3SFB3RXlmSktHQWVlNjBnekx5c0dUV2RYQUpFMWJ0ZTdiTUt5SlIzVEI1cEdXdEFTYmxDUCUyRmYxWjVzNDZ6UE0xc3VCcHFPaXdvSjRQSldXQ1Z4R0J0RUQydDdVbmJNamgyUyUyRlBVZDVyaHRlMCUyRmd0YkdPQyUyRlhJJTJGZkNoTSUyRkpjQ21vOXVIdyUzRCUzRA; rak_land_91=1; datadome=.1w3jUBvv~7AVEmDsaMieeefjoFJZ8_967QN_V_smjvmkegs2_B~6FOMoumDykjUTf7yJZa8rbKfglIanrbwebhrojyw5.2cWwwzGfdY0P2WhxyFORv0QQlCwb_hRamu
referer: https://fr.shopping.rakuten.com/restpublic/tech-web/menu
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30
    """

    headers = change_headers_tool(headers)
    res = requests.session().get(url,headers = headers).text
    return json.loads(res)["categories"]


def find_parent(parent_date,child_id) ->dict:
    """
    寻找id孩子的父亲 和爷爷 label 作为上两级类目传回
    parent_date:含有三结点逻辑的字典
    :param child_id: int
    :return: panret_name,grandpa_name
    """
    for i in parent_date:
        if child_id in parent_date[i]["children"]:
            return parent_date[i]["label"],parent_date[i]["grandpa"]


def get_implement_list() ->list:
    """
    1.返回得到符合条件的商品字典列表文件
    2.在output 下生成 TOTAL_ID_NAME_FLAG_TABLE.csv 总类目表
    :return: list
    """


    jobs = get_cata_json()
    result = []
    csv_writer = csv.writer(open(TOTAL_ID_NAME_FLAG_TABLE,"w",encoding="utf-8",newline= ""))
    csv_writer.writerow(["一级类目","二级类目","三级类目","id","链接","标志"])
    for job in jobs:
        grand_pa = job["linkLabel"]
        single_all = jsonpath.jsonpath(job,'$..children[:10]')
        if single_all == False:continue   #不符合一级类目格式时略过
        parent_date = {}

        for i in single_all:

            #遍历找出所有父亲以及他们的儿子 和儿子的爷爷 实例：540665: {'childs': [540666, 540667, 540668, 540669, 540670],'label':...
            if i.get("children") != None:
                childs = [j["id"] for j in i["children"]]
                parent_date[i["id"]] = {"children":childs,"label" : i["label"],"grandpa":grand_pa}

            #遍历制造所有儿子以及他们的父亲 和他们的link 的字典表

            else:
                #判断每个链接的flag,nav是含有价格的  event是无效链接
                flag = "nav" if "nav" in i["link"] else "event"
                parnet,grand_pa = find_parent(parent_date, i["id"])
                #判断是不是符合需要的链接
                if "event" not in i["link"] and "nav" in i["link"]:
                    result.append({
                    "id": i["id"],
                    "parent":parnet,
                    "grand_pa":grand_pa,
                    "label" :i["label"],
                    "link" : i["link"]}
                    )
                csv_writer.writerow([grand_pa,parnet,i["label"],i["id"],i["link"],flag])
    save_json_file(result,TOTAL_ID_NAME_FLAG_JSON)

def excluded(implement_list) ->list:
    """

    :param implement_list: 传入爬取到的品类逻辑列表
    :return: 返回去除已经爬取过的怕品类列表
    """
    while True:
        try:
            with open("already.txt", "r", encoding="utf-8") as file:
                contents = file.read().split("\n")
                break
        except:
            with open("already.txt", "w", encoding="utf-8") as file:
                pass
    new = []
    for i in range(len(implement_list)):
        try:
            if str(implement_list[i]["id"]) not in contents:
                new.append(implement_list[i])
        except:
            pass



    print("共得到符合的链接{}个,去除已经完成的{}个，实际运行{}个".format(len(implement_list),len(contents),len(new)))
    time.sleep(3)
    return new

def link_join(link) ->str:
    # if "nav=" not in link:
    #     return 0,0

    if "/f" not in link:
        return 0,0
    if "nav=" in link:
        try:
            name = re.findall("&nav=(.*?)&",link)[0]
        except:
            try:
                name = re.findall("&nav=(.*?)?", link)[0]
            except:
                name = re.findall("\?nav=(.*?)#", link)[0]

    else:
        if "/f" in link:
            link = link.split("/f")[0]
            name  = link.split("nav/")[-1]

        else:

            try:
                link = link.split("#")[0]
            except:
                pass

            try:
                link = link.split("?")[0]
            except:
                pass
            name  = link.split("/")[-1]
        try:
            name = name.split("#")[0]
        except:
            pass

    if "/f" in link:
        link = f"""https://fr.shopping.rakuten.com/restpublic/vis-web/navAndSearchCatalog?category={name}&ft=n&sh=fs&page=1&isMobile=false&isTablet=false"""
    else:
        link= f"""https://fr.shopping.rakuten.com/restpublic/vis-web/navAndSearchCatalog?category={name}&ft=n&sh=fs&page=1&isMobile=false&isTablet=false"""

    return link,name


def process(impletment_list,data,ori_link) ->list:
    """
    把广告部分和原始部分进行叠加 根据广告部分特有的position参数插入到原始数据 得到总表
    :param data: 广告商品列表
    :return: 包含广告商品以及原始商品的总表
    """
    try:

        neuf = data["filters"][0]["values"][0]["count"]

    except:
        neuf = None
    # =Hifi_casques - micros & f10 = gaming & f2 = Casque & s = 0 & page = 1
    try:
        oca = data["filters"][0]["values"][1]["count"]
    except:
        oca = None

    try:
        reco = data["filters"][0]["values"][2]["count"]
    except:
        reco = None
    totalnum = data["metadata"]["totalFound"]
    ads_list = data["rakutenAds"]
    natives_list = data["products"]
    for i in ads_list:
        insert_index = i["position"]-1
        natives_list.insert(insert_index,i)
    try:
        a = natives_list[0]
        # ("合并后的总某品类商品列表实例如下:\n",natives_list[0])
    except:
        return 0
    (f"\n叠加后的总列表数量为{len(natives_list)}")
    list_ = []
    position = 0
    for i in natives_list:
        # (i)
        position += 1
        #判断是否是广告商品
        try:
            rate = i["reviews"]["average"]
            rate_num = i["reviews"]["number"]
            if_ads = False
        except:
            rate = None
            rate_num = None
            if_ads = True



        try:
            best_price =  i["marketPlace"]["bestPrice"]
            is_new = str(i["marketPlace"]["isNew"])
        except:
            try:
                best_price = i["marketPlace"]["usedOffer"]["bestPrice"]
                is_new = str(i["marketPlace"]["usedOffer"]["isNewOrRefurbished"])

            except:
                try:
                    best_price = i["marketPlace"]["newOffer"]["bestPrice"]
                    is_new = str(i["marketPlace"]["newOffer"]["isNewOrRefurbished"])

                except:
                    try:
                        best_price = i["marketPlace"]["refurbishedOffer"]["primaryBestPrice"]
                        is_new = str(i["marketPlace"]["refurbishedOffer"]["isPrimaryNew"])
                    except:
                        try:
                            best_price = i["marketPlace"]["sales"]["salesPrice"]
                            is_new = str(i["marketPlace"]["sales"]["isNew"])
                        except:
                            # (i)
                            pass
        best_price = best_price.replace("€","").replace(",",".").strip()
        list_.append([impletment_list["grand_pa"],impletment_list["parent"],i['description']["designation"],i["id"],
                    best_price ,rate,rate_num,if_ads,position,ori_link,f"https://fr.shopping.rakuten.com/offer/desc?aid={i['id']}",is_new,totalnum,neuf,oca,reco])
   #将一个品类的所有列表传到数据表中
    # print(list_)

    utility.tools.save_csv_file(list_)
    #向already.txt中添加当前完成的id
    utility.tools.already(impletment_list["id"])

def single_spider(url):
    cookies = COOKIES

    headers = utility.headers_config.fill_headers(cookies=cookies)

    res = requests.get(url,headers = headers).text
    # print(res)
    # input()
    # (res)
    #定义eval需要用到的变量名
    false = False
    true = True
    try:
        eval(res)
    except:
        print("warning：间接原因 格式化json时 出现了非法字符    \n直接原因：默认为cookies失效导致的元数据错误\n建议更新cookies后重新启动以继续添加模式运行")
        input("请更新并重启")

    return eval(res) if "metadata" in res else 0

def main_spider(implement_list,flag):
    from selenium import webdriver

    #driver方式/requests方法失败的备用方案 不优先
    # driver = webdriver.Chrome(executable_path='chromedriver.exe')

    """

    :param implement_list:传入的带爬取商品列表
    :param flag: 运行方式 继续添加或者新建表重新exort
    :return: none
    """
    #如果flag是2  则新建表
    if flag == 2:
        head_row = ["一级目录","二级目录","标题","id","价格（默认最优）","评分","评分数量","广告/非广告","页面位置","品类链接","自身链接","新品","类目总数","新品","二手","翻新"]
        utility.tools.init_csv_txt_file(head_row)


    error = 0
    for i in tqdm(range(len(implement_list))):
        if i >450:
            continue
        ori_link = implement_list[i]["link"]

        print("input link: {}".format(ori_link))
        link,cata_name= link_join(ori_link)
        if link==0:
            continue

        ori_link = f"https://fr.shopping.rakuten.com{ori_link}"

        try:
            print(f"进度 第{i + 1}/{len(implement_list)}个,失败{error}个\n",f"品类id:  {implement_list[i]['id']} \n",  f"获得的类目名:  {cata_name} \n", f"api link:  {link} \n")
        except:

            # print(i,len(implement_list),error,implement_list[i],ori_link,link)
            continue

        # try:

        data = single_spider(link)
        # print(data)
        # input()
        cu = random.randint(1,9)
        time.sleep(cu)
        # print(data)

        if data:
            # input("check")
            # 处理爬取到的数据
            # print(implement_list[i]['id'])

            utility.tools.save_json_file(data,JSON_ROOT_FILE +str(implement_list[i]['id'])+".json")
            with open("already.txt", "a+", encoding="utf-8") as file:
                file.write(str(implement_list[i]['id'])+"\n")
            print("&*done&*"*50)
            # process(implement_list[i],data,ori_link)
        else:


            with open("error.txt", "a+", encoding="utf-8") as file:
                file.write(ori_link + "\n")
                pass










def main():
    with open("error.txt", "w", encoding="utf-8") as file:
        pass
    flag = int(input("请输入运行的方式并且回车:\n\t1.从原先的数据表中添加 \n\t2.新建数据表并且重新爬取\n\n请输入:"))
    if flag ==2:
        open("already.txt","w",encoding="utf-8")
        open("error.txt", "w", encoding="utf-8")
    #1.获取品类链接数据等 传入下面方法进行调用 不调用则默认从上一次的文件中读取
    # implement_list = get_implement_list()

    #2.读取商品json
    implement_list = load_json_file(TOTAL_ID_NAME_FLAG_JSON)

    #3.对引入的链接列表去重
    implement_list = excluded(implement_list)

    #3.循环调用 进入爬虫
    main_spider(implement_list,flag)


if __name__ == '__main__':
    main()