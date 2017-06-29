import xlsxwriter
from site_scraper import hackathonList

hackathons = hackathonList()

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('hackathons.xlsx')
worksheet = workbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0
# Create column titles
worksheet.write(0, col,     "Hackathon")
worksheet.write(0, col + 1, "URL")
worksheet.write(0, col + 2, "Start Date")
worksheet.write(0, col + 3, "End Date")
worksheet.write(0, col + 4, "City")
worksheet.write(0, col + 5, "State")
worksheet.write(0, col + 6, "Reimbursement")
worksheet.write(0, col + 7, "Application Opens")
worksheet.write(0, col + 8, "Application Closes")
worksheet.write(0, col + 9, "Applied?")


# Iterate over the data and write it out row by row.
for hackathon in hackathons:
    worksheet.write(row, col,     hackathon['title'])
    worksheet.write(row, col + 1, hackathon['url'])
    worksheet.write(row, col + 2, hackathon['startDate'])
    worksheet.write(row, col + 3, hackathon['endDate'])
    worksheet.write(row, col + 4, hackathon['city'])
    worksheet.write(row, col + 5, hackathon['state'])
    row += 1

workbook.close()
