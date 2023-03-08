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

__version__ = "0.1.0"
__author__ = 'Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe'
__credits__ = 'University of Liverpool, Instituto Mexicano del Petroleo: Mexico, University of Edinburgh, Imperial College London, Scripps Institution of Oceanography (La Jolla)'

class GLOBAL:

    # The global logger name.
    LOGGER_NAME = "synth-forc"

    # The format used for logging.
    LOGGER_FORMAT = "%(asctime)s — %(levelname)s — %(pathname)s:%(funcName)s:%(lineno)d — %(message)s"
