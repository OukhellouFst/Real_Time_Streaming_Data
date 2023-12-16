from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'smail-airscholar',
    'start_date' : datetime.now()
}

def get_data():
    import json
    import requests

    res = requests.get("https://randomuser.me/api/").json()
    return res['results'][0]
    
def format_data(res):
    data  = {}
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    location = res['location']
    data['address'] = f"{location['street']['number']} {location['street']['name']} " \
          f"{location['city']} {location['state']} {location['country']}" 
    data['postcode'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['register_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():
    import json 
    res = get_data()
    res = format_data(res)
    print(json.dumps(res,indent=3))


stream_data()

with DAG('user_automation',
        default_args=default_args,
        schedule_interval='@daily',
        catchup=False ) as dag: 
    
    streaming_task = PythonOperator(
        task_id = 'stream_data_from_api',
        python_callable= stream_data
    )
