from datetime import datetime

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'admin',
    'start_date': datetime(2021, 3, 1, 12, 0, 0)
}

def hello_devops_loop():
    for event in ['hello', 'world']:
        print(event)

with DAG(
    dag_id='hello_devops',
    default_args = default_args,
    schedule_interval='@once'
) as dag:

    test_start = DummyOperator(task_id='test_start')

    test_python = PythonOperator(task_id='test_python', python_callable=hello_devops_loop)

    test_bash =  BashOperator(task_id='test_bash', bash_command='echo Hello Devops!')

test_start >> test_python >> test_bash

