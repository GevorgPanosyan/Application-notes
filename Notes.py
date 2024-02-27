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

