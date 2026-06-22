# Synth FORC

Synth-FORC is a simple yet powerful tool that can generate forward models of synthetic first order reversal curves 
(FORC) using micromagnetic models.

## Installation

### Web service

You can install the `synth-forc` back-end web service using `setup.py` in the usual way. For example, from the directory containing `setup.py`

`$> pip install .

This should pull the required dependencies for the back end along with installing `synth-forc` itself. Once this is done, the service 
runs using [gunicorn](https://gunicorn.org/) - a small script called [start-web-service](https://github.com/Lesleis-Nagy/synth-forc/blob/main/start-web-service) gives an example of how to get the web service started. However its probably best to put this behind a http server such as [apache](https://httpd.apache.org/) or [nginx](https://www.nginx.com/).

In order to run the back end, you will need a database of raw first order reversal curve (FORC) data. This is stored in a [SQLite](https://sqlite.org/index.html) file (available [here](https://zenodo.org/records/8192251)) via Zenodo. If you make use of
this data set in your projects/publications we ask you to cite DOI: 10.5281/zenodo.8192251 (version 1.0.1). The concept DOI 10.5281/zenodo.7625521 always resolves to the latest version. This data was generated using the micromagnetic software package [MERRILL](https://www.rockmag.org).

> **⚠️ Database schema requirement.** The current code requires the `all_loops` table to contain a
> `SatMag` (saturation magnetisation) column, which is used to compute the Day-plot parameters. The
> Zenodo download linked above (version 1.0.1, record 8192251) includes this column. **Older databases
> — including version 1.0.0 (record 7625521) — instead have a `volume` column** and will fail with
> `no such column: SatMag`. The `volume` column is no longer needed — the code now computes grain
> volume analytically from `size` — so it cannot be aliased to `SatMag` (they are different physical
> quantities). If in doubt, check a database with:
>
> ```
> sqlite3 synth-forc-data.db "SELECT name FROM pragma_table_info('all_loops');"
> ```
>
> If this lists `volume` but not `SatMag`, you have an older database and should download version 1.0.1
> (record 8192251).

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
* `sqlite-file` is the full path to the SQLite data file (available [here](https://zenodo.org/records/8192251)). Note the `SatMag` schema requirement described above.
* `logging` is optional, however it may be useful for debugging, additional options include:
  * `file` is the location of a file to push logging information to;
  * `level` is the debug level, which should be one of (in decreasing verbosity) `debug`, `info`, `warning`, `error` or `critical`;
  * `log-to-stdout` is a flat to indicate if logging information should also go to `stdout` (this should probably always be `false`).
  
### Front end

Once the web service is running, the front end needs to be deployed. These are the files in the `html` directory. Once deployed the file
`index.js` in the `html/src` directory should be edited to update the location of the back end service. This is located in the
`backend_service_url` function and it just needs to return wherever the back end lives.

The back end is a JSON/image API only — it has **no page at `/`**, so visiting the back end's root directly returns `404 Not Found`. That is expected; the actual user interface is the `html` front end, which calls the API from the browser.

#### Running locally (two servers)

The front end and back end are served separately. The browser loads the page from the front-end server, and the JavaScript then calls the back-end API directly, so the two can live on different ports (cross-origin requests are permitted — the back end has CORS enabled).

```bash
# Terminal 1 — the back-end API (binds 0.0.0.0:8888, see start-web-service)
export SYNTH_FORC_WEB_CONFIG=/path/to/your-config.yaml
./start-web-service

# Terminal 2 — the front-end page (any static file server works)
python -m http.server 8000 --directory html
```

Then open <http://localhost:8000/> in a browser.

Note on `backend_service_url()` in `html/src/index.js`: this is evaluated **in the browser**, so it must be an address the browser can reach:

* For the two-server setup above, return the back end's explicit URL, e.g. `"http://localhost:8888"` (the default).
* Do **not** use `"http://0.0.0.0:8888"` here — `0.0.0.0` is a server *bind* address (it tells gunicorn to listen on all interfaces) and is not a valid destination for the browser; it only happens to work on Linux and fails on macOS/Windows.
* If you later serve the page from the back end itself (same origin), return `""` so the API calls become relative URLs that resolve against whatever host/port served the page (this also works unchanged behind a reverse proxy).

For anything beyond local use it is best to put the back end behind an HTTP server such as [apache](https://httpd.apache.org/) or [nginx](https://www.nginx.com/), and serve the `html` directory from there too.

## Notes for developers

When up-versioning the code you will need to change the version in the following files before tagging
* `lib/synth_forc/__init__.py`
* `setup.py`
