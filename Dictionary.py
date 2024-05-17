class Dictionary():
    """
        Deutsch-English Wörterbuch zur Übersetzung von Wörtern
    """

    def __init__(self):
        self.entries = {
            "Apfelkuchen": "apple cake",
            "Apotheke": "pharmacy",
            "April": "april",
            "Arabisch": "arabic",
            "Arbeit": "work",
        }

    def show_instructions(self):
        """
            Zeigt die Anweisungen für die Verwendung des Wörterbuchs an.
        """
        print("Willkommen zum Deutsch-Englisch Wörterbuch!")
        print("Folgende Optionen stehen zur Verfügung:")
        print("- Um die Liste aller Wörter anzuzeigen, geben Sie 'liste' ein.")
        print("- Um ein neues Wort hinzuzufügen, geben Sie 'neues wort' ein.")
        print("- Geben Sie ein Wort ein, um die Übersetzung anzuzeigen.")

    def add_new_word(self):
        """
            Hier definieren wir wie das Hinzufügen einer neuen Übersetzung funktioniert
        """
        german_word = input("Bitte gib das deutsche Wort ein")
        english_word = input("Bitte gib das englische Wort ein")
        self.entries[german_word] = english_word
        print("Das Wort wurde erfolgreich hinzugefügt")

    def find_translation(self, word):
        """
            Hier wird die Suche der jeweiligen Übersetzung definiert
        """
        if word in self.entries:
            print(f"{word} - {self.entries[word]}")
        elif word in self.entries.values():
            german_word = next(key for key, value in self.entries.items() if value == word)
            print(f"{german_word} - {word}")
        else:
            print("Das Wort befindet sich noch nicht im Wörterbuch.")

    def run(self):
        """
            startet das Wörterbuch und ermöglicht die Interaktion mit dem Nutzer
        """
        self.show_instructions()

        while True:

            operation_choice = input("Bitte geben Sie ein was Sie tun möchten: ").lower()

            if operation_choice == "liste":
                print("Liste aller Wörter:")
                for german_word, english_word in self.entries.items():
                    print(f"{german_word} - {english_word}")

            elif operation_choice == "neues wort":
                self.add_new_word()

            else:
                self.find_translation(operation_choice)

            continue_prompt = input("Wenn Sie verlassen wollen, geben sie bitte \"exit\" ein.").lower()
            if continue_prompt == "exit":
                print("Auf Wiedersehen :)")
                break

#Hauptprogramm
if __name__ == "__main__":
    my_dictionary = Dictionary()
    my_dictionary.run()