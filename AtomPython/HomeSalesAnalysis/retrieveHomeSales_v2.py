# BS4 to analyze the page for the necessary information
from bs4 import BeautifulSoup
import requests


def retrieveDataMain():
    # setup file
    filename = 'homeSalesData.txt'
    header = 'Assessment Area' + ',Address' + ',Style' + ',Stories' + \
        ',Year Built' + ',Living Area 1st Floor (sq ft)' + \
        ',Bedrooms' + ',Finished Basement' + ',Garage 1 Type' + \
        ',Garage 1 Size (sq ft)' + ',Sale Date' + ',Sales Price' + \
        ',Parcel Number' + ',Units' + ',Living Area 2nd Floor (sq ft)' + \
        ',Full Baths' + ',Garage 2 Type' + ',Garage 2 Size (sq ft)' + \
        ',Living Area 3rd Floor (sq ft)' + ',Half Baths' + ',Finished Attic'
    
    with open(filename, 'w') as file_object:
        file_object.write(header)
    
    # go to the main web page to get the options
    session = requests.Session()
    mainPageResponse = session.get('https://www.cityofmadison.com/assessor/property/salesbyarea.cfm')
    mainPageSoup = BeautifulSoup(mainPageResponse.content, 'html.parser')
    areaOptions = mainPageSoup.find(id='AssessmentArea').find_all("option")
    
    # loop over the options
    for area in areaOptions:
        count = 0
        outputList = []
        # build the formData for post and get the result page
        assessmentArea = area.attrs.get('value')
        formData = {
            "sortBy": "Address", 
            "AssessmentArea": assessmentArea,
            "search": "salesByArea"
        }
        resultPageResponse = session.post(
            'https://www.cityofmadison.com/assessor/property/salesbyarearesults.cfm',
            data=formData
            )
        # extract the data from the tables on the page
        resultPageSoup = BeautifulSoup(
            resultPageResponse.content, 'html.parser'
            )
        resultsTables = resultPageSoup.find_all(
            'table', 'table table-condensed well'
            )
        for table in resultsTables:
            count += 1
            formattedTable = formtTableData(assessmentArea, table)
            outputList.append(','.join(formattedTable.details))
        
        # output data to file
        with open(filename, 'a') as file_object:
            for string in outputList:
                file_object.write('\n' + string)
        
        # update
        print('Completed gathering ' + str(count)
            + ' entries from  assessment area '
            + str(assessmentArea) + '.'
            )


class formtTableData():
    def __init__(self, assessmentArea, htmlTable):
        """htmlTable is a list"""
        # get the cells from the htmlTable
        tableCells = htmlTable.find_all('td')
        # data that needs to be cleaned in special manner
        finishedBasement = tableCells[6].text.strip()
        finishedBasement = finishedBasement.replace(
            u'\xa0\xa0\xa0\xa0\xa0 bas', '')
        garageOneInfo = formatGarageData(tableCells[7].text.strip())
        garageTwoInfo = formatGarageData(tableCells[17].text.strip())
        salesPrice = tableCells[9].text.strip()
        salesPrice = '"' + salesPrice + '"'
        # build the table details list with only necessary items
        tableDetails = [
            assessmentArea,
            tableCells[0].text.strip(),
            tableCells[1].text.strip(),
            tableCells[2].text.strip(),
            tableCells[3].text.strip(),
            tableCells[4].text.strip(),
            tableCells[5].text.strip(),
            finishedBasement,
            garageOneInfo.getType(),
            garageOneInfo.getSize(),
            tableCells[8].text.strip(),
            salesPrice,
            tableCells[10].text.strip(),
            tableCells[12].text.strip(),
            tableCells[14].text.strip(),
            tableCells[15].text.strip(),
            garageTwoInfo.getType(),
            garageTwoInfo.getSize(),
            tableCells[24].text.strip(),
            tableCells[25].text.strip(),
            tableCells[26].text.strip()
            ]
        self.details = tableDetails


class formatGarageData():
    def __init__(self, garageDataString):
        # string should be stripped already
        garageList = garageDataString.split(' ')
        if len(garageList) == 2:
            self.type = garageList[0]
            self.size = garageList[1]
        else:
            self.type = ''
            self.size = ''
    
    def getType(self):
        return self.type

    def getSize(self):
        return self.size


if __name__ == '__main__':
    retrieveDataMain()
# loop over the possible area values, use date sort
# submit to get the home sales data
