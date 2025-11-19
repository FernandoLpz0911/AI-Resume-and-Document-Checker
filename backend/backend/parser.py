# requires pip install pypdf python-docx
# pip install PyPDF2

import io
from django.core.files.uploadedfile import UploadedFile
from typing import Optional

import PyPDF2
from docx import Document


def extractText(uploadedFile: UploadedFile) -> Optional[str]:
    """
    Analyzes the file's extension and extracts plain text content.

    Args:
        uploaded_file: The file object received from the Django request (request.FILES).

    Returns:
        The extracted text as a string, or None if extraction fails.
    """
    fileName = uploadedFile.name

    # Read the file content into an in-memory buffer
    fileBytes = uploadedFile.read()

    # Determine file type based on extension (simple check)
    if fileName.lower().endswith('.pdf'):
        
        # attempt to parse the pdf
        print("Attempting to parse PDF...")
        try:
            pdf = io.BytesIO(fileBytes)
            reader = PyPDF2.PdfReader(pdf)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text

        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return None
        
    elif fileName.lower().endswith(('.docx', '.doc')):

        # attempt to parse docx
        print("Attempting to parse DOCX...")
        try:
            document = Document(io.BytesIO(fileBytes))
            text = '\n'.join([paragraph.text for paragraph in document.paragraphs])
            return text

        except Exception as e:
            print(f"Error parsing DOCX: {e}")
            return None
    
    else:
        print(f"Unsupported file type: {fileName}")
        return None