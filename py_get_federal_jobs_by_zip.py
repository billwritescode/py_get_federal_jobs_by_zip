# py_get_federal_jobs_.py
# uses usajobs.gov api to get a list of federal jobs
# Copyright 2015 Bill Garate
# Licensed with GNU GPL 2.0

import requests

#######
#######  A bug calls the following warning to appear 
# Warning (from warnings module):
#  File "C:\Python34\lib\requests\packages\urllib3\connection.py", line 251
#    SecurityWarning
# SecurityWarning: Certificate has no `subjectAltName`,
# falling back to check for a `commonName` for now. This
# feature is being removed by major browsers and deprecated
# by RFC 2818.
# (See https://github.com/shazow/urllib3/issues/497 for details.)
######  The following line of code disables urrllib3 warnings, and the script runs
######
requests.packages.urllib3.disable_warnings()


############ CLASSES ############
class Child(object):
    def __init__(self,json_data):
        self.document_id = json_data['DocumentID']
        self.job_title = json_data['JobTitle']
        self.organization_name = json_data['OrganizationName']
        self.agency_sub_element = json_data['AgencySubElement']
        self.salary_min = json_data['SalaryMin']
        self.salary_max = json_data['SalaryMax']
        self.salary_basis = json_data['SalaryBasis']
        self.start_sate = json_data['StartDate']
        self.end_date = json_data['EndDate']
        self.who_may_apply_text = json_data['WhoMayApplyText']
        self.pay_plan = json_data['PayPlan']
        self.series = json_data['Series']
        self.grade = json_data['Grade']
        self.work_schedule = json_data['WorkSchedule']
        self.work_type = json_data['WorkType']
        self.locations = json_data['Locations']
        #self.locations = self.locations.split(';')
        self.announcement_number = json_data['AnnouncementNumber']
        self.job_summary = json_data['JobSummary']
        self.apply_online_url = json_data['ApplyOnlineURL']

    def print_job_details(self):
        print("===========")
        print("Title:", self.job_title,)
        print("Locations: ", self.locations)
        print("Grade range:", self.grade)
        print("Job summary:", self.job_summary)
        print("===========")


############ FUNCTIONS ############
def get_jobs_list(self):
    return job_posts

############ MAIN ############
def main():
    
    #populate list of valid zips
    file = open("zip_code_database.csv")

    valid_zips = []
    for line in file:
        line = line.split(',')
        
        #skip line header
        if line[0] == 'zip':
            continue

        valid_zips.append(line[0])
        
    # Get zip code to search by parameters
    user_zip = "0"
    while user_zip not in valid_zips:
        user_zip = input("Enter a zip code:")
        
    data_elements = {"LocationID":user_zip}

    # get jobs data
    request = requests.get('https://data.usajobs.gov/api/jobs?', params=data_elements)
    json_data = request.json()

    # Parse jobs JSON tree into a list of objects
    job_posts = []
    for child in json_data['JobData']:
        job_posts.append(Child(child))
  

    # Now you have a list of federal jobs and you can
    # do whatever you want with it

    #print the job information
    for post in job_posts:
       post.print_job_details()
    return

    #return job_posts

############ MAIN PROGRAM LOGIC ############

main()
