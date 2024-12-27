import json
import os
import time
import requests
from colorama import Fore, init

def read_file_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def get_user_info(token):
    header = {'authorization': token}
    r = requests.get("https://discord.com/api/v10/users/@me", headers=header)
    if r.status_code == 200:
        return r.json()["username"], True
    return "Invalid token", False

def read_emojis(file_name):
    emojis = []
    for line in read_file_lines(file_name):
        parts = line.split(":")
        if len(parts) == 2 and parts[1].isdigit():
            emojis.append({"name": parts[0], "id": parts[1]})
        else:
            emojis.append({"name": line, "id": None})
    return emojis

def change_status(token, message, emoji_name, emoji_id, new_status, hypesquad=None):
    header = {'authorization': token}
    payload = {"custom_status": {"text": message}}
    if new_status:
        payload["status"] = new_status
    if emoji_id:
        payload["custom_status"].update({"emoji_name": emoji_name, "emoji_id": emoji_id})
    else:
        payload["custom_status"]["emoji_name"] = emoji_name
    if hypesquad:
        payload["hypesquad"] = hypesquad
    r = requests.patch("https://discord.com/api/v10/users/@me/settings", headers=header, json=payload)
    return r.status_code == 200

def change_hypesquad(token, hypesquad_type):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    body = {"house_id": hypesquad_type}
    response = requests.post('https://discord.com/api/v10/hypesquad/online', headers=headers, json=body)
    if response.status_code == 204:
        print('Hypesquad successfully changed!')
        return True
    print('Error when changing Hypesquad.')
    return False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

def color_text(text, color_code):
    return f"{color_code}{text}{Fore.RESET}"

def change_bio(token, bio_text):
    url = 'https://discord.com/api/v10/users/@me/profile'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {'bio': bio_text}
    response = requests.patch(url, headers=headers, json=payload)
    if response.status_code == 200:
        print('Bio successfully changed!')
        return True
    print('Error when changing bio.')
    return False

init()

def main():
    config = load_config()
    token = config["token"]
    clear_enabled = config["clear_enabled"]
    clear_interval = config["clear_interval"]
    speed_rotator = config["speed_rotator"]
    status_sequence = config["status_sequence"]
    use_status_sequence = config["use_status_sequence"]
    hypesquad_sequence = config.get("custom_hypesquad_sequence", config["hypesquad_sequence"])
    rotate_hypesquad = config.get("rotate_hypesquad", True)
    hypesquad_rotation_interval = config.get("hypesquad_rotation_interval", 60)
    rotate_aboutme = config.get("rotate_aboutme", True)
    aboutme_rotation_interval = config.get("aboutme_rotation_interval", 60)
    aboutme_sequence = read_file_lines("aboutme.txt") if rotate_aboutme else []

    status_count = emoji_count = hypesquad_count = aboutme_count = 0
    next_hypesquad_time = next_aboutme_time = time.time()

    try:
        statuses = read_file_lines("text.txt")
        emojis = read_emojis("emojis.txt")
    except Exception as e:
        print(f"Error reading files: {e}")
        return

    user_info, is_valid_token = get_user_info(token)
    if not is_valid_token:
        print("Invalid token. Exiting the program.")
        return

    bio = aboutme_sequence[0] if rotate_aboutme and aboutme_sequence else "N/A"

    while True:
        try:
            current_status = status_sequence[status_count % len(status_sequence)] if use_status_sequence else None
            status = statuses[status_count % len(statuses)]
            time_formatted = color_text(time.strftime("%I:%M %p:"), Fore.MAGENTA)
            token_info = f"{token[:6]}****** | {user_info}"
            token_colored = color_text(token_info, Fore.GREEN if is_valid_token else Fore.RED)
            status_colored = color_text(status, Fore.CYAN)
            emoji = emojis[emoji_count % len(emojis)]
            emoji_name, emoji_id = emoji["name"], emoji["id"]
            current_time = time.time()

            hypesquad = "none"
            house_id = 0

            if rotate_hypesquad and current_time >= next_hypesquad_time:
                hypesquad = hypesquad_sequence[hypesquad_count % len(hypesquad_sequence)]
                house_id = config["hypesquad_mapping"].get(hypesquad.lower(), 0)
                print(f"{time_formatted} Rotating HypeSquad to: {hypesquad}")
                if not change_hypesquad(token, house_id):
                    print("Error when changing HypeSquad.")
                hypesquad_count += 1
                next_hypesquad_time = current_time + hypesquad_rotation_interval

            if rotate_aboutme and current_time >= next_aboutme_time:
                bio = aboutme_sequence[aboutme_count % len(aboutme_sequence)]
                print(f"{time_formatted} Rotating Bio a: {bio}")
                if not change_bio(token, bio):
                    print("Error when changing bio.")
                aboutme_count += 1
                next_aboutme_time = current_time + aboutme_rotation_interval

            print(f"{time_formatted} Status changed to: {token_colored}. New status message: {status_colored}. | Emoji: ({emoji_name}) | HypeSquad badge: {hypesquad} | Bio: {bio} | Status: {current_status}")
            if not change_status(token, status, emoji_name, emoji_id, current_status):
                print("Error when changing the status.")

            status_count += 1
            emoji_count += 1
            time.sleep(speed_rotator)
            if clear_enabled and status_count % clear_interval == 0:
                clear_console()
        except KeyboardInterrupt:
            print("Program stopped by the user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(speed_rotator)

if __name__ == "__main__":
    main()
