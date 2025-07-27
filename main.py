import os
import fitz #PyMuPDF
import json
import re
def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.splitext(os.path.basename(pdf_path))[0]  # fallback title
    outline = []
    for page_number in range(len(doc)):
        page = doc[page_number]
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" not in b:
                continue
            for line in b["lines"]:
                line_text = " ".join([span["text"] for span in line["spans"]]).strip()
                if not line_text or len(line_text.split()) > 30:
                    continue
                span = line["spans"][0]
                size = span["size"]
                flags = span["flags"]
                if size >= 20:
                    level = "H1"
                    if title == os.path.splitext(os.path.basename(pdf_path))[0]:
                        title = line_text
                elif 16 <= size < 20:
                    level = "H2"
                elif 12 <= size < 16:
                    level = "H3"
                else:
                    continue
                outline.append({
                    "level": level,
                    "text": line_text,
                    "page": page_number + 1
                })
    return {
        "title": title.strip(),
        "outline": outline
    }
def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            json_data = extract_outline_from_pdf(pdf_path)
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(output_dir, output_filename)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)
if __name__ == "__main__":
    main()
