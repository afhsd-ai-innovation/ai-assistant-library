import os
import glob

# Image to insert above the sidebar logo
NEW_IMG = '                <img src="images/logo-ai.png" alt="District AI" class="w-full h-auto rounded-xl mb-3">\n'

html_files = glob.glob('/Users/mriley/Documents/Git-Repos/ai-assistant-library/*.html')

for filepath in html_files:
    basename = os.path.basename(filepath)
    with open(filepath, 'r') as f:
        content = f.read()

    # Skip if already updated
    if 'logo-ai.png' in content:
        print(f"Skipping {basename} - already updated")
        continue

    # Target: the comment just before the sidebar logo link
    target = '<!-- Branding / Logo Area -->'
    if target in content:
        insert_pos = content.find(target)
        content = content[:insert_pos] + NEW_IMG + '                ' + content[insert_pos:]
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✅ Updated {basename}")
    else:
        print(f"❌ Could not find target in {basename}")

print("\nDone!")
