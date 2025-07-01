# /*Create an Employee Management System (EMS) application that allows us to store and manage employee information# . # The application should be able to add new employees# , display employee details, and save employee data to a file for future reference.
# Requirements:
#
# The application should have options to:
# Add a new employee
# Display employee details
# Exit the program
#
#
# Employee details should include:
# Employee ID
# Name
# Position
# Salary
#
# Employee data should be stored in a text file.
#
# When adding a new employee, the user should input the employee details, and the data should be appended to the file.
# When displaying employee details, the program should read the employee data from the file and print it.*/
# Employee Management System (EMS)

# Define the file name to store employee data
EMPLOYEE_FILE = "employee_data.txt"


def add_employee():
    """Add a new employee to the file."""
    try:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        salary = input("Enter Employee Salary: ")

        # Append employee data to the file
        with open(EMPLOYEE_FILE, "a") as file:
            file.write(f"{emp_id},{name},{position},{salary}\n")
        print("Employee added successfully!")
    except Exception as e:
        print(f"Error adding employee: {e}")


def display_employees():
    """Display all employee details from the file."""
    try:
        with open(EMPLOYEE_FILE, "r") as file:
            for line in file:
                emp_id, name, position, salary = line.strip().split(",")
                print(f"Employee ID: {emp_id}, Name: {name}, Position: {position}, Salary: {salary}")
    except FileNotFoundError:
        print("No employee data found.")
    except Exception as e:
        print(f"Error displaying employees: {e}")


def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        match choice:
            case '1':
                add_employee()
            case '2':
                display_employees()
            case '3':
                print("Exiting the program. Have a great day!")
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
