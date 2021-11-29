import csv

def filehandle(info):
    with open('student_details.csv', 'a' , newline="") as csv_file:

        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(['Name','Age','Contact Number','Email-ID'])

        writer.writerow(info)

if __name__ == '__main__':

    condition = True
    student_num = 1

    while(condition):

        student_details = input("\nEnter Student details for student {0} in following format (Name, Age, Contact_Number, Email_ID ) : ".format(student_num))

        student_info =  student_details.split(',')

        try:
            print('\nEntered details are :\nName : {}\nAge : {}\nContact Number : {}\nEmail-Id : {}'
                .format(student_info[0],student_info[1],student_info[2],student_info[3]))
        except:
            print("invalid input")
        
        user_choice = input('\nAre the entered values correct? (yes/no) : ')

        if user_choice == "yes":
            filehandle(student_info)
            condition_check = input('\nDo you want to enter details for another student (yes/no) : ')

            if condition_check == "yes":
                condition=  True
                student_num += 1

            elif condition_check == "no":
                condition = False

            else:
                print("Wrong Input")

        elif user_choice == 'no':
            print('\nPlease re-enter your values')
        
        else:
            print("Wrong Input")
