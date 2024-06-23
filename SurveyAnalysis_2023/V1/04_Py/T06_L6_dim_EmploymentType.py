import pandas as pd

# Defining route variables
vR_Root = "C:/Users/Usuario/Dropbox/00_PersonalProjects/"
vR_Ambiente = vR_Root + "App_Develop/"
vR_Proyecto = vR_Ambiente + "SurveyAnalysis_2023/V1/"
vR_Data = vR_Proyecto + "01_Data/"

print("Loading data...")

# Load the data into a DataFrame
survey_data = pd.read_csv(
    vR_Data + "L5_2023_to_2021_survey_results.csv")
df = pd.DataFrame(survey_data)

print("Initiating transformation...")

# Split each row into a list of EmploymentTypes
df["EmploymentType"] = df["Employment"].astype(str).apply(lambda a: a.split(";"))

# Replace all duplicate values in each row of the EmploymentType field
replacement_dict = {
    "Employed, full-time": "Employed full-time",
    "Employed, part-time": "Employed part-time",
    "Student, full-time": "Student full-time",
    "Student, part-time": "Student part-time"
}

def replace_emp_names(emp_list, replacement_dict):
    return [replacement_dict.get(emp.strip(), emp.strip()) for emp in emp_list]

df["EmploymentType"] = df["EmploymentType"].apply(lambda a: replace_emp_names(a, replacement_dict))

# Get a Set of unique EmploymentTypes
all_types = sorted(set(EmploymentType for sublist in df["EmploymentType"] for EmploymentType in sublist))
all_types.remove("nan")

# Create a binary field for each EmploymentTypes
for EmploymentType in all_types:
    df[EmploymentType] = df["EmploymentType"].apply(lambda a: 1 if EmploymentType in a else 0)

# Creating a separated table for the Roles
columns_to_keep = ["EmploymentType_Id"] + list(all_types)
df = df[columns_to_keep]

# Save the csv file again
name = "L6_dim_EmploymentType"
df.to_csv(vR_Data + name + ".csv", index=False)

print("Transformation completed!")
