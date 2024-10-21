# Disney Show Data Entry CLI

This is a Python-based terminal program designed to collect and store user input about their favorite Disney shows. It utilizes the `rich` library to display a visually appealing table of example shows and allows users to enter details for additional shows. The collected data is saved in either JSON or CSV format for future reference.

## Features

- Displays a table of famous Disney shows as examples.
- Prompts users to enter their favorite Disney shows, including:
  - Title of the show
  - Release year
  - Number of seasons
- Confirms user input to ensure accuracy.
- Saves the data to a JSON or CSV file in the same directory.

## How to Use

1. Clone this repository or download the `cli_data_entry.py` file.
2. Ensure you have Python installed on your machine.
3. Install the `rich` library if you haven't already:
   ```bash
   pip install rich
