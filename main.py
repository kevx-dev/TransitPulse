# main.py
from infrastructure.telegram_bot import TelegramBot
from infrastructure.transport_rest_client import TransportRestClient
from core.config.settings import Settings

if __name__ == "__main__":
    # noinspection PyArgumentList
    settings = Settings()

    client = TransportRestClient()

    telegram_bot = TelegramBot(settings.telegram_api_key)
    telegram_bot.run()

