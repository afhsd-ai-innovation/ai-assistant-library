import os
import glob

# HTML to insert (Example Use Cases nav link)
NAV_ITEM = """                <!-- Example Use Cases -->
                <a href="use-cases.html"
                    class="flex items-center gap-3 bg-white border border-slate-200 hover:bg-slate-50 text-slate-700 px-4 py-3 rounded-xl font-bold shadow-sm transition-all group hover:-translate-y-0.5">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                        stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"
                        class="w-5 h-5 text-indigo-600 opacity-90 group-hover:scale-110 transition-transform">
                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="m9 11 3 3L22 4"/>
                    </svg>
                    <span class="text-sm">Example Use Cases</span>
                </a>"""

html_files = glob.glob('/Users/mriley/Documents/Git-Repos/ai-assistant-library/*.html')

for filepath in html_files:
    # Skip the page we just created as it already has the link (and is active)
    if filepath.endswith('use-cases.html'):
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    # If already modified, skip
    if "Example Use Cases" in content and 'use-cases.html' in content:
        print(f"Skipping {os.path.basename(filepath)} - already updated")
        continue

    target = '<!-- Custom GPT vs Gem -->'
    if target in content:
        # Find closing </a> of Custom GPT vs Gem link block
        pos = content.find(target)
        end_a_pos = content.find('</a>', pos)
        if end_a_pos != -1:
            insert_pos = end_a_pos + 4
            new_content = content[:insert_pos] + "\n\n" + NAV_ITEM + content[insert_pos:]
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"Warning: Could not find target in {os.path.basename(filepath)}")

print("Done!")
