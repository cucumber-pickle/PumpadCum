import cloudscraper
import os
from core.helper import get_headers, countdown_timer, extract_user_data, config
from colorama import *
import random
from datetime import datetime
import time
from requests.exceptions import RequestException


class Pumpad:
    def __init__(self) -> None:
        self.scraper = cloudscraper.create_scraper()


    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def set_proxy(self, proxy):
        self.scraper.proxies = {
            "http": proxy,
            "https": proxy,
        }
        if '@' in proxy:
            host_port = proxy.split('@')[-1]
        else:
            host_port = proxy.split('//')[-1]
        return host_port

    def welcome(self):
        banner = f"""{Fore.GREEN}
 ██████  ██    ██   ██████  ██    ██  ███    ███  ██████   ███████  ██████  
██       ██    ██  ██       ██    ██  ████  ████  ██   ██  ██       ██   ██ 
██       ██    ██  ██       ██    ██  ██ ████ ██  ██████   █████    ██████  
██       ██    ██  ██       ██    ██  ██  ██  ██  ██   ██  ██       ██   ██ 
 ██████   ██████    ██████   ██████   ██      ██  ██████   ███████  ██   ██     
            """
        print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
        print(Fore.GREEN + f" Pumpad Bot")
        print(Fore.RED + f" FREE TO USE = Join us on {Fore.GREEN}t.me/cucumber_scripts")
        print(Fore.YELLOW + f" before start please '{Fore.GREEN}git pull{Fore.YELLOW}' to update bot")
        print(f"{Fore.WHITE}~" * 60)
    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def user_information(self, query: str):
        url = 'https://tg.pumpad.io/referral/api/v1/tg/user/information'
        self.headers.update({
            'Authorization': f'tma {query}'
        })

        response = self.scraper.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_lottery(self, query: str):
        url = 'https://tg.pumpad.io/referral/api/v1/lottery'
        self.headers.update({
            'Authorization': f'tma {query}',
        })

        response = self.scraper.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def post_lottery(self, query: str):
        url = 'https://tg.pumpad.io/referral/api/v1/lottery'
        self.headers.update({
            'Authorization': f'tma {query}',
        })

        response = self.scraper.post(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_checkin(self, query: str):
        url = 'https://tg.pumpad.io/referral/api/v1/tg/raffle/checkin'
        self.headers.update({
            'Authorization': f'tma {query}',
        })

        response = self.scraper.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def post_checkin(self, query: str):
        url = 'https://tg.pumpad.io/referral/api/v1/tg/raffle/checkin'
        self.headers.update({
            'Authorization': f'tma {query}',
        })

        response = self.scraper.post(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_ticket(self, query: str):
        url = 'https://tg.pumpad.io/referral/api/v1/tg/raffle/tickets'
        self.headers.update({
            'Authorization': f'tma {query}',
        })

        response = self.scraper.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def post_raffle(self, query: str):
        url = 'https://tg.pumpad.io/referral/api/v1/tg/raffle/bets'
        self.headers.update({
            'Authorization': f'tma {query}',
        })

        response = self.scraper.post(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_missions(self, query: str):
        url = 'https://tg.pumpad.io/referral/api/v1/tg/missions'
        self.headers.update({
            'Authorization': f'tma {query}',
        })

        response = self.scraper.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def post_missions(self, query: str, mission_id: int):
        url = f'https://tg.pumpad.io/referral/api/v1/tg/missions/check/{mission_id}'
        data = {}
        self.headers.update({
            'Authorization': f'tma {query}',
        })

        response = self.scraper.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def process_query(self, query: str):
        user = self.user_information(query)
        if not user:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED + Style.BRIGHT} Query ID Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}or{Style.RESET_ALL}"
                f"{Fore.YELLOW + Style.BRIGHT} Blocked By Cloudflare {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} [ Restart Again ] {Style.RESET_ALL}"
            )
            return

        if user:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['user_name']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            time.sleep(1)

            check_in = self.get_checkin(query)
            if check_in and not check_in['is_check_in']:
                claim = self.post_checkin(query)
                if claim and claim['raffle_count']:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} Day {check_in['consecutive_days'] + 1} {Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {claim['raffle_count']} Raffle Ticket {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} Day {check_in['consecutive_days'] + 1} {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Day {check_in['consecutive_days']} {Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT}Is Already Claimed{Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                )
            time.sleep(1)

            ticekt = self.get_ticket(query)
            if ticekt and ticekt['number_of_tickets'] > 0:
                count = ticekt['number_of_tickets']

                while count > 0:
                    raffle = self.post_raffle(query)
                    if raffle and raffle['number']:
                        count = raffle['remain_count']

                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Raffle{Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT} Is Success {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}] [ Number{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {raffle['number']} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}] [ Ticket{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {count} Left {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Raffle{Style.RESET_ALL}"
                            f"{Fore.RED + Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        break

                if count == 0:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Raffle{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} No Ticket Remaining {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Raffle{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} No Ticket Remaining {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )

            missions = self.get_missions(query)
            if missions['mission_list'] is not None and 'mission_list' in missions:
                for mission in missions['mission_list']:
                    mission_id = mission['mission']['id']
                    mission_name = mission['mission']['name']
                    mission_reward = mission['mission']['reward']
                    done_time = mission['done_time']

                    if mission_id == 38:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Mission{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {mission_name} {Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT}Skipped{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                        continue

                    if done_time == 0:
                        complete = self.post_missions(query, mission_id)
                        if complete is True:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Mission{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {mission_name} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} +{mission_reward} Draw Count {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Mission{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {mission_name} {Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Mission{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {mission_name} {Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT}Is Already Completed{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
            else:
                self.log(f"{Fore.GREEN + Style.BRIGHT}[ Mission Clear ]{Style.RESET_ALL}")
            time.sleep(1)

            draw = self.post_lottery(query)
            if draw is not None:
                if 'reward' in draw:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Draw{Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT} Is Success {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {draw['reward']['name']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Draw{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )

            lottery = self.get_lottery(query)
            if lottery is not None:
                count = lottery['draw_count']
                if count != 0:
                    while count > 0:
                        draw = self.post_lottery(query)
                        if draw is not None:
                            if 'reward' in draw:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Draw{Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {draw['reward']['name']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Draw{Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(f"{Fore.RED + Style.BRIGHT}[ Data Post Lottery Is None ]{Style.RESET_ALL}")
                        count -= 1
                else:
                    self.log(f"{Fore.YELLOW + Style.BRIGHT}[ You Don't Have Enough Draw Count ]{Style.RESET_ALL}")
            else:
                self.log(f"{Fore.RED + Style.BRIGHT}[ Data Get Lottery Is None ]{Style.RESET_ALL}")

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]
            with open('proxies.txt', 'r') as file:
                proxies = [line.strip() for line in file if line.strip()]

            while True:
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Proxy's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(proxies)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                for i, query in enumerate(queries):
                    query = query.strip()
                    if query:
                        self.log(
                            f"{Fore.GREEN + Style.BRIGHT}Account: {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT}{i + 1} / {len(queries)}{Style.RESET_ALL}"
                        )
                        if len(proxies) >= len(queries):
                            proxy = self.set_proxy(proxies[i])  # Set proxy for each account
                            self.log(
                                f"{Fore.GREEN + Style.BRIGHT}Use proxy: {Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT}{proxy}{Style.RESET_ALL}"
                            )

                        else:
                            self.log(
                                Fore.RED + "Number of proxies is less than the number of accounts. Proxies are not used!")

                        user_info = extract_user_data(query)
                        user_id = str(user_info.get('id'))
                        self.headers = get_headers(user_id)

                        try:
                            self.process_query(query)
                        except Exception as e:
                            self.log(f"{Fore.RED + Style.BRIGHT}An error process_query: {e}{Style.RESET_ALL}")

                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}" * 75)
                        account_delay = config['account_delay']
                        countdown_timer(random.randint(min(account_delay), max(account_delay)))

                cycle_delay = config['cycle_delay']
                countdown_timer(random.randint(min(cycle_delay), max(cycle_delay)))


        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Pumpad - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    pumpad = Pumpad()
    pumpad.clear_terminal()
    pumpad.welcome()
    pumpad.main()