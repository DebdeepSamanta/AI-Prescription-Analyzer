import pandas as pd
from langchain_core.documents import Document


def load_documents():
    df = pd.read_csv(r"F:\OCR_Prescription_AI\data\Medicine_Details.csv")

    #print(df.columns.tolist())
    df.drop_duplicates()
    df.fillna("Not Available", inplace=True)
    documents=[]

    for _,row in df.iterrows():

        content=f"""
    Medicine Name: {row['Medicine Name']}

    Compostion:
    {
        row['Composition']
    }

    Uses:
    {
        row['Uses']
    }

    Side Effects:
    {
        row["Side_effects"]
    }
    Manufacturer:
    {
        row["Manufacturer"]
    }
    """
        documents.append(
            Document(
                page_content=content,
                metadata={
                    "medicine_name": row["Medicine Name"],
                    "manufacturer": row["Manufacturer"],
                    "excellent_review": row["Excellent Review %"],
                    "average_review": row["Average Review %"],
                    "poor_review": row["Poor Review %"]
                }
            )
        )
    return documents