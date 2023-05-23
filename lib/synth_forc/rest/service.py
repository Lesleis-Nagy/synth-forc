import falcon

from synth_forc.rest.config import read_config_from_environ
from synth_forc.logger import setup_logger, get_logger

from synth_forc.rest.single_image_services import (
    GetForcPNG,
    GetForcPDF,
    GetForcJPG,
    GetForcLoopPNG,
    GetForcLoopPDF,
    GetForcLoopJPG
)

from synth_forc.rest.lognormal_image_services import (
    GetLogNormalForcPNG,
    GetLogNormalForcPDF,
    GetLogNormalForcJPG,
    GetLogNormalForcLoopsPNG,
    GetLogNormalForcLoopsPDF,
    GetLogNormalForcLoopsJPG
)

from synth_forc.rest.lognormal_data_services import (
    GetLogNormalFORCJsonData
)

from synth_forc.rest.middleware import ConfigurationManager, LoggerManager

config = read_config_from_environ()
setup_logger(config.logging.file, config.logging.level, config.logging.log_to_stdout)
logger = get_logger()

app = falcon.App(
    middleware=[
        ConfigurationManager(config),
        LoggerManager(logger)
    ],
    cors_enable=True
)

####################################################################################################################
# URL Routes                                                                                                       #
####################################################################################################################

forc_png = GetForcPNG()
app.add_route(
    "/forc-png", forc_png
)

forc_pdf = GetForcPDF()
app.add_route(
    "/forc-pdf", forc_pdf
)

forc_jpg = GetForcJPG()
app.add_route(
    "/forc-jpg", forc_jpg
)

forc_loop_png = GetForcLoopPNG()
app.add_route(
    "/forc-loop-png", forc_loop_png
)

forc_loop_pdf = GetForcLoopPDF()
app.add_route(
    "/forc-loop-pdf", forc_loop_pdf
)

forc_loop_jpg = GetForcLoopJPG()
app.add_route(
    "/forc-loop-jpg", forc_loop_jpg
)

lognormal_forc_png = GetLogNormalForcPNG()
app.add_route(
    "/lognormal-forc-png", lognormal_forc_png
)

lognormal_forc_pdf = GetLogNormalForcPDF()
app.add_route(
    "/lognormal-forc-pdf", lognormal_forc_pdf
)

lognormal_forc_jpg = GetLogNormalForcJPG()
app.add_route(
    "/lognormal-forc-jpg", lognormal_forc_jpg
)

lognormal_forc_loops_png = GetLogNormalForcLoopsPNG()
app.add_route(
    "/lognormal-forc-loops-png", lognormal_forc_loops_png
)

lognormal_forc_loops_pdf = GetLogNormalForcLoopsPDF()
app.add_route(
    "/lognormal-forc-loops-pdf", lognormal_forc_loops_pdf
)

lognormal_forc_loops_jpg = GetLogNormalForcLoopsJPG()
app.add_route(
    "/lognormal-forc-loops-jpg", lognormal_forc_loops_jpg
)

lognormal_forc_json_data = GetLogNormalFORCJsonData()
app.add_route(
    "/lognormal-forc-json-data", lognormal_forc_json_data
)
