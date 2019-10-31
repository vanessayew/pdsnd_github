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
    while True:
        city = input("Please Select a City. (Chicago, New York City, Washington): \n").lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print ('Sorry, you have entered an invalid city. Please enter again!')
            continue

    while True:
        ask = input("Would you like to filter the data by month, day, or apply no filter? (Enter: month, day or none)\n").lower()
        if ask == "month":
            # TO DO: get user input for month (all, january, february, ... , june)
            while True:
                month= input("Please enter the name of the month(eg:january, february, march): \n").lower()
                if month in ('january', 'february', 'march', 'april','may', 'june','july','august', 'september',                                                          'october','november','december'):
                    day = 'all'
                    print('-'*40)
                    return city, month, day
                else:
                    print ('Sorry, this is not a valid month. Please enter again!')
                    continue
        elif ask == 'day':
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            while True:
                day =  input("Please enter a day of the week (eg:monday,tuesday, wednesday): \n").lower()
                if day in ("monday", "tuesday", "wednesday", "thursday", "friday","saturday","sunday"):
                    month = 'all'
                    print('-'*40)
                    return city, month, day
                else:
                    print ('Sorry, this is not a valid day of the week. Please enter again.')
                    continue
        elif ask == 'none':
            city = city
            month = "all"
            day = "all"
            return city, month, day
        else:
            print("Sorry! Your input is not valid. Please enter again!")



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
#load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'october','may', 'june', 'july', 'august', 'september','october', 'november', 'december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('Popular times of travel')
    print('*' * 30)

# TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)
# TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', popular_day)
# TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('Popular Stations and Trip')
    print('*' * 30)

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most common Start Station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most common End Station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    fav_combination = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('Most Frequent combination:\n', fav_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('Trip Duration')
    print('*'*30)

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    print ("User statistics")
    print('*'*30)
    print(user_types)
    print ("\nGender statistics")
    print('*'*30)
    try:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
        # TO DO: Display earliest, most recent, and most common year of birth
        oldest_user = min(df['Birth Year'])
        youngest_user = max(df['Birth Year'])
        most_common_year = df['Birth Year'].mode()[0]
        print("The oldest user was born in:",oldest_user)
        print("The youngest user was born in:", youngest_user)
        print("The most common year of birth:", most_common_year)
    except:
        print("Sorry! No gender statistics available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    # iterate from 0 to the number of rows in steps of 5
    iter = 5
    row = 5
    dfLen = len(df)
    # iterate from 0 to the number of rows in steps of 5
    while True:
        ask = input("Do you want to see the raw data? Enter yes or no\n").lower()
        if ask == 'yes':
            print(df.head())
            break
        elif ask == 'no':
            break
        elif ask != "yes" and ask != "no":
            print("Sorry! The input entered is not valid. Please enter again!")
            continue

    if ask == 'yes':
        while True:
            show = input("Do you want to see more data? Enter yes or no\n").lower()

            if show == 'yes':
                if(iter != dfLen):
                    iter += row
                else:
                    iter = row
                if(iter > dfLen):
                    iter = dfLen
                print(df[iter - row: iter])
            elif show == 'no':
                break;
            elif show !='yes' and show !='no':
                print("The input is not valid! Please Enter again!")
print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
