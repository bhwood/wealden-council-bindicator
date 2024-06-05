# Wealden Council Bindicator

## Functionality
- Retrieves bin collection information for a given Unique Property Reference Number (UPRN) specifically for the Wealden Council website.
- Identifies the dates for the next bin collection and next recycling collection.
- Formats the dates in a human-readable format (DD/MM/YYYY).
- Provides a message indicating the type of bin for the next collection.

**Important Note:** This script is currently only designed to work with the Wealden Council website.

## Dependencies
- `requests`: Used for making HTTP requests to the Wealden Council website.
- `json`: Used for decoding JSON data from the response.
- `dotenv`: Used for loading environment variables (for storing UPRN securely).

## Usage

### Prerequisites:
1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project directory.

3. Add the line `UPRN=YOUR_UPRN` to the `.env` file, replacing `YOUR_UPRN` with your actual UPRN.

### Run the script:
1. Open a terminal or command prompt and navigate to the project directory.
2. Run the script using:
   ```bash
   python main.py
   ```
   (assuming the main script is named `main.py`).