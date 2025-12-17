# Python Data Cleaning Automation

A config-driven Python pipeline that cleans raw CSV data using validation, logging, and reproducible transformation rules.

## Features
- YAML-based configuration for paths, columns, and default values
- Validation of file existence and required columns
- Missing value handling for `quantity` and `price`
- Computed column: `total = quantity * price`
- Structured logging with timestamps
- Automatic creation of required directories

## Project Structure
python-data-cleaning-automation/
├── clean_data.py
├── config.yaml
├── raw_data/
│ └── sales_raw.csv
├── clean_data/
├── logs/
└── .gitignore

pgsql
Copy code

## How It Works
1. Load configuration from `config.yaml`.
2. Validate input file and expected columns.
3. Apply cleaning rules (fill missing values, compute totals).
4. Save cleaned output to `clean_data/`.
5. Log execution steps and issues to `logs/data_cleaning.log`.

## Run
python clean_data.py

shell
Copy code

### Output
Cleaned CSV:
clean_data/sales_clean.csv

makefile
Copy code

Logs:
logs/data_cleaning.log

shell
Copy code

## Tech Stack
Python, Pandas, PyYAML, Pathlib, Logging
