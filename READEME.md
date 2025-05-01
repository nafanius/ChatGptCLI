# ChatGPT CLI

**ChatGPT CLI** is a Python-based command-line interface for interacting with ChatGPT using the OpenAI API.

## Features

- 🌐 Multilingual support (English, Russian, Polish)
- 💾 Save and load conversation history
- ⚡ Quick-access commands (e.g. `q`, `n`, `e`, `r`)
- 🖋️ Formatted output using `rich`

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/nafanius/ChatGptCLI.git
   cd chatg-cli
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**

   Create a file named `credentials.py` in the project root:

   ```python
   gpt_api_key = "your_openai_api_key"
   ```

## Usage

Launch the CLI with:

```bash
python3 chatg.py
```

### Available Commands

| Command | Description                                                             |
| ------- | ----------------------------------------------------------------------- |
| `q`     | Quit the application                                                    |
| `n`     | Start a new topic                                                       |
| `0`     | Reset prefix (exit translation mode)                                    |
| `00`    | Reset prefix and start a new topic                                      |
| `e`     | Translate input to **English**                                          |
| `p`     | Translate input to **Polish**                                           |
| `r`     | Translate input to **Russian**                                          |
| `rv`    | Translate to **Russian** and explain usage with examples in **English** |
| `s`     | Save conversation history to `history.json`                             |
| `l`     | Load conversation history from `history.json`                           |
| `c`     | Clear the screen                                                        |
| `h`     | Show help message                                                       |

## Dependencies

- [`openai`](https://pypi.org/project/openai/)
- [`rich`](https://pypi.org/project/rich/)
- `readline` (usually included in Unix-based systems)

## Example `credentials.py`

```python
gpt_api_key = "your_openai_api_key"
```

## License

MIT License
