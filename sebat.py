import pandas as pd
from sebatJobDataEncoder import JobDataEncoder
from sebatJobAnalysis import  organize_job_information

def organize_job_information_from_dict(job_data):
    organized_job = {
        'email': job_data.get('Email'),
        'password': job_data.get('Password'),
        'job_title': job_data.get('job_title', '').strip(),
        'job_description': job_data.get('job_description', '').strip(),
        'application_deadline': job_data.get('application_deadline', '').strip(),
        'job_sector': job_data.get('job_sector'),
        'job_type': job_data.get('job_type'),
        'skills': job_data.get('skills'),
        'job_apply_type': job_data.get('job_apply_type'),
        'job_apply_url': job_data.get('job_apply_url'),
        'job_apply_email': job_data.get('job_apply_email'),
        'salary_type': job_data.get('salary_type'),
        'min_salary': job_data.get('min_salary'),
        'max_salary': job_data.get('max_salary'),
        'salary_currency': job_data.get('salary_currency'),
        'salary_position': job_data.get('salary_position'),
        'salary_separator': job_data.get('salary_separator'),
        'salary_decimals': job_data.get('salary_decimals'),
        'experience': job_data.get('experience'),
        'gender': job_data.get('gender'),
        'qualifications': job_data.get('qualifications'),
        'field_of_study': job_data.get('field_of_study'),
        'career_level': job_data.get('career_level'),
        'country': job_data.get('country'),
        'state': job_data.get('state'),
        'city': job_data.get('city'),
        'postal_code': job_data.get('postal_code'),
        'full_address': job_data.get('full_address'),
        'latitude': job_data.get('latitude'),
        'longitude': job_data.get('longitude'),
        'zoom': job_data.get('zoom')
    }

    return organized_job

if __name__ == "__main__":
    # Read job data from Excel
    excel_path = 'Job_details_V0.1_06-18-2024.xlsx'
    job_df = pd.read_excel(excel_path)


    for index, row in job_df.iterrows():
        job_data = row.to_dict()
        jobInfo=organize_job_information_from_dict(job_data)
        print("Befor Gpt Job  orginized",job_data)
        # job=organize_job_information(jobInfo)
        print("After Gpt Job  orginized",jobInfo)
        encoder = JobDataEncoder(login_url='https://gamezone.7jobs.co', username=jobInfo['email'], password=jobInfo['password'])
        # if encoder.register_employer_account(registration_data):
        #     print("Employer account registration successful!")
        if encoder.login():
             if encoder.navigate_to_post_job():
                 # Fill the job form
                encoder.fill_post_job_form(jobInfo)
                #Logout after posting job
                if encoder.logout():
                    print("Logged out successfully after posting job.")
                else:
                    print("Failed to log out.")
        # encoder.close()
    else:
        print("Failed to log in.")
        # encoder.close()

