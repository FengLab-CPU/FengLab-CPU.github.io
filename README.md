# Functional Genomics Lab Website

Static academic website for Yuanqing Feng’s lab, built with Jekyll and deployed via GitHub Pages.

Live site: <https://fengyq.github.io>

---

## 1. Tech Stack

- **Jekyll** – static site generator.
- **HTML / CSS** – custom page layout and styling.
- **Font Awesome** – icons in header/footer.
- **GitHub Pages** – hosting.

---

## 2. Run the Site Locally

Prerequisites: Ruby, Bundler, Git.

1. **Clone the repo**
   ```bash
   git clone https://github.com/fengyq/fengyq.github.io.git
   cd fengyq.github.io
   ```
2. **Install dependencies**
   ```bash
   bundle install
   ```
3. **Serve the site**
   ```bash
   bundle exec jekyll serve
   ```
4. **Open in browser**
   - Visit `http://localhost:4000`

---

## 3. Content Editing Cheat Sheet

This section covers the content that changes most often: **People**, **News**, and **Publications**.

### 3.1 People Page – `people.md`

#### Current lab members

- Cards live under the `<!-- Current Lab Members -->` section inside:
  ```html
  <div class="people-grid">
      ... person-card blocks ...
  </div>
  ```
- To add a member, copy an existing `<div class="person-card">...</div>` block and update the fields:
  ```html
  <div class="person-card">
      <div class="person-photo">
          <img src="/assets/images/alice.jpg" alt="Alice Zhang"
               style="width: 100%; height: 100%; object-fit: cover;">
      </div>
      <div class="person-info">
          <div class="person-name">Alice Zhang</div>
          <div class="person-title">PhD Student</div>
          <div class="person-contact">
              <a href="mailto:alice@example.edu">alice@example.edu</a>
          </div>
      </div>
  </div>
  ```
- Photos:
  - Save images to `assets/images/` (e.g. `assets/images/alice.jpg`).
  - Use `<img src="/assets/images/...">` and set a descriptive `alt` attribute.
  - Or keep using emoji avatars: `<div class="person-photo">👩‍🔬</div>`.

#### Lab alumni

- In `people.md`, scroll to the `<!-- Lab Alumni -->` section and the `<tbody>` of `.alumni-table`.
- Add a new row:
  ```html
  <tr>
      <td><strong>Jane Doe</strong></td>
      <td>PhD Student</td>
      <td class="year-cell">2024</td>
      <td class="current-cell">Postdoc, XYZ University</td>
  </tr>
  ```

#### Delete / rename people

- Delete a member: remove the entire `<div class="person-card">...</div>` block.
- Delete an alumni: remove the corresponding `<tr>...</tr>` row.
- Rename or update roles/contact: edit text inside `.person-name`, `.person-title`, and the email link.  
  The grid layout will adjust automatically.

---

### 3.2 News – `news.md`

News items are stored in the front-matter YAML list under `news_items:` at the top of `news.md`.

Example entry:
```yaml
- date: "FEB 2024"
  title: "Nature Genetics Publication"
  excerpt: "Short description of the news."
  link: "https://example.com/paper-or-article"   # optional
  pmid: "12345678"                               # optional
  category: "publication"                        # publication | award | position | presentation
```

- **Add news**
  - Add a new `-` block at the **top** of `news_items:` (latest first).
  - Choose `category` from `publication`, `award`, `position`, `presentation` to control the badge color.
  - `link`/`pmid` are optional.
- **Edit / delete news**
  - Edit fields in-place to rename/update.
  - To delete, remove the entire YAML block from `- date:` through `category: ...`.
- This list powers:
  - The `/news/` page cards, and
  - The homepage hero “What’s New” ticker.

---

### 3.3 Publications – `publications.md`

The Publications page is grouped by year and has a year filter.

#### Year headings

- Each year section starts with:
  ```html
  <h2 class="pub-year-heading" data-year="2024">2024</h2>
  ```
- For a new year (e.g. 2025), add a similar heading with `data-year="2025"` and text `2025`.

#### Publication cards

- Each publication is a `.publication-item` with a `data-year` attribute:
  ```html
  <div class="publication-item fade-in" data-year="2024">
      <div class="pub-figure">
          <img src="../assets/pub_images/2025_newpaper_cover.jpg"
               alt="Cover or schematic for the paper"
               style="width: 100%; height: auto; object-fit: contain;">
      </div>
      <div class="pub-content">
          <div class="pub-title">
              <a href="https://doi.org/10.1234/example.doi">Full paper title goes here</a>
          </div>
          <div class="pub-authors">
              <span class="author-highlight">Feng Y</span>, Lastname A, Lastname B, ...
          </div>
          <div class="pub-venue">
              <em>Journal Name</em>. 2025; volume(issue):pages.
          </div>
          <div class="pub-links">
              PMID: <a href="https://pubmed.ncbi.nlm.nih.gov/12345678/">12345678</a> |
              DOI: <a href="https://doi.org/10.1234/example.doi">10.1234/example.doi</a>
          </div>
      </div>
  </div>
  ```

#### Images for publications

- Store images in `assets/pub_images/` (e.g. `assets/pub_images/2025_newpaper_cover.jpg`).
- Within `publications.md`, reference them as `src="../assets/pub_images/..."` (note the `..`).
- Use clear `alt` text (e.g. “Nature Genetics cover showing skin pigmentation diversity in Africans”).

#### Year filter buttons

- Filter buttons at the top are inside `<div class="pub-filter-bar">`:
  ```html
  <button class="pub-filter-btn" data-year-filter="2025">2025</button>
  ```
- When adding a new year:
  - Add a matching button with `data-year-filter="YYYY"`.
  - Ensure each publication for that year has `data-year="YYYY"` and a matching year heading.

#### Delete / move publications

- Delete: remove the whole `<div class="publication-item ...">...</div>` block.
- Edit: change title/authors/journal/links in `.pub-title`, `.pub-authors`, `.pub-venue`, `.pub-links`.
- Move to another year:
  - Change `data-year="YYYY"` on the block.
  - Move it under the corresponding year heading.
  - Add/update the filter button if this is a new year.

---

## 4. Helper Script – `tools/new_snippet.py`

This script **directly edits the site files** to add new entries.

Run from the repo root:
```bash
python tools/new_snippet.py
```

You’ll be asked for a **type**:

- `news`
  - Updates `news.md`.
  - Asks for date, title, excerpt, optional link/PMID, and category.
  - Inserts a new YAML block at the **top** of `news_items:` so it becomes the latest news.
- `publication`
  - Updates `publications.md`.
  - Asks for year, title, authors, journal, citation, DOI/PMID, and optional image file name.
  - Ensures a year filter button exists for that year.
  - Inserts a new `.publication-item` under the correct year heading; if the year doesn’t exist yet, it creates the heading for you.
- `person`
  - Updates `people.md`.
  - Asks for name, role/title, optional email, and optional image file (or emoji avatar).
  - Inserts a new `person-card` into the Current Members `people-grid`.

After each operation the script prints the exact block it inserted, so you can review it before committing.

---

## 5. Git Workflow

Typical workflow after editing content or using the helper script:

1. **Check status**
   ```bash
   git status
   ```
2. **Stage changes**
   ```bash
   # Add specific files
   git add README.md news.md publications.md people.md
   # or add everything
   git add .
   ```
3. **Commit and push**
   ```bash
   git commit -m "Update content"
   git pull --rebase origin main   # optional but recommended
   git push origin main
   ```

Quick one-liner:
```bash
git add . && git commit -m "update site content" && git pull --rebase origin main && git push origin main
```

---

## 6. Contributing, License, Contact

- **Contributing** – Suggestions and pull requests are welcome.
- **License** – This project uses the MIT License (see `LICENSE`).
- **Contact** – For questions, email:  
  `Fengyuanqing2010@gmail.com`

---
