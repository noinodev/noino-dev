#!/usr/bin/env python3

import re
import shutil
from datetime import datetime,date
from pathlib import Path
import frontmatter
import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension

# ── CONFIG ────────────────────────────────────────────────────────────────────

SITE_NAME    = "noino technical blog"
#SITE_TAGLINE = "graphics & rendering"

CONTENT_TREES = [
    {
        "name":       "posts",
        "source":     "posts",       # relative to ROOT
        "web":        "posts",       # relative to WEB
        "back_label": "all posts",
        "back_href":  "/",
    },
    {
        "name":       "projects",
        "source":     "projects",
        "web":        "projects",
        "back_label": "projects",
        "back_href":  "/projects/",
    },
]

# ── PATHS ─────────────────────────────────────────────────────────────────────

ROOT     = Path(__file__).parent
WEB      = ROOT / "web"
TEMPLATE = ROOT / "template.html"

# ── HELPERS ───────────────────────────────────────────────────────────────────

def load_template():
    return TEMPLATE.read_text()

def render(template, replacements):
    out = template
    for k, v in replacements.items():
        out = out.replace("{{" + k + "}}", v)
    return out

def parse_date(date_val):
    if isinstance(date_val, datetime):
        return date_val
    if isinstance(date_val, date):
        return datetime(date_val.year, date_val.month, date_val.day)
    if isinstance(date_val, str):
        for fmt in ("%Y-%m-%d", "%d %B %Y", "%B %d, %Y"):
            try:
                return datetime.strptime(date_val, fmt)
            except ValueError:
                continue
    return datetime.today()

def make_slug(title):
    s = title.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    return s.strip('-')

def md_to_html(text):
    return markdown.markdown(text, extensions=[
        FencedCodeExtension(),
        TableExtension(),
        'markdown.extensions.smarty',
        'markdown.extensions.extra',
    ])

def date_display(dt):
    return dt.strftime("%-d %B %Y")

def date_machine(dt):
    return dt.strftime("%Y-%m-%d")

def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)

# ── ASSETS ────────────────────────────────────────────────────────────────────

def sync_assets():
    src = ROOT / "assets"
    dst = WEB / "assets"
    if not src.exists():
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"  ✓ assets/")

# ── CONTENT TREES ─────────────────────────────────────────────────────────────

def load_tree(tree):
    src = ROOT / tree["source"]
    if not src.exists():
        return []
    items = []
    for f in sorted(src.glob("*.md")):
        post  = frontmatter.load(f)
        date  = parse_date(post.get("date", ""))
        title = post.get("title", f.stem)
        items.append({
            "slug":        post.get("slug", make_slug(title)),
            "title":       title,
            "date":        date,
            "tags":        post.get("tags", []),
            "description": post.get("description", ""),
            "thumbnail":   post.get("thumbnail", ""),
            "body_html":   md_to_html(post.content),
        })
    items.sort(key=lambda p: p["date"], reverse=True)
    return items

def clean_tree(items, web_dir):
    if not web_dir.exists():
        return
    valid = {p["slug"] for p in items}
    for entry in web_dir.iterdir():
        if entry.is_dir() and entry.name not in valid:
            shutil.rmtree(entry)
            print(f"  ✗ removed {web_dir.name}/{entry.name}/")

def generate_tree(items, tree, template):
    web_dir    = WEB / tree["web"]
    back_label = tree["back_label"]
    back_href  = tree["back_href"]

    for item in items:
        tags_html  = " ".join(f'<span class="post-tag">{t}</span>' for t in item["tags"])
        thumb_html = f'<img src="{item["thumbnail"]}" alt="{item["title"]}" style="width:100%;border-radius:3px;margin-bottom:2rem">' if item["thumbnail"] else ""

        content = f"""
<a href="{back_href}" class="back-link">{back_label}</a>
<article>
  <header class="post-header">
    <time datetime="{date_machine(item['date'])}">{date_display(item['date'])}</time>
    <h1>{item['title']}</h1>
    {f'<div class="post-tags" style="margin-top:0.75rem">{tags_html}</div>' if tags_html else ''}
  </header>
  {thumb_html}
  <div class="post-body">
    {item['body_html']}
  </div>
</article>
<div class="post-footer">
  <a href="{back_href}">← {back_label}</a>
  <span style="font-size:0.75rem;color:var(--text-dimmer)">{date_display(item['date'])}</span>
</div>
"""
        html = render(template, {
            "TITLE":       item["title"],
            "SITE_NAME":   SITE_NAME,
            "DESCRIPTION": item["description"] or item["title"],
            "THUMBNAIL":   item["thumbnail"],
            "CONTENT":     content,
        })
        write(web_dir / item["slug"] / "index.html", html)
        print(f"  ✓ {tree['web']}/{item['slug']}/")

# ── LISTINGS ──────────────────────────────────────────────────────────────────

def build_list(items, url_prefix, tag_filter=None):
    filtered = [p for p in items if tag_filter is None or tag_filter in p["tags"]]
    if not filtered:
        return '<p style="color:var(--text-dim)">nothing here yet.</p>'
    rows = ""
    for item in filtered:
        tag_html   = f'<span class="post-tag">{item["tags"][0]}</span>' if item["tags"] else ""
        thumb_html = f'<img src="{item["thumbnail"]}" alt="{item["title"]}">' if item["thumbnail"] else '<div class="post-thumb-placeholder"></div>'
        rows += f"""
  <li>
    <a href="{url_prefix}/{item['slug']}/">
      {thumb_html}
      <div class="post-info">
        <span class="post-title">{item['title']}</span>
        <span class="post-meta-line">
          {tag_html}
          <span class="post-date">{date_display(item['date'])}</span>
        </span>
      </div>
    </a>
  </li>"""
    return f'<ul class="post-list">{rows}</ul>'

def generate_listing(items, template, output_path, title, tagline, description, url_prefix, tag_filter=None):
    content = f"""
<div class="index-header">
  <h1>{tagline}</h1>
  <p>{description}</p>
</div>
{build_list(items, url_prefix, tag_filter)}
"""
    html = render(template, {
        "TITLE":       title,
        "SITE_NAME":   SITE_NAME,
        "DESCRIPTION": description,
        "THUMBNAIL":   "",
        "CONTENT":     content,
    })
    write(output_path, html)
    print(f"  ✓ {output_path.relative_to(WEB)}")

# ── PAGES ─────────────────────────────────────────────────────────────────────

def generate_pages(trees_data, template):
    """
    Renders pages/*.html into web/page-name/index.html.
    Any {{TREE_NAME}} placeholder in a page is replaced with that tree's listing.
    e.g. {{POSTS}}, {{PROJECTS}}, {{PUBLICATIONS}}
    """


    pages_dir = ROOT / "pages"
    if not pages_dir.exists():
        return

    placeholders = {
        tree["name"].upper(): build_list(items, f"/{tree['web']}")
        for tree, items in zip(CONTENT_TREES, [trees_data[t["name"]] for t in CONTENT_TREES])
    }

    for f in pages_dir.glob("*.html"):
        name    = f.stem
        content = render(f.read_text(), placeholders)
        html    = render(template, {
            "TITLE":       name,
            "SITE_NAME":   SITE_NAME,
            "DESCRIPTION": f"{name} — {SITE_NAME}",
            "THUMBNAIL":   "",
            "CONTENT":     content,
        })
        #write(WEB / name / "index.html", html)
        out_path = WEB / "index.html" if name == "index" else WEB / name / "index.html"
        write(out_path, html)
        print(f"  ✓ {'index.html' if name == 'index' else name + '/'}")
        print(f"  ✓ {name}/")

# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    print(f"\nGenerating site...\n")
    WEB.mkdir(exist_ok=True)
    template = load_template()

    # Load all trees
    trees_data = {}
    for tree in CONTENT_TREES:
        items = load_tree(tree)
        trees_data[tree["name"]] = items
        print(f"  {tree['name']}: {len(items)} item(s)")

    print()
    sync_assets()

    # Clean and generate each tree
    for tree in CONTENT_TREES:
        items = trees_data[tree["name"]]
        clean_tree(items, WEB / tree["web"])
        generate_tree(items, tree, template)

    # Listing page per tree
    for tree in CONTENT_TREES:
        generate_listing(
            trees_data[tree["name"]], template,
            output_path = WEB / tree["web"] / "index.html",
            title       = tree["name"],
            tagline     = tree["name"],
            description = f"{tree['name']} — {SITE_NAME}",
            url_prefix  = f"/{tree['web']}",
        )

    # Static pages
    generate_pages(trees_data, template)

    print(f"\nDone.\n")

if __name__ == "__main__":
    main()