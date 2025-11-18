import requests
from colorama import Fore, Style init


init(autoreset=True)


DEFAULT_MODEL = "google/pegasus-Xsum"

def build_api_url(model_name):
    