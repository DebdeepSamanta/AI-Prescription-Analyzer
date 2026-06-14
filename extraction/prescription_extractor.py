
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel,Field
from typing import List, Optional

import os

from dotenv import load_dotenv

load_dotenv()


class Medicine(BaseModel):
    name: str
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    duration: Optional[str] = None
    instruction: Optional[str] = None

class Prescription(BaseModel):
    medicines: List[Medicine]

parser=PydanticOutputParser(
    pydantic_object=Prescription
)


llm= HuggingFaceEndpoint(
    repo_id=os.getenv("model_name"),
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=512,
    temperature=0.1
) 

chat_model = ChatHuggingFace(llm=llm)

prompt = ChatPromptTemplate.from_template("""
You are an expert medical prescription reader.

The following text was extracted using OCR and may contain spelling mistakes.

Your tasks:
1. Correct OCR mistakes.
2. Identify medicine names.
3. Infer dosage, frequency, and duration when possible.
4. Return the response in the exact format specified below.

{format_instructions}                                          

OCR Text:
{ocr_text}
""")


chain = (
    prompt.partial(
        format_instructions=parser.get_format_instructions()
    )
    | chat_model
    | parser
)

def extract_prescription(ocr_text):
    prescription = chain.invoke({"ocr_text": ocr_text})

    return prescription 

'''##TEST 

if __name__ == "__main__":

    sample_text = """
    Tab Paracetamol 650mg
    1-1-1
    for 5 days
    """

    result = extract_prescription(sample_text)

    print(result)'''