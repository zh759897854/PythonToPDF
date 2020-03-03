# coding=utf-8
import pdfkit
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urlparse

htmlStr = ''' 
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

options = {
    # 'page-height': '500', #页面高度
    # 'page-width': '500', #页面宽度
    # 'page-size': 'A4', #页面大小
    # 'margin-top': '1in', #页面上边距
    # 'margin-right': '0in', #页面右边距
    # 'margin-bottom': '1.2in', #页面下边距
    # 'margin-left': '0in', #页面左边距
    'encoding': "utf-8",
    # 'header-center': 'pdfKit生成pdf测试', #页眉
    # 'header-font-name': '宋体', #系统相关 没有的字体需要手动添加
    # 'header-font-size': 16, #页眉文字大小
    # 'footer-center': '视野金服', #页脚
    # 'footer-font-size': 10, #页脚文字大小
    # 'footer-line': None,
    # 'header-spacing': '1', #页眉与内容的距离
    # 'footer-spacing': '2', #页脚与内容的距离
    'javascript-delay': '1000', #添加页面延时js执行时间段
    # 'user-style-sheet': './html/css/index.css', #为所有页面添加自定义css
    # 'orientation':'Landscape',#横向 不设置默认纵向
    # 'page-offset': 1, #页码起始
    # 'enable-plugins': None, #启用已安装的插件
    # 'footer-right':'Page [page] of [toPage]', #设置页码
    # 'footer-right':'第[Page]页', #设置页码
    # 'header-html': './header.html', #html文件充当页眉
    # 'footer-html': './footer.html', #html 文件充当页脚
    # 'disable-smart-shrinking': None, #禁止只能缩放页面大小
    # 'custom-header': [ #为url添加统一的请求header
    #     ('Accept-Encoding', 'gzip, deflate, br'),
    #     ('Cookie', 'JSESSIONID=F263DFBD49024AB1EADA3A90C7AD0756; acw_tc=7b39758815821843623528706e179927a42f4ca6dd9cd3403a7d4a05d4b2c5; SERVERID=f68d48fcadd284358f711f94b4434cd2|1583145416|1583144300')
    # ],
}

# pdfkit.from_string(htmlStr.format(content = '<div>测试</div>'), 'test.pdf')

# Requests = requests.get('https://alpha.seeyii.com/v2/index.html?t=2&e=dD0xNTgzMTM2NzQ0NzU1JnRpbWVzdGFtcD0xNTgzMTM2NzQ0NzU1JmdWZXI9MjAxOTAxMDkxNDIw&timestamp=1583136744755')
# print(Requests.header)
# soup = BeautifulSoup(Requests.content, "html.parser")
# with open('seeyii.html', 'w+', encoding='utf-8') as f:
#     f.write(soup.decode('utf-8'))

pdfkit.from_url('https://www.seeyii.com/v2/oSACarryFundLP.html?t=2&e=dD0xNTgzMTQ1NzAxNzk2JnRpbWVzdGFtcD0xNTgzMTQ1NzAxNzk2JmdWZXI9MjAxOTAxMDkxNDIw&timestamp=1583145701796', 'test.pdf', )

