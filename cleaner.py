import re

def parse_script(script_file):
    conversations = []

    with open(script_file, "r") as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith("Patient"):
                patient_message = lines[i].strip().split("–")[1].strip()
                doctor_message = lines[i + 1].strip().split("–")[1].strip()
                conversations.append((patient_message, doctor_message))
                i += 2
            else:
                i += 1

    return conversations

if __name__ == "__main__":
    print(parse_script("script.txt"))