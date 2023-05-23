from synth_forc import GLOBAL


def decimal_munger(value, dp=GLOBAL.FLOAT_STR_DP):
    r"""
    This function returns a string version of the input but with decimal points replaced with the letter 'p',
    minus symbol replaced with an 'n'.
    """
    if isinstance(value, float):
        str_value = f"{value:.{dp}f}"
        return str_value.replace(".", "p").replace("-", "n").replace("+", "a")
    elif isinstance(value, int):
        str_value = f"{value}"
        return str_value
    elif isinstance(value, str) or isinstance(value, int):
        float_value = float(value)
        str_value = f"{float_value:.{dp}f}"
        return str_value.replace(".", "p").replace("-", "n").replace("+", "a")

    raise ValueError("Input to 'replace_decimal_with_p' must be 'int', 'float' or 'str' that can convert to float.")


def single_forc_file_name(size, aspect_ratio, smoothing_factor, extension, dp=GLOBAL.FLOAT_STR_DP):
    r"""
    Generate a file name for a FORC consisting of a single loop.
    """

    return f"FORCSingle" \
           f"-size-{decimal_munger(size, dp=dp)}" \
           f"-aspect_ratio-{decimal_munger(aspect_ratio, dp=dp)}" \
           f"-smoothing_factor-{smoothing_factor}" \
           f"{extension}"


def single_forc_loop_file_name(size, aspect_ratio, extension, dp=GLOBAL.FLOAT_STR_DP):
    r"""
    Generate a file name for a FORC consisting of a single loop.
    """

    return f"FORCLoopSingle" \
           f"-size-{decimal_munger(size, dp=dp)}" \
           f"-aspect_ratio-{decimal_munger(aspect_ratio, dp=dp)}" \
           f"{extension}"


def lognormal_forc_file_name(arat_shape, arat_loc, arat_scale,
                             size_shape, size_loc, size_scale,
                             smoothing_factor,
                             extension, dp=GLOBAL.FLOAT_STR_DP):
    return f"FORCLogNormalDistribution" \
           f"-arat_shape-{decimal_munger(arat_shape, dp=dp)}" \
           f"-arat_loc-{decimal_munger(arat_loc, dp=dp)}" \
           f"-arat_scale-{decimal_munger(arat_scale, dp=dp)}" \
           f"-size_shape-{decimal_munger(size_shape, dp=dp)}" \
           f"-size_loc-{decimal_munger(size_loc, dp=dp)}" \
           f"-size_scale-{decimal_munger(size_scale, dp=dp)}" \
           f"-smoothing_factor-{smoothing_factor}" \
           f"{extension}"


def lognormal_forc_loop_file_name(arat_shape, arat_loc, arat_scale,
                                  size_shape, size_loc, size_scale,
                                  extension, dp=GLOBAL.FLOAT_STR_DP):
    return f"FORCLoopsLogNormalDistribution" \
           f"-arat_shape-{decimal_munger(arat_shape, dp=dp)}" \
           f"-arat_loc-{decimal_munger(arat_loc, dp=dp)}" \
           f"-arat_scale-{decimal_munger(arat_scale, dp=dp)}" \
           f"-size_shape-{decimal_munger(size_shape, dp=dp)}" \
           f"-size_loc-{decimal_munger(size_loc, dp=dp)}" \
           f"-size_scale-{decimal_munger(size_scale, dp=dp)}" \
           f"{extension}"


def lognormal_forc_output_json_file_name(arat_shape, arat_loc, arat_scale,
                                         size_shape, size_loc, size_scale,
                                         dp=GLOBAL.FLOAT_STR_DP):
    return f"FORCDataLogNormalDistribution" \
           f"-arat_shape-{decimal_munger(arat_shape, dp=dp)}" \
           f"-arat_loc-{decimal_munger(arat_loc, dp=dp)}" \
           f"-arat_scale-{decimal_munger(arat_scale, dp=dp)}" \
           f"-size_shape-{decimal_munger(size_shape, dp=dp)}" \
           f"-size_loc-{decimal_munger(size_loc, dp=dp)}" \
           f"-size_scale-{decimal_munger(size_scale, dp=dp)}" \
           f".json"
