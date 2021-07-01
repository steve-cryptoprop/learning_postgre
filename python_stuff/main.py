import psycopg2


from connetion import CONNECTION



def main():
    with psycopg2.connect(CONNECTION) as conn:
        query_create_sensors_table = "CREATE TABLE sensors (id SERIAL PRIMARY KEY, type VARCHAR(50), location VARCHAR(50));"
        query_create_sensordata_table = """CREATE TABLE sensor_data (
                                           time TIMESTAMPTZ NOT NULL,
                                           sensor_id INTEGER,
                                           temperature DOUBLE PRECISION,
                                           cpu DOUBLE PRECISION,
                                           FOREIGN KEY (sensor_id) REFERENCES sensors (id)
                                           );"""

        query_create_sensordata_hypertable = "SELECT create_hypertable('sensor_data', 'time');"
        cursor = conn.cursor()
        cursor.execute(query_create_sensors_table)
        cursor.execute(query_create_sensordata_table)
        cursor.execute(query_create_sensordata_hypertable)
        # commit changes to the database to make changes persistent
        conn.commit()
        cursor.close()        

if __name__ == '__main__':
    main()