FROM python:3.8

WORKDIR /Docuscan 

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /Docuscan/

ENTRYPOINT ["python", "-m", "streamlit", "run"]

CMD [ "app.py" ]
