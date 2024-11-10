import subprocess
import sys
print("Copyright:2021111015位志轩")


def chk():
    libraries = [
        "Numpy", "Pandas", "Matplotlib", "Pyecharts", "Seaborn",
        "Bokeh", "HoloViews", "Plotly", "NetworkX", "pymysql",
        "altair", "xlrd", "mpld3", "mplfinance", "squarify", "pygal",
        "pytagcloud", "wordcloud", "jieba"
    ]
    for lib in libraries:
        try:
            __import__(lib)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("所有需要的库都已检查和安装")


chk()
