from synth_forc import GLOBAL


def decimal_munger(value):
    r"""
    This function returns a string version of the input but with decimal points replaced with the letter 'p',
    minus symbol replaced with an 'n'.
    """
    if isinstance(value, float):
        str_value = f"{value:.{GLOBAL.FLOAT_STR_DP}f}"
        return str_value.replace(".", "p").replace("-", "n")
    elif isinstance(value, str) or isinstance(value, int):
        float_value = float(value)
        str_value = f"{float_value:.{GLOBAL.FLOAT_STR_DP}f}"
        return str_value.replace(".", "p").replace("-", "n")

    raise ValueError("Input to 'replace_decimal_with_p' must be 'int', 'float' or 'str' that can convert to float.")


def single_forc_file_name(size: str, aspect_ratio: str, smoothing_factor: int, extension: str):
    r"""
    Generate a file name for a FORC consisting of a single loop.
    """

    return f"FORCSingle" \
           f"-size-{decimal_munger(size)}" \
           f"-aspect_ratio-{decimal_munger(aspect_ratio)}" \
           f"-smoothing_factor-{smoothing_factor}" \
           f"{extension}"


def single_forc_loop_file_name(size: str, aspect_ratio: str, extension: str):
    r"""
    Generate a file name for a FORC consisting of a single loop.
    """

    return f"FORCLoopSingle" \
           f"-size-{decimal_munger(size)}" \
           f"-aspect_ratio-{decimal_munger(aspect_ratio)}" \
           f"{extension}"


def lognormal_forc_file_name(arat_shape: str, arat_loc: str, arat_scale: str,
                             size_shape: str, size_loc: str, size_scale: str,
                             smoothing_factor: int,
                             extension: str):
    return f"FORCDistribution" \
           f"-arat_shape-{decimal_munger(arat_shape)}" \
           f"-arat_loc-{decimal_munger(arat_loc)}" \
           f"-arat_scale-{decimal_munger(arat_scale)}" \
           f"-size_shape-{decimal_munger(size_shape)}" \
           f"-size_loc-{decimal_munger(size_loc)}" \
           f"-size_scale-{decimal_munger(size_scale)}" \
           f"-smoothing_factor-{smoothing_factor}" \
           f"{extension}"


def lognormal_forc_loop_file_name(arat_shape: str, arat_loc: str, arat_scale: str,
                                  size_shape: str, size_loc: str, size_scale: str,
                                  extension: str):
    return f"FORCLoopsDistribution" \
           f"-arat_shape-{decimal_munger(arat_shape)}" \
           f"-arat_loc-{decimal_munger(arat_loc)}" \
           f"-arat_scale-{decimal_munger(arat_scale)}" \
           f"-size_shape-{decimal_munger(size_shape)}" \
           f"-size_loc-{decimal_munger(size_loc)}" \
           f"-size_scale-{decimal_munger(size_scale)}" \
           f"{extension}"
