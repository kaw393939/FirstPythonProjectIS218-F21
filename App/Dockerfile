FROM python:3.9-alpine
RUN pip install --upgrade pip
RUN adduser -D myuser
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
#ENV FLASK_ENV=development
RUN apk add --no-cache gcc musl-dev linux-headers
USER myuser
WORKDIR /home/myuser
COPY --chown=myuser:myuser requirements.txt requirements.txt
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
USER myuser
RUN pip install --user -r requirements.txt
#If you uncomment the line below you can run the test and lint when the container is built.
#You can open a terminal to run the tests manually
#RUN pytest --pylint --pylint-rcfile=tests/.pylintrc
# uncommment to run the command to start uWSGI, you can't run tests and start the server.
CMD ["uwsgi", "app.ini"]