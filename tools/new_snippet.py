#!/usr/bin/env python3
"""
Helper script to add People / News / Publications entries.

Usage (from repo root):
    python tools/new_snippet.py

The script will:
  - ask a few questions,
  - write the new block into the correct file (news.md, publications.md, people.md),
  - and print the snippet it inserted for your reference.
"""

import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NEWS_PATH = ROOT / "news.md"
PUBS_PATH = ROOT / "publications.md"
PEOPLE_PATH = ROOT / "people.md"


def ask(prompt, default=None, required=True):
    label = f"{prompt}"
    if default is not None:
        label += f" [{default}]"
    label += ": "
    while True:
        value = input(label).strip()
        if value:
            return value
        if not required:
            return default or ""
        if default is not None:
            return default
        print("  Please enter a value.")


def insert_into_news(snippet: str) -> None:
    """Insert a YAML block at the top of news_items in news.md."""
    text = NEWS_PATH.read_text(encoding="utf-8")
    marker = "news_items:"
    idx = text.find(marker)
    if idx == -1:
        raise SystemExit("Could not find `news_items:` in news.md")

    insert_pos = text.find("\n", idx)
    if insert_pos == -1:
        insert_pos = idx + len(marker)
    insert_pos += 1

    new_text = text[:insert_pos] + snippet + "\n" + text[insert_pos:]
    NEWS_PATH.write_text(new_text, encoding="utf-8")


def ensure_pub_filter_button(text: str, year: str) -> str:
    """Ensure there is a filter button for the given year."""
    token = f'data-year-filter="{year}"'
    if token in text:
        return text

    marker = '<div class="pub-filter-bar">'
    start = text.find(marker)
    if start == -1:
        return text

    close = text.find("</div>", start)
    if close == -1:
        return text

    btn_line = f'        <button class="pub-filter-btn" data-year-filter="{year}">{year}</button>\n'
    return text[:close] + btn_line + text[close:]


def insert_into_publications(year: str, snippet: str) -> None:
    """Insert a publication block under the correct year heading."""
    text = PUBS_PATH.read_text(encoding="utf-8")
    text = ensure_pub_filter_button(text, year)

    heading = f'<h2 class="pub-year-heading" data-year="{year}">{year}</h2>'
    heading_idx = text.find(heading)

    if heading_idx != -1:
        # Insert after the heading line
        insert_pos = text.find("\n", heading_idx)
        if insert_pos == -1:
            insert_pos = heading_idx + len(heading)
        insert_pos += 1
        new_text = text[:insert_pos] + snippet + "\n\n" + text[insert_pos:]
    else:
        # New year: add heading + snippet before the first existing year heading
        first_heading_marker = '<h2 class="pub-year-heading"'
        first_heading_idx = text.find(first_heading_marker)
        if first_heading_idx == -1:
            # Fallback: append near the end of the container
            insert_pos = text.rfind("</div>")
        else:
            insert_pos = first_heading_idx

        heading_block = f'    <h2 class="pub-year-heading" data-year="{year}">{year}</h2>\n\n{snippet}\n\n'
        new_text = text[:insert_pos] + heading_block + text[insert_pos:]

    PUBS_PATH.write_text(new_text, encoding="utf-8")


def insert_into_people(snippet: str) -> None:
    """Insert a person-card into the Current Members grid."""
    text = PEOPLE_PATH.read_text(encoding="utf-8")

    grid_marker = '<div class="people-grid">'
    grid_start = text.find(grid_marker)
    if grid_start == -1:
        raise SystemExit("Could not find `<div class=\"people-grid\">` in people.md")

    # Find the matching closing </div> for the grid using a simple depth counter.
    idx = grid_start
    depth = 0
    while True:
        next_open = text.find("<div", idx)
        next_close = text.find("</div>", idx)
        if next_open == -1 and next_close == -1:
            raise SystemExit("Could not locate end of people-grid block.")

        if next_open != -1 and (next_open < next_close or next_close == -1):
            depth += 1
            idx = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                closing_pos = next_close
                break
            idx = next_close + len("</div>")

    # Insert the snippet just before the closing </div> of the grid.
    new_text = text[:closing_pos] + snippet + "\n" + text[closing_pos:]
    PEOPLE_PATH.write_text(new_text, encoding="utf-8")


def generate_news():
    print("\n--- New NEWS item ---")
    date = ask("Date (e.g. FEB 2025)")
    title = ask("Title")
    excerpt = ask("Short excerpt (1–2 sentences)")
    link = ask("Link (PubMed/DOI/URL, optional)", required=False)
    pmid = ask("PMID (optional)", required=False)
    category = ask(
        "Category [publication/award/position/presentation]",
        default="publication",
    )

    def esc(s: str) -> str:
        return s.replace('"', '\\"')

    lines = [
        f'- date: "{esc(date)}"',
        f'  title: "{esc(title)}"',
        f'  excerpt: "{esc(excerpt)}"',
    ]
    if link:
        lines.append(f'  link: "{esc(link)}"')
    if pmid:
        lines.append(f'  pmid: "{esc(pmid)}"')
    lines.append(f'  category: "{esc(category)}"')

    yaml_block = "\n".join("  " + line for line in lines)
    insert_into_news(yaml_block)

    print("\nAdded this YAML block to news.md under `news_items:`:\n")
    print(yaml_block)


def generate_publication():
    print("\n--- New PUBLICATION ---")
    year = ask("Publication year (e.g. 2025)")
    title = ask("Title")
    authors = ask("Authors (comma-separated; highlight Feng Y later if you wish)")
    journal = ask("Journal name")
    citation = ask("Citation details (e.g. 2025; 10(2):123-130)")
    doi = ask("DOI (e.g. 10.1234/example.doi)", required=False)
    doi_link = f"https://doi.org/{doi}" if doi and not doi.startswith("http") else doi
    pmid = ask("PMID (optional)", required=False)
    img_file = ask(
        "Cover/figure image file in assets/pub_images (optional, e.g. 2025_paper.jpg)",
        required=False,
    )

    img_block = ""
    if img_file:
        img_block = textwrap.dedent(
            f"""\
                <div class="pub-figure">
                    <img src="../assets/pub_images/{img_file}"
                         alt="Cover or key figure for {title}"
                         style="width: 100%; height: auto; object-fit: contain;">
                </div>"""
        )
    else:
        img_block = '        <div class="pub-figure">FIGURE</div>'

    links_parts = []
    if pmid:
        links_parts.append(
            f'PMID: <a href="https://pubmed.ncbi.nlm.nih.gov/{pmid}/">{pmid}</a>'
        )
    if doi_link:
        if links_parts:
            links_parts.append(" | ")
        links_parts.append(
            f'DOI: <a href="{doi_link}">{doi or doi_link}</a>'
        )
    links_html = "".join(links_parts) if links_parts else "&nbsp;"

    snippet = textwrap.dedent(
        f"""\
        <div class="publication-item fade-in" data-year="{year}">
{img_block}
            <div class="pub-content">
                <div class="pub-title">
                    <a href="{doi_link or '#'}">{title}</a>
                </div>
                <div class="pub-authors">
                    {authors}
                </div>
                <div class="pub-venue">
                    <em>{journal}</em>. {citation}.
                </div>
                <div class="pub-links">
                    {links_html}
                </div>
            </div>
        </div>"""
    )
    # indent to match surrounding HTML (4 spaces)
    snippet = textwrap.indent(snippet.strip("\n"), "    ")

    insert_into_publications(year, snippet)

    print(
        f"\nAdded a publication for {year} to publications.md.\n"
        "Block inserted (under the appropriate year heading):\n"
    )
    print(snippet)


def generate_person():
    print("\n--- New PERSON (People page) ---")
    name = ask("Name")
    title = ask("Role / title (e.g. PhD Student)")
    email = ask("Email (optional)", required=False)
    img_file = ask(
        "Photo file name in assets/images (leave empty to use emoji avatar)",
        required=False,
    )
    emoji = ""
    if not img_file:
        emoji = ask("Emoji avatar (e.g. 👩‍🔬, optional)", default="👩‍🔬", required=False)

    if img_file:
        photo_block = textwrap.dedent(
            f"""\
                <div class="person-photo">
                    <img src="/assets/images/{img_file}" alt="{name}"
                         style="width: 100%; height: 100%; object-fit: cover;">
                </div>"""
        )
    else:
        photo_block = f'                <div class="person-photo">{emoji or "👩‍🔬"}</div>'

    contact_block = ""
    if email:
        contact_block = textwrap.dedent(
            f"""\
                    <div class="person-contact">
                        <a href="mailto:{email}">{email}</a>
                    </div>"""
        )

    snippet = textwrap.dedent(
        f"""\
        <div class="person-card">
{photo_block}
            <div class="person-info">
                <div class="person-name">{name}</div>
                <div class="person-title">{title}</div>
{contact_block}
            </div>
        </div>"""
    )
    snippet = textwrap.indent(snippet.strip("\n"), "            ")

    insert_into_people(snippet)

    print(
        "\nAdded this person-card to the Current Members grid in people.md:\n"
    )
    print(snippet)


def main():
    print("Add content type: [news / publication / person]")
    kind = ask("Type", default="news").lower()
    if kind.startswith("news"):
        generate_news()
    elif kind.startswith("pub"):
        generate_publication()
    elif kind.startswith("person") or kind.startswith("peo"):
        generate_person()
    else:
        print("Unknown type. Please run again with: news, publication, or person.")


if __name__ == "__main__":
    main()
