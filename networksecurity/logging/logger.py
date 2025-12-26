import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path = os.path.join("networksecurity", "logging", LOG_FILE)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger()
