import requests
from bs4 import BeautifulSoup
import base64
import json
import os
import shutil


def get_html_content(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML, return the
    text content, otherwise return None.
    """
    try:
        resp = requests.get(url)
        if is_good_response(resp):
            return resp.content
        else:
            return None

    except requests.RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    # Return true if the response is HTML, false otherwise.
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') >= 0)


def log_error(e):
    """
    Output and error to the screen
    """
    print(e)


def extractJSONData(pageOneScripts):
    jsonList = []
    # loop over the scripts that were found
    for script in pageOneScripts:
        # loop over the strings in the script
        for stringString in script.strings:
            # convert the bs4 class into a string
            string = str(stringString)
            # find where the JSON data starts
            startPos = string.find('var pages = JSON.parse(atob("')
            # skip the strings that don't have a start
            if startPos < 0:
                continue
            # remove the extraneous portion of the string
            startPos = startPos + 29
            # find where the string ends
            endPos = string.find('"));', startPos)
            # add the string to the list
            jsonList.append(string[startPos:endPos])
    # return the list of JSON data
    return jsonList


def extractUrlsFromJsonList(jsonList):
    urlList = []
    # loop over the JSON strings in the list
    for jsonString in jsonList:
        # decode the strings
        decodedJsonData = json.loads(base64.b64decode(jsonString))
        # loop over each piece of JSON
        for jsonData in decodedJsonData:
            # append each URL to the
            try:
                urlList.append(jsonData['url'])
            except TypeError:
                pass
    return urlList


def pageOfChapter(chapterPageUrl):
    pieces = chapterPageUrl.split('/')
    for piece in pieces:
        if piece.find('?quality=100') < 0:
            continue
        page = piece[:piece.find('?')]
    return page


def saveOnePieceChapterFiles(chapter, saveOutputPath):
    # chapter folder
    chapterFolder = 'One Piece ' + chapter + ' [JaminixBox]'
    # grab HTML data from the first page
    pageOne = get_html_content(
        'https://jaiminisbox.com/reader/read/one-piece-2/en/0/'
        + chapter
        + '/page/1'
        )

    # exit early if the page is empty
    if pageOne is None:
        exit()

    # convert the data into BeautifulSoup format
    soupedPageOne = BeautifulSoup(pageOne, 'html.parser')

    # grab the scripts from the page

    pageOneScripts = soupedPageOne.find_all('script', type='text/javascript')

    # creat a list of the JSON data
    jsonList = extractJSONData(pageOneScripts)

    # decode the json data into URLs
    urlList = extractUrlsFromJsonList(jsonList)

    # make a new folder in the desired directory
    os.chdir(saveOutputPath)
    if not os.path.exists(chapterFolder):
        os.mkdir(chapterFolder)
    os.chdir(saveOutputPath + '\\' + chapterFolder)

    # save off the images into the new folder
    for url in urlList:
        # determine the page from the url
        pageFilename = pageOfChapter(url)
        imageObject = requests.get(url, stream=True)
        print(pageFilename)
        with open(pageFilename, 'wb') as outputFile:
            shutil.copyfileobj(imageObject.raw, outputFile)
            del imageObject


if __name__ == '__main__':
    # chapter to grab
    chapter = '928'
    # where to make the new folder
    saveOutputPath = 'C:\\Users\\Alex Trim\\Downloads\\OnePiece'
    # execute primary subroutine
    saveOnePieceChapterFiles(chapter, saveOutputPath)
