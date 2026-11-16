# ecommerce-data-platform

Requests exchange rates (from USD to EUR, GBP and MXN) from the Frankfurter API and saves them to a JSON file.

## Requirements

- Python 3 (developed and tested with 3.14)
- Libraries listed in `requirements.txt`

## Setup

1. Clone the repository:

   ```powershell
   git clone https://github.com/JCdataengineer/ecommerce-data-platform.git
   ```

2. Enter the folder:

   ```powershell
   cd ecommerce-data-platform
   ```

3. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

4. Activate the virtual environment (Windows, PowerShell):

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

## Usage

Run the script from the project folder:

```powershell
python extract_rates.py
```

The script prints the exchange rate of each currency and saves the full data to `rates.json`.

## Example output

```
EUR : 0.90794
GBP : 0.75767
MXN : 18.5609
```

## Project status

This project is under development. At the moment, it only extracts and saves the data. The plan is to use it to convert prices between currencies on an e-commerce platform.
