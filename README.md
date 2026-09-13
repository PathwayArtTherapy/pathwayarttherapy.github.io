# Pathway Art Therapy website

The website for [Pathway Art Therapy](https://pathwayarttherapy.com), hosted free on GitHub Pages.
It is plain HTML and CSS, so every page is a normal file you can open and edit.

## Where things live

| What | File |
|---|---|
| Home page | `index.html` |
| Other pages | `<page-name>/index.html`, for example `about/index.html` |
| Colours, fonts, spacing | `assets/css/style.css` (colours are at the very top) |
| Photos | `assets/img/` |
| Menu and footer | `tools/partials/header.html` and `tools/partials/footer.html` |
| Booking link | `book/index.html` |

## Common changes

**Change some text.** Open the page's `index.html`, find the sentence, edit it, save.

**Change where "Book" buttons go.** Every booking button points to `/book/`.
Open `book/index.html` and replace the calendar link in the two places it appears.

**Change the menu or footer.** Edit `tools/partials/header.html` or `tools/partials/footer.html`,
then copy the change into every page by running this in Terminal from the project folder:

```bash
python3 tools/sync.py
```

**Add or swap a photo.** Put the image in `assets/img/`, then change the `src="/assets/img/…"`
part of the page. Keep photos under about 300 KB so pages load quickly.

## Preview on this Mac

From the project folder in Terminal:

```bash
python3 -m http.server 8124
```

Then open http://localhost:8124 in a browser. Press Ctrl+C in Terminal to stop it.

## Publish changes

```bash
git add -A
git commit -m "Describe what you changed"
git push
```

The live site updates about a minute after pushing.

## Contact form

The contact form sends messages through [Web3Forms](https://web3forms.com) to
loulou@pathwayarttherapy.com. The access key in `contact/index.html` is meant to be public.
