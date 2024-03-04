from selenium import webdriver
import csv

def scrape_linkedin_data(first_name, last_name):
    try:
        driver = webdriver.Chrome('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        driver.get(f'https://www.linkedin.com/search/results/people/?keywords={first_name}%20{last_name}')
        profiles = driver.find_elements_by_css_selector('.search-result__info')
        data = []
        for profile in profiles[:10]:
            name = profile.find_element_by_css_selector('.actor-name').text
            headline = profile.find_element_by_css_selector('.subline-level-1').text
            location = profile.find_element_by_css_selector('.subline-level-2').text
            data.append({'Name': name, 'Headline': headline, 'Location': location})
        return data
    except Exception as e:
        print(f"Error scraping LinkedIn data: {e}")
        return []

def save_to_csv(data):
    try:
        with open('linkedin_data_scraped.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Headline', 'Location'])
            writer.writeheader()
            writer.writerows(data)
        print("Data saved to linkedin_data_scraped.csv")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

if __name__ == "__main__":
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    profiles = scrape_linkedin_data(first_name, last_name)
    if profiles:
        save_to_csv(profiles)
    else:
        print("No profiles found")
