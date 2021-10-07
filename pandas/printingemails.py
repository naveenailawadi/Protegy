import pandas as pd


def print_emails(filename):
    df = pd.read_csv(filename)

    for index, row in df.iterrows():
        print(f"{row['company']}'s email: \n{row['email']}\n")


input_file = input('Filename: ')
print_emails(input_file)
