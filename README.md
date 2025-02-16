# FIXIT

FIXIT is a modern web application that helps users process various types of inputs (text, images, audio, and video) through an intuitive interface. The application consists of a Next.js frontend with Stytch authentication and a Flask backend.

## Project Structure

```
fixit/
├── frontend/           # Next.js frontend application
│   └── stytch/        # Stytch authentication integration
└── backend/           # Flask backend application
```

## Prerequisites

- Node.js (v16 or higher)
- Python (v3.8 or higher)
- npm or yarn
- pip (Python package manager)

## Environment Variables

### Frontend (.env.local)
```
NEXT_PUBLIC_STYTCH_PUBLIC_TOKEN=your_public_token
STYTCH_SECRET=your_secret_key
NEXT_PUBLIC_STYTCH_PROJECT_ID=your_project_id
```

### Backend (.env)
```
OPENAI_API_KEY=your_openai_api_key
FLASK_ENV=development
```

## Installation & Setup

### Backend Setup

1. Create a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install flask flask-cors python-dotenv openai
```

3. Start the backend server:
```bash
cd backend
python api.py
# or
export FLASK_APP=api.py
export FLASK_ENV=development
flask run --port 8000
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Install Node.js dependencies:
```bash
cd frontend/stytch
npm install
# or
yarn install
```

2. Start the development server:
```bash
npm run dev
# or
yarn dev
```

The frontend will be available at `http://localhost:3000`

## Features

- Secure authentication using Stytch
- Support for multiple input types:
  - Text processing
  - Image processing
  - Audio processing
  - Video processing
- Modern, responsive UI with animations
- Real-time processing feedback

## API Endpoints

### Backend

- `POST /api/input`: Process various types of inputs
  - Accepts form data with either:
    - `text`: Text input
    - `file`: File upload (image, audio, or video)

## Development

To run the full stack locally:

1. Start the backend server:
```bash
cd backend
python api.py
# or
flask run --port 8000
```

2. In a new terminal, start the frontend development server:
```bash
cd frontend/stytch
npm run dev
# or
yarn dev
```

3. Visit `http://localhost:3000` in your browser

## Production Deployment

### Frontend

Build the production version:
```bash
cd frontend/stytch
npm run build
# or
yarn build
```

### Backend

For production deployment, it's recommended to use a production-grade WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 api:app
```

## License

MIT