
Writing DAGs	
**1.**	**Make the imports**:
Begin with always importing Python DAG class. After which Operator imports are required.

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

** please note DummyOperator is deprecated, use EmptyOperator when we just want to group tasks in DAG. They are just scheduled but never executed.

**2.	Create python DAG object**
DAG object should consists of:
i)	Dag_id : unique identifier of DAG.
ii)	Start_date: tells when to begin the DAG
iii)	Schedule_interval: tells the time interval of when to trigger the DAG.
In case of warning related to deprecation, we can use schedule only.
There are 2 ways to set intervals:
a)	Using Cron job
Cron is used to automate tasks on Unix like operating system.
b)	Using timedelta object: helps in calculating differences in dates.
iv)	Catchup: is always set to False as it prevents DAG from running backfilling non-triggered DAGs.


**3.	Adding the tasks**
Here comes operators in action. We define task_id of each task and the operation to perform.

run_this_last = EmptyOperator(
    task_id="run_this_last",
)

run_this = BashOperator(
    task_id="run_after_loop",
    bash_command="echo 1",
)

**4.	Defining dependencies**
Dependencies are defined using left bitshift and right bitshift operators.
	
		run_this >> run_this_last

'run_this' will be executed first and then 'run_this_last' will be executed.


Save & place the dag.py as follows:  airflow -> example->dags -> your_dag.py

Alternatively, if not sure about where to save the dag.py. 
Execute 'airflow dags list' on terminal, it will list the paths of all the default dags which are available at UI.
This will give the correct path to place our dag.

Place the dag.py, run it once.
Open terminal on pycharm, type 'airflow standalone' to start all the components.
Navigate to UI via the provided link at terminal,alternatively at localhost:8080.
At same time, login credentials will also be provided.
At UI, we can see the dag.py which we have created. 
Click on it, un-pause that and trigger the dag.
At last, do Ctrl+C to shutdown all the airflow’s components & we can see the UI going down. 



