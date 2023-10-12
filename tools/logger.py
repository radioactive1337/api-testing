import logging
from colorama import Fore

logger = logging.getLogger("api")
logger.setLevel(logging.INFO)


def log(response, request_body=None):
    #   request
    logger.info(Fore.LIGHTYELLOW_EX + f"REQUEST METHOD: {response.request.method}\n.")
    logger.info(Fore.LIGHTYELLOW_EX + f"REQUEST URL: {response.url}\n.")
    logger.info(Fore.LIGHTYELLOW_EX + f"REQUEST HEADERS: {response.request.headers}\n.")
    logger.info(Fore.LIGHTYELLOW_EX + f"REQUEST BODY: {request_body}\n.")
    #   response
    logger.info(Fore.LIGHTGREEN_EX + f"RESPONSE STATUS CODE: {response.status_code}\n.")
    logger.info(Fore.LIGHTGREEN_EX + f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000}ms\n.")
    logger.info(Fore.LIGHTGREEN_EX + f"RESPONSE HEADERS: {response.headers}\n.")
    logger.info(Fore.LIGHTGREEN_EX + f"RESPONSE BODY: {response.text}\n.")
