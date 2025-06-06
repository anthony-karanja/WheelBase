def main():
    from main import create_customer, fetch_customers, list_customer, update_customer,delete_customer, find_car, list_cars, update_car, delete_car
    from main import create_car_rental, fetch_car_rentals, list_car_rental, update_car_rental, delete_car_rental

    while True:
        print("\n1.Manage Customers")
        print("2.Manage Cars")
        print("3. Manage car rentals")
        main_choice = input("\n\033[31mEnter your choice: \033[0m")

        if main_choice == "1" :
            print("1. Create customer")
            print("2. List customer") 
            print("3.List customer by id")   
            print("4.Update Customer")
            print("5.Delete Customer")
            print("0.Exit")

            choice = input("\n\033[35mEnter your choice: \033[0m")
            if choice == "1":
                create_customer()
            elif choice == "2":
                fetch_customers()
            elif choice == "3":
                list_customer()
            elif choice == "4":
                update_customer()
            elif choice == "5":
                delete_customer() 
            elif choice == "0":
                print("Adios!!🫡")
                break   
            else:
                print("\n\033[33mInvalid input!Try again\033[0m")   

        if main_choice == "2" :
            print("1. Find car")
            # print("2. List cars") 
            print("2.List cars")   
            print("3.Update Car")
            print("4.Delete Car")
            print("0. Exit")
            
            
            choice = input("\n\033[35mEnter your choice: \033[0m")
            if choice == "1":
                find_car()
            elif choice == "2":
                list_cars()
            elif choice == "3":
                update_car()
            elif choice == "4":
                delete_car()
            elif choice == "0":
                print("Adios!!🫡")
                break   
            else:
                print("\n\033[33mInvalid input!Try again\033[0m") 

            # choice = input("\033[31mEnter your choice: \033")
            # if choice == "1":
            #     find_car()
            
            # elif choice == "2":
            #     list_cars()
            # elif choice == "3":
            #     update_car()
            # elif choice == "4":
            #     delete_car()
            # elif choice == "0":
            #     print("Adios!!🫡")
            #     break   
            # else:
            #     print("\033[31mInvalid input!Try again\033[0m")         


        if main_choice == "3" :
            print("1. Create car rental")
            print("2. List cars rented") 
            print("3.List car rented  by id")   
            print("4.Update Car rented")
            print("5.Delete Car rented")
            print("0. Exit")

            choice = input("\033[31mEnter your choice\033[0m")
            if choice == "1":
                create_car_rental()
            elif choice == "2":
                fetch_car_rentals()
            elif choice == "3":
                list_car_rental()
            elif choice == "4":
                update_car_rental()
            elif choice == "5":
                delete_car_rental()    
            elif choice == "0":
                print("Adios!!🫡")
                break   
            else:
                print("\033[31mInvalid input!Try again\033[0m") 


if __name__ == "__main__":
    main()