import json
import os

NOTES_FILE = "notes.json"

class NoteApp:
    def __init__(self):
        self.notes = {}
        self.load_notes()

    def load_notes(self):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as file:
                self.notes = json.load(file)
        else:
            self.notes = {}

    def save_notes(self):
        with open(NOTES_FILE, "w") as file:
            json.dump(self.notes, file, indent=4)

    def add_note(self, title, content):
        self.notes[title] = content
        self.save_notes()
        print(f"Note '{title}' added.")

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
            return
        for title, content in self.notes.items():
            print(f"\nTitle: {title}\nContent: {content}\n")

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            self.save_notes()
            print(f"Note '{title}' deleted.")
        else:
            print(f"No note found with the title '{title}'.")

def main():
    app = NoteApp()

    while True:
        print("\nNote App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Enter note title: ").strip()
            content = input("Enter note content: ").strip()
            app.add_note(title, content)
        elif choice == "2":
            app.view_notes()
        elif choice == "3":
            title = input("Enter note title to delete: ").strip()
            app.delete_note(title)
        elif choice == "4":
            print("Exiting Note App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
