import pandas as pd


def convert_txt_to_excel(input_file, output_file):
    try:
        data = pd.read_csv(input_file, sep='|', header=None)

        data.to_excel(output_file, index=False, header=False, engine='openpyxl')
        print(f"Данните са успешно записани в {output_file}")
    except Exception as e:
        print(f"Възникна грешка: {e}")



input_file_name = input('Име на текстовия файл: ')
output_file_name = input('Име на таблицата: ')

input_file = fr"C:\\Users\\User\\Downloads\\{input_file_name}.txt"
output_file = fr"C:\\Users\\User\\Downloads\\{output_file_name}.xls"
convert_txt_to_excel(input_file, output_file)
