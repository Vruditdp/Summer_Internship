import mysql.connector
# Vruditkumar D Patel

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="test")
mycursor = mydb.cursor()
mycursor.execute("create table if not exists studentData(enrollment_no int, name VARCHAR(50), marks INT)")

while(True):
    print('\t Press Appropriate key : \n\t 1. To Insert Data in Table.\n\t 2. Display Data from Dtabase.\n\t 3. Update Data in Database.\n\t 4. Delete Data in Dtatabase.\n\t 5. To exit from the program.')
    c=int(input('Please enter your choice.'))
    # INSERT
    if c==1:
        enrollment_no=int(input('Enter the Enrollment Number of Student :'))
        name=input('Enter the name of student :')
        marks=int(input('Enter marks of student :'))
        mycursor.execute("insert into studentData values({},'{}',{})".format(enrollment_no, name, marks))
        mydb.commit()
        print('...SUCCESS...')
        
    elif c==2:
        print('\n\t\tPress 1 if you want to fetch data of particular studend \n\t\tPress 2 if you want to fetch all data.')
        c1=int(input('Enter your choice:'))
        if c1==1:
            enrollment_no=int(input('Enter the Enrollment Number of Student :'))
            mycursor.execute("select*from studentData where enrollment_no={}".format(enrollment_no))
            result=mycursor.fetchall()
            for i in result:
                enrollment_no=i[0]
                name=i[1]
                marks=i[2]
                print(enrollment_no,name,marks)
        elif c1==2:
            mycursor.execute("select*from studentData")
            result=mycursor.fetchall()
            for i in result:
                enrollment_no=i[0]
                name=i[1]
                marks=i[2]
                print(enrollment_no,name,marks)
    #UPDATE
    elif c==3:
        old_number=int(input('\tEnter old enrollment number:'))
        new_name=input('\tEnter new name of student:')
        new_marks=int(input('Enter new marks:'))
        mycursor.execute("UPDATE studentData SET name='{}', marks={} WHERE enrollment_no={}".format(new_name, new_marks, old_number))
        mydb.commit()
        print('Record Updated Successfully...!')

    #DELETE
    elif c==4:
        number=int(input('\tEnter the enrollment number of student whose data you want to delete:'))
        mycursor.execute("DELETE FROM studentData WHERE enrollment_no={}".format(number))
        mydb.commit()
        print('Record deleted Successfully...!')

    elif c==5:
        print('Have a nice day.....')
        mydb.close()
        break    

    else:
        print('Your input is incorrect, Please check again')    
# Vruditkumar D Patel        
print('Good Bye.....!')


        
        
    
    














