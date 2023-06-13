# Spotify Account Generator

This is a Python script for generating Spotify accounts using the Spotify API. It uses the `httpx` library for making HTTP requests. The generated accounts are then saved in a text file named "SpotifyAccounts.txt".

## Prerequisites

Before running the script, make sure you have the following requirements installed:

- Python 3.x
- `httpx` library
- `names` library

You can install the required libraries by running the following command:

```
pip install httpx names
```

## Usage

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:

```
python main.py
```

4. You will be prompted to enter the number of threads you want to run. Enter the desired number and press Enter.
5. The script will start generating Spotify accounts in parallel using the specified number of threads.

## Configuration

Before running the script, you may need to modify certain variables to fit your needs. Open the script in a text editor and look for the following variables:

- `capmonsterCaptchaKey`: Replace this variable with your Capmonster CAPTCHA API key.
- `password`: Replace this variable with the desired password for the generated accounts.
- `proxies`: Add proxies in "proxies.txt" file. Format must be "USERNAME:PASSWORD@IP:PORT"

## Important Note

Please note that generating accounts using automated scripts may violate the terms of service of the platform. Make sure you have the necessary permissions and comply with the platform's policies before using this script.

## Disclaimer

This script is provided for educational purposes only. The misuse of this script for any illegal activities is strictly prohibited. The author is not responsible for any consequences or damages caused by the misuse of this script.
