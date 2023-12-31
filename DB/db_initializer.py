import aiomysql

# global variable
CONNECTION = None


async def get_connection():
    global CONNECTION
    if not CONNECTION:
        CONNECTION = await connect_db()
    return CONNECTION


async def connect_db():
    db_server_name = "sql6.freesqldatabase.com"
    db_user = "sql6636745"
    db_password = "UhpGRQK5m6"
    db_name = "sql6636745"
    char_set = "utf8mb4"
    cursor_type = aiomysql.cursors.DictCursor
    connection_object = await aiomysql.connect(host=db_server_name, user=db_user, password=db_password,
                                               db=db_name, charset=char_set, cursorclass=cursor_type)

    return connection_object
