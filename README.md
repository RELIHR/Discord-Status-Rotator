<div id="top"></div>
<br/>
<div align="center">
  
  <h2 align="center">🔄️ Discord Status Rotator</h2>

  <p align="center">
    This script allows you to change the status of your Discord account automatically from the statuses defined in a text file and extras.

    Warning: Using scripts to automate or “self-bot” a personal Discord account violates Discord’s Terms of Service (ToS). This can lead to your account being suspended or permanently banned by Discord, and many server owners will also ban accounts that show automatically rotating statuses or other automated behavior. If you need automation, create a proper bot account via the Discord Developer Portal and follow the official API rules.
  </p>
</div>

### 📄 Table of Contents

- [Requirements & Execution](#-requirements--execution)
- [Usage](#-usage)
- [Configuration](#%EF%B8%8F-configuration)
- [How to get your token (PC & Mobile Devices)](#-how-to-get-your-token-pc--mobile-devices)
- [Change History](#-change-history)
- [Contribution](#-contribution)
- [License](#-license)

---------------------------------------

### 📂 Requirements & Execution
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
- `aboutme.txt` In this file you can rotate your “About me” in each line a new text is rotated (Test).

Nitro format: `name:id`

Format without nitro (only the emoji): `😀`

---------------------------------------

### ⚙️ Configuration

- **token**: Your Discord token account.
- **status_sequence**: Rotate the status (online, dnd, idle, offline). You can have one fixed by removing the others and leaving only the one you want.
- **use_status_sequence**: Enable or disable the status sequence rotation.
- **clear_enabled**: Enables or disables automatic console clearing.
- **clear_interval**: Number of status updates after which the console will be automatically cleared (e.g., 15 means clear console every 15 status changes).
- **speed_rotator**: Time interval between each state change (in seconds).
- **emoji_rotation_mode**: Controls when emojis change. Options are:
  - `"with_text"`: Emojis change with each text change (default behavior).
  - `"after_text_cycle"`: Emojis only change after all texts have been displayed once.
- **rotate_hypesquad**: Enables or disables HypeSquad rotation.
- **hypesquad_rotation_interval**: Time interval between each HypeSquad change (in seconds).
- **hypesquad_sequence**: Array of HypeSquad houses to rotate between.
- **hypesquad_mapping**: Maps HypeSquad house names to their IDs.
- **rotate_aboutme**: Enables or disables About Me rotation.
- **aboutme_rotation_interval**: Time interval between each About Me change (in seconds).

---------------------------------------

### 🤔 How to get your token (PC & Mobile Devices)

### - PC

1. Open your preferred browser (with developer tools) and login to [Discord](https://discord.com/app).
2. Press `CTRL + Shift + I` to open the Developer Tools and navigate to the Console tab.
3. Paste the following code into the Console and press Enter:
    ```javascript
    (webpackChunkdiscord_app.push([
        [""],
        {},
        (e) => {
            for (let t in ((m = []), e.c)) m.push(e.c[t]);
        },
    ]),
    m)
        .find((e) => e?.exports?.default?.getToken !== void 0)
        .exports.default.getToken();
    ```
4. The text that will be returned is enclosed in quotation marks and that will be YOUR token.


### - Mobile Devices

1. Open your browser 

2. Add a new bookmark (click the star icon ⭐ in the menu under the three dots).

3. Edit the bookmark name to Token Finder and set its URL with the following code:

   ```javascript
   javascript:(function () { location.reload(); var i = document.createElement("iframe"); document.body.appendChild(i); prompt("Token", i.contentWindow.localStorage.token.replace(/"/g, ""));})();
   ```
4. Visit [Discord](https://discord.com/app). and log in.

5. Click on the search bar, type Token Finder (do not press Enter or search).

6. Click on the bookmark you have named Token Finder.

7. A window will pop up with your Discord token, just copy it.


---------------------------------------

### 📃 Change History

```
(31/07/25)
  ↗️ - Added emoji rotation control: emojis can now be set to change only after completing
  a full text cycle instead of with each text change. | [FeAture]
  ↗️ - Added startup configuration display showing current settings overview. | [Feature]
  ↗️ - Improved message formatting with emojis, separators, and visual progress indicators. | [UI Terminal Enhancement]
  ↗️ - Clarified console clearing behavior: clear_interval now counts status updates, not time. | [Documentation]
(26/12/24)
  ↗️ - Added "HypeSquad" rotation feature. | [Feature]
  ↗️ - Added "About Me" rotation feature. (Test) | [Feature]
  ✅ - Fixed problem with rotation of animated and normal emojis in a 
  row. | [Error]
  ✅ - Reduced API requests when verifying the token. | [Improvement]
(06/04/24)
  ↗️ - You can now rotate the status (🟢online, ⛔dnd, 🟠idle,      
  🌑offline). | [Feature]
(01/04/24)
  ✅ - Fixed encoding (UTF-8). | [Error]
(12/03/24)
  ↗️ - Now you can rotate emojis (including animated emojis   
  (nitro)). | [Feature]
```

---------------------------------------

### 🤝 Contribution
If you find any bugs or have any suggestions for improvement, feel free to open an issue or submit a pull request!


### 📖 License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.👀

### 📞 Contact

You can contact me on Discord:

[![Discord](https://img.shields.io/badge/Discord-relih-blue?logo=discord&logoColor=white)](https://discord.com/users/728460389536235581)
