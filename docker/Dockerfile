FROM huggingface/transformers-pytorch-gpu:latest

COPY rubert-base-case/ /model/
COPY BertForSequenceClassification2.pth /model/
COPY data.csv /data/data.csv

RUN mkdir /opt/results
WORKDIR /opt/results

COPY get_prediction.py get_prediction.py

CMD python get_prediction.py /tmp/data/test.tsv > /opt/results/result.tsv
