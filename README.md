
PDF to Label Maker-----------------------------------

This project is a PDF to Label Maker script that extracts data from scanned PDF files and creates labels using a simple GUI built with tkinter. The script supports various features, including batch processing, template-based label creation, error logging, and a day/night mode toggle for the GUI.

Features
Extract Data from PDF Files: The script uses PyMuPDF to extract text from PDF files. If the PDF contains scanned images, it uses pytesseract (OCR) to extract text from images.
Create Labels: The script creates labels from the extracted text using the Pillow library. The labels can be customized with dimensions, font size, and color.
Batch Processing: The script allows processing multiple PDF files at once, creating labels for each file.
Template-Based Label Creation: The script uses predefined templates to ensure consistent formatting of labels.
Save Labels in Different Formats: Labels can be saved in different formats like PNG, JPEG, and PDF.
Error Logging to File: All actions and errors are logged to a file (label_maker.log) for better debugging.
Simple GUI with Tkinter: A simple graphical user interface built with tkinter allows users to select PDF files and the directory to save labels. It also includes a day/night mode toggle.
Notifications: The script displays pop-up messages for success and error notifications using messagebox.

Requirements
Python 3.6 or higher

fitz (PyMuPDF)

Pillow

pytesseract

tkinter

logging

Installation
To install the required packages, run the following PowerShell script:

powershell
# Check if Python is already installed
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Output "Python is already installed."
} else {
    # Download and install Python
    $pythonInstallerUrl = "https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe"
    $installerPath = "$env:TEMP\python-installer.exe"
    Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $installerPath
    Start-Process -FilePath $installerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    Remove-Item $installerPath
    Write-Output "Python has been installed."
}

# Ensure pip is up-to-date
python -m pip install --upgrade pip

# Install the required libraries for your script
pip install pymupdf Pillow pytesseract
Usage
Run the script:

sh
python pdf_to_label_maker.py
A GUI window will open. Click on Select PDF Files to choose the PDF files you want to process.

Select the directory where you want to save the labels.

The script will process the selected PDF files and create labels in the specified directory.

Use the Toggle Day/Night Mode button to switch between day and night themes.

Code Overview
Main Script
The main script includes the following functions:

setup_logging(): Sets up logging to log actions and errors to a file.

extract_text_from_pdf(pdf_path): Extracts text from a PDF file using fitz (PyMuPDF). If no text is found, it uses pytesseract to perform OCR on images.

create_label(text, label_path, dimensions=(400, 200), font_size=20): Creates a label with the extracted text using Pillow.

format_label_based_on_existing(directory): Formats the label name based on existing labels in the directory.

process_pdf_files(pdf_paths, directory): Processes multiple PDF files and creates labels for each file.

main(pdf_paths, directory): Main function to process the PDF files and create labels.

select_files(): Opens file dialogs to select PDF files and the directory to save labels.

toggle_theme(): Toggles between day and night themes for the GUI.

Packages Used
os: Provides functions to interact with the operating system.

fitz (PyMuPDF): Used to extract text from PDF files.

Pillow: Python Imaging Library (PIL) fork used to create and manipulate images.

pytesseract: Python wrapper for Google's Tesseract-OCR Engine used for optical character recognition (OCR).

sys: Provides access to system-specific parameters and functions.

argparse: Used for parsing command-line arguments.

logging: Provides a flexible framework for emitting log messages from Python programs.

tkinter: Standard Python interface to the Tk GUI toolkit.

License
This project is licensed under the MIT License

Acknowledgments
PyMuPDF

Pillow

pytesseract

tkinter
