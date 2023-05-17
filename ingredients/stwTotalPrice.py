import argparse
import os
import xml.etree.ElementTree as ET


def parse_xml_invoice(file_path):
    # Parse the XML document
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root


def calculate_total_price(root):
    # Initialize the sum variable
    total_price = 0.0

    # Iterate over each dataPackItem element
    for dataPackItem in root.findall('.//dat:dataPackItem', {'dat': 'http://www.stormware.cz/schema/version_2/data.xsd'}):
        # Find all price elements within each dataPackItem
        price_elements = dataPackItem.findall('.//typ:price', {'typ': 'http://www.stormware.cz/schema/version_2/type.xsd'})

        # Iterate over each price element and add its value to the total
        for price_element in price_elements:
            if price_element.text is not None:
                total_price += float(price_element.text)

    return total_price


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Calculate the sum of prices from an XML invoice.')
    parser.add_argument('-i', '--invoice', required=True, help='Path to the XML invoice file')
    args = parser.parse_args()

    # Verify if the file exists
    if not os.path.isfile(args.invoice):
        print(f"Error: File '{args.invoice}' does not exist.")
        exit(1)

    # Parse the XML invoice
    root = parse_xml_invoice(args.invoice)

    # Calculate the total price
    total_price = calculate_total_price(root)

    # Print the total price
    print(f'Total price: {round(total_price,2)}')


if __name__ == '__main__':
    main()