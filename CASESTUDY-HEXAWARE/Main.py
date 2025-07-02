from exception.AuthenticationException import AuthenticationException
from exception.VehicleNotFoundException import VehicleNotFoundException
from exception.ReservationException import ReservationException
from exception.InvalidInputException import InvalidInputException
from dao.CustomerServiceImpl import CustomerServiceImpl
from dao.VehicleServiceImpl import VehicleServiceImpl
from dao.ReservationServiceImpl import ReservationServiceImpl
from dao.AdminServiceImpl import AdminServiceImpl
from dao.RoleServiceImpl import RoleServiceImpl
from entity.Customer import Customer
from entity.Reservation import Reservation
from datetime import datetime
from dao.AddressServiceImpl import AddressServiceImpl
from entity.Address import Address
from entity.Vehicle import Vehicle

def main_menu():
    cust_service = CustomerServiceImpl()
    vehicle_service = VehicleServiceImpl()
    reserv_service = ReservationServiceImpl()
    admin_service = AdminServiceImpl()
    role_service = RoleServiceImpl()

    while True:
        print("\n====== CarConnect Main Menu ======")
        print("0. Admin Login")
        print("1. Register Customer")
        print("2. Login as Customer")
        print("3. View All Vehicles")
        print("4. View Available Vehicles")
        print("5. Reserve a Vehicle")
        print("6. View All Customers")
        print("7. Update Reservation")
        print("8. Cancel Reservation")
        print("9. Add Vehicle")
        print("10. Update Vehicle")
        print("11.Delete Vehicle")
        print("12. Exit")
        

        choice = input("Enter your choice: ")

        if choice == '0': 
            username = input("Admin Username: ")
            password = input("Password: ")
            
            admin = admin_service.get_admin_by_username(username)
            print("Admin object:", admin)                   
            
            if admin and admin.authenticate(password):
                role = role_service.get_role_by_id(admin.role_id)
                print(f"\nWelcome, {admin.first_name} ({role.role_name})")
                
            else:
                print("Invalid admin credentials")
                
                
        elif choice == '1':
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone Number: ")
            username = input("Username: ")
            password = input("Password: ")
            reg_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            customer = Customer(None, fname, lname, email, phone, username, password, reg_date)
            cust_service.register_customer(customer)
            last_customer = cust_service.get_customer_by_username(username)
            if last_customer:
                addr_service = AddressServiceImpl()
                print("Enter address information:")
                street = input("Street: ")
                city = input("City: ")
                state = input("State: ")
                zip_code = input("ZIP Code: ")
                addr_type = input("Address Type (Home/Office/Other): ")
                address = Address(None, last_customer.customer_id, street, city, state, zip_code, addr_type)
                addr_service.add_address(address)
                print("Registeration successfull")

        elif choice == '2':
            username = input("Enter Username : ")
            password = input("Password: ")

            customer = cust_service.get_customer_by_username(username)
            if customer and customer.authenticate(password):
                print(f"Welcome back, {customer.first_name}")
            else:
                print("Invalid credentials by durga2")


        elif choice == '3':
            vehicles = vehicle_service.get_all_vehicles()
            print("\n--- All Vehicles ---")
            for v in vehicles:
                print(f"{v.vehicle_id}. {v.make} {v.model} ({v.color}) - ₹{v.daily_rate}/day")

        elif choice == '4':
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            vehicles = vehicle_service.get_available_vehicles(start_date, end_date)
            print("\n--- Available Vehicles ---")
            for v in vehicles:
                print(f"{v.vehicle_id}. {v.make} {v.model} ({v.color}) - ₹{v.daily_rate}/day")

        elif choice == '5':
            try:
                cust_id = int(input("Enter your Customer ID: "))
                veh_id = int(input("Enter Vehicle ID to reserve: "))
                start = input("Start Date (YYYY-MM-DD): ")
                end = input("End Date (YYYY-MM-DD): ")

                vehicle = vehicle_service.get_vehicle_by_id(veh_id)
                if not vehicle:
                    raise VehicleNotFoundException()

                days = (datetime.strptime(end, "%Y-%m-%d") - datetime.strptime(start, "%Y-%m-%d")).days
                if days <= 0:
                    raise InvalidInputException("End date must be after start date.")

                cost = days * vehicle.daily_rate

                reservation = Reservation(None, cust_id, veh_id, start, end, cost, "Confirmed")
                reserv_service.create_reservation(reservation)
                print(f" Reservation confirmed! Total: ₹{cost}")

            except (VehicleNotFoundException, InvalidInputException, ReservationException) as e:
                print(e)
            except Exception as e:
                raise ReservationException(str(e))

        elif choice == '6':
            customers = cust_service.get_all_customers()
            print("\n--- Registered Customers ---")
            for c in customers:
                print(f"ID: {c.customer_id} | Name: {c.first_name} {c.last_name} | Email: {c.email} | Username: {c.username}")

        elif choice == '7':
            try:
                res_id = int(input("Reservation ID to update: "))
                start = input("New Start Date (YYYY-MM-DD): ")
                end = input("New End Date (YYYY-MM-DD): ")
                reservation = reserv_service.get_reservation_by_id(res_id)
                if reservation:
                    days = (datetime.strptime(end, "%Y-%m-%d") - datetime.strptime(start, "%Y-%m-%d")).days
                    new_cost = days * vehicle_service.get_vehicle_by_id(reservation.vehicle_id).daily_rate
                    reservation.start_date = start
                    reservation.end_date = end
                    reservation.total_cost = new_cost
                    reservation.status = "Confirmed"
                    reserv_service.update_reservation(reservation)
                else:
                    print(" Reservation not found.")
            except Exception as e:
                print("Error updating reservation:", e)

        elif choice == '8':
            try:
                res_id = int(input("Reservation ID to cancel: "))
                reserv_service.cancel_reservation(res_id)
                print("Reservation ID cancelled successfully")
            except Exception as e:
                print("Error cancelling reservation:", e)

                
        elif choice == '9':
            def add_vehicle_ui():
                print("\n--- Add New Vehicle ---")
                model = input("Model: ")
                make = input("Make: ")
                year = int(input("Enter Year: "))
                color = input("Color: ")
                registration_number = input("Registration Number: ")
                daily_rate = float(input("Daily Rental Rate: "))
                availability_input = input("Is the vehicle available? (Yes/No): ").strip().lower()
                availability = True if availability_input == 'yes' else False
                
                new_vehicle = Vehicle(
                    vehicle_id=None,
                    model=model,
                    make=make,
                    year=year,
                    color=color,
                    registration_number=registration_number,
                    daily_rate=daily_rate,
                    availability=availability
                )

                service = VehicleServiceImpl()
                success = service.add_vehicle(new_vehicle)

                if success:
                    print("Vehicle added successfully!")
                else:
                    print("Failed to add vehicle.")

            add_vehicle_ui()
        elif choice == '10':
            try:
                vehicle_id = int(input("Enter Vehicle ID to update: "))
                vehicle_service = VehicleServiceImpl()
                vehicle = vehicle_service.get_vehicle_by_id(vehicle_id)

                if vehicle:
                    print("\n--- Current Vehicle Details ---")
                    print(f"Model: {vehicle.model}")
                    print(f"Make: {vehicle.make}")
                    print(f"Year: {vehicle.year}")
                    print(f"Color: {vehicle.color}")
                    print(f"Registration Number: {vehicle.registration_number}")
                    print(f"Daily Rate: {vehicle.daily_rate}")
                    print(f"Availability: {'Yes' if vehicle.availability else 'No'}")

                    print("\n--- Enter new values (press Enter to keep current) ---")
                    model = input(f"New Model [{vehicle.model}]: ") 
                    make = input(f"New Make [{vehicle.make}]: ") 
                    year_input = input(f"New Year [{vehicle.year}]: ")
                    year = int(year_input) if year_input else vehicle.year
                    color = input(f"New Color [{vehicle.color}]: ") 
                    reg_no = input(f"New Registration Number [{vehicle.registration_number}]: ") 
                    rate_input = input(f"New Daily Rate [{vehicle.daily_rate}]: ")
                    daily_rate = float(rate_input) if rate_input else vehicle.daily_rate
                    avail_input = input(f"Is vehicle available (Yes/No) [{'Yes' if vehicle.availability else 'No'}]: ").strip().lower()

                    availability = vehicle.availability
                    if avail_input == 'yes':
                        availability = True
                    elif avail_input == 'no':
                        availability = False

                    vehicle.model = model
                    vehicle.make = make
                    vehicle.year = year
                    vehicle.color = color
                    vehicle.registration_number = reg_no
                    vehicle.daily_rate = daily_rate
                    vehicle.availability = availability

                    updated = vehicle_service.update_vehicle(vehicle)

                    if updated:
                        print("Vehicle updated successfully!")
                    else:
                        print("Update failed. No changes made.")

                else:
                    print("Vehicle not found.")

            except Exception as e:
                print("Error updating vehicle:", e)
        elif choice == '11':
            try:
                vehicle_id = int(input("Enter Vehicle ID to delete: "))
                confirm = input(f"Are you sure you want to delete Vehicle ID {vehicle_id}? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    service = VehicleServiceImpl()
                    service.delete_vehicle(vehicle_id)
                    print("Vehicle deleted successfully!")
                else:
                    print("Deletion cancelled.")
            except Exception as e:
                print("Error deleting vehicle:", e)

        elif choice == '12':
            print("Exiting CarConnect... ")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main_menu()
