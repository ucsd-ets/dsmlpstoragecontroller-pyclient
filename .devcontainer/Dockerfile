# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.238.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

COPY ./src/dsmlpstoragecontrollerclient/ /app/src/dsmlpstoragecontrollerclient
COPY ./pyproject.toml /app/
COPY ./setup.py /app/
COPY ./requirements.txt /app/
COPY ./README.md /app/

ARG TMP_PROTOS_PATH="/tmp/protos"
COPY dsmlpstoragecontrollerservice.proto ${TMP_PROTOS_PATH}/src/
COPY .devcontainer/containerutils/ ${TMP_PROTOS_PATH}/containerutils/

WORKDIR "${TMP_PROTOS_PATH}/build/"
RUN python3 -m grpc_tools.protoc \
-I../src \
--python_out=. \
--grpc_python_out=. ../src/dsmlpstoragecontrollerservice.proto

WORKDIR "${TMP_PROTOS_PATH}/build/"
RUN chmod +x ./dsmlpstoragecontrollerservice_pb2.py

WORKDIR "${TMP_PROTOS_PATH}/build/"
RUN python3 -m black ./dsmlpstoragecontrollerservice_pb2.py

WORKDIR "${TMP_PROTOS_PATH}/build/"
RUN chmod +x ./dsmlpstoragecontrollerservice_pb2_grpc.py

WORKDIR "${TMP_PROTOS_PATH}/build/"
RUN python3 -m black ./dsmlpstoragecontrollerservice_pb2_grpc.py

WORKDIR "${TMP_PROTOS_PATH}/containerutils/"
RUN python3 -m rewrite_pb2_grpc_import --pb2_grpc_path=${TMP_PROTOS_PATH}/build/dsmlpstoragecontrollerservice_pb2_grpc.py

RUN mv ${TMP_PROTOS_PATH}/build/dsmlpstoragecontrollerservice_pb2.py /app/src/dsmlpstoragecontrollerclient/
RUN mv ${TMP_PROTOS_PATH}/build/dsmlpstoragecontrollerservice_pb2_grpc.py /app/src/dsmlpstoragecontrollerclient/

WORKDIR "/"
RUN rm -rf ${TMP_PROTOS_PATH}