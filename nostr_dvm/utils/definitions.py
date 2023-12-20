import os
from dataclasses import dataclass

from nostr_sdk import Event


class EventDefinitions:
    KIND_DM = 4
    KIND_ZAP = 9735
    KIND_ANNOUNCEMENT = 31990
    KIND_NIP94_METADATA = 1063
    KIND_FEEDBACK = 7000
    KIND_NIP90_EXTRACT_TEXT = 5000
    KIND_NIP90_RESULT_EXTRACT_TEXT = KIND_NIP90_EXTRACT_TEXT + 1000
    KIND_NIP90_SUMMARIZE_TEXT = 5001
    KIND_NIP90_RESULT_SUMMARIZE_TEXT = KIND_NIP90_SUMMARIZE_TEXT + 1000
    KIND_NIP90_TRANSLATE_TEXT = 5002
    KIND_NIP90_RESULT_TRANSLATE_TEXT = KIND_NIP90_TRANSLATE_TEXT + 1000
    KIND_NIP90_GENERATE_TEXT = 5050
    KIND_NIP90_RESULT_GENERATE_TEXT = KIND_NIP90_GENERATE_TEXT + 1000
    KIND_NIP90_GENERATE_IMAGE = 5100
    KIND_NIP90_RESULT_GENERATE_IMAGE = KIND_NIP90_GENERATE_IMAGE + 1000
    KIND_NIP90_CONVERT_VIDEO = 5200
    KIND_NIP90_RESULT_CONVERT_VIDEO = KIND_NIP90_CONVERT_VIDEO + 1000
    KIND_NIP90_GENERATE_VIDEO = 5202
    KIND_NIP90_TEXT_TO_SPEECH = 5250
    KIND_NIP90_RESULT_TEXT_TO_SPEECH = KIND_NIP90_TEXT_TO_SPEECH + 1000
    KIND_NIP90_RESULT_GENERATE_VIDEO = KIND_NIP90_GENERATE_VIDEO + 1000
    KIND_NIP90_CONTENT_DISCOVERY = 5300
    KIND_NIP90_RESULT_CONTENT_DISCOVERY = KIND_NIP90_CONTENT_DISCOVERY + 1000
    KIND_NIP90_PEOPLE_DISCOVERY = 5301
    KIND_NIP90_RESULT_PEOPLE_DISCOVERY = KIND_NIP90_PEOPLE_DISCOVERY + 1000
    KIND_NIP90_CONTENT_SEARCH = 5302
    KIND_NIP90_RESULTS_CONTENT_SEARCH = KIND_NIP90_CONTENT_SEARCH + 1000
    KIND_NIP90_GENERIC = 5999
    KIND_NIP90_RESULT_GENERIC = KIND_NIP90_GENERIC + 1000
    ANY_RESULT = [KIND_NIP90_RESULT_EXTRACT_TEXT,
                  KIND_NIP90_RESULT_SUMMARIZE_TEXT,
                  KIND_NIP90_RESULT_TRANSLATE_TEXT,
                  KIND_NIP90_RESULT_GENERATE_TEXT,
                  KIND_NIP90_RESULT_GENERATE_IMAGE,
                  KIND_NIP90_CONTENT_DISCOVERY,
                  KIND_NIP90_PEOPLE_DISCOVERY,
                  KIND_NIP90_RESULT_CONVERT_VIDEO,
                  KIND_NIP90_RESULT_CONTENT_DISCOVERY,
                  KIND_NIP90_RESULT_PEOPLE_DISCOVERY,
                  KIND_NIP90_RESULT_GENERATE_VIDEO,
                  KIND_NIP90_RESULT_GENERIC]


@dataclass
class JobToWatch:
    event: str
    timestamp: int
    is_paid: bool
    amount: int
    status: str
    result: str
    is_processed: bool
    bolt11: str
    payment_hash: str
    expires: int


@dataclass
class RequiredJobToWatch:
    event: Event
    timestamp: int