from abc import ABC,abstractmethod

class BotInterface(ABC):

    @abstractmethod
    async def send_message(self, chat_id: int, text: str):
        pass

    @abstractmethod
    async def start(self):
        pass