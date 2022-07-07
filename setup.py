from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])

session = cluster.connect()

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS codebank
    WITH REPLICATION = {
        'class': 'SimpleStrategy', 'replication_factor': 1
    };
""")

session.set_keyspace("codebank")