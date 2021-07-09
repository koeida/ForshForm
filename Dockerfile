FROM python:3.9
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["export", "FLASK_APP=form.py"]
CMD ["flask", "run"]
