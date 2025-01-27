from datetime import datetime, timezone


def getActualTime():
    return datetime.now(timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )  # 2024-01-22T10:00:00Z format
