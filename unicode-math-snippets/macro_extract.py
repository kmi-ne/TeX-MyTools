import re
import json

def unicode_to_char(unicode_str):
    return chr(int(unicode_str, 16))

def process_tex_file(file_path):
    pattern = re.compile(
        r'\\UnicodeMathSymbol{"(?P<unicode>[0-9A-F]{5})}'
        r'{\\(?P<macro>[^\s]+)\s*}'
        r'{\\(?P<math_type>[^\s]+)}'
        r'{(?P<explanation>[^}]*)}%'
    )
    
    math_types = {}

    with open(file_path, 'r') as file:
        for line in file:
            match = pattern.match(line)
            if match:
                unicode_num = match.group('unicode')
                macro_name = match.group('macro')
                math_type = match.group('math_type')
                explanation = match.group('explanation')

                char = unicode_to_char(unicode_num)

                snippet = {
                    unicode_num: {
                        "scope": "latex",
                        "prefix": f"/{macro_name}",
                        "body": char,
                        "description": [char, explanation, "\r"],
                    }
                }

                if math_type not in math_types:
                    math_types[math_type] = {}
                
                math_types[math_type].update(snippet)

    for math_type, snippets in math_types.items():
        filename = f"{math_type}.code-snippets"
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(snippets, outfile, indent=4, ensure_ascii=False)
        print(f"Generated {filename}")

# table from https://github.com/latex3/unicode-math/blob/master/unicode-math-table.tex
process_tex_file('unicode-math-table.tex')
