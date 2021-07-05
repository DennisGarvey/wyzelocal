FROM python:3.8
WORKDIR /app
EXPOSE 5000

RUN wget http://ipfs.io/ipfs/QmcDwbZzY2sydYxvfXKXLUMnd1cRAHHrKSMT9Cw2JWrQn9 -P tutk/
RUN unzip tutk/QmcDwbZzY2sydYxvfXKXLUMnd1cRAHHrKSMT9Cw2JWrQn9 -d tutk/
RUN cd tutk/Lib/Linux/x64/ && g++ -fpic -shared -Wl,--whole-archive libAVAPIs.a libIOTCAPIs.a -Wl,--no-whole-archive -o libIOTCAPIs_ALL.so && cp libIOTCAPIs_ALL.so /usr/local/lib/
RUN rm -r tutk

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
COPY server.py .
COPY feed.py .

CMD ["python", "server.py"]