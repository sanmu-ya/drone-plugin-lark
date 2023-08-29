FROM python:3.8.17-alpine3.18

LABEL maintainer="sanmuya" \
  org.label-schema.name="Drone Lark Notification" \
  org.label-schema.vendor="sanmuya" \
  org.label-schema.schema-version="1.0.0"

WORKDIR /lark
COPY requements.txt /lark/requements.txt

RUN pip install -r requements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY main.py /lark/main.py
COPY plugin.py /lark/plugin.py

ENTRYPOINT ["python", "/lark/main.py"]
