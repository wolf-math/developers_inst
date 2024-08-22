from db_actions import *

def main():
    create_db()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Convert Currency")
        print("4. Export to JSON")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            currency = input("Enter currency: ")
            add_transaction(amount, category, description, date, currency)
        elif choice == '2':
            filter_by = input("Filter by (date/category/amount)? Leave blank for no filter: ")
            filter_value = None
            if filter_by:
                filter_value = input(f"Enter {filter_by} value: ")
            view_transactions(filter_by, filter_value)
        elif choice == '3':
            from_currency = input("Enter original currency: ")
            to_currency = input("Enter target currency: ")
            amount = float(input("Enter amount: "))
            converted_amount = convert_currency(amount, from_currency, to_currency)
            print(f"Converted Amount: {converted_amount} {to_currency}")
        elif choice == '4':
            export_to_json()
            print("Data exported to transactions.json")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()