
class ContactBook:
    def __init__(self):
        self.contact = {}


    def add_contact(self, name, phone, email):
        if name not in self.contact:
            self.contact[name] = {'phone' : phone, 'email' : email}
            print('contact succesfully added')
        else:
            print('contact already exict')

    def view_contact(self):
        for name, info in self.contact.items():
            print('name:', name)
            print('phone:', info['phone'])
            print('email:', info['email'])
            print('_'*50)

    def delete_contact(self, name):
        if name not in self.contact:
            print('contact not found')
        else:
            del self.contact[name]
            print('contact deleted succesfully')

    def update_contact(self, name, phone=None , email=None):
        if name in self.contact:
            if phone:
                self.contact[name]['phone'] = phone
            if email:    
                self.contact[name]['email'] = email
            print('contact updated succesfully')    
        else:
            print('contact not found')                     


if __name__ == "__main__":
    book = ContactBook()
    
    while True:
        print('\n---contact book application---')
        print('1. Add contact')
        print('2. view contacts' )
        print('3. edit contacts')
        print('4. delete contact')
        print('5. Quit')
        user_choice = input('\n please choose an option: ')

        if user_choice == '1':
            name = input('\n enter contact name: ')
            phone = input('enter contact number: ')
            email = input('enter contact email: ')
            book.add_contact(name, phone, email)

        elif user_choice == '2':
            print('\n list of contacts are: ')
            book.view_contact()


        elif user_choice == '3':
            name = input('\n enter the new contact name: ')
            phone = input('enter the new contact number: ')
            email = input('enter the new contact email: ')
            book.update_contact(name, phone or None, email or None)

        elif user_choice == '4':
            name = input('\n Enter name of contact to delete: ')
            book.delete_contact(name)


        elif user_choice == '5':
            print('\n thank you for using our app')
            break
        else:
            ('\n Invalid choice, Please try again')
















