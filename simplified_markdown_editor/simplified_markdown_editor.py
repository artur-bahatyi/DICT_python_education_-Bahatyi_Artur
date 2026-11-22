FORMATTERS = [
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line",
    "line-break",
]


def print_help():
    """Виводить доступні форматувальники та спеціальні команди."""
    print("Available formatters:", " ".join(FORMATTERS))
    print("Special commands: !help !done")


def format_plain():
    text = input("Text: ")
    return text


def format_bold():
    text = input("Text: ")
    return f"**{text}**"


def format_italic():
    text = input("Text: ")
    return f"*{text}*"


def format_inline_code():
    text = input("Text: ")
    return f"`{text}`"


def format_header():
    while True:
        level = int(input("Level: "))
        if 1 <= level <= 6:
            break
        print("The level should be within the range of 1 to 6.")
    text = input("Text: ")
    return f"{'#' * level} {text}\n"


def format_link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def format_new_line():
    return "\n"


def format_list(ordered=False):
    """Формує впорядкований або невпорядкований список."""
    while True:
        num_rows = int(input("Number of rows: "))
        if num_rows > 0:
            break
        print("The number of rows should be greater than zero")

    lines = []
    for i in range(1, num_rows + 1):
        row_text = input(f"Row #{i}: ")
        prefix = f"{i}." if ordered else "-"
        lines.append(f"{prefix} {row_text}\n")

    return "".join(lines)


def apply_formatter(formatter):
    """Застосовує обраний форматувальник та повертає фрагмент Markdown."""
    if formatter == "plain":
        return format_plain()
    if formatter == "bold":
        return format_bold()
    if formatter == "italic":
        return format_italic()
    if formatter == "inline-code":
        return format_inline_code()
    if formatter == "header":
        return format_header()
    if formatter == "link":
        return format_link()
    if formatter in ("new-line", "line-break"):
        return format_new_line()
    if formatter == "ordered-list":
        return format_list(ordered=True)
    if formatter == "unordered-list":
        return format_list(ordered=False)
    return ""


def save_to_file(content, filename="output.md"):
    """Зберігає фінальну Markdown-розмітку у файл (перезаписуючи існуючий)."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    markdown_text = ""

    while True:
        choice = input("Choose a formatter: ")

        if choice == "!done":
            save_to_file(markdown_text)
            break
        elif choice == "!help":
            print_help()
        elif choice in FORMATTERS:
            markdown_text += apply_formatter(choice)
            print(markdown_text)
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()