import gradio as gr
from gradio.components import Textbox
from transformers import pipeline

sentiments = pipeline("sentiment-analysis")


def getsentiments(inputText):
    resp = sentiments(inputText)
    label = ""
    score = 0
    if len(resp) > 0:
        dictobj = resp[0]
        label = dictobj["label"]
        score = dictobj["score"]
    return label, score


def main():
    gr.Interface(
        fn=getsentiments,
        inputs=Textbox(label="Case ID", placeholder="Case id"),
        outputs=[Textbox(label="Customer Sentiments"), Textbox(label="Score")],
        title='Sentiment analysis').launch()


if __name__ == '__main__':
    main()
