#hi
encoded_password = 0
def decode():
    decoded = " "
    for num in encoded_password:
        num = (str(num-3) % 10)
        decoded += num
        print("test")
    return decoded

