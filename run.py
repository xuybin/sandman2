from sandman2 import get_app

app = get_app('sqlite+pysqlite:///tests/data/db.sqlite3')
#app = get_app('mysql+pymysql://blog:blog@localhost:32768/blog')

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
