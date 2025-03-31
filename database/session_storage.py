# from database.database import connectionDB
from datetime import datetime


def main():
    create_session()

def create_session(time):
    # connection_toDB = connectionDB()

    today_date = datetime.today().strftime('%Y-%m-%d')
    print(type(today_date))

    # connection_toDB.execute(f"CREATE TABLE study_sessions({today_date},{time})")


def update_session():
    ...

if __name__ == "__main__":
    main()