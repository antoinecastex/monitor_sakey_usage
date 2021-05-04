import google.auth
from googleapiclient import discovery

credentials, project = google.auth.default(
scopes=['https://www.googleapis.com/auth/cloud-platform'])
resourceManagerClient = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

def iam_projects_list():
    projects_list = resourceManagerClient.projects().list().execute()
    for project in projects_list['projects']:
        project_id = project['projectId']

def iam_sa_list():
    iamClient = discovery.build('iam', 'v1', credentials=credentials)
    accounts_list = iamClient.projects().serviceAccounts().list(name="projects/myproject").execute()
    for service_account in accounts_list['accounts']:
        key = iamClient.projects().serviceAccounts().keys().list(name=service_account['name']).execute()
        for sa_key in key['keys']:
            if sa_key['keyType'] == "USER_MANAGED":
                Key_ID = (key['name']).split("keys/")[1]
                Service_Account = accounts_list['name']
                Service_Account_ID = accounts_list['uniqueId']