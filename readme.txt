"""
author:wes;
createtime:2022.03.0.3

项目概述：
	爬取品类名称和对应的产品数量，页面第一页数据。
	对于每个产品：
	 	A.标题和链接
	 	B.星级评分和评分量
	 	C.是否有Cdiscount平台服务的标记
		 D.价格
	 	E.在页面的位置（第几个）
"""


1.项目名称：https://fr.shopping.rakuten.com/ 的各类目商品信息爬虫


2.需求分析

	A.全部的品类名称和链接，分析链接（产品页和非产品页，品类ID的规律）存储到output下的TOTAL_ID_NAME_FLAG_TABLE.csv中 (此功能可选重新生成，在代码中已被注释)



3.主要代码函数实现
    main主函数运行>获取所有类目链接get_implement_list() >读取类目信息 load_json_file >
对引入的链接列表去重 excluded >main_spider

4.其他描述：
	A.already.txt 记录爬虫进度，将已经爬取的	id存档，下一次继续运行时可以去重。 
	B.每次重新运行项目（之前的数据也不要了）,选择按之前的数据运行还是重新运行可选。

5.测试：
	A.error.txt记录了l-格式链接 但是问题链接，1.本身链接问题 2.不符合多数链接的逻辑，不再编写这部分流程。

6.运行方式:

	直接运行    run.py  爬虫

安装包： 目录下 requirements.txt文件
	打开当前目录的dos窗口 输入 pip install -r  requirements.txt

