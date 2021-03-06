# xlrd is a library for examining and extracting data from Excel spreadsheets
# Documentation is available here: 
    # http://www.lexicon.net/sjmachin/xlrd.html
# Perhaps the best way to learn it is to read the source (Luke!) at:
# http://python-xlrd.sourcearchive.com/documentation/0.6.1/files.html
import xlrd    
import re

from scraperwiki import scrape
# Nice example of a spreadsheet with useful data!
url = 'http://www.hmrc.gov.uk/stats/tax_structure/incometaxrates_1974to1990.xls'
#Comment out the line above and uncomment either of the 2 lines below to change the scraper so that it works
#url = 'http://webarchive.nationalarchives.gov.uk/20140109143644/http://www.hmrc.gov.uk/stats/tax_structure/incometaxrates_1974to1990.xls'
#url = 'http://webarchive.nationalarchives.gov.uk/20130402145952/http://transparency.dh.gov.uk/files/2012/10/DailySR-Web-file-WE-02-12-12.xls'
# This line will open the spreasheet from an url
book = xlrd.open_workbook(file_contents=scrape(url))
# We can find out information about the workbook - number of sheets
print "Workbook has %s sheet(s)" % book.nsheets
# Loop over each sheet, print name, and number of rows/colums
for sheet in book.sheets():
    print "Sheet called %s has %s rows and %s columns" %(sheet.name,sheet.nrows,sheet.ncols)
# You can also access each worksheet by its index
firstSheet = book.sheet_by_index(0)
# You can loop over all the cells in the worksheet
for row in range(0,firstSheet.nrows): # for each row
    for column in range(0,firstSheet.ncols): # for each column within the row
        cell = firstSheet.cell(row,column)
        # Each cell may contain unicode
        cellValue = unicode(cell.value)
        
        # Test each cell to see if it's a year range and print each value
        match = re.match("(\d{4}-\d{2,4})",cellValue)
        #different regex for the sitreps spreadsheet - uncomment for that url
        #match = re.match("([A-Z][0-9][0-9])",cellValue) #SHA codes, e.g. Q30
        if match:
            print "Year: " + cellValue
            #print "SHA Code: " + cellValue
            
        # We could then extract the income tax rates by year.
