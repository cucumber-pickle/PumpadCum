# Pumpad bot


[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/cucumber_scripts)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/cucumber-pickle/Cucumber)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@cucumber_scripts)

## Registrations [https://t.me/Pumpad_Bot](https://t.me/Pumpad_Bot/Lucky?startapp=61251843371604851)


## Features

- **Multi-account Support:** Automate actions across multiple accounts. .
- **Auto Complete Task** Automatically perform available quest
- **Configurable Settings:** Control various aspects of the script via a `config.json` file.
- **Using a proxy**
- **Static user agent**

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/cucumber-pickle/PumpadCum.git
   cd PumpadCum
   
Create and activate a virtual environment:

   ```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
Install the required dependencies:

   ```bash
pip install -r requirements.txt
   ```

Run bot
   ```bash
   python bot.py
   ```
## Configuration
Create a config.json file in the root directory with the following structure:
   ```json
{
    "account_delay": [5, 10],
    "cycle_delay": [14400, 28800]
}
   ```

`delay_account`: Delay between processing different accounts (in seconds) - the minimum and maximum values are taken randomly

`cycle_delay`: Delay between different cycles of operations (in seconds) - the minimum and maximum values are taken randomly

## About Proxy


You can add your proxy list in `proxies.txt` and proxy format is like example below :

Format :

```
http://host:port
http://user:pass@host:port
```

Example :

```
http://127.0.0.1:6969
http://user:pass@127.0.0.1:6969
```

## How to get tgWebAppData (query_id / user_id)

1. Login telegram via portable or web version
2. Launch the bot
3. Press `F12` on the keyboard 
4. Open console
5. Сopy this code in Console for getting tgWebAppData (user= / query=):

```javascript
copy(decodeURIComponent(sessionStorage['telegram-apps/launch-params']).split('tgWebAppData=')[1].split('&tgWebAppStartParam')[0])
```

6. you will get data that looks like this

```
query_id=AA....
user=%7B%22id%....
```
7. add it to `query.txt` file or create it if you dont have one


## This bot helpfull?  Please support me by buying me a coffee: 

``` 0xc4bb02b8882c4c88891b4196a9d64a20ef8d7c36 ``` - BSC (BEP 20)

``` UQBiNbT2cqf5gLwjvfstTYvsScNj-nJZlN2NSmZ97rTcvKz0 ``` - TON

``` 0xc4bb02b8882c4c88891b4196a9d64a20ef8d7c36 ``` - Optimism

``` THaLf1cdEoaA73Kk5yiKmcRwUTuouXjM17 ``` - TRX (TRC 20)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or support, please contact [CUCUMBER TG CHAT](https://t.me/cucumber_scripts_chat)
