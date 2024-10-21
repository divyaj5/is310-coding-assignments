from rich.console import Console
from rich.table import Table
import json
import csv
import os

console = Console()
console.print("Here is some initial data:", style="bold cyan")

# Display pre-created example data
table = Table(title="Famous Disney Shows")
table.add_column("Released", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Seasons", justify="right")
table.add_row("2017", "DuckTales", "3")
table.add_row("2015", "Star vs. the Forces of Evil", "4")
table.add_row("2020", "The Owl House", "3")
table.add_row("2021", "Amphibia", "3")

console.print(table)
console.print("\n[bold cyan]Now I want you to enter your preferred Disney shows:[/bold cyan]")

def get_show_data():
    show_title = console.input("Enter the title of the show: ")
    release_year = console.input("Enter the release year of the show: ")
    seasons = console.input("Enter the number of seasons: ")
    return {
        "title": show_title,
        "release_year": release_year,
        "seasons": seasons,
    }

def confirm_and_save_data(show_data, file_format='json'):
    console.print("\n[bold cyan]Here is the data you entered:[/bold cyan]")
    console.print(f"Title: {show_data['title']}")
    console.print(f"Release Year: {show_data['release_year']}")
    console.print(f"Seasons: {show_data['seasons']}")

    confirmation = console.input("[bold cyan]Is this data correct? (yes/no): [/bold cyan]")
    
    if confirmation.lower() == 'yes':
        save_data(show_data, file_format)
    else:
        console.print("[bold red]Please re-enter the data.[/bold red]")

def save_data(show_data, file_format):
    file_name = f"disney_show_data.{file_format}"
    if file_format == 'json':
        with open(file_name, 'a') as f:
            json.dump(show_data, f)
            f.write("\n")  # Write new line for each entry
    elif file_format == 'csv':
        file_exists = os.path.isfile(file_name)
        with open(file_name, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=show_data.keys())
            if not file_exists:
                writer.writeheader()  # Write header only if the file is new
            writer.writerow(show_data)
    
    console.print(f"[bold green]Data has been saved to {os.path.abspath(file_name)}[/bold green]")

def main():
    while True:
        show_data = get_show_data()
        confirm_and_save_data(show_data)

        continue_entry = console.input("[bold cyan]Do you want to enter another show? (yes/no): [/bold cyan]")
        if continue_entry.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
