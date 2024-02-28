def process_data(data_type, value):
    if data_type == "int":
        print(int(value) * 2)
    elif data_type == "real":
        print(f"{float(value) * 1.5:.2f}")
    elif data_type == "string":
        print("$" + value + "$")


data_type = input()
value = input()

process_data(data_type, value)