def strip_indents(value, *values):
    if isinstance(value, str):
        return _strip_indents(value)

    # For handling template literal-like behavior
    processed_string = ''.join([curr + (values[i] if i < len(values) else '') for i, curr in enumerate(value)])
    return _strip_indents(processed_string)


def _strip_indents(value: str) -> str:
    return '\n'.join([line.strip() for line in value.split('\n')]).lstrip().rstrip('\r\n')

# Example usage:
# template_strings = ["This is a ", "string.", " And this is ", "another one."]
# print(strip_indents(template_strings, "first part", "second part"))
