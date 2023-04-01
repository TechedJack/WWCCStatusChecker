# WWCC-Status-Checker

An easy-to-use solution for checking WWCC card status in Victoria, Australia, ensuring organisations remain compliant.

## Features

- Check the status of a single WWCC card
- Check the status of multiple WWCC cards using a CSV file

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `requests` library
- `beautifulsoup4` library

## Usage

1. Clone the repository or download the Python script.
2. Install the required packages:
```
pip install requests beautifulsoup4
```

3. Run the script:
```
python wwcc_status_checker.py
```

4. Follow the prompts to check the status of a single card or multiple cards using a CSV file.

## Input CSV Format

For bulk checking, the input CSV file should have the following headers:

- Last Name
- First Name
- Card Number

Example:
```
Last Name,First Name,Card Number
Smith,John,123456A
Doe,Jane,789012B
```

## Output CSV Format

The output CSV file will have the following headers:

- Last Name
- First Name
- Card Number
- Status

Example:
```
Last Name,First Name,Card Number,Status
Smith,John,123456A,Status: current, Expiry Date: 25/03/2025
Doe,Jane,789012B,Status: not current, New Card Expiry Date: 01/01/2024. Please contact cardholder for updated card details.
```

## Roadmap

### Support for other states and territories
- New South Wales (NSW)
- Queensland (QLD)
- South Australia (SA)
- Tasmania (TAS)
- Western Australia (WA)
- Australian Capital Territory (ACT)
- Northern Territory (NT)

### Future Features
- Automatic periodic checks and notifications for expiring or invalid cards
- Improved error handling and input validation
- User-friendly web interface for easier interaction
- Integration with organizational management systems or HR software
- Additional output formats, such as JSON, for easier data processing

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests to help improve this project.

## License

This project is licensed under the WWCC Status Checker License. See the [LICENSE.md](LICENSE.md) file for details.
