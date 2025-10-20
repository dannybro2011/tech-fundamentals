import sqlite3

def connect_create():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS student_db(stu_id INT, name VARCHAR(255), grade VARCHAR(255), email VARCHAR(255))')
    conn.close()

# ===============================
# STEP 4: INSERT DATA
# ===============================
def insert_data():
    #so everytime this is called it asks for 4 inputs
    conn = sqlite3.connect('students.db') #connect back to that shit since it was closed
    cursor = conn.cursor()
    #grabbing the 4 inputs and formatting it
    user_input = input('enter student id, name, grade, email -- all separated by a comma no space').strip().replace(" ", "")
    #splitting the 4 inputs 
    stu_id, name, grade, email = user_input.split(',')
    #convert to valid inputs:
    #convert stu_id from str to int
    name = name.title()
    while True:
        try:
            stu_id = int(stu_id)
            break
        except ValueError:
            print('enter a whole number -- student IDs are whole numbers')

    while '@' not in email:
        email = input('Invalid email, must contain \'@\'. Retry: ').strip()

    try:
        cursor.execute('INSERT INTO student_db VALUES (?, ?, ?, ?)', (stu_id, name, grade, email))
        conn.commit() #save changes
        print("Records inserted successfully...")
    except Exception as e:
        print("Insert failed:", e)
        conn.rollback() #revert changes if an error occurs
    conn.close()

# ===============================
# STEP 5: READ DATA
# ===============================
def read_data():
    #i dont think this needs changing at all right? just prints the table
    conn = sqlite3.connect('students.db') #open dat shiet back up
    cursor = conn.cursor()
#to retrieve data from a table, the SELECT * SQL query is used
    cursor.execute("SELECT * FROM student_db")
    records = cursor.fetchall() #fetch all rows from results — the 3 rows inserted earlier
    for row in records:
        print(row)
    conn.close()

# ===============================
# STEP 6: UPDATE DATA
# ===============================
def update_data():
    conn = sqlite3.connect('students.db') #OPEN IT AGAIN
    cursor = conn.cursor()
    stu_id = int(input('which student ID\'s row to update? enter student ID: \n'))

    field = input('which field? (id, name, grade, email): \n').strip().lower()
    #hmmm okay this might get complicated. how do i selectively execute on individual fields of a student's information -- i dont know the proper SQL syntax 
    try:
        match field:
            case 'id':
                try:
                   new_id = int(input('enter new id: ').strip())
                   cursor.execute('UPDATE student_db SET stu_id = ? WHERE stu_id = ?', (new_id, stu_id))
                except:
                    print('enter a whole number -- student IDs are whole numbers')
            case 'name':
                new_name = input('Enter new name: ').strip().title()
                cursor.execute('UPDATE student_db SET name = ? WHERE stu_id = ?', (new_name, stu_id))
            case 'grade':
                new_grade = input('Enter new grade: ').strip()
                cursor.execute('UPDATE student_db SET grade = ? WHERE stu_id = ?', (new_grade, stu_id))
            case 'email':
                while True:
                    new_email = input('Enter new email: ')
                    if '@' not in new_email:
                        print('invalid email: must contain \'@\'')
                        continue
                    break
            case _:
                print('Invalid choice. Try again.')

                cursor.execute('UPDATE student_db SET email = ? WHERE stu_id = ?', (new_email, stu_id))           
        conn.commit()
        print("Record updated successfully...")
    except Exception as e:
        print("Update failed:", e)
        conn.rollback()
    conn.close()

# ===============================
# STEP 7: DELETE DATA
# ===============================
def delete_data():
    conn = sqlite3.connect('students.db') #OPEN YET AGAIN
    cursor = conn.cursor()
    try:
        stu_id = int(input('which student\'s row would you like to delete, input the student\'s ID verbatim').strip())
    except ValueError:
        print('enter a whole number -- student IDs are whole numbers')
    
    decision = input(f'are you sure you want to delete the record of {stu_id}? Enter yes or no: ').lower().strip()
    while decision not in ('yes', 'no'):  # reprompt if they typed bull
            decision = input('Invalid input. Enter YES or NO:\n').strip().lower()

    while decision == 'yes':
        try:
            #this execute yeeted row 3 from existence 
            cursor.execute('DELETE FROM student_db WHERE stu_id = ?', (stu_id,))
            conn.commit()
            print("Record deleted successfully...")
        except Exception as e:
            print("Delete failed:", e)
            conn.rollback()
    conn.close()

def main():
    #text based menu
    #prompt user if they want to open student_db, if yes
    decision = input('Do you want to open the student database? Enter yes or no: ').strip().lower()

    while decision not in ('yes', 'no'):  # reprompt if they typed bull
            decision = input('Invalid input. Enter YES or NO:\n').strip().lower()

    connect_create()
    while decision == 'yes':
        
        choice = input('do you want to 1. add new record, 2. view existing records, 3. update record, 4. delete record. Enter 1,2,3, or 4: ')
        match choice:
            case '1':
                insert_data()
            case '2':
                read_data()
            case '3':
                update_data()
            case '4':
                delete_data()
            case _:
                print('Invalid choice. Try again.')
        decision = input('Enter YES to perform more actions or NO to exit:\n').strip().lower()
        while decision not in ('yes', 'no'):  # reprompt if they typed bull
            decision = input('Invalid input. Enter YES or NO:\n').strip().lower()

# ===============================
# MAIN EXECUTION
# ===============================
if __name__ == "__main__":
    main()