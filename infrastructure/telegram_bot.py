from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CallbackQueryHandler
from infrastructure.transport_rest_client import TransportRestClient



class TelegramBot:

    def __init__(self, token: str, client: TransportRestClient):
        self.app = Application.builder().token(token=token).build()
        self.client = client

    async def handle_location(self, update, context):
        location = update.message.location
        context.user_data['last_location'] = location

        nearby_stations = self.client.get_nearby_stations(
            longitude=location.longitude,
            latitude=location.latitude
        )

        buttons = []
        for station in nearby_stations:
            button = InlineKeyboardButton(
                text=f"📍 {station.name} - ({station.distance}m)",
                callback_data=f"station_{station.id}"
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

        if query.data.startswith("station_"):
            station_id = query.data.replace("station_", "")
            await self._show_departures(query, station_id, context)

        elif query.data.startswith("maps_"):
            departure_info = query.data.replace("maps_", "")
            await self._open_maps(query, departure_info, context)

        elif query.data == "back_to_stations":
            location = context.user_data.get("last_location")
            if location:
                await self._show_stations(query, location)

    async def _show_stations(self, query, location):
        nearby_stations = self.client.get_nearby_stations(
            longitude=location.longitude,
            latitude=location.latitude
        )

        buttons = []
        for station in nearby_stations:
            button = InlineKeyboardButton(
                text=f"📍 {station.name} - ({station.distance}m)",
                callback_data=f"station_{station.id}"
            )
            buttons.append([button])

        keyboard = InlineKeyboardMarkup(buttons)

        await query.edit_message_text(
            text="Wähle eine Station",
            reply_markup=keyboard
        )

    async def _show_departures(self, query, station_id, context):
        context.user_data['current_station_id'] = station_id
        data = self.client.get_departures(station_id=station_id)

        buttons = []

        for departure in data:
            button_text = f"🚉 {departure.departure_name} | ⏰ {departure.formatted_time} | {departure.delay_display}"

            buttons.append([
                InlineKeyboardButton(
                    text=button_text,
                    callback_data=f"maps_{departure.departure_name}_{departure.latitude}_{departure.longitude}"
                )
            ])

        buttons.append([
            InlineKeyboardButton(
                text="⬅️ Zurück zu Stationen",
                callback_data="back_to_stations"
            )
        ])

        keyboard = InlineKeyboardMarkup(buttons)

        await query.edit_message_text(
            text="🚆 Wähle eine Abfahrt:",
            reply_markup=keyboard
        )

    async def _open_maps(self, query, departure_info, context):
        parts = departure_info.split("_")
        name = parts[0]
        latitude = parts[1]
        longitude = parts[2]

        station_id = context.user_data.get('current_station_id')
        maps_url = f"https://maps.google.com/?q={latitude},{longitude}"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="📍 In Google Maps öffnen", url=maps_url)],
            [InlineKeyboardButton(text="⬅️ Zurück zu Abfahrten", callback_data=f"station_{station_id}")]
        ])

        await query.edit_message_text(
            text=f"🗺️ Route zu: {name}",
            reply_markup=keyboard
        )

    def run(self):
        self.app.add_handler(MessageHandler(filters.LOCATION, self.handle_location))
        self.app.add_handler(CallbackQueryHandler(self.handle_button_click))
        self.app.run_polling()
