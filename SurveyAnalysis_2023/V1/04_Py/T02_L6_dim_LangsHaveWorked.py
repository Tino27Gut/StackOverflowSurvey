import pandas as pd

# Defining route variables
vR_Root = "C:/Users/Usuario/Dropbox/00_PersonalProjects/"
vR_Ambiente = vR_Root + "App_Develop/"
vR_Proyecto = vR_Ambiente + "SurveyAnalysis_2023/V1/"
vR_Data = vR_Proyecto + "01_Data/"

print("Loading data...")

# Load data in a Dataframe
survey_data = pd.read_csv(
    vR_Data + "L5_2023_to_2021_survey_results.csv")
df = pd.DataFrame(survey_data)

print("Initiating transformation...")

# Split each row into a list of languages
df["LangsHaveWorked"] = df["LanguageHaveWorkedWith"].astype(str).apply(
    lambda a: a.split(";")
)

# Replace duplicate languages that have different formats
replacement_dict = {
    "Bash/Shell (all shells)": "Bash/Shell",
    "COBOL": "Cobol",
    "LISP": "Lisp",
    "MATLAB": "Matlab"
}

def replace_lang_names(lang_list, replacement_dict):
    return [replacement_dict.get(lang.strip(), lang.strip()) for lang in lang_list]

df["LangsHaveWorked"] = df["LangsHaveWorked"].apply(lambda a: replace_lang_names(a, replacement_dict))

# Get a set of languages
all_langs = sorted(
    set(
        lang for list in df["LangsHaveWorked"] for lang in list
    ))
all_langs.remove("nan")

# Create binary fields for each language
for lang in all_langs:
    df[lang] = df["LangsHaveWorked"].apply(
        lambda a: 1 if lang in a else 0
    )

# Create a different Dataframe for all languages
fields_to_keep = ["LangsHaveWorked_Id"] + all_langs
df = df[fields_to_keep]

# Save the csv to ingest it in Qlik
name = "L6_dim_LangsHaveWorked"
df.to_csv(vR_Data + name + ".csv", index=False)

print("Transformation completed!")
