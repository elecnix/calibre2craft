import json
import sys
from collections import defaultdict

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

    # Initialize a dictionary to group highlights by chapter
    chapter_group = defaultdict(list)

    # Populate chapter_group with highlights
    for highlight in data['highlights']:
        chapter_info = tuple(highlight.get('toc_family_titles', []))
        chapter_group[chapter_info].append(highlight)

    last_header = [None] * 10  # Initialize last header for each level, assuming no more than 10 levels

    # Loop through each grouped chapter and append to Markdown content
    for chapter_info, highlights in chapter_group.items():
        for i, title in enumerate(chapter_info):
            if title != last_header[i]:  # Only print header if it has changed
                md_content += f"{'#' * (i + 2)} {title}\n\n"
                last_header[i] = title  # Update last header for this level

        for highlight in highlights:
            color = highlight.get('style', {}).get('which', 'black')
            unicode_marker = color_mapping.get(color, '⚫')
            text = highlight.get('highlighted_text', '')
            notes = highlight.get('notes', None)

            # Insert bullets for each subsequent line that is not empty
            bullet_text = '\n'.join([line if i == 0 or line.strip() == '' else f" - {line}" for i, line in enumerate(text.split('\n'))])
            
            md_content += f"{unicode_marker} {bullet_text}\n\n"

            # Add note as a quote if present
            if notes:
                md_content += f"> {notes}\n\n"

    # Write to Markdown file
    md_file_path = json_file_path.replace('.json', '.md')
    with open(md_file_path, 'w') as f:
        f.write(md_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calibre2color.py <input_json_file>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    convert_calibre_to_md(json_file_path)
