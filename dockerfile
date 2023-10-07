FROM python

RUN pip install -U os openai telebot dotenv 

RUN git clone https://github.com/jueves/hackaton_pycones2023.git

WORKDIR /hackaton_pycones2023

COPY *.* /hackaton_pycones2023/

CMD python main.py

