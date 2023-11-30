from myLogger import logging as LOG


def helloLoggerFunction():
    LOG.info("hello info")
    LOG.debug("hello debug")
    LOG.warning("hello warning")
    LOG.error("hello error")
    LOG.critical("hello critical")


helloLoggerFunction()
