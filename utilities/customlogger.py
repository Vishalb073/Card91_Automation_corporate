import logging
import os

class LogGen:
    @staticmethod
    def logger():
        log_dir = "/home/vishal/PycharmProjects/corporate_Automation_Project/Logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file_path = os.path.join(log_dir, "automation.log")
        logging.basicConfig(filename=log_file_path,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S',
                            level=logging.DEBUG)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
