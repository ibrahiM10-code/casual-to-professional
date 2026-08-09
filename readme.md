# Casual to Professional

A small and simple Python utility that uses Google Gemini through LangChain to convert casual messages into a more professional tone. Sometimes we spend too much time trying to figure out the right way to say (or write) something in a professional and friendly way. This utility simplify said issue and save us some time.

## Overview

This project accepts a user-provided message and returns a polished, professional version while preserving the original meaning. It is useful for turning informal chat or email drafts into a more workplace-appropriate response.

## Features

- Converts casual language into professional tone
- Preserves original meaning without adding new information
- Supports both English and Spanish responses
- Powered by Google Gemini via LangChain

## Requirements

- Python 3.11+ (recommended)
- `langchain`
- `langchain_google_genai`
- `python-dotenv`

## Setup

1. Clone the repository.
2. Create a virtual environment:

```bash
virtualenv -p python3 venv
```

3. Activate the environment:

```powershell
.\venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install langchain langchain-google-genai python-dotenv
```

5. Create a `.env` file in the repository root and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the script and enter the message you want to professionalize:

```bash
python main.py
```

Then type the casual message when prompted.

## Notes

- Make sure your Gemini API key is valid and has access to the `gemini-2.5-flash` model.
