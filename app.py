import gradio as gr
from detect_faces import MAX_OUTPUT, check_and_download_model, detect_faces


def process_image(input_image, box_margin):
    if input_image is None:
        return INITIAL_OUTPUTS
    output_images = detect_faces(input_image, box_margin=box_margin)
    output_images = [gr.Image(image, visible=True) for image in output_images]
    output_images += INITIAL_OUTPUTS[: 100 - len(output_images)]
    return output_images


INITIAL_OUTPUTS = [gr.Image(visible=False) for _ in range(MAX_OUTPUT)]
outputs = INITIAL_OUTPUTS.copy()

iface = gr.Interface(
    fn=process_image,
    inputs=[gr.Image(type="filepath"), gr.Slider(0, 40)],
    outputs=outputs,
    allow_flagging="never",
    live=True,
)
check_and_download_model()
iface.launch()
