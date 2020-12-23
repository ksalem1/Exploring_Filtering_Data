import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_list = ['january','february', 'march','april','may','june','all']
             
             
             
day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
              


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
    while True:
        city = input('Please enter a city name to filter by. You can choose from Chicago, New York City or Washington.\n').lower()
        if city not in CITY_DATA:
            print('Please enter a valid city. This could be Chicago, New York City or Washington')
            continue
        else:
            break
            

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter a month that you want to filter by. Choose from January, February, March, April, May, June or all.\n').lower()
        if month not in month_list:
            print('Please choose a valid month. This could be January, February, March, April, May, June or all')
            continue
        else:
            break
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('If you wish to filter results furthey by a particular day, please select any day of the week. This could be Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or all.\n').lower()
        if day not in day_list:
            print('Please enter a valid day. This could be Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or all.')
            continue
        else:
            break

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
    try:
        df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        

    # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['Day of week'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
        if month != 'all':
        # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = month_list.index(month) + 1

        # filter by month to create the new dataframe
            df = df[df['month'] == month]

    # filter by day of week if applicable
        if day != 'all':
        # filter by day of week to create the new dataframe
            df = df[df['Day of week']== day.title()]


        return df
    except Exception as e:
        print('Data could not be loaded due to an error: {}'.format(e))
        


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    pop_month_num = df['month'].mode()[0]
    pop_month = month_list[pop_month_num-1]#.title()
    print('Most common month is {}\n.'.format(pop_month))

    # TO DO: display the most common day of week
    pop_day = df['Day of week'].mode()[0]
    print('Most common day of week is {}.\n'.format(pop_day))
    

    # TO DO: display the most common start hour
    pop_hour = df['hour'].mode()[0]
    print('Most common hour is {}.\n'.format(pop_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station is {}\n.'.format(pop_start_station))
    

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station is {}\n.'.format(pop_end_station))
    

    # TO DO: display most frequent combination of start station and end station trip
    comb_start_end = df.groupby(['Start Station','End Station']).count()
    print('Most frequent combination of start and end stations is {}.\n'.format(comb_start_end))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_sec = sum(df['Trip Duration'])
    total_travel_time = total_time_sec/(60**2)
    print('The total travel time is {} days.\n'.format(total_travel_time))


    # TO DO: display mean travel time
    mean_time_sec = df['Trip Duration'].mean()
    mean_travel_time = mean_time_sec/60
    print('Mean travel time is {} minutes.\n'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('User types are: \n{}'.format(user_count))
    

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Gender count is: \n{}'.format(gender_count))
    except KeyError:
        print('Sorry, gender data not available in records.')
    finally:
        print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest birth year is {}.'.format(earliest_birth_year))
    except KeyError:
        print('Sorry, birth year data not available in records.')
    finally:
        print('\n\n')
    
    try:
        recent_birth_year = df['Birth Year'].max()
        print('Most recent birth year is {}.'.format(recent_birth_year))
    except Exception:
        print('Sorry, birth year data not available in records.')
    finally:
        print('\n\n')
    
    try:
        common_birth_year = df['Birth Year'].value_counts().idxmax()
        print('Most common birth year is {}.'.format(common_birth_year))
    except Exception:
       print('Sorry, an error has occured. Cannot calculate most common birth year')
    finally:
        print('\n\n')
              
              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def display_raw_data(city):
    while True:
        df_raw = pd.read_csv(CITY_DATA[city])
        more_raw_data = input('Would you like to see more raw data? Please respond with either yes or no \n').lower()
        if more_raw_data == 'yes':
     
            print(df_raw.sample(n=5))
            continue
        else:
            break
                        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()