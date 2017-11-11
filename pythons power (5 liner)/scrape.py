import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
from lxml import html
import requests



counties = ["Antrim","Armagh","Carlow","Cavan","Clare","Cork",
              "Derry","Donegal","Down","Dublin","Fermanagh","Galway",
              "Kerry","Kildare","Kilkenny","Laois","Leitrim","Limerick",
              "Longford","Louth","Mayo","Meath","Monaghan","Offaly",
              "Roscommon","Sligo","Tipperary","Tyrone","Waterford",
              "Westmeath","Wexford","Wicklow"]


for county in counties:
      url = "https://www.lawsociety.ie/Find-a-Solicitor/Solicitor-Firm-Search/?filters=t_tab2!l_"+county+"!s_firmname!p_150!n_1#tab2"

      tree = html.fromstring(requests.get(url).content)
      emails = tree.xpath('//*[@class="base clearfix"]/div/div[1]/div[2]/div[2]/a[1]/text()')

      print "\n\n", county
      print emails
