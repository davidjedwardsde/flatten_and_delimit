import pyperclip

def flatten(text: str) -> list[str]:
    # Remove all newline characters
    text = text.split('\r\n')
    return text


def recombine(text: list[str]) -> str:
  return " ".join(f"'{x}'," for x in text)


def main():
    text = pyperclip.paste()
    tokens = flatten(text)
    result = recombine(tokens)
    return pyperclip.copy(result)


if __name__ == "__main__":
    print(main())