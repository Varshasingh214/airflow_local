'''
Sample DAG authored by VS
'''
from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

args = {
    'owner': 'Airflow',
    'start_date':datetime(2022, 12, 27),
    'depends_on_past': True,
}

dag = DAG(
    dag_id='Hello_World_DAG',
    schedule='0 0 * * *',
    default_args=args,
    tags=['example',"example1"]
)

hello_my_task = BashOperator(
    task_id='hello_task',
    bash_command='echo "hello_world"',
    dag=dag
)

this_will_skip = BashOperator(
    task_id="this_will_skip",
    bash_command='echo "hello world"; exit 99;',
    dag=dag,
)

hello_my_task >> this_will_skip