import pandas as pd




def clean_csv_gama(file_paths: dict):
    conversionData = {}
    colNames = []
    clean_df = pd.read_csv(file_paths["uploaded_file_path"])
    for col_name in clean_df.columns:
        if(col_name not in colNames):
            if("date" in col_name.lower()):
                convertDate(col_name,clean_df, conversionData)
            elif("time" in col_name.lower()):
                convertTime(col_name,clean_df, conversionData)
    clean_df.to_csv(file_paths["clean_file_path"], index=False)
    return conversionData

def convertDate(column_name, clean_df, conversionData):
    try:
        clean_df[column_name] = pd.to_datetime(clean_df[column_name], format='mixed', errors='coerce')
        num_bad_dates = clean_df[column_name].isna().sum()
        num_good_dates = clean_df[column_name].notna().sum()
        conversionData[f"{column_name} failures"] = f"{num_bad_dates}"
        conversionData[f"{column_name} successful"] = f"{num_good_dates}"
    except Exception as e:
        print(e)
    
def convertTime(column_name, clean_df, conversionData):
    try:
        clean_df[column_name] = pd.to_timedelta(clean_df[column_name], errors='coerce')
        num_bad_times = clean_df[column_name].isna().sum()
        num_good_times = clean_df[column_name].notna().sum()
        conversionData[f"{column_name} failures"] = f"{num_bad_times}"
        conversionData[f"{column_name} successful"] = f"{num_good_times}"
        clean_df[column_name] = clean_df[column_name].apply(lambda x: str(x).split()[-1])
    except Exception as e:
        print(e)
    