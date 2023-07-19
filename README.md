# Earth911 Recycling Centers Web Scraper

This Python script allows you to scrape recycling center information from the Earth911 website. It searches for recycling centers that accept '#4 Rigid Plastics' within a specified distance from a given zip code.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Description

The Earth911 Recycling Centers Web Scraper is a handy tool to extract details of recycling centers near a specific location. By providing a zip code, you can retrieve information such as the center's name, type, address, and phone number. The scraped data can be used for analysis, research, or any other purpose related to recycling centers.

## Features

- Scrapes recycling center details from the Earth911 website
- Retrieves recycling centers that accept '#4 Rigid Plastics'
- Allows customization of the search by specifying the zip code and maximum distance
- Outputs the scraped details to the console

## Getting Started

To use this web scraper, follow these steps:

1. Clone the repository to your local machine using the following command:
git clone https://github.com/your-username/earth911-recycling-scraper.git


2. Install the necessary dependencies by running the following command:
pip install -r requirements.txt

3. Ensure that you have a CSV file named `uszips.csv` in the `csv` directory. This file should contain a 'zip' column with a list of zip codes. This file is required for the script to function correctly.

## Dependencies

The following dependencies are required to run the web scraper:

- Python 3.x
- requests
- BeautifulSoup
- pandas

These dependencies are listed in the `requirements.txt` file for easy installation.

## Usage

To run the web scraper, execute the following command:
python scraper.py


The script will prompt you for a zip code to search for recycling centers. After entering the zip code, it will scrape the Earth911 website and display the details of the recycling centers found in the console.

## Customization

You can customize the search parameters by modifying the code in the `scraper.py` file. Here are the options you can adjust:

- **Zip Code**: Change the `tst_zip` variable to set the zip code for the search.
- **Search Query**: Modify the search query in the URL construction inside the script to search for different materials or items.
- **Maximum Distance**: Adjust the maximum distance in the URL construction to change the radius for the search.

Feel free to customize the code to suit your specific requirements.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub. If you would like to contribute code, submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

Feel free to modify or add any additional sections or details as needed.

