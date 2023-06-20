import csv

input_file = "gl2022.txt"
output_file = "gl2022.csv"

# Define the column headers
column_headers = [
    "Date", "Number of game", "Day of week", "Visiting team", "Visiting league", "Visiting team game number",
    "Home team", "Home league", "Home team game number", "Visiting team score", "Home team score",
    "Length of game in outs", "Day/Night indicator", "Completion information", "Forfeit information",
    "Protest information", "Park ID", "Attendance", "Time of game in minutes", "Visiting line score",
    "Home line score"
    # Add the remaining column headers here
]

with open(input_file, "r") as txt_file, open(output_file, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(column_headers)  # Write the column headers to the CSV file

    for line in txt_file:
        line = line.strip()  # Remove leading/trailing whitespace and newline characters
        row = line.split(",")  # Split the line into individual fields
        writer.writerow(row)

print(f"Conversion complete. Data has been written to {output_file}.")
