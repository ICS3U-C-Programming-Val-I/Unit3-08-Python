#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: November 1, 2023
# This program asks the user for a year then tells
# them if its a leap year.


def main():
    # Input- Get year as string
    # Declaring variable year_str
    year_str = input("Enter a year: ")

    try:
        year_int = int(year_str)
        # process - checks if year is leap or not
        if year_int % 4 == 0:
            if year_int % 100 == 0:
                if year_int % 400 == 0:
                    # Output - Displays result
                    print(f"{year_int} is a leap year")
                else:
                    # Output - Displays result
                    print(f"{year_int} is not a leap year")
            else:
                # Output - Displays result
                print(f"{year_int} is a leap year")
        else:
            # Output - Displays result
            print(f"{year_int} is not a leap year")
    except ValueError:
        print(f"'{year_str}' is not a valid year")


if __name__ == "__main__":
    main()
