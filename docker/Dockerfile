FROM continuumio/miniconda3

LABEL description="Alos2App PGE Container"

# Sources
# 1. https://pythonspeed.com/articles/activate-conda-dockerfile/
# 2. https://github.com/aria-jpl/topsApp_pge/blob/develop/docker/Dockerfile

# Build context must be from root of this repository
COPY . /home/ops/alos2app_pge

# Create the environment:
RUN conda env create -f /home/ops/alos2app_pge/environment.yml

# Ensure that environment is activated on startup
RUN echo "conda activate isce2_env && python -m ipykernel install --user" >> ~/.bashrc

# set entrypoint
WORKDIR /home/ops
CMD ["/bin/bash"]