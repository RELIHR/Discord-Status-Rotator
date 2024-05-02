<div id="top"></div>
<br/>
<div align="center">
  
  <h2 align="center">Discord Status Changer</h3>

  <p align="center">
    This script allows you to change the status of your Discord account automatically from the statuses defined in a text file.
  </p>
</div>

---------------------------------------

### 📂 Requirements & Execute
- Python 3.x 
- Required packages: ``requests colorama``

Clone this repository:

```bash
git clone https://github.com/RELIHR/Discord-Status-Changer.git
```

You can install the necessary packages by running the following command:

```bash
pip install requests colorama
```
Execute the script:

```bash
python main.py
```
---------------------------------------

### 🔍 Usage

Use the code with caution. ⚠️


- `text.txt` file containing the states you want to set in Discord, one per line.

- `emojis.txt` file if you want to add rotating emojis, including nitro emojis.

Nitro format: `name:id`

Format without nitro (only the emoji): `😀`

---------------------------------------

### ⚙️ Configuration

- token: Your Discord token account.

- clear_enabled: Enables or disables console clearing after a certain number of status changes.

- clear_interval: Number of state changes after which the console will be cleared.
- sleep_interval: Time interval between each state change (in seconds).

---------------------------------------

### 📃 Changelogs

```
(01/04/24)
✅ - Fixed encoding (UTF-8)  [Error]
(12/03/24)
↗️ - Now you can rotate emojis (including nitro emojis)  [Feature]
```

---------------------------------------

### 🤝 Contribution
If you find any bugs or have any suggestions for improvement, feel free to open an issue or submit a pull request!


### 📖 License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.👀
