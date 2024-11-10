import pygal
import webbrowser

my_config = pygal.Config()
my_config.show_legend = True
my_config.style.title_font_size = 26
my_config.style.label_font_size = 16
radar_chart = pygal.Radar(my_config, fill=False, range=(0, 50))
radar_chart.title = '2020年前三季度各地区客户流失量分析'
radar_chart.x_labels = ['华东', '华北', '华中', '华南', '西南', '西北', '东北']
radar_chart.add('第一季度', [32, 21, 35, 28, 39, 42, 39])
radar_chart.add('第二季度', [30, 31, 35, 25, 41, 36, 34])
radar_chart.add('第三季度', [36, 26, 30, 35, 35, 46, 36])
radar_chart.render_to_file('雷达图.svg')

webbrowser.open('雷达图.svg')
