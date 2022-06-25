# This is a sample Python script.
import logging
import os
from logging import Formatter

import random
from logging.handlers import RotatingFileHandler

from Defination import DefinationsEveryting


class LoggerHandler:
    def __init__(self):
        # Press Shift+F10 to execute it or replace it with your code.
        # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

        self.old_factory = None
        self.log_data_format = "%(linenum)d      %(asctime)s           %(message)s"
        self.log_title_format = "%(message)s"
        # self.serial_class_obj = SerialHandler(self.log_serial_data, self.deinit_logger, self.init_logger)
        self.main_logger = None

        self.previousLogRecordFactory = logging.getLogRecordFactory()

    def record_factory_factory(self, context_id):
        def record_factory(*args, **kwargs):
            record = self.old_factory(*args, **kwargs)
            record.linenum = context_id
            return record

        return record_factory

    def add_log_formatter(self, exp_file_handler, log_file_format, setlevel=logging.INFO):
        exp_file_handler.setLevel(setlevel)
        exp_file_handler.setFormatter(Formatter(log_file_format))
        # main_logger.addHandler(console_handler)
        self.main_logger.addHandler(exp_file_handler)

    def init_logger(self):
        self.main_logger = logging.getLogger(__name__)
        self.main_logger.setLevel(logging.INFO)
        # print("pathhhh: ", self.serial_class_obj.pth)
        file_handlerWrite = RotatingFileHandler('{}'.format(DefinationsEveryting.pth), mode='w', maxBytes=512000)
        # file_handlerAppend = RotatingFileHandler('{}'.format(self.pth), mode='a', maxBytes=512000)
        # self.old_factory = logging.getLogRecordFactory()
        self.old_factory = self.previousLogRecordFactory
        # isThisFirstTime = True
        #
        # if isThisFirstTime:
        self.add_log_formatter(file_handlerWrite, self.log_title_format, logging.WARNING)
        logging.getLogger(__name__).warning(
            'Num;        Logging Time;                   MotorFreq;      MotorSpeed;     PWMVal;')
        file_handler_append = RotatingFileHandler('{}'.format(DefinationsEveryting.pth), mode='a', maxBytes=512000)

        self.add_log_formatter(file_handler_append, self.log_data_format, logging.INFO)
        # print("initimmmmmmm",DefinationsEveryting.pth)
        # try:
        #     print("deinit logger:")
        # self.deinit_logger()
        # self.main_logger.handlers.clear()
        # self.main_logger.removeHandler(file_handlerWrite)
        # file_handlerWrite.close()

        # except (OSError, ValueError):
        #     pass
        # finally:
        #     pass
        # file_handlerWrite.release()
        # self.main_logger.removeHandler(file_handlerWrite)
        # logging.shutdown()

        # else:
        #     pass

    def deinit_logger(self):
        # print("deinittttttt")
        handlers = self.main_logger.handlers[:]
        for handler in handlers:
            self.main_logger.removeHandler(handler)
            handler.close()
        handlers.clear()

    # Press the green button in the gutter to run the script.
    def test_logging(self):
        # print("appers")
        for x in range(100):
            mtrFreq = random.randint(4000, 5000)
            mtSod = random.randint(4000, 5000)
            pwm = random.randint(4000, 5000)

            logging.setLogRecordFactory(self.record_factory_factory(x))

            logging.getLogger(__name__).info("    %d;          %d;            %d;" % (mtrFreq, mtSod, pwm))
        try:
            # print("doneeee")
            self.deinit_logger()
        except (OSError, ValueError):
            pass
        finally:
            pass
            # print("shottdown")

    def log_serial_data(self, mtr_freq, mtr_speed, pwm, counters):
        # print("cnttt: ", mtr_freq, mtr_speed, pwm, counters)
        logging.setLogRecordFactory(self.record_factory_factory(counters))
        #
        logging.getLogger(__name__).info("    %d;          %d;            %d;" % (mtr_freq, mtr_speed, pwm))
