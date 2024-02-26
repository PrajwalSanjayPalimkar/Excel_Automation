import pandas as pd

# Read the initial Excel file
file_path = 'C:\\Users\\admin\\OneDrive\\Desktop\\Example.xlsx'
df = pd.read_excel(file_path)

# Validation 1: Compare column D with column A
df['Accounts Match'] = df['ACCOUNT_ID.1'] == df['ACCOUNT_ID']

# Validation 2: Compare column F with column B
df['Validation'] = df['CHARGES_WITH_ROUND.1'] == df['CHARGES_WITH_ROUND']
df['Amt Diff'] = df['CHARGES_WITH_ROUND.1'] - df['CHARGES_WITH_ROUND']

# Set default value for column N
df['Category'] = 'Undefined'

# Update column N based on conditions
for index, row in df.iterrows():
    if row['Category'] == 'Undefined':
        if '.' in str(row['CHARGES_WITH_ROUND.1']):
            if str(row['CHARGES_WITH_ROUND.1']).replace('.', '_') in df['PACKAGE_ID'].values:
                df.at[index, 'Category'] = 'PackagePriceMatch'

# Update 'MatchWithPrevBill' for matching values in column F and B
df.loc[df['CHARGES_WITH_ROUND.1'] == df['CHARGES_WITH_ROUND'], 'Category'] = 'MatchWithPrevBill'

# Save the updated DataFrame to a new Excel file
new_file_path = 'updated_excel_file.xlsx'
df.to_excel(new_file_path, index=False)

# Read the new Excel file as a new DataFrame for further validations
new_df = pd.read_excel(new_file_path)
