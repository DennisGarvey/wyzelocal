# Wyzecam Proxy
## About
Acts as a proxy between the proprietary communication standard of [wyze](https://wyze.com) cameras and exposes an mjpeg endpoint for you to use in other applications such as [Blue Iris](https://blueirissoftware.com/) and [Home Assistant](https://www.home-assistant.io/)
## Usage
1. Install [Docker](https://docs.docker.com/get-docker/) ([dockerhub repo](.hub.docker.com/r/dennisgarvey/wyzeproxy))
2. Run `docker pull dennisgarvey/wyzeproxy:0.1`
3. Run container with `docker run -p 80:5000 -e WYZE_EMAIL="YOUR EMAIL HERE" -e WYZE_PASSWORD="YOUR WYZE PASSWORD" dennisgarvey/wyzeproxy:0.1`
4. All the cameras associated with the account are exposed at the url `/cam/<index>`, for instance a url might look like `http://192.168.1.2/cam/0`
## Notes
- This currently performs pretty poorly due to it decoding and re-encoding the streams
- I put this together pretty quickly, so it lacks certain features such as audio and RTSP as well as improved performance, which may be added later.
