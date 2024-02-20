# Discord Status Changer

This script allows you to change the status of your Discord account automatically from the statuses defined in a text file.

Requirements
- #### Python 3.x 

- #### Required packages: requests


Clone this repository:

```bash
git clone https://github.com/RELIHR/
```

You can install the necessary packages by running the following command:

```bash
pip install requests
```


# Usage

Create a `config.json` file with the following structure (if you don't have it):

```JSON
{
  "token": "token_discord",
  "clear_enabled": true,
  "clear_interval": 15,
  "sleep_interval": 3
}
```

- Use the code with caution.

Be sure to replace ``token_discord`` with your own Discord token.

Create a `text.txt` file containing the states you want to set in Discord, one per line.

Execute the script with Python:

```bash
python main.py
```

# Configuration

- token: Your Discord token.

- clear_enabled: Enables or disables console clearing after a certain number of status changes.

- clear_interval: Number of state changes after which the console will be cleared.
- sleep_interval: Time interval between each state change (in seconds).

### Contribution
If you find any bugs or have any suggestions for improvement, feel free to open an issue or submit a pull request!


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.
