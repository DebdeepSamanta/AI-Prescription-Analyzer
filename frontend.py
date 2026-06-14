from backend import process_prescription
import gradio as gr


def analyze_prescription(image):

    result = process_prescription(image)

    table_data = []

    details = ""

    for med in result:

        table_data.append([
            med["name"],
            med["dosage"],
            med["frequency"],
            med["duration"]
        ])

        details += f"""
## 💊 {med['name']}

{med['details']}

---
"""

    return (
        "Upload Successful ✅",
        table_data,
        details
    )

with gr.Blocks() as demo:

    gr.Markdown("# 🩺 AI Prescription Analyzer")

    with gr.Row():

        image_input = gr.Image(
            type="filepath",
            label="Prescription"
        )

        medicine_df = gr.Dataframe(
            headers=[
                "Medicine",
                "Dosage",
                "Frequency",
                "Duration"
            ],
            label="Extracted Medicines"
        )

    analyze_btn = gr.Button("Analyze")

    status_box = gr.Textbox(
        label="Status"
    )

    details_box = gr.Markdown(
        label="Medicine Details"
    )

    analyze_btn.click(
        fn=analyze_prescription,
        inputs=image_input,
        outputs=[
            status_box,
            medicine_df,
            details_box
        ]
    )

demo.launch()