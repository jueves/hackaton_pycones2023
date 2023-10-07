FROM python

RUN pip install -upgrade pyTelegramBotAPI openai

WORKDIR /hackaton_pycones2023

COPY *.* /hackaton_pycones2023/

CMD python main.py
