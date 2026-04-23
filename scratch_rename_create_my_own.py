import os
import glob
import re

# The new "Create ADA GPT" nav block (inactive white style)
ADA_GPT_INACTIVE = """                <!-- Create ADA GPT -->
                <a href="guide.html"
                    class="flex items-center gap-3 bg-white border border-slate-200 hover:bg-slate-50 text-slate-700 px-4 py-3 rounded-xl font-bold shadow-sm transition-all group hover:-translate-y-0.5 mt-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                        stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"
                        class="w-5 h-5 text-violet-600 opacity-90 group-hover:scale-110 transition-transform">
                        <circle cx="12" cy="11" r="3"/><path d="M12 2a9 9 0 1 0 9 9"/><path d="M15 2h6v6"/><path d="M8 17.6A7 7 0 0 0 17.6 8"/>
                    </svg>
                    <span class="text-sm">Create ADA GPT</span>
                </a>"""

# The active version for guide.html
ADA_GPT_ACTIVE = """                <!-- Create ADA GPT (Active) -->
                <a href="guide.html"
                    class="flex items-center gap-3 bg-blue-600 text-white px-4 py-3 rounded-xl font-bold shadow-md shadow-blue-200 transition-all hover:-translate-y-0.5 group mt-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                        stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"
                        class="w-5 h-5 opacity-90 group-hover:scale-110 transition-transform">
                        <circle cx="12" cy="11" r="3"/><path d="M12 2a9 9 0 1 0 9 9"/><path d="M15 2h6v6"/><path d="M8 17.6A7 7 0 0 0 17.6 8"/>
                    </svg>
                    <span class="text-sm">Create ADA GPT</span>
                </a>"""

# Pattern to match the old "Create My Own" block (both active and inactive variants)
# We'll use regex to find and remove it.
CREATE_MY_OWN_PATTERN = re.compile(
    r'\s*<!-- Create My Own.*?-->\s*<a href="guide\.html".*?</a>',
    re.DOTALL
)

# Pattern to match the "Create New Gem" closing </a> to insert after
CREATE_GEM_END_PATTERN = re.compile(
    r'(<!-- Create New Gem.*?</a>)',
    re.DOTALL
)

html_files = glob.glob('/Users/mriley/Documents/Git-Repos/ai-assistant-library/*.html')

for filepath in html_files:
    basename = os.path.basename(filepath)
    with open(filepath, 'r') as f:
        content = f.read()

    # Check if already updated
    if 'Create ADA GPT' in content:
        print(f"Skipping {basename} - already updated")
        continue

    original_content = content

    # Step 1: Remove the old "Create My Own" block
    if '<!-- Create My Own' in content:
        content = CREATE_MY_OWN_PATTERN.sub('', content)
        if content == original_content:
            print(f"WARNING: Could not remove 'Create My Own' from {basename}")
        else:
            print(f"  Removed 'Create My Own' from {basename}")
    else:
        print(f"  No 'Create My Own' found in {basename}")

    # Step 2: Insert the new "Create ADA GPT" block after Create New Gem
    is_guide = basename == 'guide.html'
    new_block = ADA_GPT_ACTIVE if is_guide else ADA_GPT_INACTIVE

    match = CREATE_GEM_END_PATTERN.search(content)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + "\n\n" + new_block + content[insert_pos:]
        print(f"  Inserted 'Create ADA GPT' into {basename}")
    else:
        print(f"WARNING: Could not find 'Create New Gem' block in {basename}")

    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✅ Updated {basename}")
    else:
        print(f"❌ No changes made to {basename}")

print("\nDone!")
