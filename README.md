# JSON to VCF Converter

A simple and practical Python script to convert JSON files containing contact information into VCF (vCard) files. VCF files are a standard format for storing contact information and can be easily imported into devices like smartphones.

This tool is particularly useful for converting **Telegram contact exports** (in JSON format) into VCF files, making it easy to transfer contacts to your phone or contact management software. It fully supports **Persian characters** (UTF-8 encoding) for names and phone numbers.

---

## Features
- Converts Telegram JSON contact exports to VCF format.
- Supports **Persian and arabic characters** (Farsi and arabic names and phone numbers).
- Simple and easy to use.
- Works on any system with Python installed.

---

## How to Use

### Prerequisites
- Python 3.x
- `json` module (included in Python by default)

### Running the Script
1. Open the `JSONToVCF.py` file and specify the input JSON file path and output VCF file path:
   ```python
   json_input_path = "contacts.json"  # Path to the input JSON file
   vcf_output_path = "contacts_output.vcf"  # The name of output VCF file
2.Run the Script:
Execute the script using the following command in your terminal or command prompt:
python JSONToVCF.py

