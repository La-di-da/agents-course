import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)


async def run(query: str, email: str):
    async for chunk in ResearchManager().run(query, recipient_email=email):
        yield chunk

def set_email(email: str):
    global send_to_email
    send_to_email = email
    return email


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research")
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    email_textbox = gr.Textbox(label="Enter the email address you'd like to send this to")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")
    email = gr.Markdown(label="Email")
    
    run_button.click(fn=run, inputs=[query_textbox, email_textbox], outputs=report)
    query_textbox.submit(fn=run, inputs=[query_textbox, email_textbox], outputs=report)
    email_textbox.submit(fn=set_email, inputs=email_textbox, outputs=email)

ui.launch(inbrowser=True)

