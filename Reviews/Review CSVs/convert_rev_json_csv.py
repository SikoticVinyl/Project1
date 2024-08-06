import json
import csv
from datetime import datetime
import os

# Specify your input JSON file name here
INPUT_JSON_FILE = "reviews_275850.json"

def load_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print(f"Current working directory: {os.getcwd()}")
        print("Files in the current directory:")
        for file in os.listdir():
            print(f"  {file}")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' is not a valid JSON file.")
        return None

def convert_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def safe_get(dictionary, keys, default=None):
    for key in keys:
        if isinstance(dictionary, dict) and key in dictionary:
            dictionary = dictionary[key]
        else:
            return default
    return dictionary

def extract_review_data(review):
    return {
        'review_id': safe_get(review, ['recommendationid']),
        'author_steamid': safe_get(review, ['author', 'steamid']),
        'author_num_games_owned': safe_get(review, ['author', 'num_games_owned']),
        'author_num_reviews': safe_get(review, ['author', 'num_reviews']),
        'author_playtime_forever': safe_get(review, ['author', 'playtime_forever']),
        'author_playtime_last_two_weeks': safe_get(review, ['author', 'playtime_last_two_weeks']),
        'author_playtime_at_review': safe_get(review, ['author', 'playtime_at_review']),
        'author_last_played': convert_timestamp(safe_get(review, ['author', 'last_played'], 0)),
        'language': safe_get(review, ['language']),
        'review': safe_get(review, ['review'], '').replace('\n', ' ').replace('\r', ''),
        'timestamp_created': convert_timestamp(safe_get(review, ['timestamp_created'], 0)),
        'timestamp_updated': convert_timestamp(safe_get(review, ['timestamp_updated'], 0)),
        'voted_up': safe_get(review, ['voted_up']),
        'votes_up': safe_get(review, ['votes_up']),
        'votes_funny': safe_get(review, ['votes_funny']),
        'weighted_vote_score': safe_get(review, ['weighted_vote_score']),
        'comment_count': safe_get(review, ['comment_count']),
        'steam_purchase': safe_get(review, ['steam_purchase']),
        'received_for_free': safe_get(review, ['received_for_free']),
        'written_during_early_access': safe_get(review, ['written_during_early_access']),
        'timestamp_created_mst': safe_get(review, ['timestamp_created_mst']),
        'timestamp_updated_mst': safe_get(review, ['timestamp_updated_mst'])
    }

def save_csv(data, filename):
    if not data:
        print("No data to write to CSV.")
        return

    keys = data[0].keys()
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"CSV file successfully saved as '{filename}'")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{filename}'.")
        print("Make sure you have write permissions in this directory.")
    except Exception as e:
        print(f"An error occurred while saving the CSV file: {str(e)}")

def main():
    input_file = os.path.join(os.getcwd(), INPUT_JSON_FILE)
    print(f"Attempting to load JSON data from: {input_file}")
    
    json_data = load_json(input_file)
    if json_data is None:
        return
    
    print("Extracting review data")
    csv_data = [extract_review_data(review) for review in json_data]
    
    output_file = input_file.rsplit('.', 1)[0] + '.csv'
    print(f"Attempting to save CSV data to: {output_file}")
    save_csv(csv_data, output_file)
    
    print(f"Conversion complete. {len(csv_data)} reviews processed.")

if __name__ == "__main__":
    main()