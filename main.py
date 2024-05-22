import json
import os

# Path to your JSON file
json_file_path = './data/bookmarks-2024-05-22.json'

# Load the JSON data from a file
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create an output directory for markdown files
output_dir = "./out/bookmarks_markdown"
os.makedirs(output_dir, exist_ok=True)

# Function to convert bookmark to markdown
def bookmark_to_markdown(bookmark):
    title = bookmark.get('title', 'No Title')
    dateAdded = bookmark.get('dateAdded', 1716368772991000)
    lastModified = bookmark.get('lastModified', 1716368772991000)
    uri = bookmark.get('uri', 'No URI')
    mz_tags = bookmark.get('tags', [])
    
    markdown_content = f"---\n"
    markdown_content += f"Firefox-Title: {title}\n"
    markdown_content += f"URI: {uri}\n"
    if len(mz_tags) > 0:
        markdown_content += f"tags:\n"
        for tag in mz_tags:
            markdown_content += f"  - {tag}\n"
    markdown_content += f"topics:\n"
    markdown_content += f"  - \"[[Bookmark]]\"\n"
    # Todo: Add functionality for dateAdded / lastModified
    markdown_content += f"---\n\n"
    return markdown_content

# Recursive function to find all bookmarks of type "text/x-moz-place"
def extract_leaf_bookmarks(bookmark):
    if isinstance(bookmark, dict):
        if bookmark.get('type') == 'text/x-moz-place':
            return [bookmark]
        elif 'children' in bookmark:
            bookmarks = []
            for child in bookmark['children']:
                bookmarks.extend(extract_leaf_bookmarks(child))
            return bookmarks
    elif isinstance(bookmark, list):
        bookmarks = []
        for item in bookmark:
            bookmarks.extend(extract_leaf_bookmarks(item))
        return bookmarks
    return []

# Extract the leaf bookmarks
leaf_bookmarks = extract_leaf_bookmarks(data)
ctr = 0

# Parse each bookmark and create a markdown file
for bookmark in leaf_bookmarks:
    title = bookmark.get('title', f'No Title')
    ctr += 1
    # Create a valid filename by replacing spaces with underscores and removing special characters
    filename = ''.join(e for e in title if e.isalnum() or e.isspace()).replace(' ', '_') +"-" + str(ctr) + '.md'
    filepath = os.path.join(output_dir, filename)
    
    markdown_content = bookmark_to_markdown(bookmark)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Markdown file created: {filepath}")

print("All bookmarks have been converted to markdown files.")