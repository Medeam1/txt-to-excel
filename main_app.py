import file_format_convertions

while True:
    print("-----What do you want to do?-----")
    print("1. txt_to_excel")
    print("0. exit")

    action = int(input())

    if action == 1:
        input_file_name = input('Name of the .txt file: ')
        output_file_name = input('Name of the table: ')
        delimiter = input('Chose a delimiter: ')
        input_file = fr"C:\\Users\\My-PC\\Downloads\\{input_file_name}.txt"
        output_file = fr"C:\\Users\\My-PC\\Downloads\\{output_file_name}.xlsx"
        file_format_convertions.txt_to_excel(input_file, output_file, delimiter)
    elif action == 0:
        break
    else:
        print("-----Invalid choice-----\n--\n--\n--")