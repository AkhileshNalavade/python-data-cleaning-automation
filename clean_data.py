import pandas as pd
from pathlib import Path
import logging
import sys
import yaml


# -----------------------------
# BASE PATH
# -----------------------------
BASE_DIR = Path(__file__).parent
CONFIG_PATH =BASE_DIR / "config.yaml"


# -----------------------------
# LOAD CONFIG
# -----------------------------
if not CONFIG_PATH.exists():
    sys.exit("ERROR: config.ymal not found")
    
with open(CONFIG_PATH,"r")as f:
    config = yaml.safe_load(f)


# -----------------------------
# PATH FROM CONFIG
# -----------------------------
RAW_PATH = BASE_DIR / config["paths"]["raw_file"]
CLEAN_PATH = BASE_DIR / config["paths"]["clean_file"]
LOG_PATH = BASE_DIR / config["paths"]["log_file"]

# -----------------------------
# DIRECTORY CREATION
# -----------------------------
CLEAN_PATH.parent.mkdir(exist_ok=True)
LOG_PATH.parent.mkdir(exist_ok=True)


# -----------------------------
# LOGGING CONFIGURATION
# -----------------------------
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# -----------------------------
# MAIN LOGIC
# -----------------------------
def clean_sales_data():
    logging.info("Data cleaning started")

    if not RAW_PATH.exists():
        logging.error(f"Raw file missing: {RAW_PATH}")
        sys.exit("ERROR: Raw CSV not found")

    try:
        df = pd.read_csv(RAW_PATH)
        logging.info("CSV loaded")

        qty_col = config["columns"]["quantity"]
        price_col = config["columns"]["price"]

        # Column validation
        for col in [qty_col, price_col]:
            if col not in df.columns:
                logging.error(f"Missing column: {col}")
                sys.exit(f"ERROR: Column {col} missing")

        # Cleaning rules
        df[qty_col] = df[qty_col].fillna(config["defaults"]["quantity_fill"])

        if config["defaults"]["price_strategy"] == "mean":
            df[price_col] = df[price_col].fillna(df[price_col].mean())

        df["total"] = df[qty_col] * df[price_col]

        df.to_csv(CLEAN_PATH, index=False)
        logging.info(f"Clean file saved: {CLEAN_PATH}")

    except Exception as e:
        logging.exception("Data cleaning failed")
        sys.exit(e)

    logging.info("Data cleaning completed successfully")

# -----------------------------
# SCRIPT ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    
    clean_sales_data()
