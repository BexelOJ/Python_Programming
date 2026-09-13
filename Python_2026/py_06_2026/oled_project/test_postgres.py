import psycopg
from datetime import datetime

conn = psycopg.connect(
    host="127.0.0.1",
    port=5432,
    dbname="yantraSthiti_DB",
    user="monitor_yantrasthiti_app",
    password="SUPPORt@1615"
)

with conn.cursor() as cur:

    cur.execute(
        """
        INSERT INTO system_metrics
        (timestamp, device_id, ip, cpu, ram, disk)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            datetime.now(),
            "Ei Labs Server_01",
            "127.0.0.1",
            30.5,
            45.2,
            57.8
        )
    )

conn.commit()

print("Data inserted successfully!")

conn.close()


