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
# File: synthforc_db.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

import sqlite3

import pandas as pd

from synth_forc.plotting.log_normal import log_normal_fractions
from synth_forc.plotting.log_normal import random_fractions_by_height

def records_to_data_frame(rows, index=None):
    return pd.DataFrame({"id": [row[0] for row in rows],
                         "geometry": [row[1] for row in rows],
                         "temperature": [row[2] for row in rows],
                         "aspect_ratio": [row[3] for row in rows],
                         "size": [row[4] for row in rows],
                         "Br": [row[5] for row in rows],
                         "B": [row[6] for row in rows],
                         "M": [row[7] for row in rows],
                         "volume": [row[8] for row in rows]}, index=index)



class SynthForcDB:

    def __init__(self, db_file):
        self.db_file = db_file

        self.sizes = []
        self.aratios = []

        self.validate_db_file()
        self.populate_sizes_and_aratios()

    def validate_db_file(self):
        pass

    def populate_sizes_and_aratios(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Populate sizes.
        cursor.execute(r"""
            select distinct
                size
            from
                all_loops
            order by
                size
        """)
        sizes = cursor.fetchall()
        self.sizes = [row[0] for row in sizes]
        # Populate aspect ratios.
        cursor.execute(r"""
            select distinct
                aspect_ratio
            from
                all_loops
            order by 
                aspect_ratio
        """)
        aratios = cursor.fetchall()
        self.aratios = [row[0] for row in aratios]

        conn.close()

    def single_forc_loops_by_aspect_ratio_and_size(self, aspect_ratio, size):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(r"""
            select
                id, geometry, temperature, aspect_ratio, size, Br, B, M, volume
            from
                all_loops
            where
                aspect_ratio=? and size=?
        """, (aspect_ratio, size))

        forc_loops = cursor.fetchall()

        return records_to_data_frame(forc_loops, None)


    def check_single_forc_loop_by_aspect_ratio_and_size(self, aspect_ratio, size):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(r"""
            select count(1) from all_loops where aspect_ratio=? and size=?
        """, (aspect_ratio, size))
        rows = cursor.fetchall()

        if rows[0][0] == 0:
            return False
        else:
            return True


    def combine_loops(self, ar_shape, ar_location, ar_scale, size_shape, size_location, size_scale):
        lgnrmw_ar = log_normal_fractions(ar_shape, ar_location, ar_scale, self.aratios)
        lgnrmw_size = log_normal_fractions(size_shape, size_location, size_scale, self.sizes)

        ar_fractions = lgnrmw_ar.weights
        size_fractions = lgnrmw_size.weights

        tot = 0.0

        result = None
        for (ar, ar_frac) in ar_fractions:
            for (size, size_frac) in size_fractions:
                df = self.single_forc_loops_by_aspect_ratio_and_size(ar, size)
                frac = ar_frac * size_frac
                if df.shape[0] == 0:
                    print(f"WARNING: a FORC loop for aspect ratio {ar} and size {size} is missing.")
                else:
                    if result is None:
                        result = {"geometry": df["geometry"].tolist(),
                                  "temperature": df["temperature"].tolist(),
                                  "aspect_ratio": df["aspect_ratio"].tolist(),
                                  "size": df["size"].tolist(),
                                  "Br": df["Br"].tolist(),
                                  "B": df["B"].tolist(),
                                  "M": [frac*M for M in df["M"].tolist()],
                                  "volume": df["volume"].tolist()}
                        tot = ar_frac * size_frac
                    else:
                        result["M"] = [M0 + frac*M1 for (M0, M1) in zip(result["M"], df["M"].tolist())]
                        tot += ar_frac * size_frac

        return pd.DataFrame(result)

    def combine_loops_random(self):
        lgnrmw_ar = random_fractions_by_height(self.aratios)
        lgnrmw_size = random_fractions_by_height(self.sizes)

        ar_fractions = lgnrmw_ar.weights
        size_fractions = lgnrmw_size.weights

        tot = 0.0

        result = None
        for (ar, ar_frac) in ar_fractions:
            for (size, size_frac) in size_fractions:
                df = self.single_forc_loops_by_aspect_ratio_and_size(ar, size)
                frac = ar_frac * size_frac
                if df.shape[0] == 0:
                    print(f"WARNING: a FORC loop for aspect ratio {ar} and size {size} is missing.")
                else:
                    if result is None:
                        result = {"geometry": df["geometry"].tolist(),
                                  "temperature": df["temperature"].tolist(),
                                  "aspect_ratio": df["aspect_ratio"].tolist(),
                                  "size": df["size"].tolist(),
                                  "Br": df["Br"].tolist(),
                                  "B": df["B"].tolist(),
                                  "M": [frac*M for M in df["M"].tolist()],
                                  "volume": df["volume"].tolist()}
                        tot = ar_frac * size_frac
                    else:
                        result["M"] = [M0 + frac*M1 for (M0, M1) in zip(result["M"], df["M"].tolist())]
                        tot += ar_frac * size_frac

        return pd.DataFrame(result), ar_fractions, size_fractions
