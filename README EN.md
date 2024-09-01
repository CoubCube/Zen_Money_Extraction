This repository contains three Python scripts for extracting data from the Zen Money API, saving it as JSON files, and loading it into a PostgreSQL database.

Scripts Overview

1. config_directories.py: Stores configuration details such as API credentials and PostgreSQL connection parameters.
2. json_extract.py: Extracts data from the Zen Money API and saves it as JSON files.
3. export_from_json_to_postgres.py: Loads JSON data into PostgreSQL tables.

Prerequisites:
- Python 3.6 or later
- 'requests' library for API requests
- 'pandas' library for data manipulation
- 'sqlalchemy' library for database interaction
- 'psycopg2' library for PostgreSQL connection
Install the required libraries using pip: pip install requests pandas sqlalchemy psycopg2

Configuration
Before running the scripts, you need to update the config_directories.py file with the necessary credentials and paths.
Replace the placeholders with your actual API credentials, directory paths, and PostgreSQL connection details.
You can get your personal API token from here: https://zerro.app/token

Script Details

- json_extract.py
Purpose: Extracts data from the Zen Money API and saves it to JSON files.
Ensure the config_directories.py file is configured with your API credentials and directory paths.

Functionality:
Sends a POST request to the Zen Money API.
Receives and parses the response data.
Saves the data to JSON files in the specified directory.

- export_from_json_to_postgres.py
Purpose: Loads JSON data into PostgreSQL tables.
Ensure the config_directories.py file is configured with your PostgreSQL connection details.

Functionality:
Reads JSON files from the specified directory into pandas DataFrames.
Writes the DataFrames to PostgreSQL tables using SQLAlchemy.

- config_directories.py
Purpose: Stores configuration details such as API credentials and PostgreSQL connection parameters.
Usage: Update this file with your specific configuration details. This file is imported by the other scripts to access configuration settings.

Troubleshooting

ModuleNotFoundError: Ensure all required libraries are installed.
Connection Errors: Verify your API credentials and PostgreSQL connection parameters.
File Paths: Ensure the JSON file paths in extract_data.py are correct.

Feel free to adjust any sections to better fit your project or requirements.
