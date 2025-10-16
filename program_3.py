# Title: Population Data
# Author: Arianna Endres
# Date: 10/15/2025

def main():
    # In this program, the user inputs year, name of state, and population.
    # This data is stored in a list of lists. The user can then search these
    # lists for a specific year and find the population data for that year.

    all_entered_values = []

    add_another_list = 'y'

    while add_another_list == 'y':
        # Get the population data input from the user.
        print('Enter the information for the set of data.')
        year = int(input('Year the data was collected: '))
        state = input('State from which the data was collected: ')
        population = int(input('Population: '))

        # Create a list containing the values.
        list1 = [year, state, population]

        # Append the values to the main list.
        all_entered_values.append(list1)

        # Ask user whether or not they'd like to add more data.
        add_another_list = input('Add another set of data? (Y/N) ')

    search_another_year = 'y'

    while search_another_year == 'y':
        # Now have the user enter a year.
        search = int(input('Enter the year you would like to search: '))

        # Pass the list and year to the sum_population_for_year
        sum_population_for_year(all_entered_values, search)

        # Ask user whether or not they'd like to search for another year.
        search_another_year = input('Search another year? (Y/N) ').lower()


def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year.

    populations_for_year = []

    # Find the populations for the inputted year.
    for x in all_entered_values:
        if x[0] == year_to_sum:
            populations_for_year.append(x[2])

    # Sum the populations for that year.
    totalled_population = sum(populations_for_year)

    # Display message to input another year if year not found.
    if totalled_population == 0:
        print('No data found for that year.')
        return

    # Print the totalled population.
    print(f'The total population for the year {year_to_sum} was {totalled_population}')


# Call the main function.
if __name__ == '__main__':
    main()