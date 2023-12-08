# Each line: Calibration value can be found by combining the FIRST and LAST digit (in
# that order) to a single two-digit number.

input_data = open('./data.txt', 'r')
if input_data.closed:
    print('File did not open')
else:
    calibration_value = int()
    while True:
        line = str(input_data.readline())
        if not line:
            break
        digit_lst = []
        for char in line:
            if char.isdigit():
                digit_lst.append(char)
        first_digit = str(digit_lst[0])
        second_digit = str(digit_lst[len(digit_lst) - 1])
        final_digit = str(first_digit + second_digit)
        calibration_value += int(final_digit)
    print("This is the total calibration value: ", calibration_value)
