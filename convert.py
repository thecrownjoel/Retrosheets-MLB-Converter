import csv
#
input_file = "gl2022.txt"
output_file = "gl2022.csv"

# Define the column headers
column_headers = [
    "date", "number_of_game", "day_of_week", "visiting_team", "visiting_league", "visiting_team_game_number",
    "home_team", "home_league", "home_team_game_number", "visiting_team_score", "home_team_score",
    "length_of_game_in_outs", "day_night_indicator", "completion_information", "forfeit_information",
    "protest_information", "park_id", "attendance", "time_of_game_in_minutes", "visiting_line_score",
    "home_line_score"
]

# Add the remaining column headers // Visiting team offensive stats
column_headers.extend([
    "(visiting)_at-bats", "(visiting)_hits", "(visiting)_doubles", "(visiting)_triples", "(visiting)_home_runs",
    "(visiting)_rbi", "(visiting)_sacrifice_hits", "(visiting)_sacrifice_flies", "(visiting)_hit-by-pitch",
    "(visiting)_walks", "(visiting)_intentional_walks", "(visiting)_strikeouts", "(visiting)_stolen_bases",
    "(visiting)_caught_stealing", "(visiting)_grounded_into_double_plays",
    "(visiting)_awarded_first_on_catcher's_interference", "(visiting)_left_on_base"
])

# Add the remaining column headers // Visiting team pitching stats
column_headers.extend([
    "visiting_pitchers_used", "visiting_individual_earned_runs", "visiting_team_earned_runs",
    "visiting_wild_pitches", "visiting_balks"
])

# Add the remaining column headers // Visiting team defensive stats
column_headers.extend([
    "visiting_putouts", "visiting_assists", "visiting_errors", "visiting_passed_balls",
    "visiting_double_plays", "visiting_triple_plays"
])

# Add the remaining column headers // Home team offensive stats
column_headers.extend([
    "at-bats_(home)", "hits_(home)", "doubles_(home)", "triples_(home)", "home_runs_(home)", "rbi_(home)",
    "sacrifice_hits_(home)", "sacrifice_flies_(home)", "hit-by-pitch_(home)", "walks_(home)",
    "intentional_walks_(home)", "strikeouts_(home)", "stolen_bases_(home)", "caught_stealing_(home)",
    "grounded_into_double_plays_(home)", "awarded_first_on_catcher's_interference_(home)",
    "left_on_base_(home)"
])

# Add the remaining column headers // Home team pitching stats
column_headers.extend([
    "home_pitchers_used", "home_individual_earned_runs", "home_team_earned_runs",
    "home_wild_pitches", "home_balks"
])

# Add the remaining column headers // Home team defensive stats
column_headers.extend([
    "home_putouts", "home_assists", "home_errors", "home_passed_balls",
    "home_double_plays", "home_triple_plays"
])

# Add the remaining column headers // Umpire and Manager info
column_headers.extend([
    "home_plate_umpire_id_and_name", "1b_umpire_id_and_name", "2b_umpire_id_and_name",
    "3b_umpire_id_and_name", "lf_umpire_id_and_name", "rf_umpire_id_and_name"
])

column_headers.extend([
    "visiting_team_manager_id_and_name", "home_team_manager_id_and_name"
])

# Add the remaining column headers // Winning, Losing, Saving pitcher info
column_headers.extend([
    "winning_pitcher_id_and_name", "losing_pitcher_id_and_name", "saving_pitcher_id_and_name",
    "game_winning_rbi_batter_id_and_name", "visiting_starting_pitcher_id_and_name",
    "home_starting_pitcher_id_and_name"
])

# Add the remaining column headers // Starting players info
column_headers.extend([
    f"(visiting)_player_{i+1}_id_name_and_defensive_position" for i in range(27)
])

column_headers.extend([
    f"(home)_player_{i+1}_id_name_and_defensive_position" for i in range(27)
])

# Add the remaining column headers // Additional info and acquisition info
column_headers.extend([
    "additional_information", "acquisition_information"
])

with open(input_file, "r") as txt_file, open(output_file, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(column_headers)  # Write the column headers to the CSV file

    for line in txt_file:
        line = line.strip()  # Remove leading/trailing whitespace and newline characters
        row = line.split(",")  # Split the line into individual fields
        writer.writerow(row)

print(f"Conversion complete. Data has been written to {output_file}.")
