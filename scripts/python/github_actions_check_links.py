import re
import os
import sys

def check_links(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split content into lines
    lines = content.splitlines()
    errors = []

    # Check each line for href links, name anchors, and internal links
    for line_number, line in enumerate(lines, start=1):
        # Search for href links
        href_links = re.findall(r'href="#([^"]+)"', line)
        for link in href_links:
            if ' ' in link:
                errors.append(f"Error on line {line_number}: the href link '{link}' contains spaces.")
            if not link.islower():
                errors.append(f"Error on line {line_number}: the href link '{link}' is not in lowercase.")

        # Search for name anchors
        name_anchors = re.findall(r'<a\s+name="([^"]+)"', line)
        for anchor in name_anchors:
            if ' ' in anchor:
                errors.append(f"Error on line {line_number}: the name anchor '{anchor}' contains spaces.")
            if not anchor.islower():
                errors.append(f"Error on line {line_number}: the name anchor '{anchor}' is not in lowercase.")

        # Search for internal links starting with ](# and ending with )
        internal_links = re.findall(r'\]\(#([^)]*)\)', line)
        for internal_link in internal_links:
            if ' ' in internal_link:
                errors.append(f"Error on line {line_number}: the internal link '{internal_link}' contains spaces.")
            if not internal_link.islower():
                errors.append(f"Error on line {line_number}: the internal link '{internal_link}' is not in lowercase.")

    return errors

def main():
    # Build the path to the file at the root of the repository
    file = os.path.join(os.path.dirname(__file__), '../../', 'CppCoreGuidelines.md')
    errors = check_links(file)

    if errors:
        print('\n'.join(errors))
        sys.exit(1)  # Exit with an error code
    else:
        print("No errors found.")
        sys.exit(0)  # Exit successfully

if __name__ == "__main__":
    main()
