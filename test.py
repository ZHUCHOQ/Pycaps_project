from pycaps import CapsPipelineBuilder

# The pipeline contains multiples stages to render the final video
pipeline = (
    CapsPipelineBuilder()
    .with_input_video("input.mp4")
    .add_css("css_file.css")
    .build()
)
pipeline.run() # When this is executed, it starts to render the video