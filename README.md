# Mirror of Thought

A self-reflection notebook with AI integration using Django and Google's Gemini AI.

## Features

- Clean, minimalist text editor for journaling
- AI-powered reflection assistance using Gemini
- Dark/light mode toggle
- Customizable text size and color
- Responsive design

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mirror-of-thought
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On macOS/Linux
   # or
   myenv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```bash
   echo "GEMINI_API_KEY=your_actual_gemini_api_key_here" > .env
   ```
   Replace `your_actual_gemini_api_key_here` with your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Getting Started

1. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

2. **Start the development server**
   ```bash
   python manage.py runserver
   ```

3. **Access the application locally**
   - http://127.0.0.1:8000/

## Usage

1. Start typing in the text editor to begin your reflection
2. Click "Dive Deeper 💭" to get AI-powered insights
3. Use the color and size controls to customize your experience
4. Toggle between dark and light modes using the buttons in the header

## Project Structure

```
mirror-of-thought/
├── config/                 # Django project settings
├── notes/                  # Main app
│   ├── ml_models/         # AI integration
│   └── views.py           # App views
├── static/                # CSS, JS, and static assets
├── templates/             # HTML templates
└── manage.py             # Django management script
```

## Technologies Used

- **Django** - Web framework
- **Google Gemini AI** - AI reflection assistance
- **SQLite** - Database
- **CSS3** - Styling and responsive design
- **JavaScript** - Interactive features

## License

This project is licensed under the MIT License - see the LICENSE file for details.
