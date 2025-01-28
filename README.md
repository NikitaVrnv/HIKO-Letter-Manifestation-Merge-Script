# HIKO Letter Manifestation Merge Script
# Letter Data Processing Script

This Python script processes a CSV file containing letter metadata, specifically focusing on the `copies` column. It performs data transformation and validation to ensure consistency in the JSON structure of the `copies` field.

## Description

The script reads a CSV file (`input.csv`) where each row contains metadata about letters, including a `copies` column that stores JSON data. The script:
- Validates and parses the JSON data in the `copies` column.
- Transforms the data based on predefined logic for `ms_manifestation` and `preservation` fields.
- Outputs a new CSV file (`output.csv`) with the updated `copies` column.

Key transformations include:
- Mapping `ms_manifestation` values to corresponding `preservation` values.
- Handling cases where `ms_manifestation` or `preservation` fields are missing or invalid.
- Ensuring valid JSON structure for the `copies` column.

## Installation

### Prerequisites
- Python 3.13 or higher
- `pip` package manager

### Steps

#### On Windows:
1. Install Python from [python.org](https://www.python.org/downloads/).
2. Open Command Prompt and run:
   ```bash
   python -m venv venv
   venv\Scripts\activate
  
#### On macOS:
1. Open Terminal and run:
2. ```bash
   python3 -m venv venv
   source venv/bin/activate

## Usage

1. Place your input CSV file (`input.csv`) in the project directory.
2. Run the script:
   ```bash
   python hiko-script.py
   ```
3. The processed CSV file (`output.csv`) will be generated in the same directory.

## Logic Overview

The script processes each row in the CSV file as follows:
1. Checks if the `copies` column contains valid JSON.
2. Iterates through each entry in the `copies` JSON array.
3. Applies transformation rules:
   - If `ms_manifestation` is present, map it to a corresponding `preservation` value.
   - If `preservation` is invalid or missing, replace it with a default value.
4. Writes the updated data back to a new CSV file.

## Error Handling

- Rows with empty or invalid `copies` fields are skipped, and warnings are logged.
- Invalid JSON entries are flagged for manual review.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
