# task one 
import sys 
# global variables 
service_ticket_dictionary = {}
number_tickets = 0

# functions for adding service tickets, asks for each of the variables and stores in the global
# variable service_ticket_dictionary

def open_ticket():
    while True: 
            global number_tickets
            number_tickets += 1
            new_ticket_number = (f"{number_tickets}")
            customer_name = input("\n Customer Name: ")
            issue_description = input("\n Describe Issue: ")
            issue_status = input("\n Issue Open or Closed: ")
            while issue_status not in ["Open" ,"Closed"]:
                issue_status = input("Please type either Open or Closed?: ")
            service_ticket_dictionary[new_ticket_number] = {"Customer": customer_name, "Issue": issue_description, "Status": issue_status}
            try_again = input("\nWould you like to add another ticket? (Y/N): ")
            while try_again not in ["Y", "N"] :
                input("\nPlease type 'Y' or'N': ")
            if try_again == 'N':
                break 

#function to update the status of the ticket, selection number two on the menu

def update_status():
    while True:    
        if number_tickets == 0:
            print("\nThere are no tickets currently on record")
            break 
        for ticket_id in service_ticket_dictionary:
            print("\n----------------")
            print("Ticket ID: {}".format(ticket_id))
            print("Customer: {}".format(service_ticket_dictionary[ticket_id]["Customer"]))
            print("Issue: {}".format(service_ticket_dictionary[ticket_id]["Issue"]))
            print("Status: {}".format(service_ticket_dictionary[ticket_id]["Status"]))
            print("-----------------")  
    
        change_status = input("Which ticket number do you want to update?: ") 
        for status in service_ticket_dictionary:
            if status == change_status:
                    issue_status = input("\nIssue Open or Closed: ")
                    while issue_status not in ["Open" ,"Closed"]:
                        issue_status = input("Please type either Open or Closed?: \n")
                    service_ticket_dictionary[change_status]["Status"] = issue_status
        break
               
                

# function for displaying ticket, option number three in the menu 
            
def display_ticket():
    if number_tickets == 0:
        print("There are no tickets currently on record")
    for ticket_id in service_ticket_dictionary:
        print("\n-----------------")
        print("Ticket ID: {}".format(ticket_id))
        print("Customer: {}".format(service_ticket_dictionary[ticket_id]["Customer"]))
        print("Issue: {}".format(service_ticket_dictionary[ticket_id]["Issue"]))
        print("Status: {}".format(service_ticket_dictionary[ticket_id]["Status"]))
        print("-----------------")

# function for main menu and menu selections, each selection callsone of the previous functions 

def main_menu_selection():
    while True:
        menu_selection = input("\n -------------------------------------\n \t SERVICE TICKET MENU \n \t 1. Open a new ticket \n \t 2. Update existing ticket \n \t 3. Display all tickets \n\t 4. Close program\n-------------------------------------\n\n\n Please type a number: ")
        while menu_selection not in ["1", "2", "3", "4"] :
            menu_selection = input(" Please type a number listed in the menu: ")
        if menu_selection == "1":
            open_ticket() 
        elif menu_selection == "2":
            update_status()
        elif menu_selection == "3":
            display_ticket() 
        elif menu_selection == "4":
             sys.exit(0)


# call the main menu function 
main_menu_selection()       
        