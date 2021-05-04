from google.cloud import bigquery

bigqueryClient = bigquery.Client()

def bigqueryInsert(
    var_projectid,
    var_saemail,
    var_said,
    var_keyid,
    var_start,
    var_end,
    var_value):
    row = [
        {
        u"project_id": var_projectid,
        u"sa_email": var_saemail,
        u"sa_id": var_said,
        u"key_id": var_keyid,
        u"start_time": var_start,
        u"end_time": var_end,
        u"value": var_value
        }
    ]
    bigqueryClient.insert_rows_json("dataset.table", row, row_ids=[None] * len(row))