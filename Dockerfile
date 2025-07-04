FROM ghcr.io/hassio-addons/base-python:latest

RUN apk add --no-cache py3-pip && \
    pip3 install --no-cache-dir pyserial paho-mqtt

COPY rp2040_usb_bridge.py /rp2040_usb_bridge.py
COPY run.sh /run.sh

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
