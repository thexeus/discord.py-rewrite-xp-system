# Discord Leveling Bot

This bot tracks user activity in a Discord server and assigns experience points (XP) to users when they send messages. The XP is saved in a JSON file (`level.json`) to maintain user progress.

## Features

- Assigns random XP (between 5 and 25) to users when they send a message.
- Saves user XP data persistently in a JSON file.
- Ignores bot messages to prevent unintended behavior.

## Requirements

- Python 3.8+
- The following Python libraries:
  - `discord`
  - `discord.ext`
  - `json`
  - `random`

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install discord.py
   ```

3. **Set up the `level.json` file**:
   Ensure that a `level.json` file exists in the same directory as the bot code. If the file doesn't exist, the script will create it automatically. The file should have the following structure:
   ```json
   {
       "users": []
   }
   ```

4. **Add the cog to your bot**:
   In your bot's main file, add the following to load the leveling system:
   ```python
   from discord.ext import commands
   from level import setup

   client = commands.Bot(command_prefix="!")
   setup(client)

   client.run("YOUR_DISCORD_BOT_TOKEN")
   ```

## Usage

- Start the bot by running your main bot file.
- The bot will monitor user messages and update the `level.json` file with their XP progress.

## File Structure

```
.
├── level.py            # Contains the leveling cog
├── level.json          # Stores user XP data
├── main.py             # Your main bot script (example)
├── README.md           # This README file
```

## How It Works

1. **Message Listener**:
   The `on_message` event listener monitors every message sent in the server.

2. **XP Calculation**:
   A random XP value (between 5 and 25) is assigned to the user who sent the message.

3. **Data Persistence**:
   User XP data is saved in `level.json`. If the user already exists in the file, their XP is updated; otherwise, a new entry is created.

## Contributing

Feel free to fork this repository and submit pull requests with improvements or additional features.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

### Notes

- Ensure the bot has permissions to read messages in the channels it is monitoring.
- Be mindful of rate limits when running the bot on large servers with high activity.
