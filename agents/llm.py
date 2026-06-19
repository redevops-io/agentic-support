"""OpenAI-compatible LLM client."""

import os
from openai import OpenAI


def get_client() -> OpenAI:
    base_url = os.environ.get("OPENAI_BASE_URL")
    api_key = os.environ.get("OPENAI_API_KEY", "EMPTY")
    return OpenAI(base_url=base_url, api_key=api_key)


def get_model() -> str:
    return os.environ.get("MODEL", "default-model")
