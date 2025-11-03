def main():
    print("=== BinBuz: BIN Details Generator ===\n")

    #input
    bin_number = input("Input your BIN: ")
    entity_name = input("Name of the Entity: ")
    trading_name = input("Trading Brand Name (N/A if none): ")
    old_bin = input("Old BIN: ")
    etin = input("e-TIN: ")
    registration = input("Registration (e.g., Registered for VAT): ")
    date_issue = input("Date of Issue (DD/MM/YYYY): ")
    date_effect = input("Date of Effect (DD/MM/YYYY): ")
    address = input("Address: ")
    ownership = input("Type of Ownership: ")
    major_activity = input("Major Area of Economic Activity: ")

    # Output
    output = f"""
Business Identification Number (BIN) Details
BIN : {bin_number}
Name of the Entity : {entity_name}
Trading Brand Name : {trading_name}
Old BIN : {old_bin}
e-TIN : {etin}
Registration : {registration}
Date of Issue : {date_issue}
Date of Effect : {date_effect}
Address: {address}
Type of Ownership: {ownership}
Major Area of Economic Activity: {major_activity}
"""

    print("\n=== Generated BIN Details ===")
    print(output)

    # save to file
    save_file = input("Do you want to save this to a text file? (y/n): ").lower()
    if save_file == 'y':
        filename = f"output/BIN_{bin_number.replace('/', '-')}.txt"
        import os
        if not os.path.exists("output"):
            os.makedirs("output")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Saved successfully to {filename}")

if __name__ == "__main__":
    main()
