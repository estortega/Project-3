import pandas as pd

# Read the CSV file
data = pd.read_csv(r'C:\Users\preit\OneDrive\Desktop\project_3\alzheimers_disease_data.csv')

# Define the mapping for binary columns to normal values
binary_columns = {
    'Gender': {0: 'Male', 1: 'Female'},
    'Ethnicity': {0: 'White', 1: 'Black', 2: 'Other'},
    'Smoking': {0: 'No', 1: 'Yes'},
    'AlcoholConsumption': {0: 'Low', 1: 'High'},
    'FamilyHistoryAlzheimers': {0: 'No', 1: 'Yes'},
    'CardiovascularDisease': {0: 'No', 1: 'Yes'},
    'Diabetes': {0: 'No', 1: 'Yes'},
    'Depression': {0: 'No', 1: 'Yes'},
    'HeadInjury': {0: 'No', 1: 'Yes'},
    'Hypertension': {0: 'No', 1: 'Yes'},
    'MemoryComplaints': {0: 'No', 1: 'Yes'},
    'BehavioralProblems': {0: 'No', 1: 'Yes'},
    'Confusion': {0: 'No', 1: 'Yes'},
    'Disorientation': {0: 'No', 1: 'Yes'},
    'PersonalityChanges': {0: 'No', 1: 'Yes'},
    'DifficultyCompletingTasks': {0: 'No', 1: 'Yes'},
    'Forgetfulness': {0: 'No', 1: 'Yes'},
    'Diagnosis': {0: 'No', 1: 'Yes'}  # Assuming Diagnosis column is binary as well
}

# Define mappings for other columns (EducationLevel, etc.)
other_columns = {
    'EducationLevel': {0: 'None', 1: 'Primary', 2: 'Secondary', 3: 'Higher'},
    'DietQuality': {0: 'Poor', 1: 'Fair', 2: 'Good', 3: 'Excellent'},
    'SleepQuality': {0: 'Poor', 1: 'Fair', 2: 'Good', 3: 'Excellent'},
    'PhysicalActivity': {0: 'None', 1: 'Low', 2: 'Moderate', 3: 'High'},
    'BMI': {0: 'Underweight', 1: 'Normal', 2: 'Overweight', 3: 'Obese'}
}

# Define mappings for additional columns (e.g., blood pressure, cholesterol levels, etc.)
numeric_columns = {
    'SystolicBP': lambda x: 'Normal' if x < 120 else 'Elevated' if x < 130 else 'High',
    'DiastolicBP': lambda x: 'Normal' if x < 80 else 'High',
    'CholesterolTotal': lambda x: 'Normal' if x < 200 else 'High',
    'CholesterolLDL': lambda x: 'Normal' if x < 100 else 'High',
    'CholesterolHDL': lambda x: 'Low' if x < 40 else 'Normal' if x < 60 else 'High',
    'CholesterolTriglycerides': lambda x: 'Normal' if x < 150 else 'High',
    'MMSE': lambda x: 'Normal' if x >= 24 else 'Impaired',  # Mini-Mental State Examination
    'FunctionalAssessment': lambda x: 'Normal' if x >= 10 else 'Impaired',
    'ADL': lambda x: 'Independent' if x >= 6 else 'Dependent'  # Activities of Daily Living
}

# Apply conversion for binary columns
for column, mapping in binary_columns.items():
    if column in data.columns:
        data[column] = data[column].map(mapping)

# Apply conversion for other categorical columns
for column, mapping in other_columns.items():
    if column in data.columns:
        data[column] = data[column].map(mapping)

# Apply conversion for numeric columns using lambda functions
for column, func in numeric_columns.items():
    if column in data.columns:
        data[column] = data[column].apply(func)

# Replace 'XXXConfid' in the 'DoctorInCharge' column (if any)
data['DoctorInCharge'].replace('XXXConfid', None, inplace=True)

# Check the first few rows to confirm the changes
print("Cleaned Data Preview:")
print(data.head())

# Save cleaned data to a new CSV file
cleaned_file_path = r'C:\Users\preit\OneDrive\Desktop\project_3\cleaned_alzheimers_disease_data.csv'
data.to_csv(cleaned_file_path, index=False)

# Print confirmation message
print(f"Cleaned data saved to {cleaned_file_path}")


