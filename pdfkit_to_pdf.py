# coding=utf-8

import pdfkit
import os, sys

"""
from_url(url, output_path, options=None, toc=None, cover=None,configuration=None, cover_first=False)

url: 转换的文件地址
output_path： 输出的PDF地址
options： 设置生成pdf是的样式参数 eg:

1in = 25.4mm = 96px
1mm = 3.78px
"""

htmlTemplate = ''' 
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        {content}
    </body>
    </html>
'''

#生成pdf所继承的类
class toPdf:
    path_wk = ''
    config = ''
    options = ''
    path = ''
    def __init__(self, configURL, options):
        print('----------------Start-------------------')
        self.options = options
        try:
            self.path = pdfkit.configuration().wkhtmltopdf
            print('----------------完成输出配置-------------------')
        except:
            # 防止wkhtmltopdf系统环境变量配置不成功，切换本地配置
            self.path_wk = configURL
            self.config = pdfkit.configuration(wkhtmltopdf=self.path_wk)
            print('----------------系统变量未配置，启用本地配置项-------------------')

    # 自定义数据生成理想格式输出
    def data_to_pdf(self, fuc, from_url, out_url):
        print('----------------完成参数配置-------------------')
        with open(from_url+'.html', 'w+', encoding='utf-8') as f:
            f.write(fuc)
        print('----------------生成临时文件-------------------')
        try:
            print('----------------',self.path,'-------------------')
            if self.path != '':
                pdfkit.from_file(from_url+'.html', out_url+'.pdf', options=self.options)
            else:
                pdfkit.from_file(from_url + '.html', out_url + '.pdf', options=self.options, configuration=self.config)
            print('----------------生成pdf成功-------------------')
        except:
            print('----------------生成pdf失败-------------------')
        os.remove(from_url + '.html')
        print('----------------删除临时文件-------------------')
        print('----------------End-------------------')

    # 直接处理外部html文件
    def html_to_pdf(self, file_url, out_url):
        try:
            print('----------------', self.path, '-------------------')
            if self.path != '':
                pdfkit.from_file(file_url, out_url + '.pdf', options=self.options)
            else:
                pdfkit.from_file(file_url, out_url + '.pdf', options=self.options, configuration=self.config)
            print('----------------生成pdf成功-------------------')
        except:
            print('----------------生成pdf失败-------------------')
        print('----------------End-------------------')

    # url链接生成pdf
    def url_to_pdf(self, url_, out_url):
        try:
            print('----------------', self.path, '-------------------')
            if self.path != '':
                pdfkit.from_url(url_, out_url + '.pdf', options=self.options)
            else:
                pdfkit.from_url(url_, out_url + '.pdf', options=self.options, configuration=self.config)
            print('----------------生成pdf成功-------------------')
        except:
            print('----------------生成pdf失败-------------------')
        print('----------------End-------------------')

#处理数据 整理成想要输出的格式
def dealWithData(data):
    dataStr = '<div>'
    for item in data:
        dataStr += '<h3 style="color: red;">'+ item['title'] +'</h3>' +\
                   '<div><span style="color: #999;">公司名称：</span><span>'+ item['companyName'] +'<span></div>'+ \
                   '<div><span style="color: #999;">法定代表人：</span><sapn>'+ item['legalPersonName'] +'</span></div>' + \
                   '<div><span style="color: #999;">注册资金：</span><sapn>' + item['regCapital'] + '</span></div>'
    dataStr += '</div>'
    dataStr = htmlTemplate.format(content=dataStr)
    return dataStr

options = {
    # 'page-height': '500', #页面高度
    # 'page-width': '500', #页面宽度
    'page-size': 'A4', #页面大小
    'margin-top': '1in', #页面上边距
    'margin-right': '0in', #页面右边距
    'margin-bottom': '1.2in', #页面下边距
    'margin-left': '0in', #页面左边距
    'encoding': "utf-8",
    # 'header-center': 'pdfKit生成pdf测试', #页眉
    # 'header-font-name': '宋体', #系统相关 没有的字体需要手动添加
    # 'header-font-size': 16, #页眉文字大小
    # 'footer-center': '视野金服', #页脚
    # 'footer-font-size': 10, #页脚文字大小
    # 'footer-line': None,
    'header-spacing': '1', #页眉与内容的距离
    'footer-spacing': '2', #页脚与内容的距离
    'javascript-delay': '1000', #添加页面延时js执行时间段
    # 'user-style-sheet': './html/css/index.css', #为所有页面添加自定义css
    # 'orientation':'Landscape',#横向 不设置默认纵向
    # 'page-offset': 1, #页码起始
    # 'enable-plugins': None, #启用已安装的插件
    # 'footer-right':'Page [page] of [toPage]', #设置页码
    # 'footer-right':'第[Page]页', #设置页码
    'header-html': './html/header_footer/header.html', #html文件充当页眉
    'footer-html': './html/header_footer/footer.html', #html 文件充当页脚
    # 'disable-smart-shrinking': None, #禁止只能缩放页面大小
    # 'custom-header': [ #为url添加统一的请求header
    #     ('Accept-Encoding', 'gzip')
    # ],
}

dataList = [
    {
        'title': '公司基本信息1',
        'companyName': '天津华瑞达汽车消声器有限公司',
        'legalPersonName': '崔绍印',
        'regCapital': '1000.00万人民币'
    },
    {
        'title': '公司基本信息2',
        'companyName': '北京华瑞达汽车消声器有限公司',
        'legalPersonName': '李绍印',
        'regCapital': '1000.00万人民币'
    }
]
sources = r'D:/wkhtmltopdf/bin/wkhtmltopdf.exe'

if __name__ == '__main__':
    pdf = toPdf(sources, options)
    # pdf.data_to_pdf(dealWithData(dataList), 'from', 'string_pdf')
    pdf.html_to_pdf(r'./html/pdf_.html','file_pdf')
    # pdf.url_to_pdf('https://www.baidu.com', 'url_pdf')