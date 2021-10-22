FROM python:3.9.7

SHELL ["/bin/bash", "-c"]

RUN useradd --create-home cicd_user
USER cicd_user

ENV HOME /home/cicd_user
ENV PATH $HOME/.local/bin:$PATH
WORKDIR $HOME

COPY pyproject.toml pyproject.toml

RUN pip install poetry --user
RUN poetry install