from model.email import Email
from model.phone import Phone
from model.name import Name


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        for i in self.phones[:]:
            if i.value == phone:
                self.phones.remove(i)

    def edit_phone(self, phone_to_edit: str, new_phone: str):
        for i in self.phones[:]:
            if i.value == phone_to_edit:
                try:
                    self.phones.append(Phone(new_phone))
                except ValueError:
                    return "New phone value is incorrect"
                self.phones.remove(i)
                return "Phone updated"

        return "Phone to edit does not exists for such user"

    def find_phone(self, phone: str):
        for i in self.phones:
            if i.value == phone:
                return i

    def add_birthday(self, birthday: str):
        self.birthday = birthday

    def add_email(self, email):
        try:
            self.email = Email(email)
            return "Email added successfully"
        except ValueError as e:
            return f"Error adding email: {str(e)}"

    def __str__(self) -> str:
        email = self.email.value if self.email else "No email"
        return (f"Contact name: {self.name.value},"
                f" phones: {'; '.join(p.value for p in self.phones)},"
                f" Email: {email},"
                f" Birthday: {self.birthday}")
