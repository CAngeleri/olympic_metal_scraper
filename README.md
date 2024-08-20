## Olympic Medal Table Scraper
This Python script scrapes Olympic medal data from a Wikipedia page and saves the information into a JSON file.

## Overview
The script performs the following tasks:

Fetches the HTML content of the Wikipedia page containing the all-time Olympic Games medal table.
Parses the HTML to find and extract the relevant data from the table.
Collects the top 10 countries and their medal counts.
Saves the extracted data to a JSON file.

## Prerequisites
Ensure you have the following Python packages installed:

requests
beautifulsoup4

You can install them using pip:
bash

pip install requests beautifulsoup4

## Script Details
URL: The Wikipedia page URL is https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table. 
</br>
Table Extraction: The script locates the table with the class wikitable.
</br>
Data Extraction: The script extracts country names, gold, silver, bronze, and total medal counts.
</br>
Output: The data for the top 10 countries is saved in a file named medal_counts.json.
</br>
Running the Script
Save the script to a file, e.g., scraper.py.

## Run the script using Python:

bash
Copy code
python scraper.py
The JSON file medal_counts.json will be created in the same directory as the script.

## Output Format
The output JSON file will contain an array of objects with the following structure:

json
Copy code
[
    {
        "Country": "Country Name",
        "Total Medals": "Total Number",
        "Gold Medals": "Number",
        "Silver Medals": "Number",
        "Bronze Medals": "Number"
    },
    ...
]
Each object represents a country and its medal counts.

## Notes
The script currently processes only the top 10 countries for efficient testing.
Adjust the script as needed to scrape more data or modify the output format.