# Trade_It!
Trading Bot for Cryptocurrencies, Indices, Funds, Forex etc 
# Welcome to the Trade_It repository!

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (any version -- hopefully the latest version at the time of reading this file)
- Python library - PANDAS
- Python library - Sklearn
- Python library - OANDA API and its related packages
- Python library - NumPy
- Python library - Yfinance
- Python library - datetime
  
### Installation

1. Choose and install the code Editor of your choice
2. Install python on machine from https://www.python.org/downloads/
3. Ensure pip is installed with the command: python -m ensurepip --upgrade
4. Install libraries using: python -m pip install <library_name_here>

## Usage

The config file contains information relating to the chart you are trading on, the API access key to the account, the account ID and the currency pair/ trading instrument that the user wants to trade.
Set those up and run Main.py 
The script will continuously run at intervals determined by the chart granularity set by the chart being traded on.
The bot will automatically set stop losses and take profit points depending on whether it is in a sell or buy state.
The bot will continuously search for market entry and exit points.

- CandleStick_Patterns.py - contains functions to determine common candlestick patterns that can be used to find market entry and exit points
- SignalGenerator.py - contains functions that allow the bot to determine whether to buy, sell or not take any action
- Support_and_Resistance.py - contains functions that allow the bot to determine  accurate price action points and use those areas as potential market entry or exit points
- Main.py - is the execution file, connecting to the OANDA account to retrieve data on the traded instrument and execute trades

## Contributing

We welcome contributions from the community! If you'd like to contribute to Trade_It!, please follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request explaining your changes.

Please ensure your pull request adheres to our [Code of Conduct](CODE_OF_CONDUCT.md) and [Contributing Guidelines](CONTRIBUTING.md).

## Contact
goshomip@gmail.com or 
https://web.groupme.com/contact/103653571/4OWCyvi9
Thank you for your interest in Trade_It! We hope you find it useful and we look forward to your contributions.
