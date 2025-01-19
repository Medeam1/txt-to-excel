import pandas as pd
from pandas.errors import ParserError


def txt_to_excel(input_file, output_file, delimiter):
    try:

        with open(input_file, 'r', encoding='utf-8') as file:
            max_cols = max(len(line.split(delimiter)) for line in file)

        data = pd.read_csv(input_file,
                           sep=delimiter,
                           header=None,
                           names=range(max_cols))

        data.to_excel(output_file, index=False, header=False)
        print(f"Data is successfully saved as: {output_file}")


    except Exception as e:
            print(f"Error occurred: {e}")


