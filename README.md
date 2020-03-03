#### PythonToPDF-Python转pdf工具

### -------------------------------------------------

[py 生成pdf工具参数详解](https://www.jianshu.com/p/4d65857ffe5e)

```
运行环境:
1.Python3
2.本地安装wkhtmltopdf 并且import pdfkit 
3.安装完成后需要配置wkhtmltopdf 的环境系统变量 D:\wkhtmltopdf\bin并重启
数据格式：
	    全部编写成html通过pdfkit生成pdf
全局选项：
      --image-dpi <integer>         嵌入图像时，将它们缩放至此dpi（默认值） 600）
      --image-quality <integer>     使用jpeg压缩图像时使用此质量（默认值为94）
      --license                     输出许可证信息并退出
      --log-level <级别>            将日志级别设置为：无，错误，警告或 info（默认信息）
  -l，--lowquality                  生成较低质量的pdf / 有用的节省文档空间
  -B，--margin-bottom<unitreal>     设置的页下边距
  -L，--margin-left<unitreal>       设置的页面的左边距（默认10毫米）
  -R，--margin-right <unitreal>     设置页面右页边距（默认为10mm）
  -T，--margin-top <unitreal>       设置页面上页边距
  -O，--orientation <orientation>   将方向设置为横向或纵向（默认纵向）
      --page-height <unitreal>      页面高度
  -s，--page -size <Size>           将纸张尺寸设置为：A4，Letter等（默认A4）
      --page-width <unitreal>       页面宽度
      --no-pdf-compression          不要对pdf对象使用无损压缩
  -q，--quiet                       极简模式
      --read-args-from-stdin        从stdin读取命令行参数
      --readme                      输出程序自述文件
      --title<文本>                 生成的pdf文件的标题（如果未定，则使用第一个文档的标题）
      --version                      输出版本信息并退出
目录选项：
      --dump-default-toc-xsl        将默认的TOC xsl样式表转储到stdout 
      --dump-outline                <file>将大纲转储到文件中
      --outline                     将大纲转入pdf（默认）
      --no-outline                  不要在pdf文件中添加轮廓线
      --outline-depth               <level>设置轮廓线的深度（默认4）
页面选项：
      --allow <path>                允许将指定文件夹中的一个或多个文件加载（可重复）
      --background                  不打印背景（默认）
      --no-background               不打印背景--bypass-proxy-for <值>绕过主机的代理（可重复）
      --cache-dir                   <路径> Web缓存目录
      --checkbox-checked-svg        <路径>呈现选中的复选框时使用此SVG文件
      --checkbox-svg                <路径>呈现未选中的复选框时，请使用此SVG文件
      --cookie <名称>               <值>设置其他cookie（可重复），值应为url编码。
      --custom-header <名称>        <值>设置附加的HTTP标头（可重复） 
      --custom-header-propagation   为每个资源请求添加由--custom-header 指定的HTTP标头。
      --no-custom-header-propagation不要为每个资源请求添加由--custom-header 指定的HTTP标头。
      --debug-javascript            显示javascript调试输出
      --no-debug-javascript         不显示javascript调试输出（默认） 
      --default-header              添加默认标题，页面名称位于左侧，页码位于右边，缩写：
        -- header-left ='[webpage]'
        -- header-right ='[page] / [toPage]'
        --top 2cm 
      --header-line 
      --encoding <encoding>        设置默认文本编码，用于输入
      --disable-external-links     不链接到远程网页
      --enable-external-links      链接到远程网页（默认） 
      --disable-forms              不要将HTML表单字段转换为pdf表单字段（默认）
      --enable-forms               将HTML表单字段转换为pdf表单字段
      --images                     加载或打印图像（默认）
      --no-images                  不加载或打印图像
      --disable-internal-links     不创建本地链接
      --enable                     内部链接设置本地链接（默认）
  -n，--disable-javascript         不允许网页运行javascript
      --enable-javascript          允许网页运行javascript默认）
      --javascript -delay<msec>    等待几毫秒的javascript完成（默认200）
      --keep-relative-links        保持相对外部链接为相对外部链接-加载错误处理<处理程序>指定如何处理无法加载的页面：中止，忽略或跳过（默认中止）
      -- load-media-error-handling       <处理程序>指定如何处理媒体文件无法加载的文件：中止，忽略或跳过（默认忽略）
      -- disable-local-file-access       不允许将本地文件转换为读取其他本地文件，除非--allow 
      --enable-local               明确允许-file-access允许将本地文件转换为读取其他本地文件。（默认）
      --minimum-font-size <int>   最小字体大小
      --exclude-from-outline      不要在目录和大纲中包括该页面
      --include-in-outline        在目录和大纲中包括页面（默认）
      --page-offset <offset>      设置起始页码（默认0）
      --password <password>       HTTP身份验证密码
      --disable- plugins          禁用已安装的插件（默认）
      --enable-plugins            启用已安装的插件（插件可能不起作用）
      --post <名称>               <value>添加一个附加的post字段（可重复）
      --post文件<name>            <path>发布一个附加文件（可重复） 
      --print-media-type          使用print media-type代替屏幕
      --no-print-media-type       不使用打印介质类型代替屏幕（默认）
  -p，--proxy <proxy>               使用代理
      --proxy-hostname-lookup       使用代理解析主机名
      --radiobutton -checked-svg    <路径>呈现选中的单选按钮时使用此SVG文件--radiobutton-svg <路径>呈现未选中的单选按钮时使用此SVG文件-
      -resolve-relative-links       将相对外部链接解析为绝对链接（默认）
      --run-script <js>             页面加载完成后运行此附加javascript （可重复）
      --disable-smart-shrinking     禁用WebKit使用的智能收缩策略，该策略使像素/ dpi  比率不恒定
      --enable-smart -shrinking     启用WebKit使用的智能缩小策略，该策略使像素/ dpi比率不恒定（默认值）
      --ssl-crt-path <path>         ssl客户端证书公共密钥的路径OpenSSL PEM格式，可选的后跟中间的ca和受信任的证书
      --ssl-key-password <密码>     ssl客户端证书私钥的密码
      --ssl-key-path <path>         OpenSSL PEM格式的ssl客户端证书私钥的路径
      --stop-slow-scripts           停止运行缓慢的javascript（默认）
      --no-stop-slow-scripts        不要停止运行缓慢的javascript 
      --disable-toc-back-links      不要从节标题链接到toc（默认）
      --enable-toc-back-links       从节标题到toc的链接
      --user-style-sheet            <URL>指定要加载到每个页面的用户样式表
      --username <username>         HTTP身份验证用户名
      --viewport-size               如果您具有自定义 滚动条或CSS属性溢出，请设置视口大小模拟窗口大小：
      --window-status               <windowStatus>等待渲染页面之前window.status等于此字符串
      --zoom <float>                使用此缩放因子（默认为1）
页眉和页脚选项：
      --footer-center <text >       页脚居中文字
      --footer-font-name <名称>     设置页脚字体名称（默认为Arial） 
      --footer-font-size <size>     设置页脚字体大小（默认为12） 
      --footer-html <url>           添加html页脚
      --footer-left <文本>          左对齐的页脚文本
      --footer-line                 在页脚上方显示行
      --no-footer-line              不显示页脚上方的行（默认）
      --footer-right <文本>         右对齐页脚文本
                                    [page]       当前正在被输出页面的页码
                                    [frompage]   第一页在文档中的页码
                                    [topage]     最后一面在文档中的页码
                                    [webpage]    当前正在被输出页面的URL
                                    [section]    当前正在被输出的章节的名字
                                    [subsection] 当前正在被输出的小节的名字
                                    [date]       本地系统格式的当前日期
                                    [isodate]    ISO 8601 格式的当前日期
                                    [time]       本地系统格式的当前时间
                                    [title]      当前对象的标题
                                    [doctitle]   输出文档的标题
                                    [sitepage]   当前正在处理的对象中当前页面的页码
                                    [sitepages]  当前正在处理的对象中的总页数
      --footer-spacing <real>       页脚和内容之间的间距，以毫米为单位（默认为0） 
      --header-center <text>        标题文字居中
      --header-font-name <名称>     设置标题字体名称（默认Arial）
      --header-font-size <size>     设置标题字体大小（默认12） 
      --header-html <url>           添加html标头
      --header-left <文本>          左对齐的标题文本
      --header-line                 在标题下方显示行
      --no-header-line              不显示标题下方的行（默认） 
      --header-right <文本>         右对齐标题文本
      --header-spacing <real>       标头和内容之间的间距，以毫米为单位（默认为0）
      --replace <名称> <值>         用页眉和页脚中的值替换[名称] （可重复）

页面大小：
      --page-size选项，可以将其更改为几乎所有其他内容，例如：A3，Letter和Legal。有关支持的页面大小的完整列表，请参见http://qt-         project.org/doc/qt-4.8/qprinter.html#PaperSize-enum
  为了更精细地控制页面大小，可以使用--page-height和--page-width选项
  ```


### pip install fake_useragent 失败多尝试几次

[wkhtmltopdf下载](https://wkhtmltopdf.org/downloads.html)
