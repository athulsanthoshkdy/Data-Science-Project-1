# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 23:03:01 2025

@author: athul
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_fertilizer_change(df_old, df_new):
    # Summing total usage across all states
    total_old = df_old['Total_2009_10'].sum()
    total_new = df_new['Total_2019_20'].sum()

    # Data for the plot
    periods = ['2007-2010', '2015-2020']
    totals = [total_old, total_new]

    # Plotting
    plt.bar(periods, totals, color=['skyblue', 'orange'])
    plt.title('Fertilizer Usage Over Time')
    plt.xlabel('Period')
    plt.ylabel('Total Fertilizer Usage')
    plt.show()
    
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

def zone_wise_analysis_with_plots(df_new, df_old, state_zone_mapping):
    # Step 1: Combine df_new and df_old
    df_combined = pd.concat([df_new, df_old], ignore_index=True)
    
    # Step 2: Add a 'Zone' column by mapping states to their respective zones

    #df_combined['Zone'] = df_combined['State/Zone'].map(state_zone_mapping)
    
    # Step 3: Extract total NPK columns for both old and new data
    # For old data (2007-08 to 2009-10)
    df_combined['Total_N_2007_08'] = df_combined['N_2007_08'] if 'N_2007_08' in df_combined.columns else 0
    df_combined['Total_P_2007_08'] = df_combined['P_2007_08'] if 'P_2007_08' in df_combined.columns else 0
    df_combined['Total_K_2007_08'] = df_combined['K_2007_08'] if 'K_2007_08' in df_combined.columns else 0
    
    df_combined['Total_N_2008_09'] = df_combined['N_2008_09'] if 'N_2008_09' in df_combined.columns else 0
    df_combined['Total_P_2008_09'] = df_combined['P_2008_09'] if 'P_2008_09' in df_combined.columns else 0
    df_combined['Total_K_2008_09'] = df_combined['K_2008_09'] if 'K_2008_09' in df_combined.columns else 0
    
    df_combined['Total_N_2009_10'] = df_combined['N_2009_10'] if 'N_2009_10' in df_combined.columns else 0
    df_combined['Total_P_2009_10'] = df_combined['P_2009_10'] if 'P_2009_10' in df_combined.columns else 0
    df_combined['Total_K_2009_10'] = df_combined['K_2009_10'] if 'K_2009_10' in df_combined.columns else 0
    
    # For new data (2015-16 to 2019-20)
    df_combined['Total_N_2015_16'] = df_combined['N_2015_16'] if 'N_2015_16' in df_combined.columns else 0
    df_combined['Total_P_2015_16'] = df_combined['P_2015_16'] if 'P_2015_16' in df_combined.columns else 0
    df_combined['Total_K_2015_16'] = df_combined['K_2015_16'] if 'K_2015_16' in df_combined.columns else 0
    
    df_combined['Total_N_2016_17'] = df_combined['N_2016_17'] if 'N_2016_17' in df_combined.columns else 0
    df_combined['Total_P_2016_17'] = df_combined['P_2016_17'] if 'P_2016_17' in df_combined.columns else 0
    df_combined['Total_K_2016_17'] = df_combined['K_2016_17'] if 'K_2016_17' in df_combined.columns else 0
    
    df_combined['Total_N_2017_18'] = df_combined['N_2017_18'] if 'N_2017_18' in df_combined.columns else 0
    df_combined['Total_P_2017_18'] = df_combined['P_2017_18'] if 'P_2017_18' in df_combined.columns else 0
    df_combined['Total_K_2017_18'] = df_combined['K_2017_18'] if 'K_2017_18' in df_combined.columns else 0
    
    df_combined['Total_N_2018_19'] = df_combined['N_2018_19'] if 'N_2018_19' in df_combined.columns else 0
    df_combined['Total_P_2018_19'] = df_combined['P_2018_19'] if 'P_2018_19' in df_combined.columns else 0
    df_combined['Total_K_2018_19'] = df_combined['K_2018_19'] if 'K_2018_19' in df_combined.columns else 0
    
    df_combined['Total_N_2019_20'] = df_combined['N_2019_20'] if 'N_2019_20' in df_combined.columns else 0
    df_combined['Total_P_2019_20'] = df_combined['P_2019_20'] if 'P_2019_20' in df_combined.columns else 0
    df_combined['Total_K_2019_20'] = df_combined['K_2019_20'] if 'K_2019_20' in df_combined.columns else 0
    
    # Step 4: Calculate the total nutrient values for N, P, K for each zone
    df_combined['Total_N_old'] = df_combined[['Total_N_2007_08', 'Total_N_2008_09', 'Total_N_2009_10']].sum(axis=1)
    df_combined['Total_P_old'] = df_combined[['Total_P_2007_08', 'Total_P_2008_09', 'Total_P_2009_10']].sum(axis=1)
    df_combined['Total_K_old'] = df_combined[['Total_K_2007_08', 'Total_K_2008_09', 'Total_K_2009_10']].sum(axis=1)
    
    df_combined['Total_N_new'] = df_combined[['Total_N_2015_16', 'Total_N_2016_17', 'Total_N_2017_18', 'Total_N_2018_19', 'Total_N_2019_20']].sum(axis=1)
    df_combined['Total_P_new'] = df_combined[['Total_P_2015_16', 'Total_P_2016_17', 'Total_P_2017_18', 'Total_P_2018_19', 'Total_P_2019_20']].sum(axis=1)
    df_combined['Total_K_new'] = df_combined[['Total_K_2015_16', 'Total_K_2016_17', 'Total_K_2017_18', 'Total_K_2018_19', 'Total_K_2019_20']].sum(axis=1)
    
    # Step 5: Calculate the differences in total NPK between old and new data
    df_combined['Total_N_diff'] = df_combined['Total_N_new'] - df_combined['Total_N_old']
    df_combined['Total_P_diff'] = df_combined['Total_P_new'] - df_combined['Total_P_old']
    df_combined['Total_K_diff'] = df_combined['Total_K_new'] - df_combined['Total_K_old']
    
    # Step 6: Group by Zone and calculate the mean differences for N, P, and K
    zone_wise_analysis = df_combined.groupby('Zone')[['Total_N_diff', 'Total_P_diff', 'Total_K_diff']].mean()
    
    # Step 7: Plotting the trends for N, P, and K differences across the zones
    zone_wise_analysis.plot(kind='bar', figsize=(10, 6))
    plt.title('Change in Total Nutrient Content (N, P, K) from 2007-10 to 2015-20 by Zone')
    plt.xlabel('Zone')
    plt.ylabel('Average Change in Total Nutrient Content')
    plt.xticks(rotation=45)
    plt.legend(title='Nutrients', labels=['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)'])
    plt.tight_layout()
    
    # Step 8: Display the plot
    plt.show()

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

def plot_statewise_change(df_old, df_new):
    # Merging the datasets on 'State/Zone'
    merged = pd.merge(df_old[['State/Zone', 'Total_2009_10']],
                      df_new[['State/Zone', 'Total_2019_20']],
                      on='State/Zone')

    # Calculating the change
    merged['Change'] = merged['Total_2019_20'] - merged['Total_2009_10']

    # Sorting for better visualization
    merged = merged.sort_values(by='Change', ascending=False)

    # Barplot
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Change', y='State/Zone', data=merged, palette='coolwarm')
    plt.title('Change in Fertilizer Usage by State (2007-2020)')
    plt.xlabel('Change in Fertilizer Usage')
    plt.ylabel('State/Zone')
    plt.axvline(0, color='gray', linestyle='--')  # Reference line for no change
    plt.show()

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
    

    #Data From https://iced.niti.gov.in/climate-and-environment/environment/land    
    # Define a dictionary with assumed area in hectares for each zone
    state_area = {
        'Andhra Pradesh': 13324491, 'Telangana': 114840, 'Karnataka': 11072472, 'Kerala': 2169344,
        'TamilNadu': 6431574, 'Puducherry': 32560, 'A&N Islands': 31725, 'Lakshadweep': 32,
        'Gujarat': 11018409, 'Madhya Pradesh': 18279038, 'Chhattisgarh': 5759488, 'Maharashtra': 18474607,
        'Rajasthan': 13890865, 'Goa': 56419, 'Daman & Diu': 3771, 'D&N Haveli': 12075,
        'Haryana': 3780642, 'Punjab': 4318654, 'Uttar Pradesh': 17045043, 'Uttarakhand': 956497,
        'Himachal Pradesh': 660807, 'J&K': 1092998, 'Delhi': 46940, 'Chandigarh': 1391,
        'Bihar': 5967725, 'Jharkhand': 3275222, 'Odisha': 7664812, 'West Bengal': 5199258,
        'Assam': 2365561, 'Tripura': 138816, 'Manipur': 155402, 'Meghalaya': 126261,
        'Nagaland': 58135, 'Arunachal Pradesh': 255229, 'Mizoram': 16523, 'Sikkim': 58393
    }
    
    # Step 1: Convert df_old values from thousand tonnes to kg
    columns_to_convert = [
        "N_2007_08", "P_2007_08", "K_2007_08", "Total_2007_08",
        "N_2008_09", "P_2008_09", "K_2008_09", "Total_2008_09",
        "N_2009_10", "P_2009_10", "K_2009_10", "Total_2009_10"
    ]
    
    df_old[columns_to_convert] = df_old[columns_to_convert] * 1000000
    
    for state, area in state_area.items():
        # Convert the data for each state by dividing by its area (in hectares)
        df_old.loc[df_old['State/Zone'] == state, columns_to_convert] = \
            df_old.loc[df_old['State/Zone'] == state, columns_to_convert].div(area)
    
    # Now df_old has values in kg per hectare for each zone
    print(df_new)
    print(df_old)
    
    plot_fertilizer_change(df_old, df_new)
    plot_statewise_change(df_old, df_new)
    zone_wise_analysis_with_plots(df_new, df_old, state_zone_mapping)



