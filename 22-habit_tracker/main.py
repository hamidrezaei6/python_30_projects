# python -m pip install pandas
# python -m pip install tabulate

import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit


def main():
    habits = [
        track_habit('coffee', datetime(2023, 6, 3), cost=1, minutes_used=5),
        track_habit('cigarette', datetime(2021, 12, 25), cost=0.5, minutes_used=2),
        track_habit('sugar drink',datetime(2024,1,15),cost=0.45,minutes_used=4)
    ]

    df = pd.DataFrame(habits)

    print(tabulate(df, headers='keys', tablefmt='psql'))


if __name__ == '__main__':
    main()
