import json
# This script parses the INPUT_DOCUMENT and creates a .json files where each file is a single question with title and content
INPUT_DOCUMENT = "input-data/janka-farmacia-otazky-all.md"
OUTPUT_DIRECTORY = "output-data"
IMPORTANT_SECTION = "Farmakodynamické, farmakokinetické aspekty, terapeutické použitie, NÚ"
NOT_IMPORTANT_SECTION = "Farmakochemické aspekty skupiny, vzťah medzi chem. štruktúrou a účinkom"
ABBREVIATION_MAPPING = {
    "LI": "Liekové interakcie",
    "KI": "Kontraindikácie",
    "MÚ": "Mechanizmus účinku",
    "NÚ": "Nežiadúce účinky"
}

def replace_all_abbrevoations(text: str) -> str:
    known_abbreviations = ABBREVIATION_MAPPING.keys()
    for abbreviaton in known_abbreviations:
        if abbreviaton in text:
            text = text.replace(abbreviaton, ABBREVIATION_MAPPING[abbreviaton])
    return text

class ImportantContent:
    def __init__(self):
        self.title = ""
        self.content = ""


def main():
    document = open(INPUT_DOCUMENT, "r", encoding="utf-8")
    in_important_section = False
    previous_line = ""
    current_important_content: ImportantContent = ImportantContent()
    important_contents: list[ImportantContent] = []
    for line in document:
        #line = line.strip()
        if in_important_section and NOT_IMPORTANT_SECTION in line:
            important_contents.append(current_important_content)
            in_important_section = False
            print(f"Ended section: {current_important_content.title}")
        elif in_important_section:
            line = replace_all_abbrevoations(line)
            current_important_content.content += line
        elif not in_important_section and IMPORTANT_SECTION in line:
            in_important_section = True
            current_important_content = ImportantContent()
            current_important_content.title = previous_line
            line = replace_all_abbrevoations(line)
            current_important_content.content += line
            print(f"Beginning section: {current_important_content.title}")
        previous_line = line
    
    for content in important_contents:
        file_name = content.title.replace("**", "").strip() + ".json"
        with open(f"{OUTPUT_DIRECTORY}/{file_name}", "w", encoding="utf-8") as f:
            json.dump(content.__dict__, f, ensure_ascii=False, indent=4)

    
            



if __name__ == "__main__":
    main()