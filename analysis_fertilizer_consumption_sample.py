# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:08:40 2025

@author: athul
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_fertilizer_usage(df_old, df_new,state_zone_mapping):
    # Question 1: Fertilizer usage change over 2007-2010 and 2015-2020
    # For old data (2007-2010) - using only the total columns
    df_old_sum = df_old[['State/Zone', 'Total_2007_08', 'Total_2008_09', 'Total_2009_10']].copy()
    df_old_sum['Total_Fertilizer'] = df_old_sum[['Total_2007_08', 'Total_2008_09', 'Total_2009_10']].sum(axis=1)

    # For new data (2015-2020) - using only the total columns
    df_new_sum = df_new[['State/Zone', 'Total_2015_16', 'Total_2016_17', 'Total_2017_18', 'Total_2018_19', 'Total_2019_20']].copy()
    df_new_sum['Total_Fertilizer'] = df_new_sum[['Total_2015_16', 'Total_2016_17', 'Total_2017_18', 'Total_2018_19', 'Total_2019_20']].sum(axis=1)

    plt.figure(figsize=(12, 6))

    # Old data plot (2007-2010)
    sns.barplot(x='State/Zone', y='Total_Fertilizer', data=df_old_sum, color='blue')
    plt.title('Total Fertilizer Usage (2007-2010) - Old Data')
    plt.xlabel('State/Zone')
    plt.ylabel('Total Fertilizer Usage')
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.show()

    # New data plot (2015-2020)
    plt.figure(figsize=(12, 6))
    sns.barplot(x='State/Zone', y='Total_Fertilizer', data=df_new_sum, color='green')
    plt.title('Total Fertilizer Usage (2015-2020) - New Data')
    plt.xlabel('State/Zone')
    plt.ylabel('Total Fertilizer Usage')
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.show()
    
    total_old = df_old_sum['Total_Fertilizer'].sum()
    total_new = df_new_sum['Total_Fertilizer'].sum()
    
    # Plot for Question 1 - Fertilizer usage change over time
    plt.figure(figsize=(8, 6))
    sns.barplot(x=['Old Data (2007-2010)', 'New Data (2015-2020)'], y=[total_old, total_new], palette='Blues')
    plt.title('Total Fertilizer Usage: Old vs New Data (Across All States)')
    plt.xlabel('Period')
    plt.ylabel('Total Fertilizer Usage')
    plt.grid(True)
    plt.show()
    
    # Summing N, P, and K fertilizer usage by zone for old data (2007-2010)
    df_old_sum = df_old[['State/Zone', 'N_2007_08', 'P_2007_08', 'K_2007_08', 'N_2008_09', 'P_2008_09', 'K_2008_09', 'N_2009_10', 'P_2009_10', 'K_2009_10']].copy()
    df_old_sum['N'] = df_old_sum[['N_2007_08', 'N_2008_09', 'N_2009_10']].sum(axis=1)
    df_old_sum['P'] = df_old_sum[['P_2007_08', 'P_2008_09', 'P_2009_10']].sum(axis=1)
    df_old_sum['K'] = df_old_sum[['K_2007_08', 'K_2008_09', 'K_2009_10']].sum(axis=1)
    
    # Map states to zones
    df_old_sum['Zone'] = df_old_sum['State/Zone'].map(state_zone_mapping)
    
    # Sum N, P, and K fertilizer usage by zone for old data
    old_zone_sum = df_old_sum.groupby('Zone')[['N', 'P', 'K']].sum().reset_index()
    
    # Summing N, P, and K fertilizer usage by zone for new data (2015-2020)
    df_new_sum = df_new[['State/Zone', 'N_2015_16', 'P_2015_16', 'K_2015_16', 'N_2016_17', 'P_2016_17', 'K_2016_17', 'N_2017_18', 'P_2017_18', 'K_2017_18', 'N_2018_19', 'P_2018_19', 'K_2018_19', 'N_2019_20', 'P_2019_20', 'K_2019_20']].copy()
    df_new_sum['N'] = df_new_sum[['N_2015_16', 'N_2016_17', 'N_2017_18', 'N_2018_19', 'N_2019_20']].sum(axis=1)
    df_new_sum['P'] = df_new_sum[['P_2015_16', 'P_2016_17', 'P_2017_18', 'P_2018_19', 'P_2019_20']].sum(axis=1)
    df_new_sum['K'] = df_new_sum[['K_2015_16', 'K_2016_17', 'K_2017_18', 'K_2018_19', 'K_2019_20']].sum(axis=1)
    
    # Map states to zones
    df_new_sum['Zone'] = df_new_sum['State/Zone'].map(state_zone_mapping)
    
    # Sum N, P, and K fertilizer usage by zone for new data
    new_zone_sum = df_new_sum.groupby('Zone')[['N', 'P', 'K']].sum().reset_index()
    
    # Plotting for old data (2007-2010)
    plt.figure(figsize=(12, 6))
    bar_width = 0.25
    index = range(len(old_zone_sum))
    
    # Plotting the bars for N, P, K
    plt.bar(index, old_zone_sum['N'], bar_width, label='N', color='blue')
    plt.bar([i + bar_width for i in index], old_zone_sum['P'], bar_width, label='P', color='orange')
    plt.bar([i + 2 * bar_width for i in index], old_zone_sum['K'], bar_width, label='K', color='green')
    
    plt.title('Fertilizer Usage by Zone (2007-2010) - Old Data')
    plt.xlabel('Zone')
    plt.ylabel('Fertilizer Usage (N, P, K)')
    plt.xticks([i + bar_width for i in index], old_zone_sum['Zone'], rotation=45)
    plt.legend(title='Fertilizer Type')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Plotting for new data (2015-2020)
    plt.figure(figsize=(12, 6))
    
    # Plotting the bars for N, P, K
    plt.bar(index, new_zone_sum['N'], bar_width, label='N', color='blue')
    plt.bar([i + bar_width for i in index], new_zone_sum['P'], bar_width, label='P', color='orange')
    plt.bar([i + 2 * bar_width for i in index], new_zone_sum['K'], bar_width, label='K', color='green')
    
    plt.title('Fertilizer Usage by Zone (2015-2020) - New Data')
    plt.xlabel('Zone')
    plt.ylabel('Fertilizer Usage (N, P, K)')
    plt.xticks([i + bar_width for i in index], new_zone_sum['Zone'], rotation=45)
    plt.legend(title='Fertilizer Type')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    try:
        # Summing N, P, and K fertilizer usage by year for old data (2007-2010)
        old_data_years = ['2007_08', '2008_09', '2009_10']
        df_old_sum = df_old[[
            'State/Zone', f'N_{old_data_years[0]}', f'P_{old_data_years[0]}', f'K_{old_data_years[0]}',
            f'N_{old_data_years[1]}', f'P_{old_data_years[1]}', f'K_{old_data_years[1]}',
            f'N_{old_data_years[2]}', f'P_{old_data_years[2]}', f'K_{old_data_years[2]}'
        ]]
    
        # Extract total N, P, K for the years (2007-2010)
        sum_old_n = df_old_sum[[f'N_{year}' for year in old_data_years]].sum(axis=0).values
        sum_old_p = df_old_sum[[f'P_{year}' for year in old_data_years]].sum(axis=0).values
        sum_old_k = df_old_sum[[f'K_{year}' for year in old_data_years]].sum(axis=0).values
    
        # Summing N, P, and K fertilizer usage by year for new data (2015-2020)
        new_data_years = ['2015_16', '2016_17', '2017_18', '2018_19', '2019_20']
        df_new_sum = df_new[[
            'State/Zone', f'N_{new_data_years[0]}', f'P_{new_data_years[0]}', f'K_{new_data_years[0]}',
            f'N_{new_data_years[1]}', f'P_{new_data_years[1]}', f'K_{new_data_years[1]}',
            f'N_{new_data_years[2]}', f'P_{new_data_years[2]}', f'K_{new_data_years[2]}',
            f'N_{new_data_years[3]}', f'P_{new_data_years[3]}', f'K_{new_data_years[3]}',
            f'N_{new_data_years[4]}', f'P_{new_data_years[4]}', f'K_{new_data_years[4]}'
        ]]
    
        # Extract total N, P, K for the years (2015-2020)
        sum_new_n = df_new_sum[[f'N_{year}' for year in new_data_years]].sum(axis=0).values
        sum_new_p = df_new_sum[[f'P_{year}' for year in new_data_years]].sum(axis=0).values
        sum_new_k = df_new_sum[[f'K_{year}' for year in new_data_years]].sum(axis=0).values
    
        # Plotting for old data (2007-2010)
        plt.figure(figsize=(10, 6))
        plt.plot(old_data_years, sum_old_n, label='N', color='green', marker='o')
        plt.plot(old_data_years, sum_old_p, label='P', color='blue', marker='o')
        plt.plot(old_data_years, sum_old_k, label='K', color='red', marker='o')
        plt.title('Fertilizer Usage (NPK) over the years (2007-2010) - Old Data')
        plt.xlabel('Year')
        plt.ylabel('Total Fertilizer Usage')
        plt.legend()
        plt.grid(True)
        plt.show()
    
        # Plotting for new data (2015-2020)
        plt.figure(figsize=(10, 6))
        plt.plot(new_data_years, sum_new_n, label='N', color='green', marker='o')
        plt.plot(new_data_years, sum_new_p, label='P', color='blue', marker='o')
        plt.plot(new_data_years, sum_new_k, label='K', color='red', marker='o')
        plt.title('Fertilizer Usage (NPK) over the years (2015-2020) - New Data')
        plt.xlabel('Year')
        plt.ylabel('Total Fertilizer Usage')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


   


def filter_state_wise_data(d1, d2):
    

    d2['Sl.'] = pd.to_numeric(d2['Sl.'], errors='coerce')  # Convert column A to numeric, non-numeric to NaN
    df_new = d2.dropna(subset=['Sl.'])  # Drop rows where column A is NaN
    #df_new['Sl.'] = df_new['Sl.'].astype(int)
    # Reset the index if required
    df_new = df_new.reset_index(drop=True)
    # Show the new DataFrame
    #print(df_new)
    
    d1['Sl.'] = pd.to_numeric(d1['Sl.'], errors='coerce')  # Convert column A to numeric, non-numeric to NaN
    df_old = d1.dropna(subset=['Sl.'])  # Drop rows where column A is NaN
    #df_old['Sl.'] = df_old['Sl.'].astype(int)
    # Reset the index if required
    df_old = df_old.reset_index(drop=True)
    # Show the new DataFrame
    #print(df_old)
    
    return df_new, df_old

def create_state_zone_mapping(df_new, df_old):
    # Combine the states from both dataframes into a single list
    states_combined = pd.concat([df_new['State/Zone'], df_old['State/Zone']]).unique()
    
    # Define the state-to-zone mapping based on your knowledge of regions
    # You can manually categorize the states into their respective zones here.
    # Example of mapping (expand this as necessary):
    state_zone_mapping = {
        "Andhra Pradesh": "South",
        "Telangana": "South",
        "Karnataka": "South",
        "Kerala": "South",
        "TamilNadu": "South",
        "Puducherry": "South",
        "A&N Islands": "South",
        "Lakshadweep": "South",
        "Gujarat": "West",
        "Madhya Pradesh": "West",
        "Chhattisgarh": "West",
        "Maharashtra": "West",
        "Rajasthan": "West",
        "Goa": "West",
        "Daman & Diu": "West",
        "D&N Haveli": "West",
        "Haryana": "North",
        "Punjab": "North",
        "Uttar Pradesh": "North",
        "Uttarakhand": "North",
        "Himachal Pradesh": "North",
        "J&K": "North",
        "Delhi": "North",
        "Chandigarh": "North",
        "Bihar": "East",
        "Jharkhand": "East",
        "Odisha": "East",
        "West Bengal": "East",
        "Assam": "East",
        "Tripura": "East",
        "Manipur": "East",
        "Meghalaya": "East",
        "Nagaland": "East",
        "Arunachal Pradesh": "East",
        "Mizoram": "East",
        "Sikkim": "East",
        "Pondicherry": "South"
    }

    # Ensure that all the states in the combined list have a corresponding zone
    missing_states = [state for state in states_combined if state not in state_zone_mapping]
    if missing_states:
        print(f"Warning: The following states are missing in the zone mapping: {missing_states}")

    return state_zone_mapping


if __name__ == "__main__":
    # Load the Excel sheet
    file_name = "Fertilizer_Consumption.xlsx" #enter your path here accordingly
    sheet_name = "2007-10"
    
    # Read the data without assuming a header
    data_old = pd.read_excel(file_name, sheet_name=sheet_name, header=None)
    
    # Assign appropriate column names manually
    data_old.columns = [
        "Sl.", "State/Zone",
        "N_2007_08", "P_2007_08", "K_2007_08", "Total_2007_08",
        "N_2008_09", "P_2008_09", "K_2008_09", "Total_2008_09",
        "N_2009_10", "P_2009_10", "K_2009_10", "Total_2009_10"
    ]
    
    # Remove the row immediately below the header
    data_old = data_old.drop(index=0).reset_index(drop=True)
    data_old = data_old.drop(index=0).reset_index(drop=True)
    
    # Preview the cleaned data
    #print(data_old.head())
    
    # Save the cleaned data to a new file for reference (optional)
    data_old.to_csv("Fertilizer_Consumption_Cleaned_old.csv", index=False)
    
    sheet_name = "2015-20"
    
    # Read the data without assuming a header
    data_new = pd.read_excel(file_name, sheet_name=sheet_name, header=None)
    
    # Assign appropriate column names manually
    data_new.columns = [
        "Sl.", "State/Zone",
        "N_2015_16", "P_2015_16", "K_2015_16", "Total_2015_16",
        "N_2016_17", "P_2016_17", "K_2016_17", "Total_2016_17",
        "N_2017_18", "P_2017_18", "K_2017_18", "Total_2017_18",
        "N_2018_19", "P_2018_19", "K_2018_19", "Total_2018_19",
        "N_2019_20", "P_2019_20", "K_2019_20", "Total_2019_20"
    ]
    
    # Remove the row immediately below the header
    data_new = data_new.drop(index=0).reset_index(drop=True)
    data_new = data_new.drop(index=0).reset_index(drop=True)
    
    # Preview the cleaned data
    #print(data_new.head())
    
    # Save the cleaned data to a new file for reference (optional)
    data_new.to_csv("Fertilizer_Consumption_Cleaned_new.csv", index=False)

    df_new,df_old = filter_state_wise_data(data_old, data_new)  
    state_zone_mapping = create_state_zone_mapping(df_new, df_old)
    df_new['Zone'] = df_new['State/Zone'].map(state_zone_mapping)
    df_old['Zone'] = df_old['State/Zone'].map(state_zone_mapping)
    
    analyze_fertilizer_usage(df_old,df_new,state_zone_mapping)
