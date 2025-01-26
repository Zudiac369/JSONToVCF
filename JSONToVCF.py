import json

def convert_json_to_vcf(json_file, output_vcf):
    """
    Converts a JSON file with contact information to a VCF file.

    :param json_file: Path to the input JSON file.
    :param output_vcf: Path to save the output VCF file.
    """
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract contacts list
    contacts = data.get('contacts', {}).get('list', [])

    # Prepare VCF content
    vcf_entries = []
    for contact in contacts:
        first_name = contact.get('first_name', '').strip()
        last_name = contact.get('last_name', '').strip()
        phone_number = contact.get('phone_number', '').strip()

        # Construct the N field
        if first_name and last_name:
            n_field = f"{last_name};{first_name};;;"
        elif last_name:
            n_field = f"{last_name};;;;"
        elif first_name:
            n_field = f";{first_name};;;"
        else:
            n_field = ";;;;"

        # Construct the FN field
        fn_field = f"{first_name} {last_name}".strip()

        # Create the VCF entry
        vcf_entry = (
            "BEGIN:VCARD\n"
            "VERSION:2.1\n"
            f"N:{n_field}\n"
            f"FN:{fn_field}\n"
            f"TEL:{phone_number}\n"
            "END:VCARD"
        )
        vcf_entries.append(vcf_entry)

    # Combine all entries into one VCF content
    vcf_content = "\n".join(vcf_entries)

    # Save the VCF file
    with open(output_vcf, 'w', encoding='utf-8') as file:
        file.write(vcf_content)

    print(f"VCF file has been created: {output_vcf}")

# Example usage
json_input_path = "contacts.json"
vcf_output_path = "contacts_output.vcf"
convert_json_to_vcf(json_input_path, vcf_output_path)
