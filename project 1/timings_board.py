import sys
import os
import csv

def parse_driver_info(file_path):
    """Parse the driver information file to extract driver details from a CSV file."""
    try:
        driver_info = {}
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:  # driver_code, driver_name, team_name
                    driver_code, driver_name, team_name = row
                    driver_info[driver_code] = {
                        'name': driver_name,
                        'team': team_name
                    }

        print("Driver Information:")  # Debugging line to print the driver info
        print(driver_info)  # Print the driver info to verify it is correct
        
        return driver_info
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading driver info file: {e}")
        sys.exit(1)



def parse_lap_file(file_path):
    """Parse a lap data file to extract race name and lap times."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        race_name = lines[0].strip()  
        lap_data = []

        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 2:  
                driver_code = parts[0]
                try:
                    lap_time = float(parts[1])  
                    lap_data.append((driver_code, lap_time))
                except ValueError:
                    print(f"Warning: Could not convert lap time '{parts[1]}' for driver {driver_code}. Skipping line.")
            else:
                print(f"Warning: Invalid line format: '{line.strip()}'. Skipping line.")

        return race_name, lap_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading lap file: {e}")
        sys.exit(1)



def analyze_lap_times(lap_data):
    """Analyze the lap times and compute required metrics."""
    from collections import defaultdict

    driver_times = defaultdict(list)

    for driver_code, lap_time in lap_data:
        driver_times[driver_code].append(lap_time)

    fastest_driver = None
    fastest_time = float('inf')

    driver_stats = {}

    for driver, times in driver_times.items():
        min_time = min(times)
        avg_time = sum(times) / len(times)

        driver_stats[driver] = {
            'fastest_time': min_time,
            'average_time': avg_time,
        }

        if min_time < fastest_time:
            fastest_driver = driver
            fastest_time = min_time

    overall_average_time = sum(time for _, time in lap_data) / len(lap_data)

    return fastest_driver, fastest_time, driver_stats, overall_average_time

def display_results(race_name, fastest_driver, fastest_time, driver_stats, overall_average_time, driver_info):

    print(f"Driver Info: {driver_info}")  # Debugging line

    print(f"Race: {race_name}\n")
    print(f"Fastest Driver: {fastest_driver} ({driver_info.get(fastest_driver, {}).get('name', 'Unknown')}) with a time of {fastest_time:.3f} seconds\n")

    print("Driver Stats:")
    print(f"{'Driver':<10}{'Name':<20}{'Team':<20}{'Fastest Time':<15}{'Average Time':<15}")
    print("-" * 80)

    sorted_drivers = sorted(driver_stats.items(), key=lambda x: x[1]['fastest_time'])

    for driver, stats in sorted_drivers:
        name = driver_info.get(driver, {}).get('name', 'Unknown')
        team = driver_info.get(driver, {}).get('team', 'Unknown')
        print(f"{driver:<10}{name:<20}{team:<20}{stats['fastest_time']:<15.3f}{stats['average_time']:<15.3f}")

    print("\nOverall Average Lap Time: {:.3f} seconds".format(overall_average_time))

'''def main():
    if len(sys.argv) < 3:
        print("Usage: python timings_board.py <driver_info_file> <lap_file1> [<lap_file2> ...]")
        sys.exit(1)

    driver_info_file = sys.argv[1]
    lap_files = sys.argv[2:]

    if not os.path.isfile(driver_info_file):
        print(f"Error: Driver info file '{driver_info_file}' does not exist.")
        sys.exit(1)

    for lap_file in lap_files:
        if not os.path.isfile(lap_file):
            print(f"Error: Lap file '{lap_file}' does not exist.")
            sys.exit(1)

    driver_info = parse_driver_info(driver_info_file)
    all_lap_data = []
    race_name = None

    for lap_file in lap_files:
        current_race_name, lap_data = parse_lap_file(lap_file)
        all_lap_data.extend(lap_data)
        if race_name is None:
            race_name = current_race_name
        elif race_name != current_race_name:
            print(f"Warning: Mismatched race names in files. Using race name from first file: {race_name}")

    fastest_driver, fastest_time, driver_stats, overall_average_time = analyze_lap_times(all_lap_data)
    
    display_results(race_name, fastest_driver, fastest_time, driver_stats, overall_average_time, driver_info)'''

def main():
    if len(sys.argv) < 3:
        print("Usage: python timings_board.py <driver_info_file> <lap_file1> [<lap_file2> ...]")
        sys.exit(1)

    driver_info_file = sys.argv[1]
    lap_files = sys.argv[2:]

    if not os.path.isfile(driver_info_file):
        print(f"Error: Driver info file '{driver_info_file}' does not exist.")
        sys.exit(1)

    for lap_file in lap_files:
        if not os.path.isfile(lap_file):
            print(f"Error: Lap file '{lap_file}' does not exist.")
            sys.exit(1)

    driver_info = parse_driver_info(driver_info_file)
    
    # Store results for each race
    all_race_data = []

    for lap_file in lap_files:
        race_name, lap_data = parse_lap_file(lap_file)
        fastest_driver, fastest_time, driver_stats, overall_average_time = analyze_lap_times(lap_data)
        all_race_data.append((race_name, fastest_driver, fastest_time, driver_stats, overall_average_time, lap_data))

    # Display results for each race
    for race_name, fastest_driver, fastest_time, driver_stats, overall_average_time, lap_data in all_race_data:
        display_results(race_name, fastest_driver, fastest_time, driver_stats, overall_average_time, driver_info)


if __name__ == "__main__":
    print(f"Arguments received: {sys.argv}")
    main()
