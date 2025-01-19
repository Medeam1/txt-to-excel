import pandas as pd


def convert_txt_to_excel(input_file, output_file):
    try:
        # Четене на текстовия файл
        data = pd.read_csv(input_file, sep='|', header=None)

        # Запис на Excel файла с правилния двигател
        data.to_excel(output_file, index=False, header=False, engine='openpyxl')
        print(f"Данните са успешно записани в {output_file}")
    except Exception as e:
        print(f"Възникна грешка: {e}")

# Пример за пътища


input_file_name = input('Име на текстовия файл: ')
output_file_name = input('Име на таблицата: ')

input_file = fr"C:\\Users\\User\\Downloads\\{input_file_name}.txt"
output_file = fr"C:\\Users\\User\\Downloads\\{output_file_name}.xls"
convert_txt_to_excel(input_file, output_file)
