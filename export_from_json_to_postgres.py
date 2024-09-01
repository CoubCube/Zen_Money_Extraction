import pandas as pd
from sqlalchemy import create_engine
import config_directories

# read the json file into a pandas dataframe
accounts_df = pd.read_json(f"{config_directories.raw_area}accounts.json")
companies_df = pd.read_json(f"{config_directories.raw_area}companies.json")
countries_df = pd.read_json(f"{config_directories.raw_area}countries.json")
budget_df = pd.read_json(f"{config_directories.raw_area}budget.json")
instruments_df = pd.read_json(f"{config_directories.raw_area}instruments.json")
reminders_df = pd.read_json(f"{config_directories.raw_area}reminders.json")
reminderMarker_df = pd.read_json(f"{config_directories.raw_area}reminderMarker.json")
tags_df = pd.read_json(f"{config_directories.raw_area}tags.json")
transactions_df = pd.read_json(f"{config_directories.raw_area}transactions.json")
users_df = pd.read_json(f"{config_directories.raw_area}users.json")


# write dataframes to postgres tables
def save_to_postgres(df, table_name):
    # Create a SQLAlchemy engine
    engine = create_engine(f"postgresql://{config_directories.postgres_user}:{config_directories.postgres_password}@localhost:{config_directories.postgres_localhost}/{config_directories.postgres_database}")

    # Write the dataframe to the PostgreSQL table
    df.to_sql(table_name, engine, if_exists='replace', index=False)


save_to_postgres(accounts_df, "account")
save_to_postgres(companies_df, "company")
save_to_postgres(countries_df, "country")
save_to_postgres(budget_df, "budget")
save_to_postgres(instruments_df, "instrument")
save_to_postgres(reminders_df, "reminder")
save_to_postgres(reminderMarker_df, "reminderMarker")
save_to_postgres(tags_df, "tag")
save_to_postgres(transactions_df, "transaction")
save_to_postgres(users_df, "\"user\"")
