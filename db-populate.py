# populating the database with records
import sqlite3

db_local = 'patients.db'
conn = sqlite3.connect(db_local)
c = conn.cursor()

# c.execute(""" INSERT INTO pInfo(pname, page, pgender, pbgrp, pmedhist, pphone, pdate, presult) VALUES('Rohan','34','M','A+','none','8454979345','21/04/2021','Tumor Detected')
#     """)


c.execute("""INSERT INTO doctors(dId, name, contact, description, website, city) VALUES(15, 'Dr. Devshi Visana','099048 65577','Dr. Devshi Visana is an experienced Neurologist from Ahmedabad endowed with high teaching and clinical skills in Neurology.', 'http://www.neurologistahmedabad.com/', 'Ahmedabad')""")
c.execute("""INSERT INTO doctors(dId, name, contact, description, website, city) VALUES(16, 'Dr. Sudhir Shah','079 2646 7052','At our neurology centre-clinic-I give neurology services on OPD base and offer consultation regarding variety of neurological problems like stroke, epilepsy, headaches, parkinsonism, dementia, ataxia, neuritis, multiple sclerosis amongst other diseases', 'http://www.sudhirneuro.org/', 'Ahmedabad')""")

# c.execute("""DELETE FROM doctors WHERE dId=3 """)

conn.commit()
conn.close()
