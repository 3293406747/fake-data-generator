# 伪数据生成工具

伪数据生成工具,支持命令行和浏览器两种方式生成伪数据。可生成姓名、手机号、身份证号、统一社会信用代码等数据，数据生成后自动复制到剪切板。

## 部署

1. 下载源码。确保本地已安装git，打开控制台使用`git clone https://github.com/3293406747/fake-data-generator.git` 命令下载源代码。
2. 安装依赖。确保本地已安装python，确认控制台中目录为项目根目录，之后执行`pip install -r requirements.txt`。

## 使用方法

### 浏览器

1. 进入'web'目录找到'flask_app.py'文件并执行该文件。
2. 浏览器访问url`http://127.0.0.1:5000`。

### 命令行

1. 进入'command'目录找到'__init__.py文件并执行该文件。
2. 在用户交互页面输入要生成的内容，如要生成姓名可输入name。

## 打包成可执行文件（.exe）

1. 安装pyinstaller工具。在命令行中执行`pip install pyinstaller`。
2. 打包第一步。在控制台中进入'command'目录，执行`pyinstaller -D __init__.py`。
3. 打包第二步。打包完成后生成'dist'目录，进入'dist'目录下的'__init__'目录。
4. 打包第三步。将'data'目录复制到'dist'目录下的'__init__'目录中。
5. 运行可执行文件第一步。在命令行进入到'dist'目录下的'__init__'目录中。
6. 运行可执行文件第二步。在命令行输入`__init__ -t name`命令。

## 命令行命令说明

`__init__ -t name`命令中的-t后面跟的是要生成的数据。如要生成姓名可输入'name'。

## 支持

如果你喜欢该项目可以在github进行star或分享。