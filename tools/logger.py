import logging
from colorama import Fore

logger = logging.getLogger("api")
logger.setLevel(logging.INFO)


def log(response, request_body=None):
    #   request
    logger.info(Fore.LIGHTGREEN_EX + f"REQUEST METHOD: {response.request.method}")
    logger.info(Fore.LIGHTGREEN_EX + f"REQUEST URL: {response.url}")
    logger.info(Fore.LIGHTGREEN_EX + f"REQUEST HEADERS: {response.request.headers}")
    logger.info(Fore.LIGHTGREEN_EX + f"REQUEST BODY: {request_body}")
    #   response
    logger.info(Fore.LIGHTYELLOW_EX + f"RESPONSE STATUS CODE: {response.status_code}")
    logger.info(Fore.LIGHTYELLOW_EX + f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000}ms")
    logger.info(Fore.LIGHTYELLOW_EX + f"RESPONSE HEADERS: {response.headers}")
    logger.info(Fore.LIGHTYELLOW_EX + f"RESPONSE BODY: {response.text}")
