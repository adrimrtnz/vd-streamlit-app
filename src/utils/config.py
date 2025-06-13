"""
Configuration file for the Streamlit application.

Stores constants such as data paths and filenames to be used across the application.
This helps in centralizing configuration and making it easier to update paths
if the project structure changes.
"""
DATA_PATH = '../data'

# Defines the relative path to the primary data directory from within the src/utils directory.
# When used by scripts in src/pages or src/utils, this path correctly points to the data folder
# at the root of the project if those scripts are run with the src directory as part of Python's path
# or if Streamlit runs them from the project root.
# For direct execution of scripts in src/utils (like data loading tests if they were standalone),
# care must be taken with the current working directory.
# However, for Streamlit apps run via `streamlit run app.py` from the project root,
# paths constructed like `os.path.join(DATA_PATH, ...)` in `utils/data.py` will be relative
# to the project root if `DATA_PATH` is treated as relative from where `data.py` is,
# or it might need adjustment if `data.py` assumes it's run from `src`.
# Given current usage in `os.path.join(DATA_PATH, CSV_PUB)`, if `data.py` is in `src/utils`,
# `../data` correctly points to `project_root/data`.

CSV_PUB = 'annual-scholarly-publications-on-artificial-intelligence/annual-scholarly-publications-on-artificial-intelligence.csv'
CSV_INV = 'global-investment-in-generative-ai/global-investment-in-generative-ai.csv'
CSV_PRINV = 'private-investment-in-artificial-intelligence/private-investment-in-artificial-intelligence.csv'
WORLD_MAP = 'maps/world.geojson'
TIMELINE_DATA = 'timeline.json'