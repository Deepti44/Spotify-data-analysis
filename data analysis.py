import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv(r"C:\Users\DEEPTI\OneDrive\Documents\spotify_dataset.csv")
df.set_index('Index', inplace=True)
print(df)

# Menu Functions
def display_menu():
    print('|--------------------------------------------------|')
    print('|                      MENU                        |')
    print('|--------------------------------------------------|')
    print('|              1: Data Analysis                    |')
    print('|              2: Data Manipulation                |')
    print('|              3: Data Visualization               |')
    print('|              0: EXIT                             |')
    print('|--------------------------------------------------|')

def display_analysis_menu():
    print('--------------------------------------------------')
    print('         WELCOME TO DATA ANALYSIS SECTION         ')
    print('--------------------------------------------------')
    print('1: TO SEE THE DATAFRAME')
    print('2: TO SEE THE FIRST n NUMBERS OF RECORDS')
    print('3: TO SEE THE LAST n NUMBERS OF RECORDS')
    print('4: TO ACCESS ANY ROW')
    print('5: TO SEE THE INDEX OF THE DATAFRAME')
    print('6: TO SEE THE COLUMNS OF THE DATAFRAME')
    print('7: TO SEE THE SHAPE AND SIZE OF THE DATAFRAME')
    print('8: TO CHECK IF THE DATAFRAME HAS ANY EMPTY VALUES')
    print('9: TO SEE THE MAX, MIN POPULARITY')
    print('10: TO SEE THE NUMBER OF TIMES SONG CHARTED')
    print('0: TO COME OUT OF ANALYSIS SECTION')

def display_manipulation_menu():
    print('--------------------------------------------------')
    print('         WELCOME TO DATA MANIPULATION SECTION     ')
    print('--------------------------------------------------')
    print('1: TO ADD A ROW')
    print('2: TO RENAME A COLUMN:')
    print('3: TO DELETE A ROW')
    print('4: TO DELETE A COLUMN')
    print('0: EXIT')

def add_row(df):
    values = []
    print('Enter the column details:')
    for col in df.columns:
        print(col + ": ", end="")
        col_input = input()
        values.append(col_input)
    df.loc[max(df.index) + 1] = values
    print('ROW ADDED')

def rename_col(df):
    print(df.columns)
    col = input('WHICH COLUMN YOU WOULD LIKE TO CHANGE?: ')
    new_col = input('ENTER THE NEW COLUMN NAME: ')
    if col in df.columns:
        df.rename(columns={col: new_col}, inplace=True)
        print('Column Renamed')
    else:
        print('This column does not exist')

def delete_row(df):
    row = int(input('ENTER THE ROW INDEX WHICH YOU WANT TO DELETE?: '))
    if row in df.index:
        df.drop(row, inplace=True)
        print('Row Deleted')
    else:
        print('This row does not exist')

def delete_col(df):
    col = input('ENTER THE COLUMN WHICH YOU WANT TO DELETE: ')
    if col in df.columns:
        df.drop(col, axis=1, inplace=True)
        print('Column Deleted')
    else:
        print('Column does not exist')

def display_visualization_menu():
    print('--------------------------------------------------')
    print('         WELCOME TO DATA VISUALIZATION SECTION    ')
    print('--------------------------------------------------')
    print('1: BARCHART FOR POPULARITY ANALYSIS')
    print('2: BARCHART FOR NUMBER OF TIMES SONG CHARTED')
    print('3: LINECHART FOR POPULARITY ANALYSIS')
    print('4: LINECHART FOR NUMBER OF TIMES SONG CHARTED')
    print('0: EXIT')

# Main Program
while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        while True:
            display_analysis_menu()
            ch = int(input("Enter your choice: "))
            if ch == 1:
                print(df)
            elif ch == 2:
                n = int(input('ENTER THE VALUE OF n: '))
                print(df.head(n))
            elif ch == 3:
                n = int(input('ENTER THE VALUE OF n: '))
                print(df.tail(n))
            elif ch == 4:
                row = int(input('Enter row index: '))
                print(df.loc[row])
            elif ch == 5:
                print(df.index)
            elif ch == 6:
                print(df.columns)
            elif ch == 7:
                print('Shape:', df.shape)
                print('Size:', df.size)
            elif ch == 8:
                print(df.isnull().any())
            elif ch == 9:
                print('Max Popularity:', df['Popularity'].max())
                print('Min Popularity:', df['Popularity'].min())
            elif ch == 10:
                print('Number of Times Song Charted:')
                print(df['Number of Times Charted'].value_counts())
            elif ch == 0:
                break

    elif choice == 2:
        while True:
            display_manipulation_menu()
            ch = int(input("Enter your choice: "))
            if ch == 1:
                add_row(df)
            elif ch == 2:
                rename_col(df)
            elif ch == 3:
                delete_row(df)
            elif ch == 4:
                delete_col(df)
            elif ch == 0:
                print(df)
                break

    elif choice == 3:
        while True:
            display_visualization_menu()
            ch = int(input("Enter your choice: "))
            if ch == 1:
                plt.figure(figsize=(18, 6))
                plt.bar(df['Song Name'].head(50), df['Popularity'].head(50), color='coral')
                plt.title('Top 50 Songs by Popularity')
                plt.xlabel('Song Name')
                plt.ylabel('Popularity')
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.show()
            elif ch == 2:
                plt.figure(figsize=(18, 6))
                plt.bar(df['Song Name'].head(50), df['Number of Times Charted'].head(50), color='green')
                plt.title('Top 50 Songs by Times Charted')
                plt.xlabel('Song Name')
                plt.ylabel('Number of Times Charted')
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.show()
            elif ch == 3:
                plt.figure(figsize=(18, 6))
                plt.plot(df['Song Name'].head(50), df['Popularity'].head(50), marker='o', color='blue')
                plt.title('Line Chart: Top 50 Songs Popularity')
                plt.xlabel('Song Name')
                plt.ylabel('Popularity')
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.show()
            elif ch == 4:
                plt.figure(figsize=(18, 6))
                plt.plot(df['Song Name'].head(50), df['Number of Times Charted'].head(50), marker='o', color='purple')
                plt.title('Line Chart: Top 50 Songs Charted Count')
                plt.xlabel('Song Name')
                plt.ylabel('Number of Times Charted')
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.show()
            elif ch == 0:
                break

    elif choice == 0:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
