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

# Split each row into a list of DbEngines
df["Dbs"] = df["DatabaseHaveWorkedWith"].astype(str).apply(
    lambda a: a.split(";")
)

# Replace all duplicate values in each row of the Dbs field
replacement_dict = {
    "Couch DB": "CouchDB",
    "Dynamodb": "DynamoDB",
    "Firebase Realtime Database": "Firebase",
    "Neo4J": "Neo4j"
}

def replace_db_names(db_list, replacement_dict):
    return [replacement_dict.get(db.strip(), db.strip()) for db in db_list]

df["Dbs"] = df["Dbs"].apply(lambda a: replace_db_names(a, replacement_dict))

# Get a Set of unique DbEngines
all_dbs = sorted(
    set(
        db for list in df["Dbs"] for db in list
    )
)

if "nan" in all_dbs:
    all_dbs.remove("nan")

# Create a binary field for each DbEngine
for db in all_dbs:
    df[db] = df["Dbs"].apply(
        lambda a: 1 if db in a else 0
    )

# Creating a separated table for the DbEngines
fields_to_keep = ["DatabaseHaveWorkedWith_Id"] + all_dbs
df = df[fields_to_keep]

# Save the csv file again
name = "L6_dim_DbHaveWorked"
df.to_csv(vR_Data + name + ".csv", index=False)

print("Transformation completed!")
