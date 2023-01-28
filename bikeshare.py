import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_filters = ['chicago', 'new york city', 'washington']
    city = input("Enter which city you would like to see its data: Chicago, New York or Washington: ")
    city=city.lower()
    while city not in city_filters:
           city = input('Invalid input! Please enter valid city name ')
           city=city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    month_filter = ['all', 'january', 'february', 'march', 'april', 'may', 'june']    
    month = input('Enter month to filter by: ')
    month=month.lower()
    while month not in month_filter:
        month = input('Invalid input! Please enter a valid month or type \"all\" to select every month: ')
        month=month.lower()
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days_filter = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = input('Enter day to filter by: ')
    day=day.lower()
    while day not in days_filter:
        day = input('Invalid input! Please enter a valid day or type \"all\" to select every day ')
        day=day.lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # loading data file into dataframe
    df=pd.read_csv(CITY_DATA[city])
    
    
    # convert Start Time to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    
    # extract month / day of week / hour from Start Time and creating three new columns
    df['month']=df['Start Time'].dt.month
    df['day_of_the_week']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month)+1
        df=df[df['month']==month]
        
    #filter by day if applicable
    if day != 'all':      
        df=df[df['day_of_the_week']==day.title()]
        
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # convert start time column to datetime
    #df['Start Time']=pd.to_datetime(df["Start Time"])

    # TO DO: display the most common month
    #df['month']=df['Start Time'].dt.month
    popular_month=df['month'].mode()[0]
    #months=['January', 'February', 'March', 'April', 'May', 'June']
    print(f'The Most Popular Month is: {popular_month}')


    # TO DO: display the most common day of week   
    popular_day=df['day_of_the_week'].mode()[0]    
    print(f'The Most Popular Day is: {popular_day}')


    # TO DO: display the most common start hour
    popular_hour=df['hour'].mode()[0]
    print(f'The Most popular Start Hour is: {popular_hour}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most popular Start Station: ', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('The most popular End Station: ', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of Start and End Station Trips:\n\n', df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    # modification 1
    print("\nDisclaimer: The most frequent combination of Start and End Stations indicates that their might not be any bicyles available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Trip Duration: ', df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('Mean Trip Duration: ', df['Trip Duration'].mean())
          
          


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print(f'Counts of user types:\n{user_type}')
    
                   
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
          gender=df['Gender'].value_counts()
          print(f'Counts of user gender:\n {gender}')
    else:
        print('Dataset does not contain Gender column')
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest Year of Birth: ', df['Birth Year'].min(),'\n')
        print('Most Recent Year of Birth: ', df['Birth Year'].max(),'\n')
        print('Most Common Year of Birth: ', df['Birth Year'].mode()[0],'\n')
    else:
        print('Dataset does not contain Birth Year column')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Modification 2
    print("\nPro tip: Use these statistics to find out who is targeted demographic.")  

    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
          
        # ask user whether they would like to see raw data
        user_input = input('Would you like to see raw data? Enter Yes or No. \n')
        enter = ['yes', 'no']
          
        while user_input.lower() not in enter:
          user_input=input('Please enter Yes or No: ')          
          
        n=0
        while True:
          if user_input.lower() == 'yes':
             print(df.iloc[n:n+5])
             n+=5
             user_input=input('Would you like to see more data? Enter Yes or No. \n ')
             while user_input.lower() not in enter:
                 user_input=input('Please enter Yes or No: ')
                 user_input=user_input.lower()
          else:
             break
          
          

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart not in enter:
          restart = input('Please enter Yes or No: ')
          restart=restart.lower()
          
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
        main()
