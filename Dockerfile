FROM python:3.5
RUN pip install flask requests
WORKDIR /src
ADD *.py /src/
CMD ["python" ,"/src/wchatsrvr4pi.py"]

EXPOSE 8080