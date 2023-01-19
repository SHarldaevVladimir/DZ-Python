import func

func.cls()
fileName = 'Phonebook.txt'

while True:
    func.main_menu()
    user_choice = int(input('Выберете необходимый пункт меню: '))
    if user_choice == 1:
        func.readFile(fileName)
    if user_choice == 2:
        func.findContactByKeyWord(fileName)
    if user_choice == 3:
        func.writeFile(fileName)
    if user_choice == 4:
        func.DeleteContact(fileName)
    if user_choice == 5:
        func.ReplaceData(fileName)
    if user_choice == 0:
        print('Пока!')
        break
