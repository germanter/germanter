import pymysql
# from dotenv import load_dotenv  ###shut down all dotenv in push
import os

# load_dotenv()  ###shut down all dotenv in push
def load_data():
    timeout = 10
    connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="mysql-2b98ccbd-usersuer32-ae57.e.aivencloud.com",
    password=os.getenv('passdb'),  ###security
    read_timeout=timeout,
    port=10406,
    user="avnadmin",
    write_timeout=timeout,
    )
    
    try:
        dataset = []
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM jobs")
        info = cursor.fetchall()
        for i in info:
            dataset.append(dict(i))
        print("SUCCESSFUL DATABASE CONNECTION!")
        return dataset
    except:
        print('FAILED DATABASE CONNECTION!')
    finally:
        connection.close()
        
def load_job(id):
    timeout = 10
    connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="mysql-2b98ccbd-usersuer32-ae57.e.aivencloud.com",
    password=os.getenv('passdb'),  ###security
    read_timeout=timeout,
    port=10406,
    user="avnadmin",
    write_timeout=timeout,
    )
    
    try:
        dataset = []
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM jobs WHERE id = %s",(id,))
        info = cursor.fetchall()
        for i in info:
            dataset.append(dict(i))
        print("SUCCESSFUL DATABASE CONNECTION!")
        return dataset
    except:
        print('FAILED DATABASE CONNECTION!')
    finally:
        connection.close()

def insert_application(job_id,appl):
    timeout = 10
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="mysql-2b98ccbd-usersuer32-ae57.e.aivencloud.com",
        password=os.getenv('passdb'),  ###security
        read_timeout=timeout,
        port=10406,
        user="avnadmin",
        write_timeout=timeout,
    )
    
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO applications (job_id, full_name, email, work_experience, resume_link) VALUES(%s,%s,%s,%s,%s)",
            (
                job_id,
                appl['full_name'],
                appl['email'],
                appl['work_experience'],
                appl['resume_link'],
                
            )
        )
        connection.commit()
        print("APPLICATION SUCCESSFULLY INSERTED!")
    except Exception as e:
        print(f"FAILED TO INSERT APPLICATION: {e}")
    finally:
        connection.close()