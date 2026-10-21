from pathlib import Path
import gradio as gr
import spaces

BASE_DIR = Path(__file__).resolve().parent
HTML_PATH = BASE_DIR / "index.html"

# Required by the free ZeroGPU runtime; no GPU work is performed by TVStream.
@spaces.GPU
def zero_gpu_runtime_check():
    return "ok"

# The file route is provided by Gradio. Load the original HTML in an iframe so
# its scripts run as a normal document instead of being injected with innerHTML.
with gr.Blocks(title="TVStream") as demo:
    gr.HTML(f"""
    <style>
      html, body, .gradio-container {{ margin:0!important; padding:0!important; }}
      .gradio-container {{ max-width:none!important; }}
      header, footer {{ display:none!important; }}
      #tvstream-frame {{ position:fixed; inset:0; width:100vw; height:100vh; border:0; background:#141414; }}
    </style>
    <iframe id="tvstream-frame" src="/gradio_api/file={HTML_PATH}" title="TVStream"></iframe>
    """)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        allowed_paths=[str(HTML_PATH)],
        css="footer, header { display: none !important; } .gradio-container { padding: 0 !important; max-width: none !important; }",
    )
