from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])

session = cluster.connect()

session.set_keyspace('codebank');

session.execute("""CREATE TABLE IF NOT EXISTS problems_by_tag(
        id text,
        title text,
        type text,
        difficulty int,
        company text,
        submits int,
        solved int,
        tag text,
        time_step bigint,
        PRIMARY KEY((tag), id));
    """)

session.execute("""
    CREATE MATERIALIZED VIEW company_tags AS
        SELECT * FROM problems_by_tag
        WHERE tag IS NOT NULL AND difficulty IS NOT NULL AND id IS NOT NULL AND company IS NOT NULL
        PRIMARY KEY ((company, tag), id);
""")