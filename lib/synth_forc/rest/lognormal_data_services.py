r"""
A service to retrieve FORC data.
"""
import json

import falcon

from synth_forc.logger import get_logger
from synth_forc.rest.lognormal_data import generate_lognormal_data, LogNormalRequestParameters

from synth_forc.cli.response import Response, DayParameters
from synth_forc.cli.response import WebResponse


class GetLogNormalFORCJsonData:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        logger = get_logger()

        params = LogNormalRequestParameters(req)

        resp.status = generate_lognormal_data(params)

        if resp.status == falcon.HTTP_OK:
            with open(params.forc_output_json_abs_path) as fin:
                resp.content_type = "text/json"

                response_data = Response(json.load(fin))
                response_data.validate()

                web_response_data = WebResponse()
                day_parameters = DayParameters()
                day_parameters.mr = response_data.day_parameters.mr
                day_parameters.ms = response_data.day_parameters.ms
                day_parameters.bc = response_data.day_parameters.bc
                day_parameters.bcr = response_data.day_parameters.bcr
                day_parameters.mrms = response_data.day_parameters.mrms
                day_parameters.bcrbc = response_data.day_parameters.bcrbc
                web_response_data.day_parameters = day_parameters

                resp.body = json.dumps(web_response_data.to_primitive())
        else:
            logger.debug("Some kind of error occurred when attempting to run GetLogNormalFORCData service.")
