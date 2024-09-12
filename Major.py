import os
import json
import time
import random
import requests

from ctypes import windll
from text import print_name, clear_console
from colorama import Fore, Style
from typing import Union

windll.kernel32.SetConsoleTitleW("Major Hack by Argona")


# {"Account Name":["query","user-agent"]}
def get_data_from_file() -> Union[dict, bool]:
    user_folder = os.path.expanduser("~")
    tokens_file_path = os.path.join(user_folder, "major.json")

    if os.path.exists(tokens_file_path):
        with open(tokens_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not data["accounts"]:
                print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Accounts need to be added!")
                time.sleep(2)
                return False
            accounts_dict = {}
            accounts_names = list(data["accounts"].keys())
            for i in accounts_names:
                account = data["accounts"][i]
                accounts_dict[i] = [account["query"], account["user-agent"]]

            return accounts_dict

    else:
        data = {
            "accounts": {}
        }
        with open(tokens_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print(
                Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"File not found. A new file has been created at the path: {tokens_file_path}")
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Accounts need to be added!")
            time.sleep(2)
            return False


def get_access_token(query: str, user_agent: str, max_attempts: int) -> str:
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to get access token......")

    headers = {
        "user-agent": user_agent,
        "accept": "application/json, text/plain, */*",
        "origin": "https://major.glados.app",
        "referer": "https://major.glados.app/",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    url = "https://major.glados.app/api/auth/tg/"
    body = {"init_data": query}
    for _ in range(max_attempts):
        response = requests.post(url=url, headers=headers, json=body)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "Successful!")
            data = response.json()["access_token"]
            time.sleep(2)
            return data
        else:
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to get access token!")
    return ""


def visit(headers: dict, max_attempts: int) -> bool:
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to post visit......")
    url = "https://major.glados.app/api/user-visits/visit/"
    for _ in range(max_attempts):
        response = requests.post(url=url, headers=headers)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "Successful!")
            time.sleep(2)
            return True
        else:
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to post visit!")
    return False


def get_daily_tasks(headers: dict, max_attempts: int) -> dict:
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to get daily tasks......")
    params = {"is_daily": "true"}
    url = "https://major.bot/api/tasks/"
    for _ in range(max_attempts):
        response = requests.get(url=url, headers=headers, params=params)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "Successful!")
            time.sleep(2)
            return response.json()
        else:
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to get daily tasks")
    return {}


def get_permanent_tasks(headers: dict, max_attempts: int) -> dict:
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to get permanent tasks......")
    params = {"is_daily": "false"}
    url = "https://major.bot/api/tasks/"
    for _ in range(max_attempts):
        response = requests.get(url=url, headers=headers, params=params)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "Successful!")
            time.sleep(2)
            return response.json()
        else:
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to get permanent tasks")
    return {}


def post_task(task: int, name_task: str, headers: dict, max_attempts: int):
    print(Fore.YELLOW + Style.BRIGHT + f"Attempting to post task: {name_task}")
    url = "https://major.bot/api/tasks/"
    body = {"task_id": task}
    for _ in range(max_attempts):
        response = requests.post(url=url, headers=headers, json=body)
        if response.status_code == 201:
            if response.json()["is_completed"]:
                print(Fore.LIGHTGREEN_EX + "Successful!")
            else:
                print(Fore.LIGHTRED_EX + "Failure")
            time.sleep(2)
            return True
        else:
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + f"Failed to post task: {name_task}")
    return False


def tasks(headers: dict):
    tasks_daily = get_daily_tasks(headers, 3)
    if tasks_daily:
        for i in tasks_daily:
            if i["id"] in [29, 16, 5]:
                if not i["is_completed"]:
                    post_task(i["id"], i["title"], headers, 3)
                    time.sleep(2.5)

    task_permanent = get_permanent_tasks(headers, 3)
    if task_permanent:
        for i in task_permanent:
            if not i["is_completed"]:
                if not i["id"] in [33, 21, 20]:
                    post_task(i["id"], i["title"], headers, 3)
                    time.sleep(2.5)


def get_streak_daily(headers: dict):
    url = "https://major.glados.app/api/user-visits/streak/"
    response = requests.get(url=url, headers=headers)
    print(Fore.YELLOW + Style.BRIGHT + f"Send streak daily: {response.status_code}")
    time.sleep(1)


def get_coins_game(headers: dict, max_attempts: int):
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to get coins game info......")
    url = "https://major.glados.app/api/bonuses/coins/"
    for _ in range(max_attempts):
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "Successful!")
            time.sleep(2)
            return True
        else:
            data = response.json()
            if "detail" in data:
                print(Fore.LIGHTMAGENTA_EX + "The coins game has already been played!")
                time.sleep(2)
                return False
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to get coins game info")
    return False


def post_coins_game(headers: dict, max_attempts: int):
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to post coins game......")
    url = "https://major.glados.app/api/bonuses/coins/"
    coins = random.choice([885, 915])
    body = {"coins": coins}
    for _ in range(max_attempts):
        response = requests.post(url=url, headers=headers, json=body)
        if response.status_code == 201:
            print(Fore.LIGHTGREEN_EX + f"Successful: {coins}")
            time.sleep(2)
            return True
        else:
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to post coins game")
    return False


def get_roulette_game(headers: dict, max_attempts: int):
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to get roulette game info......")
    url = "https://major.glados.app/api/roulette/"
    for _ in range(max_attempts):
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "Successful!")
            time.sleep(2)
            return True
        else:
            data = response.json()
            if "detail" in data:
                print(Fore.LIGHTMAGENTA_EX + "The roulette game has already been played!")
                time.sleep(2)
                return False
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to get roulette game info")
    return False


def post_roulette_game(headers: dict, max_attempts: int):
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to post roulette game......")
    url = "https://major.glados.app/api/roulette/"
    for _ in range(max_attempts):
        response = requests.post(url=url, headers=headers)
        if response.status_code == 201:
            print(Fore.LIGHTGREEN_EX + f"Successful: {response.json()['rating_award']}")
            time.sleep(2)
            return True
        else:
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to post roulette game")
    return False


def get_swipe_game(headers: dict, max_attempts: int):
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to get swipe game info......")
    url = "https://major.glados.app/api/swipe_coin/"
    for _ in range(max_attempts):
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "Successful!")
            time.sleep(2)
            return True
        else:
            data = response.json()
            if "detail" in data:
                print(Fore.LIGHTMAGENTA_EX + "The swipe game has already been played!")
                time.sleep(2)
                return False
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to get swipe game info")
    return False


def post_swipe_game(headers: dict, max_attempts: int):
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to post swipe game......")
    url = "https://major.glados.app/api/swipe_coin/"
    coins = 2300 + random.randint(-150, 150)
    body = {"coins": coins}
    for _ in range(max_attempts):
        response = requests.post(url=url, headers=headers, json=body)
        if response.status_code == 201:
            print(Fore.LIGHTGREEN_EX + f"Successful: {coins}")
            time.sleep(2)
            return True
        else:
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to post swipe game")
    return False


def get_durov(headers: dict, max_attempts: int):
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to get durov info......")
    url = "https://major.bot/api/durov/"
    for _ in range(max_attempts):
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "Successful!")
            time.sleep(2)
            return True
        else:
            data = response.json()
            if "detail" in data:
                print(Fore.LIGHTMAGENTA_EX + "The durov game has already been played!")
                time.sleep(2)
                return False
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to get durov info")
    return False


def post_durov(headers: dict, max_attempts: int):
    print(Fore.YELLOW + Style.BRIGHT + "Attempting to post durov info......")
    url = "https://major.bot/api/durov/"

    numbers = list(range(1, 17))
    chosen_list = list()

    for i in range(4):
        chosen_number = random.choice(numbers)
        chosen_list.append(chosen_number)
        numbers.remove(chosen_number)

    body = {"choice_1": chosen_list[0], "choice_2": chosen_list[1], "choice_3": chosen_list[2], "choice_4": chosen_list[3]}
    for _ in range(max_attempts):
        response = requests.get(url=url, headers=headers, json=body)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + f"Successful!: {response.json()}")
            time.sleep(2)
            return True
        else:
            print(Fore.LIGHTBLACK_EX + f"Error: status code {response.status_code}")
            print(Fore.LIGHTBLACK_EX + "Attempting to reconnect")
            time.sleep(2)

    print(Fore.LIGHTRED_EX + "Failed to post durov info")
    return False


def main():
    try:
        print_name()
        clear_console()
        accounts_dict = get_data_from_file()  # {"Account Name":["query","user-agent"]}
        if not accounts_dict:
            return
        accounts_names = list(accounts_dict.keys())

        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + f"Available accounts: {' '.join(accounts_names)}")
        time.sleep(0.5)
        StrExcludedAccounts = input(Fore.LIGHTCYAN_EX + "Which accounts to exclude from the automation list?: ")
        ExcludeAccounts = StrExcludedAccounts.split()
        for i in range(len(accounts_names)):
            try:
                name = accounts_names[i]
                if name in ExcludeAccounts:
                    continue

                query = accounts_dict[name][0]
                user_agent = accounts_dict[name][1]

                print(Fore.BLUE + Style.BRIGHT + f"The account begins: {name}\n")

                access_token = get_access_token(query, user_agent, 3)

                headers = {
                    "Authorization": f"Bearer {access_token}",
                    "user-agent": user_agent,
                    "accept": "application/json, text/plain, */*",
                    "origin": "https://major.glados.app",
                    "referer": "https://major.glados.app/",
                    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
                }

                visit(headers, 3)
                get_streak_daily(headers)
                tasks(headers)
                if get_coins_game(headers, 3):
                    time.sleep(60)
                    post_coins_game(headers, 3)
                if get_roulette_game(headers, 3):
                    time.sleep(10)
                    post_roulette_game(headers, 3)
                if get_swipe_game(headers, 3):
                    time.sleep(60)
                    post_swipe_game(headers, 3)
                if get_durov(headers, 3):
                    time.sleep(10)
                    post_durov(headers, 3)

                time.sleep(3.5)
                clear_console()
            except Exception as e:
                print(Fore.LIGHTRED_EX + Style.BRIGHT + f"Error: {e}")
                time.sleep(2)
                clear_console()
                continue
    except Exception as e:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + f"Error: {e}")
        time.sleep(5)
        return


if __name__ == '__main__':
    main()
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX + "\nThe automation has been completed successfully!")
    time.sleep(3)
