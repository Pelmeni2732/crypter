def encrypt(text, key):
  offset = sum([ord(c) for c in key]) % 128
  
  encrypted_text = ""
  for c in text:
    encrypted_text += chr(ord(c) + offset)

  return encrypted_text

def decrypt(text, key):
  offset = sum([ord(c) for c in key]) % 128
  
  decrypted_text = ""
  for c in text:
    decrypted_text += chr(ord(c) - offset)

  return decrypted_text

def main():
  selection = input("Выберите операцию: 1 - Зашифровать, 2 - Расшифровать ")
  if selection == "1":
    encryption_type = input("Выберите тип шифрования: 1 - Символ, 2 - Группа, 3 - Слово ")
    if encryption_type != "1" and encryption_type != "2" and encryption_type != "3":
      print("Неверный ввод")

      return
    
    stride = 1
    if encryption_type == "2":
      stride = int(input("Введите количество символов в группе: "))
    elif encryption_type == "3":
      stride = " "
    
    msg = input("Введите сообщение: ")
    key = input("Введите ключ: ")

    encrypted_msg = ""

    chunks = []
    if stride == " ":
      chunks = msg.split(" ")
    else:
      chunks = [msg[i:i + stride] for i in range(0, len(msg), stride)]

    for chunk in chunks:
      encrypted_msg += encrypt(chunk, key)

    print()
    print()

    print("Зашифрованное сообщение:")
    print(encrypted_msg)
  elif selection == "2":
    encryption_type = input("Выберите тип шифрования: 1 - Символ, 2 - Группа, 3 - Слово ")
    if encryption_type != "1" and encryption_type != "2" and encryption_type != "3":
      print("Неверный ввод")

      return
    
    stride = 1
    if encryption_type == "2":
      stride = int(input("Введите количество символов в группе: "))
    elif encryption_type == "3":
      stride = " "

    msg = input("Введите зашифрованное сообщение: ")
    key = input("Введите ключ: ")

    decrypted_msg = ""

    chunks = []
    if stride == " ":
      chunks = msg.split(" ")
    else:
      chunks = [msg[i:i + stride] for i in range(0, len(msg), stride)]

    for chunk in chunks:
      decrypted_msg += decrypt(chunk, key)

    print()
    print()

    print("Расшифрованное сообщение:")
    print(decrypted_msg)
  else:
    print("Неизвестная команда")

main()
