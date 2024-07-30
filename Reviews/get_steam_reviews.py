import requests
import json
import time
from datetime import datetime
import pytz

def fetch_reviews(app_id, cursor="*", day_range=None):
    url = f"https://store.steampowered.com/appreviews/{app_id}"
    params = {
        "json": 1,
        "cursor": cursor,
        "num_per_page": 100,
        "language": "english",
        "review_type": "all",
        "purchase_type": "all"
    }
    if day_range:
        params["day_range"] = day_range
        params["filter"] = "all"
    else:
        params["filter"] = "recent"
    
    response = requests.get(url, params=params)
    return response.json()

def convert_to_mst(timestamp):
    utc_time = datetime.utcfromtimestamp(timestamp)
    utc_time = utc_time.replace(tzinfo=pytz.UTC)
    mst_tz = pytz.timezone('US/Mountain')
    mst_time = utc_time.astimezone(mst_tz)
    return mst_time.strftime('%Y-%m-%d %H:%M:%S %Z')

def process_review(review):
    review['timestamp_created_mst'] = convert_to_mst(review['timestamp_created'])
    review['timestamp_updated_mst'] = convert_to_mst(review['timestamp_updated'])
    return review

def save_reviews(reviews, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, indent=4, ensure_ascii=False)

def main(app_id, day_range=None, max_reviews=150000):
    all_reviews = []
    unique_review_ids = set()
    cursor = "*"
    no_progress_count = 0
    max_no_progress = 10  # Increased from 5 to 10
    batch_size = 100
    
    while len(all_reviews) < max_reviews:
        print(f"Fetching reviews with cursor: {cursor}")
        data = fetch_reviews(app_id, cursor, day_range)
        
        if not data['success']:
            print("Error fetching reviews.")
            break
        
        reviews = data['reviews']
        if not reviews:
            print("No more reviews returned. Ending fetch.")
            break
        
        initial_review_count = len(all_reviews)
        new_reviews_count = 0
        
        for review in reviews:
            review_id = review['recommendationid']
            if review_id not in unique_review_ids:
                unique_review_ids.add(review_id)
                all_reviews.append(process_review(review))
                new_reviews_count += 1
        
        print(f"Batch added {new_reviews_count} new reviews. Total unique reviews: {len(all_reviews)}")
        
        if new_reviews_count == 0:
            no_progress_count += 1
            print(f"No new reviews in this batch. No progress count: {no_progress_count}")
            if no_progress_count >= max_no_progress:
                print(f"No new reviews for {max_no_progress} consecutive batches. Ending fetch.")
                break
        else:
            no_progress_count = 0
        
        if 'cursor' not in data or not data['cursor']:
            print("No more cursors available. Ending fetch.")
            break
        
        cursor = data['cursor']
        
        if len(all_reviews) % 1000 == 0:
            print(f"Milestone: Fetched {len(all_reviews)} unique reviews so far...")
        
        time.sleep(2)  # Be nice to Steam's servers

    print(f"Total unique reviews fetched: {len(all_reviews)}")
    filename = f"reviews_{app_id}.json"
    if day_range:
        filename = f"reviews_{app_id}_last_{day_range}_days.json"
    save_reviews(all_reviews, filename)
    print(f"Reviews saved to {filename}")

if __name__ == "__main__":
    app_id = 346110  # Game App ID
    day_range = None  # Set to None to fetch all reviews, or specify a number of days (max 365)
    max_reviews = 150000  # Set maximum number of reviews to fetch
    main(app_id, day_range, max_reviews)