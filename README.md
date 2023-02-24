# ThreatTracker

ThreatTracker is a Python script that helps you stay up-to-date with the latest trends in cyber attacks, vulnerabilities, and threat actors by monitoring threat intelligence sources and displaying the top 5 articles.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/cyphercut/ThreatTracker.git
   ```

2. Install the required packages:
   ```bash
   pip3 install -r requirements.txt
   ```

## Usage
To run the script, navigate to the project directory and enter the following command:
   ```bash
   python3 main.py
   ```

This will display the top 5 articles from the following threat intelligence sources:

- KrebsOnSecurity
- The Hacker News
- Threatpost

The articles will be displayed in the terminal with clickable links that can be opened in a web browser. The titles of the articles will be colored to make them more readable.

## Contributing
Contributions to ThreatTracker are welcome! To contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits for contributions

- [shadowdevnotreal](https://github.com/shadowdevnotreal) - [Pull Request](https://github.com/cyphercut/ThreatTracker/pull/1): 
   - Code modification: Termcolor module replaces Colorama for output colorization, simplifying the code.
   - Start parameter used in enumerate to index at 1, not 0.
   - Unnecessary f-string brackets removed from print statements.
   - Argparse module used to define and parse command-line arguments.
   - -n/--num-articles option specifies the number of articles to display.
   - -f/--output-format option allows text, HTML, and JSON output formats.
   - -v/--verbose option enables verbose logging.
   - add_argument method defines -n/--num_articles argument that takes integer value with default of 5.
   - help parameter provides brief description of argument displayed with -h/--help option.
   - Value of argument retrieved using args.num_articles attribute.
  
## Do you like this project?
<a href="https://www.buymeacoffee.com/cyphercut" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 145px !important;" ></a>
