import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the data
df = pd.read_csv(r'C:\Users\Farhan\Downloads\Data_Science_Python_Notes\hw1_demo\pandas data frame\pokemon_data.csv')

# Function to display menu
def display_menu():
    print("\nWelcome to the Pokémon Database")
    print("Please choose an option:")
    print("1. View Pokémon sorted by HP")
    print("2. View Pokémon sorted by Attack")
    print("3. View Pokémon sorted by Defense")
    print("4. View Pokémon sorted by Special Attack")
    print("5. View Pokémon sorted by Special Defense")
    print("6. View Pokémon sorted by Speed")
    print("7. View Pokémon by Type")
    print("8. View Legendary or Non-Legendary Pokémon")
    print("9. View Pokémon by Generation")
    print("10. Search Pokémon by Name")
    print("11. Compare Pokémon by Stats")  # New option
    print("12. Exit")

# Function to display sorted Pokémon
def display_sorted_pokemon(stat, ascending=True):
    sorted_df = df.sort_values(by=stat, ascending=ascending)
    print(sorted_df[['Name', 'Type 1', 'Type 2', stat]])


# Function to compare Pokémon by stats using a line graph
def compare_pokemon_stats():
    num_pokemon = int(input("Enter the number of Pokémon to compare (2 to 6): "))
    if num_pokemon < 2 or num_pokemon > 6:
        print("Invalid number of Pokémon. Please enter a number between 2 and 6.")
        return
    
    pokemon_names = []
    while len(pokemon_names) < num_pokemon:
        pokemon_name = input(f"Enter the name of Pokémon {len(pokemon_names) + 1}: ").strip().capitalize()
        if pokemon_name in df['Name'].values:
            pokemon_names.append(pokemon_name)
        else:
            print(f"Pokemon '{pokemon_name}' not found. Please enter a valid Pokémon name.")

    stats_columns = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    filtered_df = df[df['Name'].isin(pokemon_names)]
    
    # Plotting the stats using a line graph
    plt.figure(figsize=(12, 6))
    for index, stat in enumerate(stats_columns):
        plt.plot(filtered_df['Name'], filtered_df[stat], marker='o', label=stat)

    plt.xlabel('Pokémon')
    plt.ylabel('Stats')
    plt.title(f'Stats Comparison for {", ".join(pokemon_names)}')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.show()


# Function to filter Pokémon by type
def filter_by_type():
    type1 = input("Enter the primary type of Pokémon: ").capitalize()
    filtered_df = df[df['Type 1'] == type1]
    print(filtered_df[['Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']])

# Function to filter Pokémon by legendary status
def filter_by_legendary():
    status = input("Enter 'True' for Legendary Pokémon or 'False' for non-Legendary Pokémon: ").capitalize()
    filtered_df = df[df['Legendary'] == status]
    print(filtered_df[['Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']])

# Function to filter Pokémon by generation
def filter_by_generation():
    generation = int(input("Enter the generation (1-6): "))
    filtered_df = df[df['Generation'] == generation]
    print(filtered_df[['Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']])


# Function to search Pokémon by name
def search_pokemon_by_name():
    pokemon_name = input("Enter the name of the Pokémon: ").capitalize()
    filtered_df = df[df['Name'].str.contains(pokemon_name)]
    
    if len(filtered_df) == 0:
        print(f"No Pokémon found with the name '{pokemon_name}'.")
    else:
        print(filtered_df[['Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']])


# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")

        if choice == '1':
            order = input("Sort by HP (1: Highest to Lowest, 2: Lowest to Highest): ")
            display_sorted_pokemon('HP', ascending=(order == '2'))
        elif choice == '2':
            order = input("Sort by Attack (1: Highest to Lowest, 2: Lowest to Highest): ")
            display_sorted_pokemon('Attack', ascending=(order == '2'))
        elif choice == '3':
            order = input("Sort by Defense (1: Highest to Lowest, 2: Lowest to Highest): ")
            display_sorted_pokemon('Defense', ascending=(order == '2'))
        elif choice == '4':
            order = input("Sort by Special Attack (1: Highest to Lowest, 2: Lowest to Highest): ")
            display_sorted_pokemon('Sp. Atk', ascending=(order == '2'))
        elif choice == '5':
            order = input("Sort by Special Defense (1: Highest to Lowest, 2: Lowest to Highest): ")
            display_sorted_pokemon('Sp. Def', ascending=(order == '2'))
        elif choice == '6':
            order = input("Sort by Speed (1: Highest to Lowest, 2: Lowest to Highest): ")
            display_sorted_pokemon('Speed', ascending=(order == '2'))
        elif choice == '7':
            filter_by_type()
        elif choice == '8':
            filter_by_legendary()
        elif choice == '9':
            filter_by_generation()
        elif choice == '10':
            search_pokemon_by_name()
        elif choice == '11':
            compare_pokemon_stats()  # Call the new function for comparing Pokémon stats
        elif choice == '12':
            print("Thank you for using the Pokémon Database. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 12.")

# Run the main function
if __name__ == "__main__":
    main()
