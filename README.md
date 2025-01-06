# Google Maps Data Scraper

Google Maps Data Scraper is a Python project for scraping data from Google Maps based on keyword input. The data scraped includes:

- **Title** (Location name)
- **Address**
- **Rating**
- **Reviews** (Number of reviews)
- **Link** (URL of the location)

The output data will be saved in a CSV file with a `|` delimiter, stored in the `results` folder.

## Features

- Scraping based on keyword input.
- Supports scraping the following data:
  - Location name
  - Address
  - Rating
  - Number of reviews
  - Location URL
- Output in CSV format with `|` delimiter.
- Uses Selenium WebDriver for navigation and data retrieval.

## Installation

### Prerequisites

Ensure you have:

- Python 3.7 or newer
- Google Chrome (or another browser supported by Selenium)
- ChromeDriver (version must match your Google Chrome version)

### Installation Steps

1. Clone this repository:

   ```bash
   git clone <REPOSITORY_URL>
   cd <REPOSITORY_FOLDER_NAME>
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. Install dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure `ChromeDriver` is accessible to Selenium. Place the `chromedriver` file in your PATH or in the project directory.

## Usage

1. Run the script with a keyword input:

   ```bash
   python app.py
   ```

2. The scraped data will be saved in the `results` folder with a timestamped file name.

### Output

The CSV file will have the following format:

| Title           | Address            | Rating | Reviews | Link                        |
| --------------- | ------------------ | ------ | ------- | --------------------------- |
| Location Name 1 | Location Address 1 | 4.5    | 120     | https://maps.google.com/... |
| Location Name 2 | Location Address 2 | 4.0    | 85      | https://maps.google.com/... |

![image](https://github.com/user-attachments/assets/7cbbd4a2-6e21-4b01-8a35-56373a1ffebd)

## Project Structure

```
.
|── app.py           # Main script for scraping
|── requirements.txt     # Python dependencies
|── results/             # Folder to store outputs
|── chromedriver/        # Folder to run webdriver
|── README.md            # Project documentation
|── .gitignore           # File to ignore specific files in Git
```

## Contribution

Contributions are welcome! If you find any bugs or have features you'd like to add, feel free to create a pull request or report an issue in the issues section.

## License

This project is licensed under the [MIT License](LICENSE).

## Important Notes

- The use of this project must comply with Google Maps' terms of service.
- Scraping data without permission may violate Google's service policies.
- Use this project for personal or educational purposes only.
