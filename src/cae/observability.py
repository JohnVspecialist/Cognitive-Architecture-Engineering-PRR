import logging

# Configure a basic logger once
_logger = logging.getLogger("cae_prr")
if not _logger.handlers:
    _logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    _logger.addHandler(handler)

def log_event(event: str, data: dict | None = None) -> None:
    """Structured logging for the unified engine."""
    if data is None:
        data = {}
    _logger.info("%s | %s", event, data)
