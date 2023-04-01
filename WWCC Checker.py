"""
Author: Jack Moore
Twitter: @TechedJack
Copyright (C) 2023 Jack Moore. All rights reserved.
"""
import requests
from bs4 import BeautifulSoup
import csv
import re
import io
import os

def get_wwcc_status(card_number, last_name):
    url = "https://online.justice.vic.gov.au/wwccu/checkstatus.doj"
    data = {
        "viewSequence": 1,
        "language": "en",
        "cardnumber": card_number,
        "lastname": last_name,
        "pageAction": "Submit",
        "Submit": "submit",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.status_code}"

def parse_response(html_content, card_number, first_name, last_name):
    soup = BeautifulSoup(html_content, "html.parser")
    full_name = f"{first_name} {last_name.upper()}"

    if len(card_number) == 6:
        return f"{full_name} (Card Number: {card_number}) - Status: Exempt (VIT Card)"

    result_success = soup.find("div", {"class": "success"})
    result_error = soup.find("div", {"class": "error"})

    if result_success:
        text = result_success.get_text(strip=True)
        pattern_current = r"Working with Children Check number (\w+) .* for (.*) is (current|not current).* expires on (.*)\."
        pattern_not_current = r"Working with Children Check number (\w+) is no longer current. (.*) has a new card that is current. This person may engage in child related work and their current \(Employee\) card expires on (.*)\. Please contact cardholder for updated card details."

        match_current = re.search(pattern_current, text)
        match_not_current = re.search(pattern_not_current, text)

        if match_current:
            card_number = match_current.group(1)
            full_name = match_current.group(2).strip()
            status = match_current.group(3)
            expiry_date = match_current.group(4)

            if len(card_number) == 6:
                return f"{full_name} (Card Number: {card_number}) - Status: Exempt (VIT Card)"

            return f"{full_name} (Card Number: {card_number}) - Status: {status}, Expiry Date: {expiry_date}"
        elif match_not_current:
            card_number = match_not_current.group(1)
            full_name = match_not_current.group(2).strip()
            new_expiry_date = match_not_current.group(3)
            return f"{full_name} (Old Card Number: {card_number}) - Status: not current, New Card Expiry Date: {new_expiry_date}. Please contact cardholder for updated card details."
    
    elif result_error:
        text = result_error.get_text(strip=True)

        if "one or more fields are missing or incorrect" in text:
            return f"Error: {full_name} (Card Number: {card_number}) - The field format is incorrect."
        elif "This family name and application/card number combination do not match" in text:
            return f"Error: {full_name} (Card Number: {card_number}) - The family name and application/card number combination do not match."

    return "No results found."

def check_single_card():
    card_number = input("Please enter the card number: ")
    last_name = input("Please enter the last name: ")

    html_content = get_wwcc_status(card_number, last_name)
    status = parse_response(html_content, card_number, last_name)

    print("\nResult:")
    print(status)

def check_bulk_csv(input_file, output_filename):
    results = []
    current_count = 0
    vit_count = 0
    field_format_error_count = 0
    name_mismatch_error_count = 0
    no_results_count = 0

    with open(output_filename, "w", newline='') as output_file:
        fieldnames = ["Last Name", "First Name", "Card Number", "Status"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        reader = csv.DictReader(input_file)

        for row in reader:
            last_name = row["Last Name"]
            first_name = row["First Name"]
            card_number = row["Card Number"]
            card_number = card_number.split('-')[0]

            html_content = get_wwcc_status(card_number, last_name)
            status = parse_response(html_content, card_number, first_name, last_name)

            writer.writerow({"Last Name": last_name, "First Name": first_name, "Card Number": card_number, "Status": status})
            print(status)

            results.append(status)
            if "Exempt (VIT Card)" in status:
                vit_count += 1
            elif "The field format is incorrect" in status:
                field_format_error_count += 1
            elif "The family name and application/card number combination do not match" in status:
                name_mismatch_error_count += 1
            elif "No results found" in status:
                no_results_count += 1
            else:
                current_count += 1

    print("\nResults:")
    print("\n".join(results))
    print("\nSummary:")
    print(f"Total checks: {len(results)}")
    print(f"Current: {current_count}")
    print(f"VIT Exempt: {vit_count}")
    print(f"Field format errors: {field_format_error_count}")
    print(f"Name and card number mismatch errors: {name_mismatch_error_count}")
    print(f"No results found: {no_results_count}")

def main():
    print("WWCC-Status-Checker by Jack Moore")
    print("Copyright (C) 2023 Jack Moore. All rights reserved.")
    print("For any inquiries, please contact me via Twitter @TechedJack\n")
    
    while True:
        print("\nSelect an option:")
        print("1. Check a single card")
        print("2. Check cards from a CSV file")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            check_single_card()
        elif choice == "2":
            input_filename = input("Please enter the input CSV file path: ")
            output_filename = input("Please enter the output CSV file name: ")
            with open(input_filename, "r") as input_file:
                check_bulk_csv(input_file, output_filename)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
