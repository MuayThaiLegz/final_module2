# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(output_path, qualifying_loans):
    """Writes the CSV file to the path provided.

    Args:
        output_path (Path): The csv file output.

        header (Tittle row): The first line.

        qualifying_loans (List): List of wliing banks.

    Saves:
        qualifying_loans to csv
     """
    with open(output_path,'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(qualifying_loans)




