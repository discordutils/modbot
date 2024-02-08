# Advanced Moderation Discord Bot

This Discord bot provides advanced moderation features, including kicking, banning, clearing messages, and logging moderation actions.

## Prerequisites

- Python 3.x
- pip
- Discord account and a bot token (create a new bot at [Discord Developer Portal](https://discord.com/developers/applications))
- Discord server where you have the `kick_members`, `ban_members`, and `manage_messages` permissions

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/advanced-moderation-bot.git
    cd advanced-moderation-bot
    ```

2. **Install the required libraries:**
    ```bash
    pip install discord.py python-dotenv
    ```

3. **Create a `.env` file in the project directory and add your bot token and log channel ID:**
    ```env
    DISCORD_TOKEN=your_bot_token
    LOG_CHANNEL_ID=your_log_channel_id
    ```
    Replace `your_bot_token` with your actual bot token and `your_log_channel_id` with the ID of the channel where you want to log moderation actions.

## Usage

Run the bot script:
```bash
python advanced_moderation_bot.py
