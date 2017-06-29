import xlsxwriter
from site_scraper import hackathonList

# Canadian Provinces
prov_terrs = {
    'AB': 'Alberta',
    'BC': 'British Columbia',
    'MB': 'Manitoba',
    'NB': 'New Brunswick',
    'NL': 'Newfoundland and Labrador',
    'NT': 'Northwest Territories',
    'NS': 'Nova Scotia',
    'NU': 'Nunavut',
    'ON': 'Ontario',
    'PE': 'Prince Edward Island',
    'QC': 'Quebec',
    'SK': 'Saskatchewan',
    'YT': 'Yukon'
}

american_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def country(state):
    if state == 'MX':
        return 'Mexico'
    for prov_terr in prov_terrs:
        if state == prov_terr:
            return "Canada"
    for american_state in american_states:
        if state == american_state:
            return "United States"
    return "Unknown"




def hackathonSpreadsheet():
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
    worksheet.write(0, col + 6, "Country")
    worksheet.write(0, col + 7, "Reimbursement")
    worksheet.write(0, col + 8, "Application Opens")
    worksheet.write(0, col + 9, "Application Closes")
    worksheet.write(0, col + 10, "Applied?")
    worksheet.write(0, col + 11, "Abroad?")





    # Iterate over the data and write it out row by row.
    for hackathon in hackathons:
        worksheet.write(row, col,     hackathon['title'])
        worksheet.write(row, col + 1, hackathon['url'])
        worksheet.write(row, col + 2, hackathon['startDate'])
        worksheet.write(row, col + 3, hackathon['endDate'])
        worksheet.write(row, col + 4, hackathon['city'])
        worksheet.write(row, col + 5, hackathon['state'])
        worksheet.write(row, col + 6, country(hackathon['state']))
        row += 1

    workbook.close()

hackathonSpreadsheet()
