# Jupyter OMERO ContentsManager Docker image

Docker image for Jupyter with the [OMERO](https://github.com/manics/fs-omero-pyfs) [ContentsManager](https://github.com/manics/jupyter-pyfilesystem).


## Usage

Run this Docker image with the following environment variables set:
- `OMERO_HOST`
- `OMERO_USER` or `OMERO_SESSION`
- `OMERO_PASSWORD` or `OMERO_SESSION`


## JupyterHub

If you are using JupyterHub with [Jupyter OMERO Authenticator](https://github.com/manics/jupyter-omero-authenticator) you can automatically pass the required environment variables to the spawner.
