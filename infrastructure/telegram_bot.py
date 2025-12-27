from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CallbackQueryHandler
from infrastructure.transport_rest_client import TransportRestClient


class TelegramBot:

    def __init__(self, token:str, client: TransportRestClient):
        self.app = Application.builder().token(token=token).build()
        self.client = client

    async def handle_location(self, update, context):
        location = update.message.location

        nearby_stations = self.client.get_nearby_stations(longitude=location.longitude,latitude=location.latitude)

        buttons = []

        for station in nearby_stations:
            button = InlineKeyboardButton(
                text=f"📍 {station.name} - ({station.distance}m)",
                callback_data=station.id

            )
            buttons.append([button])

        keyboard = InlineKeyboardMarkup(buttons)

        await update.message.reply_text(
            "Wähle eine Station",
            reply_markup=keyboard
        )


    async def handle_button_click(self, update, context):
        query = update.callback_query
        await query.answer()
        station_id = query.data
        data = self.client.get_departures(stop_id=station_id)

        await query.edit_message_text(
            text=f"{data}"
        )

    def run(self):
        self.app.add_handler(MessageHandler(filters.LOCATION,self.handle_location))
        self.app.add_handler(CallbackQueryHandler(self.handle_button_click))
        self.app.run_polling()





