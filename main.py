# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""

"""
import json
import pyecharts
from pyecharts.charts import Bar
from pyecharts import options

print(pyecharts.__version__)


bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

bar.set_global_opts(
    options.TitleOpts()
)


# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()





# data = [{"name": "长大三", "age": 15}, {"name": "网大崔", "age": 34}]
# jsonStr = json.dumps(data, ensure_ascii=False)
# print(jsonStr)

# if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
