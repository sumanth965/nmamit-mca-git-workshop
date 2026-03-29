"""
Utility functions for the student directory app.
"""

from datetime import datetime


def get_timestamp() -> str:
    """Return the current timestamp as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_name(first: str, last: str) -> str:
    """Format a full name from first and last name."""
    return f"{first.strip().title()} {last.strip().title()}"


def validate_email(email: str) -> bool:
    """Basic email validation."""
    return "@" in email and "." in email.split("@")[-1]
