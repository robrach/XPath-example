import requests
from lxml import html

page_path = 'https://halloween.friko.net/imieniny/'
page = requests.get(page_path)
tree = html.fromstring(page.text)

names_today_list = tree.xpath("//table[@class=\"table table-condensed table-striped\"]/tr[2]/td/a/text()")

"""
Names in the 'names_today_list' are duplicated, because they appear in two places on the requested page.
And these two places are not distinguishable by id or class name. So we have to halve the list. It is made below.
"""
indicator = int(len(names_today_list)/2)
names_today_list = names_today_list[:indicator]

print("Names for today:", names_today_list)
