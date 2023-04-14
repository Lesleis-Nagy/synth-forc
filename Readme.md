# Synth FORC

Synth-FORC is a simple yet powerful tool that can generate forward models of synthetic first order reversal curves 
(FORC) using micromagnetic models.

## Installation

### Web service

You can install the `synth-forc` back-end web service using `setup.py` in the usual way. For example, from the directory containing `setup.py`

`$> pip install .

This should pull the required dependencies for the back end along with installing `synth-forc` itself. Once this is done, the service 
runs using [gunicorn](https://gunicorn.org/) - a small script called [start-web-service](https://github.com/Lesleis-Nagy/synth-forc/blob/main/start-web-service) gives an example of how to get the web service started. However its probably best to put this behind a http server such as [apache](https://httpd.apache.org/) or [nginx](https://www.nginx.com/).

In order to run the back end, you will need a database of raw first order reversal curve (FORC) data. This is stored in a [SQLite](https://sqlite.org/index.html) file (available [here](https://zenodo.org/record/7625521) via Zenodo. If you make use of
this data set in your projects/publications we ask you to cite DOI: 10.5281/zenodo.7625521. This data was generated using micromagnetic software
[MERRILL](https://www.rockmag.org).

Finally to run the back end, you will need to create an environment variable called `SYNTH_FORC_WEB_CONFIG` which points to a configuration file. The contents of this file should look like this

```
image-directory: <path to images dir>
sqlite-file: <path to>/synth-forc-data.db
logging:
  file: <path to>/your-log-file.log
  level: debug
  log-to-stdout: false
```

* `image-directory` is a directory that will store FORC images and loops - this is used for caching and if the back end cannot find an image corresponding with the user's input, it will generate a new one in here, and then serve that image.
* `sqlite-file` is the full path to the SQLite data file (available [here](https://zenodo.org/record/7625521)).
* `logging` is optional, however it may be useful for debugging, additional options include:
  * `file` is the location of a file to push logging information to;
  * `level` is the debug level, which should be one of (in decreasing verbosity) `debug`, `info`, `warning`, `error` or `critical`;
  * `log-to-stdout` is a flat to indicate if logging information should also go to `stdout` (this should probably always be `false`).
  
### Front end

Once the web service is running, the front end needs to be deployed. These are the files in the `html` directory. Once deployed the file
`index.js` in the `html/src` directory should be edited to update the location of the back end service. This is located in the
`backend_service_url` function and it just needs to return wherever the back end lives. 

## Notes for developers

When up-versioning the code you will need to change the version in the following files before tagging
* `lib/synth_forc/__init__.py`
* `setup.py`
