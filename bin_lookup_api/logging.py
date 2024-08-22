import sys

from loguru import logger

from .settings import settings

# logger configuration

logger.remove()  # Remove the default logger to avoid duplicate logs

logger.add(
    sink=sys.stderr,
    level=settings.log.level,
    format=settings.log.format,
    colorize=True,
    #serialize=True
)

# Custom log level definitions
logger.level("TRACE", color="<cyan>", icon="🔍")
logger.level("DEBUG", color="<blue>", icon="🐛")
logger.level("INFO", color="<green>", icon="ℹ️")
logger.level("SUCCESS", color="<bold><green>", icon="✅")
logger.level("WARNING", color="<yellow>", icon="⚠️")
logger.level("ERROR", color="<red>", icon="❌")
logger.level("CRITICAL", color="<bold><red>", icon="💥")
#logger.level("FATAL", color="<red>", icon="!!!")
