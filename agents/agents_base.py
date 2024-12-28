import openai
from abc import ABC, abstractmethod
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

class AgentBase(ABC):
    def __init__ (self, name, max_retries=2, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
    def call_openai(self, messages, temperature=0.7, max_tokens=150):
        retries=0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[(self.name)] sending message to openai")
            
            except Exception as e: