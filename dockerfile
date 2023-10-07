FROM python

RUN pip install pyTelegramBotAPI openai

WORKDIR /hackaton_pycones2023

COPY *.* /hackaton_pycones2023/

CMD python main.py

