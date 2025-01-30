
# Alright so this script will take a PDF image that has been scanned and will create labels for it 
# if theres any features you would like me to add please reach out! 


import os
import fitz  # PyMuPDF
from PIL import Image, ImageDraw, ImageFont
import pytesseract
import sys
import argparse
import logging
from tkinter import Tk, Label, Button, filedialog, messagebox, ttk

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='label_maker.log', filemode='w')

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        if not text.strip():  # If no text is found, perform OCR
            images = [page.get_pixmap().tobytes() for page in doc]
            text = " ".join([pytesseract.image_to_string(Image.open(io.BytesIO(img))) for img in images])
        logging.info(f"Extracted text from {pdf_path}")
        return text.strip()
    except Exception as e:
        logging.error(f"Failed to extract text from {pdf_path}: {e}")
        messagebox.showerror("Error", f"Failed to extract text from {pdf_path}")
        sys.exit(1)

def create_label(text, label_path, dimensions=(400, 200), font_size=20):
    try:
        img = Image.new('RGB', dimensions, color='white')
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", font_size)
        d.text((10, 10), text, font=font, fill=(0, 0, 0))
        img.save(label_path)
        logging.info(f"Created label: {label_path}")
        messagebox.showinfo("Success", f"Created label: {label_path}")
    except Exception as e:
        logging.error(f"Failed to create label: {e}")
        messagebox.showerror("Error", f"Failed to create label: {e}")
        sys.exit(1)

def format_label_based_on_existing(directory):
    try:
        label_files = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg', '.pdf'))]
        new_label_name = f'label_{len(label_files) + 1}.png'
        return os.path.join(directory, new_label_name)
    except Exception as e:
        logging.error(f"Failed to format label: {e}")
        messagebox.showerror("Error", f"Failed to format label: {e}")
        sys.exit(1)

def process_pdf_files(pdf_paths, directory):
    for pdf_path in pdf_paths:
        text = extract_text_from_pdf(pdf_path)
        new_label_path = format_label_based_on_existing(directory)
        create_label(text, new_label_path)

def main(pdf_paths, directory):
    process_pdf_files(pdf_paths, directory)
    sys.exit()  # Properly end the script

def select_files():
    pdf_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")])
    if pdf_paths:
        directory = filedialog.askdirectory(title="Select Label Directory")
        if directory:
            main(pdf_paths, directory)

def toggle_theme():
    if root.tk.call("ttk::style", "theme", "use") == "default":
        root.tk.call("ttk::style", "theme", "use", "alt")
        root.configure(bg="black")
        for widget in root.winfo_children():
            widget.configure(bg="black", fg="white")
    else:
        root.tk.call("ttk::style", "theme", "use", "default")
        root.configure(bg="white")
        for widget in root.winfo_children():
            widget.configure(bg="white", fg="black")

if __name__ == "__main__":
    setup_logging()
    
    root = Tk()
    root.title("Label Maker")
    root.geometry("300x200")

    # Set up the style
    style = ttk.Style(root)
    style.theme_use("default")  # Default theme

    Label(root, text="PDF to Label Maker").pack(pady=10)
    Button(root, text="Select PDF Files", command=select_files).pack(pady=5)
    Button(root, text="Toggle Day/Night Mode", command=toggle_theme).pack(pady=5)

    root.mainloop()
