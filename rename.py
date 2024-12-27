import os
import re

POSTS_DIR = "posts"

if not os.path.exists(POSTS_DIR):
    print(f"Directory '{POSTS_DIR}' does not exist.")
    exit(1)

pattern = re.compile(r"^post_\d{14}_(.+)\.html$")

for filename in os.listdir(POSTS_DIR):
    match = pattern.match(filename)
    if match:
        title = match.group(1)

        new_filename = f"post_{title}.html"
        
        old_path = os.path.join(POSTS_DIR, filename)
        new_path = os.path.join(POSTS_DIR, new_filename)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
        except Exception as e:
            print(f"Error renaming '{filename}': {e}")

print("Renaming complete.")
