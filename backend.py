import easyocr  

from extraction.prescription_extractor import extract_prescription
from retrieval.retriever import get_medicine_info

reader= easyocr.Reader(['en'])

def process_prescription(image_path):
    result= reader.readtext(image_path)

    ocr_text= "\n".join([item[1] for item in result])

    prescription=extract_prescription(
        ocr_text
    )
    output=[]
    for medicine in prescription.medicines:
        docs=get_medicine_info(
            medicine.name
        )
        output.append({
            "name": medicine.name,
            "dosage": medicine.dosage,
            "frequency": medicine.frequency,
            "duration": medicine.duration,
            "details": docs.page_content
        })
    return output