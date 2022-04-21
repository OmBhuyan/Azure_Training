FROM continuumio/miniconda3 AS builder

COPY env.yml .

RUN conda env create -f env.yml

RUN conda install -c conda-forge conda-pack

RUN conda-pack -n env -o /tmp/env.tar && \
    mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
    rm /tmp/env.tar

RUN /venv/bin/conda-unpack


FROM python:3.8-slim-buster

COPY --from=builder /venv /venv

COPY . .

SHELL ["/bin/bash", "-c"]

EXPOSE 5000

ENTRYPOINT source /venv/bin/activate && flask run -h 0.0.0.0