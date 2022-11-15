import requests
import csv
import random
import time

from bs4 import BeautifulSoup


# function to append row data into csv file.
def writeMyCSV(dataArr):
    with open("pincode.csv", 'a') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rowsArr
        # as we have already added the column names in csv, we don't need first raw.
        csvwriter.writerows(dataArr[1:])


def main(pageUrl):
    page = requests.get(pageUrl)

    soup = BeautifulSoup(page.content, 'html.parser')

    # data for given pincode is present in table tag with `table table-bordered` class name.
    table1 = soup.find("table", class_='table table-bordered')

    pincodeDataArr = []
    rowsArr = []

    x = 1
    # table data is stored in `b` tag
    for i in table1.find_all('b'):
        # we have five columns on web table.
        # so we have to add our rowsArr in pincodeDataArr and reset our rowsArr after every five column data.
        if x == 5:
            title = i.text
            rowsArr.append(title)
            pincodeDataArr.append(rowsArr)
            rowsArr = []
            x = 1
        else:
            # appending data into rowsArr to construct a single row.
            title = i.text
            rowsArr.append(title)
            x += 1

    # this function is appding data into pincode.csv file.
    writeMyCSV(pincodeDataArr)


if __name__ == "__main__":
    # list of pincodes for which you want to collect data from indiamapia.com
    pincodes = [202524, 440009, 733213]

    for i in pincodes:
        # constructing url to look for a specific pincode data on indiamapia.com
        url = 'https://indiamapia.com/'+str(i)+'.html'

        print("Processing for Pincode: ", i)

        # calling main() func to scrap the data and store into pincode.csv file.
        main(url)

        if i == pincodes[-1]:
            print("Hurrahhh.. !! We are all done. ")

        # adding random sleep timer to not to spam the webside API.
        time.sleep(random.randint(0, 9))
