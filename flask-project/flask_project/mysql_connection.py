import pymysql

class MySQLConnection:

    # Host: sql12.freesqldatabase.com
    # Database name: sql12730238
    # Database user: sql12730238
    # Database password: 6hWrY8SfEY
    # Port number: 3306
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def create_table(self, table_name, table_schema):
        """Creates a table with the specified name and schema."""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({table_schema})"
                cursor.execute(create_table_query)
                connection.commit()
                print(f"Table '{table_name}' created successfully.")
            except pymysql.MySQLError as e:
                print(f"Error creating table: {e}")
            finally:
                self.close()
        

    def connect(self):
        """Establishes a connection to the MySQL database."""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection successful!")
        except pymysql.MySQLError as e:
            print(f"Error connecting to database: {e}")
            self.connection = None
        return self.connection

    def get_connection(self):
        """Returns the connection object, establishing it if not already connected."""
        if self.connection is None:
            return self.connect()
        else:
            return self.connection
        
    def get_cursor(self):
        """ return cusror to execute queries"""
        if self.connection is None:
            self.get_connection()
        return self.connection.cursor()

    def close(self):
        """Closes the database connection if it exists."""
        if self.connection:
            try:
                self.connection.close()
                print("Connection closed.")
            except pymysql.MySQLError as e:
                print(f"Error closing connection: {e}")
