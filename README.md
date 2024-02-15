# Getting Started in AI

Welcome to our project on getting started in AI! This guide will walk you through the initial steps to set up your development environment, access OpenAI's API, and run your first AI application.

## Prerequisites

Before you start, make sure you have the following:

- Python 3.9 or later installed
- A GitHub account
- An account with OpenAI (to access API keys)

## Step 1: Setting Up Your OpenAI Account

1. Go to [OpenAI](https://openai.com/) and sign up for an account if you haven't already.
2. Once logged in, navigate to the API section and take note of your API keys. You'll need these to interact with OpenAI's services programmatically.

## Step 2: Installing Visual Studio Code

1. Download and install Visual Studio Code (VS Code) from [here](https://code.visualstudio.com/).
2. Launch VS Code after installation.

## Step 3: Installing Extensions

To make the most out of VS Code for AI development, install the following extensions:

- Python: For writing and executing Python code.
- GitHub Copilot: Offers AI-powered code suggestions.

To install an extension, click on the Extensions view icon on the Sidebar or press `Ctrl+Shift+X` and search for the extension by name. Click Install to add it to your VS Code.

## Step 4: Setting Up a Virtual Environment

### From within VS code, click on view, and then command palette, then type python Create environment

or 

1. Open a terminal in VS Code (`Ctrl+` `` `).
2. Navigate to your project directory.
3. Run the following command to create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

- On Windows:

```bash
.\venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

## Step 5: Storing Your OpenAI API Key Securely

Before running your AI application, it's important to securely store your OpenAI API key. We'll use a `.env` file for this purpose.

1. With your virtual environment activated, create a file named `.env` in your project directory.
2. Open the `.env` file in VS Code and add the following line:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

## Running Your Application

Ensure your virtual environment is activated, and run the following command in the terminal:

```bash
python app.py
```

## Conclusion

Congratulations! You've set up your AI development environment and are ready to start building AI applications. Remember to explore the OpenAI documentation and API references to learn more about the capabilities available to you.