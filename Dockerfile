FROM python:3.6.4
ENV TERM='xterm-256color'
WORKDIR /src
RUN pip install -U pycodestyle
RUN pip install -U pylint
CMD ["python", "app.py"]
