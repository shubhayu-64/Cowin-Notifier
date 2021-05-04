# Cowin-Notifier

This is a python script that tweets available slots on the Cowin website for both 45+ and 18+ age range. This uses the Cowin Public APIs.

The Twitter handle of the Bot: [@CowinNotifier](https://twitter.com/CowinNotifier)

## Features

- Find any open slots in any district and tweet important information.
- Runs 24/7 and updates at an interval of 12 hours.

## Installation

1. Clone the repo or download manually.

```bash
git clone https://github.com/shubhayu-64/Cowin-Notifier.git
```

2. Move to cloned/downloaded directory ` cd Cowin-Notifier`
3. Run `pip install requirements.txt`
4. Update `config.py` with your Twitter API credentials.
5. Start the script by `python main.py`


## Screenshots
- [@CowinNotifier](https://twitter.com/CowinNotifier) Twitter account

![Profile Image](/img/profile.png)

- Tweets posted.

![Tweets Image](/img/tweets.png)

- Terminal of the script

![Terminal Image](/img/terminal.png)

## Deploying

Since Cowin APIs are Geo-fenced, it might be difficult to get responses if hosted somewhere else.

I have hosted in my Raspberry Pi 3 Model B+ with my local network. This solved the issue for me.

## Contributing

Pull requests are welcome. For major changes, feel free to open an issue first to discuss what you would like to change.

## License

[MIT © Shubhayu Majumdar](https://github.com/shubhayu-64/Cowin-Notifier/blob/main/LICENSE)

## 🙋‍♂️ Support

💙 If you like this project, give it a ⭐ and share it with friends!

[☕ Buy me a coffee](https://www.buymeacoffee.com/shubhayu64)

---

Made with ❤️ and Python
