import sqlite3

import pandas as pd

from synth_forc.plotting.log_normal import log_normal_fractions

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
        _, ar_fractions = log_normal_fractions(ar_shape, ar_location, ar_scale, self.aratios)
        _, size_fractions = log_normal_fractions(size_shape, size_location, size_scale, self.sizes)

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

        print(f"tot frac: {tot}")
        return pd.DataFrame(result)
