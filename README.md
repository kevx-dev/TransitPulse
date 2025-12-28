# 🚆 TransitPulse

A Telegram bot that provides real-time public transport information in Germany using location sharing. Built with Clean Architecture principles and the transport.rest API.

## ✨ Features

- 📍 Share your location via Telegram to find nearby transit stations
- 🚉 View real-time departure information with delays
- 🗺️ Open routes directly in Google Maps
- ⏱️ Formatted departure times and delay information
- ⬅️ Intuitive navigation with back buttons

## 🛠️ Tech Stack

- **Python 3.11+**
- **python-telegram-bot** - Telegram Bot API wrapper
- **requests** - HTTP client for API calls
- **transport.rest API** - Public transport data provider (no authentication required)
- **pytest** - Testing framework

## 🏗️ Project Structure

The project follows Clean Architecture principles with clear separation of concerns:

```
TransitPulse/
├── core/                      # Domain Layer
│   ├── domains/
│   │   ├── station.py         # Station entity with validation
│   │   └── departure.py       # Departure entity with time formatting
│   └── exceptions/
│       └── transport_rest_client_exception.py
├── infrastructure/            # Infrastructure Layer
│   ├── transport_rest_client.py    # API client for transport.rest
│   └── telegram_bot.py              # Telegram bot implementation
├── service/                   # Service Layer
│   └── settings.py            # Configuration management
├── tests/                     # Test Suite
│   ├── test_station.py
│   └── test_transport_rest_client.py
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── .gitignore
└── README.md
```

## 🚀 Setup & Installation

### Prerequisites

- Python 3.11 or higher
- Telegram Bot Token (get it from [@BotFather](https://t.me/botfather))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kevx-dev/TransitPulse.git
cd TransitPulse
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file or set your Telegram bot token in `service/settings.py`:
```python
TELEGRAM_BOT_TOKEN = "your_bot_token_here"
```

5. Run the bot:
```bash
python main.py
```

## 📖 Usage

1. Start a chat with your bot on Telegram
2. Share your location using Telegram's location sharing feature
3. Select a nearby station from the button list
4. View real-time departures with delay information
5. Click on a departure to open the route in Google Maps
6. Use the "Zurück" (Back) button to navigate back

## 🌐 API Information

This project uses the **transport.rest API** ecosystem:
- **API Documentation**: [v6.db.transport.rest](https://v6.db.transport.rest/)
- **API Overview**: [transport.rest](https://transport.rest/)
- **Rate Limits**: 100 requests/minute (burst: 150 req/min)
- **Coverage**: Deutsche Bahn (DB) network including regional trains, S-Bahn, U-Bahn, buses, and trams
- **No authentication required**

Check the [status page](https://transport.rest) for uptime and planned maintenance.

## 🏛️ Architecture

### Clean Architecture Layers

**Core (Domain Layer)**
- Pure business logic
- Domain entities (`Station`, `Departure`)
- Data validation and formatting
- No external dependencies

**Infrastructure Layer**
- External API integration (`transport_rest_client.py`)
- Telegram Bot interface (`telegram_bot.py`)
- Concrete implementations of interfaces

**Service Layer**
- Application configuration (`settings.py`)
- Orchestration between layers

### Key Design Decisions

- **Domain Validation**: All domain objects validate their data in `__post_init__`
- **Property Pattern**: Time formatting via `@property` for clean separation
- **Custom Exceptions**: Type-safe error handling with custom exception classes
- **Type Hints**: Full type annotation for better IDE support and maintainability
- **Inline Keyboards**: Interactive button-based UI instead of text commands

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

Current test coverage includes:
- Station domain validation
- Transport REST client API integration
- Error handling scenarios

## 🔮 Future Enhancements

- [ ] Add journey planning between two locations
- [ ] Implement departure filtering (only specific lines)
- [ ] Add favorite stations
- [ ] Multi-language support
- [ ] Docker containerization
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Extended test coverage
- [ ] Database for user preferences

## 🤝 Contributing

This is a personal learning project, but suggestions and feedback are welcome! Feel free to:
- Open an issue for bugs or feature requests
- Suggest improvements to the architecture
- Share ideas for new features

## 📝 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- [transport.rest](https://transport.rest/) for providing free public transport APIs
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for the excellent Telegram Bot framework
- Deutsche Bahn for the public transport data

## 👨‍💻 Author

**kevx-dev**
- GitHub: [@kevx-dev](https://github.com/kevx-dev)

---

**Built with ❤️ and Clean Architecture principles**
