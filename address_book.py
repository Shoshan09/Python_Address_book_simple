import os
import glob

# saves the default dir
path = os.path.abspath(os.curdir)


class Contact:
    def __init__(self, firstname, lastname, telephone):
        self.firstname = firstname
        self.lastname = lastname
        self.telephone = telephone

    def __repr__(self):
        return "[% s, % s, % s]" % (self.firstname, self.lastname, self.telephone)

    def __eq__(self, other):
        return (self.firstname, self.lastname, self.telephone) == (other.firstname, other.lastname, other.telephone)


class AddressBook(Contact):
    def __init__(self, folder):
        # returns to project default directory(easier to work)
        os.chdir(path)
        # if dir exists than opens the dir.if not creates new dir
        if os.path.exists(folder):
            self.folder = os.path.expanduser(folder)
        else:
            os.makedirs(folder)
        os.chdir(folder)

    def add_contact(self, contact):
        name = contact.firstname + " " + contact.lastname + " " + contact.telephone
        file = open(name, "w")
        file.write(contact.firstname + "\n" + contact.lastname + "\n" + contact.telephone)
        file.close()

    def get_contacts(self):
        list_of_contacts = []
        list_of_files = glob.glob('./*')
        # go through all file in TXT files in dir
        for file in list_of_files:
            temp = open(file, "r")
            if os.stat(file).st_size == 0:
                raise AddressBookException("file is empty")

            list_of_info = []
            # put the lines into a list without the \n
            while True:
                try:
                    line = temp.readline().strip('\n')

                    if not line:
                        # add the contact to the contact list
                        contact = Contact(list_of_info[0], list_of_info[1], list_of_info[2])
                        list_of_contacts.append(contact)
                        break
                    list_of_info.append(line)
                #     if the file is not a text file raise exception
                except UnicodeDecodeError:
                    raise AddressBookException("file is not in text format")
        return list_of_contacts

    def find_contact(self, firstname, lastname, telephone):
            contact = Contact(firstname, lastname, telephone)
            list_of_contacts = self.get_contacts()
            for con in list_of_contacts:
                if con == contact:
                    return con
            return "contact not found"


class AddressBookException(Exception):
    pass


if __name__ == '__main__':
    d = AddressBook('ad')
    c = Contact("new", "contract", "085462")
    b = Contact("another", "test", "1234")
    d.add_contact(b)
    d.add_contact(c)
    try:
        print(d.get_contacts())
    except AddressBookException as e:
        print(e)
    try:
        print(d.find_contact('another', 'test', '1234'))
    except AddressBookException as t:
        print(t)
        a = AddressBook('test')
