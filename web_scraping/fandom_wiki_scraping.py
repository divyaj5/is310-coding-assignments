import requests
from bs4 import BeautifulSoup
import csv

url = 'https://disney.fandom.com/wiki/Disney_Princess'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    character_section = soup.find('span', id='Members')
    if character_section:
        members = character_section.find_parent('h2').find_next_sibling('table')
        with open('disney_princess_characters.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Film Debut', 'Original Voice'])
            for row in members.find_all('tr')[1:]:  
                columns = row.find_all('td')
                if len(columns) >= 2:
                    character_name = columns[0].text.strip()  
                    film_debut = columns[1].text.strip()  
                    writer.writerow([character_name, film_debut])  
                    print(f"Character Name: {character_name}, Film Debut: {film_debut}")
    else:
        print("Character section not found.")
else:
    print(f"Failed to retrieve the page: {response.status_code}")
