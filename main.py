# main.py
from infrastructure.telegram_bot import TelegramBot
from infrastructure.transport_rest_client import TransportRestClient
from core.config.settings import Settings

if __name__ == "__main__":
    # noinspection PyArgumentList
    settings = Settings()

    client = TransportRestClient()

    telegram_bot = TelegramBot(token=settings.telegram_api_key,client=client)
    telegram_bot.run()






