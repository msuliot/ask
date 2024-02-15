# Ask

Ask is a super simple example of how to create an OpenAI chatbot.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of Python.

### Installing Ask

To install Ask, follow these steps:

1. Clone the repo
   ```
   git clone https://github.com/<your-github-username>/ask.git
   ```
2. Change to the directory
   ```
   cd ask
   ```
3. Create a virtual environment
   ```
   python3 -m venv env
   ```
4. Activate the virtual environment
   ```
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
5. Install the requirements
   ```
   pip install -r requirements.txt
   ```

### Using Ask

To use Ask, you need to create a `.env` file for your OpenAI key. You can get the OpenAI key

Create the `.env` file, add the following line:

```
OPENAI_API_KEY = your-key-here
```

Replace `your-key-here` with your actual OpenAI key.