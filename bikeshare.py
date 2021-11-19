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
        city = input("\n would you like to see data for  chicago , new york city or washington?")
        city = city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
           print("please,try again")
           continue
        else:
           break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
         month = input("\n would you like to filter the data by months? choose: january,february,march, april, may, june or all")
         month = month.lower()
         if month not in( 'january','february','march', 'april', 'may', 'june', 'all' ):
             print("please,try again")
             continue
         else:
             break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n would you like to filter data by day? chooes:saturday,sunday,monday,tuesday,wednesday,thursday,friday or all")
        day = day.lower()
        if day not in ('saturday','sunday','monday','tuesday','wednesday','thursday','friday','all'):
            print("please,try again")
            continue
        else:
            break
    

    print('-'*40)
    return city ,month ,day

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name



    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    
        # filter by month to create the new dataframe
        df = df[df["month"] == month]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month= df["month"].mode()[0]
    print("\nmost common month:",most_common_month)

    # TO DO: display the most common day of week
    most_common_day= df["day_of_week"].mode()[0]
    print("\nnmost common day:",most_common_day)


    # TO DO: display the most common start hour
    most_common_start_hour= df["Start Time"].mode()[0]
    print("\nmost common start hour:",most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start= df["Start Station"].mode()[0]
    print("\nmost commonly used start station:",start)

    # TO DO: display most commonly used end station
    end= df["End Station"].mode()[0]
    print("\nmost commonly used end station:",end)
    
    combination= df.groupby(["Start Station", "End Station"]).count()
    print("\n most frequent combination of start station and end station trip:",'start '"&" ' end')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    t_travel_time= df["Trip Duration"].sum()
    print("\ntotal travel time:",t_travel_time/60*60*24,"day")
   
    # TO DO: display mean travel time
    m_travel_time= df["Trip Duration"].mean()
    print("\nmean travel time:",m_travel_time/60,"min")
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types= df["User Type"].value_counts().to_frame()
    print("\nuser types:", user_types)

    # TO DO: Display counts of gender
    try:
      gender= df["Gender"].value_counts()
      print("\ngender types:",gender)
    except KeyError:
      print("\ngender types:not available")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      e_year=df["Birth Year"].min()
      print("\nearliest year:", e_year)
    except KeyError:
       print("\nearliest year:not available")
    
    try:
      mr_year=df["Birth Year"].max()
      print("\nmost recent year:", mr_year)
    except KeyError:
       print("\nmost recent year :not available")

    try:
      mc_year=df["Birth Year"].mode()[0]
      print("\nmost common year:", mc_year)
    except KeyError:
       print("\nmost common year :not available")


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)
    
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """Displays data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_data = input("Would you like to view 5 rows of individual trip data? enter yes or no?")
        if view_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        while True:
           view_data = input("Would you like to view 5 rows of individual trip data? enter yes or no?")
           if view_data.lower() != 'yes':
               break
           display_data(df)
           break
            
      
        restart = input('\nwould you like to restart? enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
