print()

word = input("Enter a word: ")

while True:
  command = input("\nEnter a command [reverse/pig latin/scramble]: ")

  if command == "reverse":
    print(word[::-1])
  elif command == "pig latin":
    first = word[0].lower()

    if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
      print(word[1:] + word[0] + "ay")
    else:
      print(word + "ay")
  elif command == "scramble":
    print(word[::2] + word[1::2])
  else:
    print("Invalid command.")
