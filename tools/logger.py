import logging

logger = logging.getLogger("api")
logger.setLevel(logging.INFO)


def log(response, request_body=None):
    #   request
    logger.info(f"REQUEST METHOD: {response.request.method}\n")
    logger.info(f"REQUEST URL: {response.url}\n")
    logger.info(f"REQUEST HEADERS: {response.request.headers}\n")
    logger.info(f"REQUEST BODY: {request_body}\n")
    #   response
    logger.info(f"RESPONSE STATUS CODE: {response.status_code}\n")
    logger.info(f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000}ms\n")
    logger.info(f"RESPONSE HEADERS: {response.headers}\n")
    logger.info(f"RESPONSE BODY: {response.text}\n")
