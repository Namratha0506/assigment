import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def line_plot(data):
    """
    Create a line plot to visualize the trend of new deaths over time in specific countries.

    Parameters:
    data (DataFrame): A Pandas DataFrame containing COVID-19 data, including 'Country', 'Date_reported', and 'New_deaths' columns.

    Returns:
    None

    This function takes a DataFrame containing COVID-19 data and plots the trend of new deaths over time
    for the following countries: Nigeria, Paraguay, and Afghanistan. The x-axis represents the date of reporting,
    and the y-axis represents the number of new deaths. The plot is displayed with a legend.

    Note:
    Make sure the 'Country' column in the DataFrame contains the country names as specified in the code.
    """

    # Extract rows corresponding to different countries
    afghanistan_rows = data[data['Country'] == 'Afghanistan']
    Paraguay_rows = data[data['Country'] == 'Paraguay']
    Nigeria_rows = data[data['Country'] == 'Nigeria']

    # Create a new figure for the plot
    plt.figure(figsize=(20, 10))

    # Plot the data for Nigeria with a label
    plt.plot(Nigeria_rows.Date_reported, Nigeria_rows.New_deaths, label="Nigeria")
    
    # Plot the data for Paraguay with a label
    plt.plot(Paraguay_rows.Date_reported, Paraguay_rows.New_deaths, label="Paraguay")
    
    # Plot the data for Afghanistan with a label
    plt.plot(afghanistan_rows.Date_reported, afghanistan_rows.New_deaths, label="Afghanistan")
    
    # Customize the plot by removing ticks and setting labels
    plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)
    plt.xlabel('Year')
    plt.ylabel('Death')
    
    # Display a legend to distinguish the countries on the plot
    plt.legend()
    
    # Show the plot
    plt.show()


def barplot(df):
    """
    Create a bar plot comparing the total number of deaths in three countries.

    Parameters:
    df (pandas.DataFrame): A DataFrame containing the data to be plotted.

    Returns:
    None
    """
    # Filter data for each country
    afghanistan_rows = df[df['Country'] == 'Afghanistan']
    paraguay_rows = df[df['Country'] == 'Paraguay']
    nigeria_rows = df[df['Country'] == 'Nigeria']
    
    # Calculate the total deaths for each country
    afghan_death_sum = afghanistan_rows['New_deaths'].sum()
    nigeria_death_sum = nigeria_rows['New_deaths'].sum()
    paraguay_death_sum = paraguay_rows['New_deaths'].sum()
    
    # Data for the bar plot
    countries = ['Nigeria', 'Afghanistan', 'Paraguay']
    counts = [nigeria_death_sum, afghan_death_sum, paraguay_death_sum]
    
    # Define bar colors
    bar_colors = ['tab:blue', 'tab:orange', 'tab:green']
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Create the bar plot
    ax.bar(countries, counts, color=bar_colors)
    
    # Set labels and title
    ax.set_ylabel('Deaths per country')
    ax.set_xlabel('Countries')
    ax.set_title('Death vs Country')
    
    # Display the plot
    plt.show()

def box_plot(data):
    """
    Create a box plot to visualize the distribution of new cases for specific countries.

    Parameters:
    data (DataFrame): A Pandas DataFrame containing COVID-19 data, including 'Country' and 'New_cases' columns.

    Returns:
    None

    This function takes a DataFrame containing COVID-19 data and creates a box plot to visualize the distribution
    of new cases for the countries Afghanistan, Paraguay, and Nigeria. The 'Country' column is used to group the data,
    and the 'New_cases' column is used for the box plot. Outliers are not shown on the plot.

    Note:
    Make sure the 'Country' column in the DataFrame contains the country names as specified in the code.
    """

    # Extract rows corresponding to different countries
    afghanistan_rows = data[data['Country'] == 'Afghanistan']
    Paraguay_rows = data[data['Country'] == 'Paraguay']
    Nigeria_rows = data[data['Country'] == 'Nigeria']

    # Concatenate the rows for the selected countries into a new DataFrame
    new_df = pd.concat([Nigeria_rows, afghanistan_rows, Paraguay_rows])

    # Create a box plot based on the 'Country' column grouping and 'New_cases' column data
    new_df.boxplot(by='Country', column=['New_cases'], grid=True, autorange=True, showfliers=False)
    
    # Display the box plot
    plt.show()


if __name__ == "__main__":
    # This block of code will be executed when the script is run directly, not when it's imported as a module.

    # Read data from a CSV file and select specific columns
    df = pd.read_csv('WHO-COVID.csv', usecols=['Date_reported', 'Country_code', 'Country', 'New_cases', 'New_deaths'])

    # Convert the 'Date_reported' column to a datetime data type
    df['Date_reported'] = pd.to_datetime(df['Date_reported'])

    # Generate a box plot to visualize the distribution of new cases for specific countries
    box_plot(df)

    # Generate a line plot to visualize the trend of new deaths over time for specific countries
    line_plot(df)

    # Call a function (barplot) that is not defined in the provided code. Make sure to define 'barplot' function separately.
    barplot(df)

