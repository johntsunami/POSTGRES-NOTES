# Must install the postgres software first from their website.  
# Used default server,db,port,username, inputted password which does not populate on the cmd fyi.. just entered it and pressed enter
# open PGADMIN GUI to view tables in posgres


import psycopg2
 
# Connect to your postgres DB
con = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='winwin',
    )

# Open a cursor to perform database operations
cur = con.cursor()

################################################
#####################   CREATE ################

        ### CREATE DATABASE ### 
#CANNOT BE DONE INSIDE TRANSACTION BLOCK #DID IT THROUGH THE  PGADMIN GUI


        ### CREATE TABLE ### 
# cur.execute("CREATE TABLE test_table (id serial PRIMARY KEY, num integer, data varchar);")

        ### CREATE TABLE PREVENT DUPLICATE ###   IF ERROR psycopg2.errors.DuplicateTable: relation "table3" already exists
# cur.execute("CREATE TABLE IF NOT EXISTS table3 (id serial PRIMARY KEY, num integer, data varchar);")


        ### Add NEW column to existing table
# cur.execute("ALTER TABLE test_table ADD city VARCHAR(100);")

 

####################  Add data to TABLE Placeholders in NEW ROW ##############
# cur.execute("INSERT INTO test_table (num, data) VALUES (%s, %s)",(200, "New_data"))



        ### Add data to part of a row ###
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(350, "cat"))


###############################################################
####################  CHANGE DATA #############################
    ## UPDATE ALL LINES OF A COLUMN TO SAME DATA ###    
# cur.execute("UPDATE test SET num = 333;")  #if says NO RESULTS TO FETCH.. its because you cant print CUR from this function.. it only updates it.

    ## UPDATE ONE LINE and one column OF DATA TO SPECIFIC VALUE
# cur.execute("UPDATE test SET data = 'cat' WHERE ID = 3;")


    ### UPDATE ONE LINE OF DATA TO NULL IN SPECIFIC COLUMN
# cur.execute("UPDATE test SET num = NULL WHERE ID = 1;")




###########################################################
#########################  ACCESS  ########################

    ### PRINT COLUMN NAMES  ###       # IF U WANT DATA TOO JUST print for i in cur.. print i
# cur.execute("Select * FROM test_table")
# colnames = [desc[0] for desc in cur.description]
# print(colnames)

    ### PRINT COLUMN NAMES WITH types ###
# cur.execute("Select * FROM test_table")
# colnames = cur.description
# print(colnames)

    ### PRINT ROWS OF TABLE ###
# cur.execute("SELECT * FROM test_table")
# for row in cur:
#     print(row)


    ### Print column ###
# cur.execute("SELECT id FROM test_table")
# for row in cur:
#     print(row)

    ### PRINT Multiple COLUMNS ###
# cur.execute("SELECT id,num FROM test_table")
# for row in cur:
#     print(row)

  ##########  Print / Filter Data by ID ############
# cur.execute("SELECT * FROM test_table WHERE id = 1")  # CAN USE ANY PYTHON OPERATORS > <, != ETC, OR, AND, NOT, IN,NOT IN, 
# for row in cur:
#     print(row)

    ### FILTER DATA BY MULTIPLE VALUES ####
# cur.execute("SELECT * FROM test_table WHERE id IN (1,2)")  # CAN USE ANY PYTHON OPERATORS > <, != ETC, OR, AND, NOT, IN,NOT IN
# for row in cur:
#     print(row)

    ### FILTER BETWEEN TWO NUMS ###
# cur.execute("SELECT * FROM test_table WHERE id BETWEEN 1 AND 2")  # CAN USE ANY PYTHON OPERATORS > <, != ETC, OR, AND, NOT, IN,NOT IN
# for row in cur:
#     print(row)


    ### PRINT Sorted A-Z or SMall to Big.
# cur.execute("SELECT * FROM test_table ORDER BY data")  #Sorts A to Z
# for row in cur:
#     print(row)

    ### GET ONLY NON DUPLICATES IN A COLUMN ###
# cur.execute("SELECT DISTINCT num FROM test_table")   
# for row in cur:
#     print(row)

    ############ CALCULATE WITHIN FUNCTION ###############

# CHANGE ORDER OF OPERATIONS IN MATH  using ()
# cur.execute("SELECT id,(num + 10) * 100 FROM test_table")
# for row in cur:
#     print(row)

# PRINT Calculated new column with its own name
# cur.execute("SELECT id,num,(num + 10) * 100 as new_col FROM test_table")
# for row in cur:
#     print(row)

    #################### SEARCHING BY STRINGS ##########################
        ####  FIND ROW BY STRING that starts with char ###
# cur.execute("SELECT * FROM test_table WHERE data LIKE 'N%' ")

        ###FIND ROW with STRING anywhere in it ###
# cur.execute("SELECT * FROM test_table WHERE data LIKE '%data%' ")

        ###FIND ROW with that ENDS WITH char ###
# cur.execute("SELECT * FROM test_table WHERE data LIKE '%a' ")

        # FIND ROW BY STR WITH A CERTAIN CHAR AND NUMBER OF CHAR
# cur.execute("SELECT * FROM test_table WHERE data LIKE '_______a' ")

        # FIND STR THAT STARTS AND ENDS WITH CERTAIN CHAR AND HAS SAME LEN ##
# cur.execute("SELECT * FROM test_table WHERE data LIKE 'N______a' ")

        ### FIND STR that doesnt contain these char ###
# cur.execute("SELECT * FROM test_table WHERE data NOT LIKE 'New_%' ")
   
        ### Video 8 shows regexp searches for strings.. id on't think this library supports it. because this didn't work
# cur.execute("SELECT * FROM test_table WHERE REGEXP 'New_data'")

        ###  Find line that is missing / empty data.. aka has NULL in space.
# cur.execute("SELECT * FROM test_table WHERE data is NULL")

        ## OPOSITE of Null... find data that is not missing info 
# cur.execute("SELECT * FROM test_table WHERE data is NOT NULL")    

        ### RECEIVE LINES OF DATA IN CERTAIN ARANGMENT ###
# cur.execute("SELECT * FROM test ORDER BY data")   
       
        ### SORT IN DESC ORDER ###    
# cur.execute("SELECT * FROM test ORDER BY data DESC")  

        ### Sort multiple rows by two columns.. First one is priority.. second one follows ###
# cur.execute("SELECT * FROM test ORDER BY data,num")   
        ### Saving alias name to sorting
# cur.execute("SELECT num + 300 AS new_number FROM test WHERE data = 'cat' ORDER BY new_number DESC") 

        ### LIMIT THE NUMBER OF RECORDS RETURNED FROM QUERY ###  
# cur.execute("SELECT num FROM test LIMIT 3")   # EX1
# cur.execute("SELECT num + 300 AS new_number FROM test WHERE data = 'cat' ORDER BY new_number DESC LIMIT 2")   #EX 2

        ### SKIP FIRST record then select the ones after
# cur.execute("SELECT num FROM test LIMIT 3 OFFSET 1")  ### OFFSET IS THE NUMBER OF ITEMS TO SKIP.. might just be for postgres for mysql maybe try cur.execute("SELECT num FROM test LIMIT 3,1")


#############################################################
        ####  COMBINE ALL COLUMNS OVER MULTIPLE TABLES that EQUAL ID ##############################
# cur.execute("SELECT * FROM test JOIN test_table ON test.id = test_table.id ")

        ### COMBINE COLUMNS FROM TWO TABLES
# cur.execute("SELECT data,name FROM test JOIN test_table ON test.id = test_table.id")

        ### COMBINE SOME COLUMNS OVER TWO TABLES THAT DONT HAVE SAME COLUMN NAMES ###
# cur.execute("SELECT * FROM test JOIN test_table ON test.id = test_table.id")

        ### COMBINE SOME COLUMNS OVER TWO TABLES THAT ""HAVE""" SAME COLUMN NAMES ###

                #VIDEO 1
                #first column , second column on separate table
# cur.execute("SELECT te.favorite_animal,t.city  FROM test te JOIN test_table t ON te.id = t.id")   # Just have to prefix the column name with one of the table names since we are searching for items w same id, can abbreviate tables on the FROM

        ### COMBINE COLUMNS OF DATA FROM MULTIPLE DATABASES
# cur.execute("SELECT te.favorite_animal,t.city  FROM test te JOIN test_table t ON te.id = t.id")
## PREFIX only the current database

        ### JOIN TABLE WITH ITSELF ###
# cur.execute("SELECT te.favorite_animal,a.favorite_plant  FROM test te JOIN test a ON a.id = te.id")

        ### JOIN MORE THAN 2 tables ###                     # MIGHT NEED TO SELECT SQL database as "USE database_name;"
# cur.execute("SELECT * FROM test t JOIN test_table te ON t.id = te.id JOIN table3 t3 ON t.id = te.id")

        ## JOIN CERTAIN COLUMN FROM 3 columns or more
# cur.execute("SELECT te.data FROM test t JOIN test_table te ON t.id = te.id JOIN table3 t3 ON t.id = te.id")

        ### ON VIDEO 5





try:
    for row in cur:
        print(row)
except:
    pass
















con.commit()
con.close()



######RULES
# if you want two words without _ between then use quotes around them like a regular string within your query.
# ONLY SORT BY COLUMN NAMES NOT POSITIONS AS SOME PROGRAMMERS DO.. he explains on 9- order by clause
## CURRECT ORDER ..  SELECT-FROM-WHERE-ORDER BY-LIMIT
# Use separate tables for data that changes often and ones that dont'







