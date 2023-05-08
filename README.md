# Overview

A Discord bot in Python that responds to @ messages with the OpenAI API for text completion.

## 😎 Create virtual environment

```python
python3 -m venv my_env
```

Now set the virtual environment as the current.

```python
source my_env/bin/activate
```

## 💾 Install libraries

```python
pip install discord
pip install openai
pip install python-dotenv
```

## 🖥️ Set environment variables

Create a `.env` file in application root and set two values for the bot's API credentials:

```python
DISCORD_TOKEN = your-token
OPENAI_KEY = your-key
```

## 🚀 Start the bot

```python
python3 bot.py
```