from models import DataSource
from com.phoenix.connections.connectionFactory import get_Connection

def test_Impala():
    ds = DataSource(db_type="Impala", host="10.10.8.102", database="fdm_db", port=21050)
    conn = get_Connection(ds)
    
    sql = 'select zsxm_dm,zsxmmc,zsxmjc,xybz,yxbz,sjzsxm_dm,yxqz,yxqq from odm_db.o_hx_qg_dm_gy_zsxm'
    rows=conn.query(sql)
    for row in rows:
        print("zsxm_dm:%s, zsxmmc:%s, zsxmjc:%s, xybz:%s, yxbz:%s, sjzsxm_dm:%s, yxqz:%s, yxqq:%s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

def test_MySQL():
    ds = DataSource(db_type="MySQL", host="10.10.8.104", database="fdm_db", port=4000, user="etlusr", password="etlusr")
    conn = get_Connection(ds)
    
    sql = 'select spbm,spmc from fdm_db.f_dm_gy_spbm'
    rows=conn.query(sql)
    for row in rows:
        print("spbm:%s, spmc:%s" % (row[0], row[1]))

#test_Impala()

test_MySQL()
