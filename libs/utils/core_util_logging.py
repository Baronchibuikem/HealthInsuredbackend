#==================
#package imports
#==================
import logging

def log_print(param_message):
    print("|")
    print("=============================")
    print("DEBUG PRINT")
    print("=============================")
    print("|")
    print(param_message)
    print("|")

def make_log(param_log_url,param_err_mode,log_name_label, log_message, file_name,
    file_ext="log", file_mode='w', log_level="error"):
    """
    log an exception

    Args:
        :param log_name_label:
        :param log_message: the Exception object
        :param file_name: name of the log file
        :param file_ext: extension of the log file
        :param file_mode: set if the file should be overwritten or appended if it already exists
        :param log_level: the type of log -exception|message..
    """
    module_wrapper = Py_Logging_Wrapper()
    log_except_dir = param_log_url
    log_output_mode = param_err_mode

    if log_output_mode=="FILE":
        module_wrapper.log_to_file(
            log_name_label,
            log_except_dir,
            file_name,
            file_ext,
            file_mode,
            log_level,
            log_message
        )
    elif log_output_mode=="STDOUT":
        module_wrapper.log_to_stdout(
            log_name_label,
            log_level,
            log_message
        )
    elif log_output_mode=="BOTH":
        module_wrapper.log_to_file(
            log_name_label,
            log_except_dir,
            file_name,
            file_ext,
            file_mode,
            log_level,
            log_message
        )
        module_wrapper.log_to_stdout(
            log_name_label,
            log_level,log_message
        )
    else:
        module_wrapper.log_to_stdout(
            log_name_label,
            log_level,
            log_message
        )

class Py_Logging_Wrapper(object):
    """
    wrapper class for python logging functions
    """
    def __init__(self):
        self.logging_format_str=\
            '+++++++++++++++++++++++++++++++++++++LOG START+++++++++++++++++++++++++++++++++++++\n'+\
            '|\n'+\
            '=====================================================\n'+\
            '========================HEADING=======================\n'+\
            '=======================================================\n'+\
            '|\n'+\
            'log-time=>{asctime} \n'+ \
            '|\n'+\
            'log-file-name=>{name} \n'+ \
            '|\n'+\
            'log-level=>{levelname}\n'+\
            '|\n'+\
            '========================================================\n'+\
            '=====================MESSAGE-(EXC_TEXT)==================\n'+\
            '==========================================================\n'+\
            '|\n'+\
            '{message} \n'+\
            '|\n'+\
            '+++++++++++++++++++++++++++++++++++++LOG END+++++++++++++++++++++++++++++++++++++++'

    def log_to_file(self, log_name, file_dir, file_name, file_ext, log_file_mode, log_level, log_content):
        """
        make a log to a file

        Args:
            :param log_name: the name label for the log
            :param file_dir: directory path to store the log file
            :param file_name: name of the log file
            :param file_ext: extension of the log file
            :param log_file_mode: set if the file should be overwritten or appended if it already exists
            :param log_level: the type of log -exception|message..
            :param log_content: the log content
        """
        # build log file path
        logging_dir = os.path.join(file_dir, file_name + "." + file_ext)
        #get logger instance
        file_logger=logging.getLogger(log_name+"_file_log")
        file_logger.setLevel(logging.DEBUG)
        # create formatter
        log_output_formatter = logging.Formatter(self.logging_format_str,style='{')
        #config file handler
        file_logger_file_handler=logging.FileHandler(logging_dir,log_file_mode)
        file_logger_file_handler.setFormatter(log_output_formatter)
        #add handler to logger
        file_logger.addHandler(file_logger_file_handler)

        #log based on level
        if log_level== "error":
            file_logger.error(log_content)
        else:
            file_logger.error(log_content)

    def log_to_stdout(self, log_name, log_level, log_content):
        """
        make a log to the stdout

        Args
            :param log_name:
            :param log_level:
            :param log_content:
        """
        #get logger
        stdout_logger=logging.getLogger(log_name+"_stdout_log")
        stdout_logger.setLevel(logging.DEBUG)
        # create formatter
        log_output_formatter = logging.Formatter(self.logging_format_str,style='{')
        #config handlers
        stdout_logger_stream_handler=logging.StreamHandler()
        stdout_logger_stream_handler.setFormatter(log_output_formatter)
        #add handlers to logger
        stdout_logger.addHandler(stdout_logger_stream_handler)

        #make log
        if log_level=="error":
            stdout_logger.error(log_content)
        else:
            stdout_logger.error(log_content)