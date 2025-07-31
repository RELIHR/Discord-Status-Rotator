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

def print_banner():
    banner = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════╗
║                    🔄 Discord Status Rotator                  ║
║                          by RELIHR                            ║
╚═══════════════════════════════════════════════════════════════╝{Fore.RESET}
"""
    print(banner)

def print_status_change(time_formatted, token_colored, status_colored, emoji_name, hypesquad, bio, current_status, status_count, total_statuses):
    separator = f"{Fore.BLUE}{'─' * 65}{Fore.RESET}"
    
    print(separator)
    print(f"{Fore.YELLOW}⏰ Time:{Fore.RESET} {time_formatted}")
    print(f"{Fore.GREEN}👤 User:{Fore.RESET} {token_colored}")
    print(f"{Fore.CYAN}💬 Status:{Fore.RESET} {status_colored}")
    print(f"{Fore.MAGENTA}😀 Emoji:{Fore.RESET} {color_text(emoji_name, Fore.YELLOW)}")
    print(f"{Fore.RED}🏆 HypeSquad:{Fore.RESET} {color_text(hypesquad, Fore.LIGHTBLUE_EX)}")
    print(f"{Fore.LIGHTGREEN_EX}📝 Bio:{Fore.RESET} {color_text(bio[:30] + '...' if len(bio) > 30 else bio, Fore.WHITE)}")
    print(f"{Fore.LIGHTRED_EX}🔮 Discord Status:{Fore.RESET} {color_text(str(current_status), Fore.LIGHTMAGENTA_EX)}")
    print(f"{Fore.LIGHTYELLOW_EX}📊 Progress:{Fore.RESET} {color_text(f'{status_count % total_statuses + 1}/{total_statuses}', Fore.LIGHTCYAN_EX)}")
    
    progress = (status_count % total_statuses + 1) / total_statuses
    bar_length = 20
    filled_length = int(bar_length * progress)
    bar = f"{Fore.GREEN}{'█' * filled_length}{Fore.LIGHTBLACK_EX}{'░' * (bar_length - filled_length)}{Fore.RESET}"
    print(f"{Fore.LIGHTYELLOW_EX}📈 Progress Bar:{Fore.RESET} {bar} {progress*100:.1f}%")

def print_rotation_message(time_formatted, rotation_type, value):
    icons = {
        "hypesquad": "🏆",
        "bio": "📝",
        "emoji": "😀"
    }
    
    icon = icons.get(rotation_type, "🔄")
    print(f"\n{Fore.LIGHTGREEN_EX}✨ {icon} {time_formatted} Rotating {rotation_type}: {color_text(value, Fore.YELLOW)}{Fore.RESET}")

def print_error_message(error_type):
    error_messages = {
        "status": "❌ Error changing status",
        "hypesquad": "❌ Error changing HypeSquad",
        "bio": "❌ Error changing bio"
    }
    
    message = error_messages.get(error_type, "❌ Unknown error")
    print(f"{Fore.RED}{message}{Fore.RESET}")

def print_startup_info(user_info, is_valid_token):
    status_color = Fore.GREEN if is_valid_token else Fore.RED
    status_text = "✅ Valid" if is_valid_token else "❌ Invalid"
    
    print(f"\n{Fore.LIGHTBLUE_EX}🚀 Starting Discord Status Rotator...{Fore.RESET}")
    print(f"{Fore.YELLOW}👤 Connected user:{Fore.RESET} {color_text(user_info, Fore.CYAN)}")
    print(f"{Fore.YELLOW}🔑 Token:{Fore.RESET} {status_color}{status_text}{Fore.RESET}")
    print(f"{Fore.GREEN}{'─' * 50}{Fore.RESET}\n")

def print_configuration_info(config, total_statuses, total_emojis):
    print(f"{Fore.LIGHTBLUE_EX}⚙️  Current configuration:{Fore.RESET}")
    print(f"{Fore.CYAN}   • Rotation speed:{Fore.RESET} {config['speed_rotator']} seconds")
    print(f"{Fore.CYAN}   • Total statuses:{Fore.RESET} {total_statuses}")
    print(f"{Fore.CYAN}   • Total emojis:{Fore.RESET} {total_emojis}")
    print(f"{Fore.CYAN}   • Emoji mode:{Fore.RESET} {config.get('emoji_rotation_mode', 'with_text')}")
    print(f"{Fore.CYAN}   • Console clear:{Fore.RESET} {'✅ Every ' + str(config.get('clear_interval', 15)) + ' updates' if config.get('clear_enabled', False) else '❌ Disabled'}")
    print(f"{Fore.CYAN}   • HypeSquad rotation:{Fore.RESET} {'✅ Enabled' if config.get('rotate_hypesquad', False) else '❌ Disabled'}")
    print(f"{Fore.CYAN}   • Bio rotation:{Fore.RESET} {'✅ Enabled' if config.get('rotate_aboutme', False) else '❌ Disabled'}")
    print(f"{Fore.GREEN}{'─' * 50}{Fore.RESET}\n")

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
    emoji_rotation_mode = config.get("emoji_rotation_mode", "with_text")
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
        print(f"{Fore.RED}❌ Error reading files: {e}{Fore.RESET}")
        print(f"{Fore.YELLOW}💡 Make sure 'text.txt' and 'emojis.txt' files exist{Fore.RESET}")
        return

    user_info, is_valid_token = get_user_info(token)
    if not is_valid_token:
        print(f"{Fore.RED}❌ Invalid token. Exiting the program.{Fore.RESET}")
        return

    clear_console()
    print_banner()
    print_startup_info(user_info, is_valid_token)
    print_configuration_info(config, len(statuses), len(emojis))

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
                print_rotation_message(time_formatted, "hypesquad", hypesquad)
                if not change_hypesquad(token, house_id):
                    print_error_message("hypesquad")
                hypesquad_count += 1
                next_hypesquad_time = current_time + hypesquad_rotation_interval

            if rotate_aboutme and current_time >= next_aboutme_time:
                bio = aboutme_sequence[aboutme_count % len(aboutme_sequence)]
                print_rotation_message(time_formatted, "bio", bio)
                if not change_bio(token, bio):
                    print_error_message("bio")
                aboutme_count += 1
                next_aboutme_time = current_time + aboutme_rotation_interval

            print_status_change(time_formatted, token_colored, status_colored, emoji_name, hypesquad, bio, current_status, status_count, len(statuses))
            
            if not change_status(token, status, emoji_name, emoji_id, current_status):
                print_error_message("status")

            status_count += 1
            
            if emoji_rotation_mode == "with_text":
                emoji_count += 1
            elif emoji_rotation_mode == "after_text_cycle" and status_count % len(statuses) == 0:
                emoji_count += 1
                print_rotation_message(time_formatted, "emoji", f"Cycle completed - New emoji: {emojis[emoji_count % len(emojis)]['name']}")
            
            if clear_enabled and status_count % clear_interval == 0:
                time.sleep(speed_rotator)
                clear_console()
                print_banner()
            else:
                time.sleep(speed_rotator)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}⚠️  Program stopped by user.{Fore.RESET}")
            print(f"{Fore.CYAN}👋 Thanks for using Discord Status Rotator!{Fore.RESET}")
            break
        except Exception as e:
            print(f"{Fore.RED}❌ An error occurred: {e}{Fore.RESET}")
            time.sleep(speed_rotator)

if __name__ == "__main__":
    main()
