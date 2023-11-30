import logging

logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(funcName)s() %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
)

# Create a FileHandler to log to a file
file_handler = logging.FileHandler("logs.log")
file_handler.setLevel(logging.DEBUG) # Set the desired log level for the file handler

# Create a formatter for the file handler (if you want a different format)
file_formatter = logging.Formatter("%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(funcName)s() %(message)s")
file_handler.setFormatter(file_formatter)

# Add the file handler to the root logger
logging.getLogger().addHandler(file_handler)
