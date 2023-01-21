
import re

def redact_sensitive_info(document: str, keywords: list) -> str:
    """
    Redacts sensitive information from a document using a list of keywords
    """
    for keyword in keywords:
        pattern = re.compile(r"\b" + keyword + r"\b")
        document = pattern.sub("[REDACTED]", document)
    return document

document = "This is a document containing sensitive information such as email addresses and phone numbers."
keywords = ["email", "phone", "address"]

redacted_document = redact_sensitive_info(document, keywords)
print(redacted_document)
