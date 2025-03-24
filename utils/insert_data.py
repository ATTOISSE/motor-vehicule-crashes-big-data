import psycopg2
import csv
import os

DATABASE_URL = os.getenv("DATABASE_URL","postgresql://user:password@postgres-db:5432/accidents")
table_name = "motos_craches"

create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    Year INT,
    CaseVehicleID BIGINT PRIMARY KEY,
    VehicleBodyType VARCHAR(50) NULL,
    RegistrationClass VARCHAR(50) NULL,
    ActionPriorToAccident VARCHAR(100) NULL,
    TypeAxlesOfTruckOrBus VARCHAR(50) NULL,
    DirectionOfTravel VARCHAR(50) NULL,
    FuelType VARCHAR(50) NULL,
    VehicleYear INT NULL,
    StateOfRegistration VARCHAR(10) NULL,
    NumberOfOccupants INT NULL,
    EngineCylinders INT NULL,
    VehicleMake VARCHAR(50) NULL,
    ContributingFactor1 VARCHAR(50) NULL,
    ContributingFactor1Description VARCHAR(100) NULL,
    ContributingFactor2 VARCHAR(50) NULL,
    ContributingFactor2Description VARCHAR(100) NULL,
    EventType VARCHAR(100) NULL,
    PartialVIN VARCHAR(50) NULL
);
"""


table_columns = [
    'Year', 'CaseVehicleID', 'VehicleBodyType', 'RegistrationClass', 
    'ActionPriorToAccident', 'TypeAxlesOfTruckOrBus', 'DirectionOfTravel', 
    'FuelType', 'VehicleYear', 'StateOfRegistration', 'NumberOfOccupants', 
    'EngineCylinders', 'VehicleMake', 'ContributingFactor1', 
    'ContributingFactor1Description', 'ContributingFactor2', 
    'ContributingFactor2Description', 'EventType', 'PartialVIN'
]


try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connexion réussie à la base de données")
    conn.close()
except Exception as e:
    print(f"Erreur de connexion : {e}")

print(table_name)

insert_query = f"""
    INSERT INTO {table_name} ({', '.join(table_columns)})
    VALUES ({', '.join(['%s' for _ in table_columns])})
    ON CONFLICT DO NOTHING;
"""

def get_conn():
    return psycopg2.connect(DATABASE_URL)

def create_user_table(conn):
    cur = conn.cursor()
    try:
        cur.execute(create_table_query)
        conn.commit()
        print("Table users created successfully or already exists.")
        cur.close()
    except Exception as e:
        print(f"Error: {e}")

def insert_user_data(conn, input_file_path):
    with conn.cursor() as cursor, open(input_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Ignorer la première ligne si c'est un header
        
        insert_query = f"""
        INSERT INTO {table_name} ({', '.join(headers)})
        VALUES ({', '.join(['%s' for _ in headers])})
        ON CONFLICT DO NOTHING;
        """

        for row in reader:
            # Remplace les chaînes vides par None (NULL dans PostgreSQL)
            row = [None if value == '' else value for value in row]
            cursor.execute(insert_query, row)

    conn.commit()
    
    cursor.close()
    print(f"Data successfully loaded from {input_file_path} into the users table.")

if __name__ == '__main__':
    conn = get_conn()
    create_user_table(conn)
    insert_user_data(conn, "data/Motor.csv")
    # insert_user_data(conn, "data/countries.csv")
