class Reservation : 
    # constructor
    def __init__(self) :
        try:
            # open the TEXT.TXT to read the content
            file = open('text.txt', 'r')
            # get the last row of the list(content of the TEXT.TXT)
            last_row = file.readlines()[-1]
            # split the last row by "|", turned into list
            # get the reservation id in index 0
            self.last_id = int(last_row.split('|')[0]) 
        except (IndexError, ValueError):
            self.last_id = 0
        # initialize the next reservation ID by incrementing the last id from the TEXT.TXT
        self.nextID = self.last_id + 1

    # method for adding or creating new reservation
    def add(self, inputs):
        try:
            # open the TEXT.TXT to append the content
            file = open('text.txt', 'a')
            # calculate the total
            total = self.total_price( inputs['no_adult'], inputs['no_children'] )
            # concatinating all the reservation information into one string of data
            reservation = f"{self.nextID}|{inputs['name']}|{inputs['date']}|{inputs['time']}|{str(inputs['no_adult'])}|{str(inputs['no_children'])}|{total}\n"
            # appending the TEXT.TXT content with the new reservation string
            file.write(reservation)
            print('New reservation added')
        except FileNotFoundError as e:
            # raise an error when TEXT.TXT is not present
            print(e)
        except TypeError as typeError :
            # raise an error when data type is not right
            print(typeError)

    # method for displaying all the records in TEXT.TXT
    def view(self):
        # open the TEXT.TXT to read the content
        file = open('text.txt', 'r')
        # get all the content in TEXT.TXT
        reservations = file.readlines()
        # check if the TEXT.TXT has records
        if len(reservations) >= 1 :
            # declaring list of column names for header
            headers = ("#", "Date", "Time", "Name", "Adults", "Children")
            # print header
            print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*headers))
            # loop through list of reservation 
            for reservation in reservations:
                # split each row to extract the data from the string
                data = reservation.strip().split('|')
                # declaring list of data from the list of reservation
                row_data = [data[0], data[2], data[3], data[1], data[4], data[5]]
                # print the data
                print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*row_data))
        else:
            # print if TEXT.TXT has no records
            print("No reservations yet\n")          
    
    # method for removing existing reservation
    # accepts argument "id" for id reservation
    def deleteRecord(self, id):
        try:
            # open the TEXT.TXT to read the content
            readFile = open('text.txt', 'r')
            # get all the content in TEXT.TXT (this is list)
            lines = readFile.readlines()
            # open the TEXT.TXT to write the content
            writeFile = open('text.txt', 'w')
            # loop through list of reservation 
            for index, x in enumerate(lines):
                # checks if the reservation id of row is equal to id inputted by the user
                if int(x[0]) == id :
                    # if true, the row will be remove from the list
                    del lines[index]
            # overwriting the content of the TEXT.TXT
            writeFile.writelines(lines)
            print(f"Reservation {id} is deleted.")
        except IndexError as indexError:
            # raise an error if the inputted id is now present in the list
            writeFile.writelines(lines)
            print(indexError)

    # method for generating of reports
    def report(self):
        # open the TEXT.TXT to read the content
        file = open('text.txt', 'r')
        # get all the content in TEXT.TXT (this is list)
        reservations = file.readlines()
        # check if the TEXT.TXT has records
        if len(reservations) > 0:
            total_adults = 0
            total_children = 0
            total_sales = 0
            print("\n=====================================================REPORT=====================================================\n")
            # declaring list of column names for header
            headers = ("#", "Date", "Time", "Name", "Adults", "Children", "Subtotal")
            # print header
            print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*headers))
            # loop through list of reservation 
            for index, reservation_ in enumerate(reservations):
                # split each row to extract the data from the string
                data = reservation_.strip().split('|')
                # declaring list of data from the list of reservation
                row_data = [data[0], data[2], data[3], data[1], data[4], data[5], data[6]]
                # print the data
                print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*row_data))
                # collect all the numbers of adult and children in records
                # add up the total sales of all the reservation
                total_adults += int(data[5])
                total_children += int(data[6]) if data[6] else 0
                total_sales += float(data[6].replace('$',''))
            print(f"\nTotal number of adults: {total_adults}")
            print(f"Total number of children: {total_children}")
            print(f"Grand Total: PHP {total_sales:.2f}\n")
            print("..................................................nothing follows..................................................\n")
        else:
            print("No reservations yet")

    # method for getting the total bill of reservation
    # accepts two arguments, number of adults and number of childrens
    def total_price(self, adult, children) :
            # 1 adult is equal to 500
            # 1 children is equal to 250
            return adult * 500 + children * 250
    
    #close the instance of the class 
    def close(self):
        print('')

################################################################

while True :
    try:
        print("\nRESTAURANT RESERVATION SYSTEM")
        print("System Menu")
        print("a. Make Reservation")
        print("b. View Reservation")
        print("c. Delete Reservation")
        print("d. Generate Report")
        print("e. Exit")
        choice = input("Action: ")

        reservation = Reservation()

        if choice == "a" : 
            inputs = {}
            inputs['name'] = str(input("Name: "))
            inputs['date'] = str(input("Date: "))
            inputs['time'] = str(input("Time: "))
            inputs['no_adult'] = int(input("No. of adults: "))
            inputs['no_children'] = int(input("No. of children: "))

            reservation.add(inputs)
            
        elif choice == "b" :
            reservation.view()
        elif choice == "c" :
            reservationID = int(input("Input reservation number: "))
            reservation.deleteRecord(reservationID)
            reservation.view()
        elif choice == "d" :
             reservation.report()
        elif choice == "e" :
            break
        else :
            raise ValueError("Invalid Input")
    except ValueError as e:
        print(e)
    finally :
        reservation.close()
        
