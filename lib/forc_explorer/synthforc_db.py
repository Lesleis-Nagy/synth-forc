import sqlite3

import pandas as pd

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

        return pd.DataFrame({"id":           [row[0] for row in forc_loops],
                             "geometry":     [row[1] for row in forc_loops],
                             "temperature":  [row[2] for row in forc_loops],
                             "aspect_ratio": [row[3] for row in forc_loops],
                             "size":         [row[4] for row in forc_loops],
                             "Br":           [row[5] for row in forc_loops],
                             "B":            [row[6] for row in forc_loops],
                             "M":            [row[7] for row in forc_loops],
                             "volume":       [row[8] for row in forc_loops]}, index=None)

