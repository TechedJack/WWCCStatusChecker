# WWCC Status Checker

A simple and easy-to-use solution for organisations to remain compliant with Working With Children Check (WWCC) laws in Australia. This script allows you to check the status of WWCC cards for Victoria (VIC). Support for other states and territories is planned for future releases.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using:

```bash
pip install requests beautifulsoup4
```
### Usage

1. Clone the repository or download the `wwcc_status.py` script.
2. Run the script using the following command:

```bash
python wwcc_status.py
```

3. Follow the prompts to enter the card number and last name.
4. The script will send a request to the specified endpoint and display the extracted information.

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
- Support for bulk checking of multiple cards at once (e.g., from a CSV file)
- Automatic periodic checks and notifications for expiring or invalid cards
- Improved error handling and input validation
- User-friendly web interface for easier interaction
- Integration with organizational management systems or HR software
- Additional output formats, such as JSON or CSV, for easier data processing

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests to help improve this project.

## License

This project is licensed under the WWCC Status Checker License. See the [LICENSE.md](LICENSE.md) file for details.
