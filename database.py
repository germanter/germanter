import pymysql
# from dotenv import load_dotenv  ### shut down all dotenv in push
import os

# load_dotenv()  ### shut down all dotenv in push

def get_db_connection():
    return pymysql.connect(
        charset="utf8mb4",
        connect_timeout=10,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="mysql-2b98ccbd-usersuer32-ae57.e.aivencloud.com",
        password=os.getenv('passdb'),  ### security
        read_timeout=10,
        port=10406,
        user="avnadmin",
        write_timeout=10,
    )

def load_data():
    connection = get_db_connection()
    try:
        dataset = []
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM jobs")
        info = cursor.fetchall()
        for i in info:
            dataset.append(dict(i))
        print("SUCCESSFUL DATABASE CONNECTION!")
        return dataset
    except Exception as e:
        print(f"FAILED DATABASE CONNECTION: {e}")
    finally:
        connection.close()

def load_job(id):
    connection = get_db_connection()
    try:
        dataset = []
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM jobs WHERE id = %s", (id,))
        info = cursor.fetchall()
        for i in info:
            dataset.append(dict(i))
        print("SUCCESSFUL DATABASE CONNECTION!")
        return dataset
    except Exception as e:
        print(f"FAILED DATABASE CONNECTION: {e}")
    finally:
        connection.close()

def insert_application(job_id, appl):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO applications (job_id, full_name, email, work_experience, resume_link) VALUES(%s, %s, %s, %s, %s)",
            (
                job_id,
                appl['full_name'],
                appl['email'],
                appl['work_experience'],
                appl['resume_link'],
            ),
        )
        connection.commit()
        print("APPLICATION SUCCESSFULLY INSERTED!")
        return 1
    except Exception as e:
        print(f"FAILED TO INSERT APPLICATION: {e}")
        return 0
    finally:
        connection.close()
