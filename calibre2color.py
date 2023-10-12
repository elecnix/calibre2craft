import json
import sys
import os

# Mapping of Calibre colors to Unicode markers
color_mapping = {
    'red': '🔴',
    'orange': '🟠',
    'black': '⚫',
    'white': '⚪',
    'purple': '🟣',
    'green': '🟢',
    'yellow': '🟡',
    'blue': '🔵'
}

def convert_calibre_to_md(json_file_path):
    # Read the JSON file
    with open(json_file_path, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)

    # Initialize Markdown content
    md_content = "# Highlights\n"

    last_header = [None] * 10  # Initialize last header for each level, assuming no more than 10 levels

    # Iterate through each highlight and append to Markdown content
    for highlight in data['highlights']:
        chapter_info = highlight.get('toc_family_titles', [])

        # Print headers if they've changed
        for i, title in enumerate(chapter_info):
            if title != last_header[i]:
                md_content += f"{'#' * (i + 2)} {title}\n\n"
                last_header[i] = title

        color = highlight.get('style', {}).get('which', 'black')
        unicode_marker = color_mapping.get(color, '⚫')
        text = highlight.get('highlighted_text', '')
        notes = highlight.get('notes', None)

        # Insert bullets for each subsequent line that is not empty
        bullet_text = '\n'.join([line if i == 0 or line.strip() == '' else f" - {line}" for i, line in enumerate(text.split('\n'))])
        
        md_content += f"{unicode_marker} {bullet_text}\n\n"

        # Add notes as a quote if present
        if notes:
            md_content += f"> {notes}\n\n"

    # Write to Markdown file
    name, ext = os.path.splitext(json_file_path)
    md_file_path = f"{name}.md"
    with open(md_file_path, 'w') as f:
        f.write(md_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calibre2color.py <input_json_file>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    convert_calibre_to_md(json_file_path)
