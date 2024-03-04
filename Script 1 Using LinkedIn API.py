import requests
import csv

def get_linkedin_data(first_name, last_name):
    access_token = 'XXXXXXXXXXXXXXXXXXXX'
    url = f'https://api.linkedin.com/v2/people/?first_name={first_name}&last_name={last_name}&q=people&start=0&count=10'
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        profiles = data.get('elements', [])
        return profiles
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from LinkedIn API: {e}")
        return []

def save_to_csv(profiles):
    try:
        with open('linkedin_data_api.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Headline', 'Location'])
            writer.writeheader()
            for profile in profiles:
                name = profile.get('title', '')
                headline = profile.get('headline', '')
                location = profile.get('locationName', '')
                writer.writerow({'Name': name, 'Headline': headline, 'Location': location})
        print("Data saved to linkedin_data_api.csv")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

if __name__ == "__main__":
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    profiles = get_linkedin_data(first_name, last_name)
    if profiles:
        save_to_csv(profiles)
    else:
        print("No profiles found")
