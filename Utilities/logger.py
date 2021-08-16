import logging


class Logger:

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s',
                        filename='C:\\Users\\roxyk\\PycharmProjects\\pythonProject3\\Log\\tests_output.log',
                        filemode='a')

    logger = logging.getLogger(__name__)