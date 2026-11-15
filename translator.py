from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Any, Optional

from deep_translator import MyMemoryTranslator


class TranslationError(Exception):
    """Custom exception for translation-related failures."""


@dataclass
class TranslationResult:
    service_name: str
    source_text: str
    translated_text: str
    source_language: str
    target_language: str
    raw_response: Optional[Dict[str, Any]] = None


class BaseTranslator(ABC):

    @property
    @abstractmethod
    def service_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> TranslationResult:
        raise NotImplementedError


class MockTranslator(BaseTranslator):

    @property
    def service_name(self) -> str:
        return "MockTranslator"

    def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> TranslationResult:

        fake_translation = f"[MOCK {source_language}->{target_language}] {text}"

        return TranslationResult(
            service_name=self.service_name,
            source_text=text,
            translated_text=fake_translation,
            source_language=source_language,
            target_language=target_language,
            raw_response={"mock": True},
        )


class DeepLTranslator(BaseTranslator):

    @property
    def service_name(self) -> str:
        return "MyMemoryTranslator_A"

    def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> TranslationResult:

        try:
            language_map = {
                "en": "english",
                "es": "spanish",
                "fr": "french",
                "de": "german",
                "hu": "hungarian"
            }

            source_lang = language_map.get(source_language, source_language)
            target_lang = language_map.get(target_language, target_language)

            translated_text = MyMemoryTranslator(
                source=source_lang,
                target=target_lang
            ).translate(text)

        except Exception as exc:
            raise TranslationError(str(exc))

        return TranslationResult(
            service_name=self.service_name,
            source_text=text,
            translated_text=translated_text,
            source_language=source_language,
            target_language=target_language,
            raw_response={"service": "MyMemory"},
        )


class GoogleCloudTranslator(BaseTranslator):

    @property
    def service_name(self) -> str:
        return "MyMemoryTranslator_B"

    def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> TranslationResult:

        try:
            language_map = {
                "en": "english",
                "es": "spanish",
                "fr": "french",
                "de": "german",
                "hu": "hungarian"
            }

            source_lang = language_map.get(source_language, source_language)
            target_lang = language_map.get(target_language, target_language)

            translated_text = MyMemoryTranslator(
                source=source_lang,
                target=target_lang
            ).translate(text)

        except Exception as exc:
            raise TranslationError(str(exc))

        return TranslationResult(
            service_name=self.service_name,
            source_text=text,
            translated_text=translated_text,
            source_language=source_language,
            target_language=target_language,
            raw_response={"service": "MyMemory"},
        )