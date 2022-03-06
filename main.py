#-*- coding:utf-8 -*-
import random
import time

import requests
import re
class TiebaSpider:
    def __init__(self,name):
        self.Encoding = 'gbk'
        self.name =name
        self.url_temp='https://search.51job.com/list/170200%252C170300,000000,0000,00,9,99,'+name+',2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        self.heards={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1,2)]

    def parse_url(self,url):
        response = requests.get(url,headers=self.heards)
        return response.content.decode('gbk')
    def save(self,html,num):
        file_path = '{}-第{}页.html'.format(self.name,num)
        with open(file_path,"w",encoding=self.Encoding) as f:
            f.write(html)

    def useRegex(self, input):
        pattern = re.compile("^(window.__SEARCH_RESULT__) = .*$",re.M)
        x = pattern.search(input)
        list = [i for i in x.group()]

        return "".join(list).replace('window.__SEARCH_RESULT__ = ','').replace("</script>","")

    def run(self):
        url_list = self.get_url_list()

        for i in url_list:
            print(i)
            html = self.parse_url(i)
            print(html)
            json=self.useRegex(html)
            page_num = url_list.index(i)+1
            self.save(json,page_num)
            # time.sleep(random.randint(10,20))



a = TiebaSpider("java")
a.run()
# url='https://search.51job.com/list/170200%252c170300,000000,0000,00,9,99,java,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
# r=requests.get(url)
# print(r.content.decode('gbk'))


# input='"engine_jds":[{"type":"engine_jds","jt":"0_0","tags":[],"ad_track":"","jobid":"82332481","coid":"2720339","effect":"1","is_special_job":"","job_href":"https:\/\/jobs.51job.com\/erqiqu\/82332481.html?s=sou_sou_soulb&t=0_0","job_name":"诚聘 Java中、高级软件工程师","job_title":"诚聘 Java中、高级软件工程师","company_href":"https:\/\/jobs.51job.com\/all\/co2720339.html","company_name":"云计划软件科技（上海）有限公司","providesalary_text":"0.7-1万\/月","workarea":"170202","workarea_text":"郑州-二七区","updatedate":"03-04","iscommunicate":"","companytype_text":"合资","degreefrom":"5","workyear":"4","issuedate":"2022-03-04 18:22:17","isFromXyz":"","isIntern":"","jobwelf":"免费班车 专业培训 定期体检 年终奖金 五险 补充医疗保险 员工旅游","jobwelf_list":["免费班车","专业培训","定期体检","年终奖金","五险","补充医疗保险","员工旅游"],"isdiffcity":"","attribute_text":["郑州-二七区","2年经验","大专","招8人"],"companysize_text":"150-500人","companyind_text":"计算机软件","adid":""},xxx]'
# x=useRegex(input)
# print("".join(list))
