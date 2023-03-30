from subprocess import Popen, PIPE

from synth_forc import GLOBAL
from synth_forc.logger import get_logger


def generate_single_forc_images(sqlite_file, aspect_ratio, size,
                                major_ticks, minor_ticks,
                                x_limits_from, x_limits_to,
                                y_limits_from, y_limits_to,
                                contour_start, contour_end, contour_step,
                                forc_png_abs_path, forc_pdf_abs_path, forc_jpg_abs_path,
                                forc_loop_png_abs_path, forc_loop_pdf_abs_path, forc_loop_jpg_abs_path,
                                smoothing_factor, log_file=None, log_level="debug"):
    r"""
    Spawn a process and execute the synth-forc-cli tool to generate an image of a single crystal FORC.
    """
    logger = get_logger()

    cmd_array = ["synth-forc-cli", "single",
                 "--input-data-file", sqlite_file,
                 "--aspect-ratio", str(aspect_ratio),
                 "--size", str(size),
                 "--major-ticks", str(major_ticks),
                 "--minor-ticks", str(minor_ticks),
                 "--x-limits-from", str(x_limits_from),
                 "--x-limits-to", str(x_limits_to),
                 "--y-limits-from", str(y_limits_from),
                 "--y-limits-to", str(y_limits_to),
                 "--contour-start", str(contour_start),
                 "--contour-end", str(contour_end),
                 "--contour-step", str(contour_step),
                 "--forc-plot-png", forc_png_abs_path,
                 "--forc-plot-pdf", forc_pdf_abs_path,
                 "--forc-plot-jpg", forc_jpg_abs_path,
                 "--forc-loops-plot-png", forc_loop_png_abs_path,
                 "--forc-loops-plot-pdf", forc_loop_pdf_abs_path,
                 "--forc-loops-plot-jpg", forc_loop_jpg_abs_path,
                 "--smoothing-factor", str(smoothing_factor),
                 "--dpi", str(GLOBAL.DPI),
                 "--json-output"]
    if log_file:
        cmd_array.append("--log-file")
        cmd_array.append(log_file)
        cmd_array.append("--log-level")
        cmd_array.append(log_level)

    proc = Popen(
        cmd_array,
        stdout=PIPE, stderr=PIPE,
        universal_newlines=True
    )

    stdout, stderr = proc.communicate()

    logger.debug(f"stdout: {stdout}")
    logger.debug(f"stderr: {stderr}")

    return stdout, stderr


def generate_lognormal_forc_images(sqlite_file,
                                   arat_shape, arat_loc, arat_scale,
                                   size_shape, size_loc, size_scale,
                                   major_ticks, minor_ticks,
                                   x_limits_from, x_limits_to,
                                   y_limits_from, y_limits_to,
                                   contour_start, contour_end, contour_step,
                                   forc_png_abs_path, forc_pdf_abs_path, forc_jpg_abs_path,
                                   forc_loop_png_abs_path, forc_loop_pdf_abs_path, forc_loop_jpg_abs_path,
                                   smoothing_factor, log_file=None, log_level="debug"):
    r"""
    Spawn a process and execute the synth-forc-cli tool to generate an image of a single crystal FORC.
    """
    logger = get_logger()

    cmd_array = ["synth-forc-cli", "log-normal",
                 "--input-data-file", sqlite_file,
                 "--ar-shape", str(arat_shape),
                 "--ar-location", str(arat_loc),
                 "--ar-scale", str(arat_scale),
                 "--size-shape", str(size_shape),
                 "--size-location", str(size_loc),
                 "--size-scale", str(size_scale),
                 "--major-ticks", str(major_ticks),
                 "--minor-ticks", str(minor_ticks),
                 "--x-limits-from", str(x_limits_from),
                 "--x-limits-to", str(x_limits_to),
                 "--y-limits-from", str(y_limits_from),
                 "--y-limits-to", str(y_limits_to),
                 "--contour-start", str(contour_start),
                 "--contour-end", str(contour_end),
                 "--contour-step", str(contour_step),
                 "--forc-plot-png", forc_png_abs_path,
                 "--forc-plot-pdf", forc_pdf_abs_path,
                 "--forc-plot-jpg", forc_jpg_abs_path,
                 "--forc-loops-plot-png", forc_loop_png_abs_path,
                 "--forc-loops-plot-pdf", forc_loop_pdf_abs_path,
                 "--forc-loops-plot-jpg", forc_loop_jpg_abs_path,
                 "--smoothing-factor", str(smoothing_factor),
                 "--dpi", str(GLOBAL.DPI),
                 "--json-output"]
    if log_file:
        cmd_array.append("--log-file")
        cmd_array.append(log_file)
        cmd_array.append("--log-level")
        cmd_array.append(log_level)

    proc = Popen(
        cmd_array,
        stdout=PIPE, stderr=PIPE,
        universal_newlines=True
    )

    stdout, stderr = proc.communicate()
    logger.debug(f"stdout: {stdout}")
    logger.debug(f"stderr: {stderr}")

    return stdout, stderr
