import os
import re
import glob

def find_newest_log_file(logs_directory):
    log_files = glob.glob(os.path.join(logs_directory, 'log-*.txt'))
    
    if not log_files:
        print("Error: No log files found.")
        return None
    
    # Get the newest log file based on modification time
    newest_log_file = max(log_files, key=os.path.getmtime)
    return newest_log_file

def extract_salad_info(log_file_path):
    # Check if the file exists
    if not os.path.exists(log_file_path):
        print(f"Error: Log file '{log_file_path}' not found.")
        return

    print(f"Reading log file: {log_file_path}")

    # Read the latest log file
    with open(log_file_path, 'r') as file:
        # Read all lines and search for lines with data
        lines = file.readlines()

    # Define regular expressions for extracting information
    timestamp_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')
    earnings_pattern = re.compile(r'Predicted Earnings Report: ([\d.]+)')
    wallet_balance_pattern = re.compile(r'Wallet: Current\(([\d.]+)\)')


    # Initialize variables for timestamp and predicted earnings
    timestamp = None
    predicted_earnings = None
    wallet_balance = None
    earnings_match = None
    wallet_balance_match = None

    # Iterate through lines in reverse order
    for line in reversed(lines):
        # Extract timestamp
        timestamp_match = timestamp_pattern.match(line)

        # Extract predicted earnings information
        if earnings_match != 0:
            earnings_match = earnings_pattern.search(line)
        if wallet_balance_match != 0:
            wallet_balance_match = wallet_balance_pattern.search(line)

        if earnings_match or wallet_balance_match:
            print(f"Timestamp: {timestamp_match.group(1)}")

            # Print the extracted information
            if earnings_match:
                print(f"Predicted Earnings: {earnings_match.group(1)}")
                earnings_match = 0
            if wallet_balance_match:
                print(f"Wallet Balance: {wallet_balance_match.group(1)}")
                wallet_balance_match = 0
            
            if earnings_match == None and wallet_balance_match == None:
                break

# Specify the directory where Salad log files are located
logs_directory = './'

# Find the newest log file in the specified directory
newest_log_file_path = find_newest_log_file(logs_directory)

if newest_log_file_path:
    print(f"Selected newest log file: {newest_log_file_path}")
    # Extract and display information from the newest log file
    extract_salad_info(newest_log_file_path)
