# alos2app_pge

This Product Generation Executable (PGE) invokes the `alos2app.py` in ISCE2, which is the work of many including [Professor Cunren Liang](https://scholar.google.com/citations?user=d9VwuYsAAAAJ&hl=en). The tutorial with references for this ISCE2 application can be found [here](https://github.com/isce-framework/isce2/blob/main/examples/input_files/alos2/alos2_tutorial.txt).

This PGE is a major overhaul of the IFG-generator found [here](https://github.com/aria-jpl/ariamh/blob/alos2/interferogram/alos/create_alos2_ifg.py), translating the python scripts into [notebooks](https://jupyter.org/) and orchestrating them with [papermill](https://papermill.readthedocs.io/en/latest/). We have also provided a end-to-end test using sample ALOS-2 data using the [HYSDS](https://github.com/hysds) operational framework.

The original authors of the ALOS-2 PGE are [David Bekaert](https://www.davidbekaert.com/) and [Mohammed Karim](https://github.com/mkarim2017). The current PGE is still a work in progress and important To-Dos can be found at the end of this readme.

The major improvements are:

1. Using papermill to orchestrate Jupyter Notebooks for the PGE
    + This streamlines algorithmic improvements, equating operational behavior to that which is within a jupyter-notebook. An end-user can more easily provide direct feedback to the processing pipeline and/or inspect the process themselves.
    + The notebooks are now the logs and can be used to traceback operational errors.

2. Using xarray to package georeferenced ISCE products into a netcdf.
3. Providing an end-to-end test of the PGE on sample ALOS-2 data.


## Structure of the Repo

### notebooks/

This is where development occurs. The sample data is downloaded to this directory and the PGE is run in this directory. The notebooks here will become those used to run the pipeline. They will be "orchestrated" using `create_alos2_ifg.py`.

### tests/

This is where we copy the relevant data (using file-aliases) and run the papermill script that calls those from the Notebook directory.

### ifg-tools/

This is where we store a few commonly used functions as python files including routines rasterio and a class that reads environment variables according to [HYSDS](https://github.com/hysds) operations.


## Running Locally

Because we use a miniconda docker container, we believe that the operational behavior can be pretty well simulated using `conda`. Here are some rough instructions.

1. `conda env create -f /home/ops/alos2app_pge/environment.yml`
2. `python -m ipykernel install --user`
3. Download ALOS-2 SLC data and modify the `_context.json` as seen in `notebooks/_context.json`.

To run all the notebooks at once use:

```
python <absolute_path_to_repo>/alos2app_pge/create_alos2_ifg.py > create_alos2_ifg.log 2>&1
```

You can remove the redirects to see the output in real time as well.

*Warning*:

+ ALOS-2 Scansar SLCs are massive files; each zip file is almost 60 GB.
+ The runtime of the SLC processing can be upwards of 4 hours.

## Running locally with Jupyter

Go through the notebooks in numerical order.

## Building

To build a suitable image and further validate the PGE, navigate the terminal to this repo and run:

```
docker build -f docker/Dockerfile -t alos2app_img .
```

This ensures that the [context](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#understand-build-context) for the build is correct.

## Testing

See [tests/README.md](tests/readme.md), where we provide some more details of setting up the test.

## To Dos

- Ensuring short-circuiting of the PGE, i.e. if a product exists than throw an exception
- Add Imaging Geometry and Radar Metadata to the NetCDF
- Create Browse PNGs for distribution

## Release History

* v1.0.0
    * Reorganized Repo from [here](https://github.com/aria-jpl/ariamh/blob/alos2/interferogram/alos/create_alos2_ifg.py)
    * Introduced papermill, xarray, and jupyter to pipeline
    * Use miniconda docker image

## Contributing

1. Fork this repo
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Support

Please put issues in `Issues` page in this repo so we can track needed feature requets.

## Acknowledgements

We are deeply grateful to JAXA using the SLC data from ALOS-2/PALSAR-2.


