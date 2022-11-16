import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;UID=sch83401;PWD=j7QZUHGAtUGbPhns",'','')

#To retrive all the records from DB2

sql = "SELECT * FROM PLASMADONOR"
stmt = ibm_db.exec_immediate(conn, sql)
dictionary = ibm_db.fetch_both(stmt)
values=dictionary
while dictionary != False:
    #print(dictionary)
    print ("The Name is : ",  dictionary["NAME"])
    print ("The Email is : ", dictionary["EMAIL"])
    print ("The Phone is : ", dictionary["PHONE"])
    print(" ******************* ")
    values.update(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

print(values)
