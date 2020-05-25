FROM python
COPY app /app
RUN pip install flask
CMD python3 /app/1.py
