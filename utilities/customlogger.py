import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".Logs/automation.log" ,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S',
                            level=logging.DEBUG)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger