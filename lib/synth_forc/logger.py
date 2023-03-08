# Copyright 2023 L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice, this list of conditions and the
#      following disclaimer.
#
#   2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#      following disclaimer in the documentation and/or other materials provided with the distribution.
#
#   3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
#      products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#
# Project: synth-forc
# File: logger.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

import logging

from synth_forc import GLOBAL

def str_to_log_level(log_level: str):
    r"""
    Retrieve the log level associated with the input.
    :param log_level: the log level we want.
    :return: a log level.
    """
    if log_level.upper() == "CRITICAL":
        return logging.CRITICAL
    elif log_level.upper() == "ERROR":
        return logging.ERROR
    elif log_level.upper() == "WARNING":
        return logging.WARNING
    elif log_level.upper() == "WARN":
        return logging.WARN
    elif log_level.upper() == "INFO":
        return logging.INFO
    elif log_level.upper() == "DEBUG":
        return logging.DEBUG
    else:
        raise ValueError(f"Unknown log level '{log_level}'.")


def setup_logger(log_file: str = None, log_level: str = None, log_to_stdout=False):
    r"""
    :param log_file: the name of a file to write logging data to.
    :param log_level: the level at which to perform logging.
    :param log_to_stdout: boolean flag, if true logging information is displayed on standard output.
    :return:
    """

    # Set up logging
    if log_level is None:
        log_level = "ERROR"
    logger = logging.getLogger(GLOBAL.LOGGER_NAME)
    logger.setLevel(str_to_log_level(log_level))

    if log_file is not None:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(str_to_log_level(log_level))
        file_formatter = logging.Formatter(GLOBAL.LOGGER_FORMAT)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    if log_to_stdout:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(str_to_log_level(log_level))
        stream_formatter = logging.Formatter(GLOBAL.LOGGER_FORMAT)
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)


def get_logger():
    r"""
    Retrieve the global application logger.
    :return: the global application logger.
    """
    logger = logging.getLogger(GLOBAL.LOGGER_NAME)
    return logger
