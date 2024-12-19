import pymysql
from dotenv import load_dotenv
import os

load_dotenv()  ###security
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