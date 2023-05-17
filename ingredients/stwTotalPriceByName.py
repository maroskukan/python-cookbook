import argparse
import csv
import os
import xml.etree.ElementTree as ET


def parse_xml_invoice(file_path):
    # Parse the XML document
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root


def extract_price_and_name(dataPackItem):
    # Extract price and name from a dataPackItem element
    price_elements = dataPackItem.findall('.//typ:price', {'typ': 'http://www.stormware.cz/schema/version_2/type.xsd'})
    name_elements = dataPackItem.findall('.//inv:text', {'inv': 'http://www.stormware.cz/schema/version_2/invoice.xsd'})

    # Get the price values
    prices = [float(element.text) for element in price_elements]

    # Get the name values
    names = [element.text for element in name_elements]

    return prices, names


def calculate_prices_with_names(root):
    # Initialize the dictionary to store prices with names
    prices_with_names = {}

    # Iterate over each dataPackItem element
    for dataPackItem in root.findall('.//dat:dataPackItem', {'dat': 'http://www.stormware.cz/schema/version_2/data.xsd'}):
        # Extract the prices and names from the dataPackItem element
        prices, names = extract_price_and_name(dataPackItem)

        # Add the prices to the dictionary for each unique name
        for name, price in zip(names, prices):
            if name in prices_with_names:
                prices_with_names[name] += price
            else:
                prices_with_names[name] = price

    return prices_with_names


def export_to_csv(prices_with_names, file_path):
    # Create or overwrite the CSV file
    with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Item', 'Price'])  # Write the header

        # Write each row with item name and price
        for name, price in prices_with_names.items():
            writer.writerow([name, price])


def print_to_screen(prices_with_names):
    for name, price in prices_with_names.items():
        print(f'{name}: {price}')


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Calculate prices with names from an XML invoice.')
    parser.add_argument('-i', '--invoice', required=True, help='Path to the XML invoice file')
    parser.add_argument('-e', '--export', help='Export the resulting dataset to a CSV file')
    parser.add_argument('-p', '--print', action='store_true', help='Print data to screen')
    args = parser.parse_args()

    # Verify if the file exists
    if not os.path.isfile(args.invoice):
        print(f"Error: File '{args.invoice}' does not exist.")
        exit(1)

    # Parse the XML invoice
    root = parse_xml_invoice(args.invoice)

    # Calculate the prices with names
    prices_with_names = calculate_prices_with_names(root)

    # Export to CSV if export argument is provided
    if args.export:
        export_to_csv(prices_with_names, args.export)
        print(f'Data exported to {args.export}.')

    # Print to screen if print argument is provided
    if args.print:
        print_to_screen(prices_with_names)


if __name__ == '__main__':
    main()
