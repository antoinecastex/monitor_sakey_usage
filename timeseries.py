import google.auth
import json
from google.auth.transport.requests import AuthorizedSession

credentials, project = google.auth.default(
scopes=['https://www.googleapis.com/auth/cloud-platform'])

def timeSeries():
    TIMESERIES_URL = "https://monitoring.googleapis.com/v3/projects/myproject/timeSeries?filter=metric.type%3D%22iam.googleapis.com%2Fservice_account%2Fkey%2Fauthn_events_count%22%20AND%20metric.labels.key_id%3D%22"+str(KEY_ID)+"%22&interval.endTime=2021-04-26T15:01:23Z&interval.startTime=2021-04-20T15:01:23Z"
    AUTHORIZED_SCOPE = ["https://www.googleapis.com/auth/cloud-platform"]
    credential = google.auth.default(scopes=AUTHORIZED_SCOPE)[0]
    authed_session = AuthorizedSession(credential)
    response = authed_session.request(
    method="GET", url=TIMESERIES_URL)
    key_usage = response.json()
    test =  "timeSeries" in key_usage
    if test is True:
        timeSeries = key_usage['timeSeries'][0]['points']
        for window in timeSeries:
            print(window['interval']['startTime'])
            print(window['interval']['endTime'])
            print(window['value']['int64Value'])