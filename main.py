import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
from lxml import html
import requests





#**************************************
#********* MAIN PROGRAM ***************
#**************************************
def main():

    counties = ["Antrim","Armagh","Carlow","Cavan","Clare","Cork",
                "Derry","Donegal","Down","Dublin","Fermanagh","Galway",
                "Kerry","Kildare","Kilkenny","Laois","Leitrim","Limerick",
                "Longford","Louth","Mayo","Meath","Monaghan","Offaly",
                "Roscommon","Sligo","Tipperary","Tyrone","Waterford",
                "Westmeath","Wexford","Wicklow"]

    emailCount = 0;

    # Clear the previous .csv
    f = open("emails.csv","w+")
    f.write("")
    f.close()

    noSeperationUnique(counties)


def noSeperationUnique(counties):
    # gives a unique list of all emails

    allEmails = []
    emailCount = 0

    # Scrape info for each county
    print "Scraping emails.."
    for county in counties:
        url = "https://www.lawsociety.ie/Find-a-Solicitor/Solicitor-Firm-Search/?filters=t_tab2!l_"+county+"!s_firmname!p_150!n_1#tab2"

        tree = html.fromstring(requests.get(url).content)
        emails = tree.xpath('//*[@class="base clearfix"]/div/div[1]/div[2]/div[2]/a[1]/text()')
        emailCount = emailCount + len(emails)

        allEmails.extend(emails)

    print "\n\nTotal Emails:", emailCount

    #Remove duplicates
    allEmails = list(set(allEmails))

    #Write to .csv
    print "Writing to .csv.."
    f = open("emails.csv","a")
    for email in allEmails:
        f.write(email+"\n")
    f.close()





def countySeperated(counties):

    # Will contain duplicates
    emailCount = 0
    # Scrape info for each county
    for county in counties:
        url = "https://www.lawsociety.ie/Find-a-Solicitor/Solicitor-Firm-Search/?filters=t_tab2!l_"+county+"!s_firmname!p_150!n_1#tab2"

        tree = html.fromstring(requests.get(url).content)
        emails = tree.xpath('//*[@class="base clearfix"]/div/div[1]/div[2]/div[2]/a[1]/text()')
        emailCount = emailCount + len(emails)

        print "\n\n", county
        print emails

    print "\n\nTotal Emails:", emailCount





if __name__ == '__main__':
    main()
