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

# Split each row into a list of DevTypes (Roles)
df["Roles"] = df["DevType"].astype(str).apply(lambda a: a.split(";"))

# Get a Set of unique DevTypes (Roles)
all_roles = sorted(set(role for sublist in df["Roles"] for role in sublist))
all_roles.remove("Other (please specify):")

# Create a binary field for each DevType
for role in all_roles:
    df[role] = df["Roles"].apply(lambda a: 1 if role in a else 0)

# Creating a separated table for the Roles
columns_to_keep = ["DevType_Id"] + list(all_roles)
df = df[columns_to_keep]

# Save the csv file again
name = "L6_dim_DevType"
df.to_csv(vR_Data + name + ".csv", index=False)

print("Transformation completed!")
