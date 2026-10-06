import sqlite3

# Connect to the database
conn = sqlite3.connect('payment.db')
cursor = conn.cursor()

# Create table only if it doesn't exist (Runs schema.sql safely)
with open('schema.sql', 'r') as file:
    sql_script = file.read()
cursor.executescript(sql_script)
conn.commit()

while True:
    print("\n--- Payment Backend Menu ---")
    print("1. Add New Payment Record")
    print("2. Search Customer by Name")
    print("3. Exit")
    
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    
    if choice == '1':
        # --- Add New Record ---
        try:
            new_id = int(input("Enter ID (e.g., 116): "))
            new_name = input("Enter Name: ").strip().lower()
            new_product = input("Enter Product: ").strip().lower()
            new_mode = input("Enter Mode (cash/netbanking): ").strip().lower()
            new_city = input("Enter City: ").strip().lower()

            cursor.execute('''
                INSERT OR IGNORE INTO pay_history (ID, NAME, PRODUCT, MODE, CITY)
                VALUES (?, ?, ?, ?, ?)
            ''', (new_id, new_name, new_product, new_mode, new_city))
            
            conn.commit()
            print("-> Success: New record added permanently to the database!")
        except ValueError:
            print("-> Error: ID must be a number.")
            
    elif choice == '2':
        # --- Search Record ---
        search_name = input("Enter customer name to search: ").strip().lower()
        cursor.execute("SELECT * FROM pay_history WHERE LOWER(NAME) = ?", (search_name,))
        results = cursor.fetchall()

        if results:
            print(f"\nFound! Records for '{search_name}':")
            for row in results:
                print(row)
        else:
            print(f"\nNo record found for '{search_name}'.")
            
    elif choice == '3':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter")