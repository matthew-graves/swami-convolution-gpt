from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        self.discord_token = os.getenv("DISCORD_TOKEN")
        self.openai_token = os.getenv("OPENAI_API_KEY")
        self.discord_command_prefix = "!"
    