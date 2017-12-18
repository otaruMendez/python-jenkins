
import jenkins
import sqlite3
import datetime

db = sqlite3.connect("seedstart-python-jenkins.sqlite")
iterator = db.cursor()
iterator.execute("create table if not exists jobs (name, status, time)")


server = jenkins.Jenkins('http://localhost:8080', username='xxxxxxxx', password='xxxxxx')
all_jobs = server.get_all_jobs()

for i, entry in enumerate(all_jobs):
    job_name = entry['name']
    job_status = entry['color']
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    iterator.execute("insert into jobs values (?, ?, ?)", (job_name, job_status, time_stamp))

#
# For Debugging purpose : To display all db entries 
#
# iterator.execute("select * from jobs")
# for job in iterator.fetchall():
#     print(job)

db.commit()
