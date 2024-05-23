import gradio as gr
import re
from transformers import AutoTokenizer,TextClassificationPipeline
from adapters import AutoAdapterModel

def preprocess(issue):
    issue = re.sub(r'```.*?```', ' ', issue, flags=re.DOTALL)
    issue = re.sub(r'\n', ' ', issue)
    issue = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', issue)
    issue = re.sub(r'\d+', ' ', issue)
    issue = re.sub(r'[^a-zA-Z0-9?\s]', ' ', issue)
    issue = re.sub(r'\s+', ' ', issue)
    return issue

def text_classification(text):
    tokenizer = AutoTokenizer.from_pretrained("FacebookAI/roberta-base", max_length=256, truncation=True, padding="max_length")
    model = AutoAdapterModel.from_pretrained("FacebookAI/roberta-base")
    adapter_react = model.load_adapter("buelfhood/irc-single-adapter", source = "hf",set_active=True)
    classifier = TextClassificationPipeline(model=model, tokenizer=tokenizer, max_length=256, padding="max_length", truncation=True,top_k=None)
    preprocessed_issue = preprocess (text)
    out = classifier(preprocessed_issue)[0]
    label_scores = {result['label']: result['score'] for result in out}
    return label_scores

examples=["This is a question", "This is a bug", "This is an enhancement" ]

io = gr.Interface(fn=text_classification,
                         inputs= gr.Textbox(lines=3, label="Text", placeholder="Enter the text of the issue here:"),
                         outputs="label",
                         title="Issue Report Classification",
                         description="Enter a text of an issue and see whether it is a bug, feature or question?",
                         examples=examples)

io.launch(share=True)
