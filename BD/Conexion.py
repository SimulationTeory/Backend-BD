from sqlalchemy import create_engine

class ConectionBD:

    def __init__(self):
        self.server = "serverunah.database.windows.net"
        self.database = "bdunah"
        self.user = "adminunah"
        self.password = "Unah1800"  
        self.driver = "ODBC+Driver+18+for+SQL+Server"

    def getConection(self):
        try:
            connection_str = (
                f"mssql+pyodbc://{self.user}:{self.password}@{self.server}/{self.database}"
                f"?driver={self.driver}"
                "&Encrypt=yes"
                "&TrustServerCertificate=no"
                "&ConnectionTimeout=30"
            )

            engine = create_engine(connection_str)

            conn = engine.connect()
            conn.close()
            return engine

        except Exception as e:
            print(e)
            return None
