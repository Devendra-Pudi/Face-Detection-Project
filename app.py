import gradio as gr
from detect_faces import detect_faces


def process_image(input_image, box_margin):
    if input_image is None:
        return []
    output_images = detect_faces(input_image, box_margin=box_margin)

    return output_images


from_file = gr.Interface(
    fn=process_image,
    inputs=[gr.Image(type="filepath"), gr.Slider(0, 40)],
    outputs=gr.Gallery(height="100%", label="Faces"),
    allow_flagging="never",
    live=True,
)

from_camera = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(sources=["webcam"], streaming=True, type="filepath"),
        gr.Slider(0, 40),
    ],
    outputs=gr.Gallery(height="100%", label="Faces"),
    allow_flagging="never",
    live=True,
)


tabs = gr.TabbedInterface([from_file, from_camera], ["From File", "From Camera"])

tabs.launch()
