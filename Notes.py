import json
from datetime import datetime

class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self. title = title
        self.body = body
        self.date = date

class NoteApp:
    def __init__(self):
        self.notes = []

    def add_note(self, title, body):
        id = len(self.notes) + 1
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(id, title, body, date)
        self.notes.append(note)
        self.save_notes()

    def save_notes(self): 
        with open ("notes.json", "w") as file:
            data = []
            for note in self.notes:
                note_data = {
                    "id": note.id,
                    "title": note.title,
                    "body": note.body,
                    "date": note.date

                }   
                data.append(note_data)
            json.dump(data, file, indent = 4)

    def read_notes(self):
        with open("notes.json", "r") as file:
            data = json.load(file)
            self.notes = []
            for note_data in data:
                note = Note(
                    note_data["id"],
                    note_data["title"],
                    note_data["body"],
                    note_data["date"]
                )                
                self.notes.append(note)
   def edit_note(self, id, new_title, new_body):
       for note in self.notes:
           if note.id == id:
               note.title = new_title
               note.body = new_body
               note.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
               self.save_notes()
               break

  def delete_note(self, id):
      for note in self.notes:
          if note.id == id:
              self.notes.remove(note)
              self.save_notes()
              break
  def filter_notes_by_date(self, date):
      filtered_notes = []
      for note in self.notes:
          if note.date.split()[0] == date:
              filtered_notes.append(note)
      return filtered_notes

app = NoteApp()

while True:
    command = input("Введите команду: ")

if command == "add":
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    app.add_note(title, body)
    print("Заметка успешно сохранена")

elif command == "read":
    app.read_notes()
    for note in app.notes:
        print(f"ID:{note.id}")
        print(f"Заголовок:{note.title}")
        print(f"Тело:{note.body}")
        print(f"Дата:{note.date}")
        print()

elif command == "edit":
    id = int(input("Введите ID заметки для редактирования: "))
    new_title = input("Введите новый заголовок: ")
    new_body = input("Введите новое тело: ")
    app.edit_note(id, new_title, new_body)
    print("Заметка успешно отредактирована")

elif command == "delete":
    id = int(input("Введите ID заметки для удаления: "))
    app.delete_note(id)
    print("Заметка успешно удалена")

elif command == "filter":
    date = input("Введите дату для фильтрации (ГГГГ-ММ-ДД): ")
    filtered_notes = app.filter_notes_by_date(date)
    for note in filtered_notes:
        print(f"ID:{note.id}"})
        print(f"Заголовок:{note.title}")
        print(f"Тело:{note.body}")
        print(f"Дата:{note.date}")
        print()

elif command == "exit":
    break

else:
    print("Некорректная команда")

  

