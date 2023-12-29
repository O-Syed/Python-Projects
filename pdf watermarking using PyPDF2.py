import PyPDF2

def add_watermark(input_pdf_path, watermark_pdf_path, output_pdf_path):
    # Open the input PDF file in binary mode
    with open(input_pdf_path, 'rb') as input_file:
        # Create a PDF reader object for the input PDF
        pdf_reader = PyPDF2.PdfReader(input_file)

        # Open the watermark PDF file in binary mode
        with open(watermark_pdf_path, 'rb') as watermark_file:
            # Create a PDF reader object for the watermark PDF
            watermark_reader = PyPDF2.PdfReader(watermark_file)

            # Create a PDF writer object
            pdf_writer = PyPDF2.PdfWriter()

            # Iterate through each page of the input PDF
            for page_num in range(len(pdf_reader.pages)):
                # Get the page from the input PDF
                page = pdf_reader.pages[page_num]

                # Overlay the watermark on the page
                page.merge_page(watermark_reader.pages[0])

                # Add the modified page to the output PDF
                pdf_writer.add_page(page)

            # Write the output PDF to a new file
            with open(output_pdf_path, 'wb') as output_file:
                pdf_writer.write(output_file)

# Example usage
add_watermark('input_file.pdf', 'watermark.pdf', 'output_file.pdf')
