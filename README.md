# Tripple B Farms Education

Free farming and homesteading lessons from Tripple B Farms in Raber, Michigan.

This repository is the source for lesson text, printable PDFs, worksheets, and other learning materials. Visit [Farm Learning](https://www.tripplebfarms.com/education) to browse classes on the farm website. Lesson downloads are hosted directly in this repository. Visitors do not need a GitHub account to download public files.

<!-- PUBLISHED-LESSONS:START -->
## Table of Contents

| Class / lesson | Topic | Published PDFs |
| --- | --- | --- |
| [Agronomy Fundamentals](lessons/agronomy-fundamentals/README.md) | Soil & Compost | [Lesson 1 — Soil Science & Farm Management (PDF)](lessons/agronomy-fundamentals/downloads/part-01-soil-science-and-farm-management.pdf)<br>[Lesson 2 — Soil Chemistry & Cation Exchange (PDF)](lessons/agronomy-fundamentals/downloads/part-02-soil-chemistry-and-cation-exchange.pdf)<br>[Lesson 3 — The Soil Food Web (PDF)](lessons/agronomy-fundamentals/downloads/part-03-the-soil-food-web.pdf) |
| [Pasture and Grazing Fundamentals](lessons/pasture-and-grazing-fundamentals/README.md) | Pasture & Grazing | [Lesson 1 — How Pasture Plants Grow (PDF)](lessons/pasture-and-grazing-fundamentals/downloads/part-01-how-pasture-plants-grow.pdf)<br>[Lesson 2 — What Grows in a Pasture (PDF)](lessons/pasture-and-grazing-fundamentals/downloads/part-02-what-grows-in-a-pasture.pdf)<br>[Lesson 3 — What Happens After a Bite (PDF)](lessons/pasture-and-grazing-fundamentals/downloads/part-03-what-happens-after-a-bite.pdf)<br>[Lesson 4 — How to Tell When a Paddock Is Ready (PDF)](lessons/pasture-and-grazing-fundamentals/downloads/part-04-how-to-tell-when-a-paddock-is-ready.pdf)<br>[Lesson 5 — How Much Forage Is Available? (PDF)](lessons/pasture-and-grazing-fundamentals/downloads/part-05-how-much-forage-is-available.pdf)<br>[Lesson 6 — How Much Forage Does the Herd Need? (PDF)](lessons/pasture-and-grazing-fundamentals/downloads/part-06-how-much-forage-does-the-herd-need.pdf)<br>[Lesson 7 — Designing Paddocks and a Grazing Rotation (PDF)](lessons/pasture-and-grazing-fundamentals/downloads/part-07-designing-paddocks-and-a-grazing-rotation.pdf)<br>[Lesson 8 — Grazing Through an Upper Peninsula Year (PDF)](lessons/pasture-and-grazing-fundamentals/downloads/part-08-grazing-through-an-upper-peninsula-year.pdf)<br>[Lesson 9 — Why Pastures Thin Out (PDF)](lessons/pasture-and-grazing-fundamentals/downloads/part-09-why-pastures-thin-out.pdf)<br>[Lesson 10 — A Year in the Life of a Grazing Farm (PDF)](lessons/pasture-and-grazing-fundamentals/downloads/part-10-a-year-in-the-life-of-a-grazing-farm.pdf) |
| [Livestock Nutrition Fundamentals](lessons/livestock-nutrition-fundamentals/README.md) | Animal Care | [Lesson 1 — How Cattle Digest Forage (PDF)](lessons/livestock-nutrition-fundamentals/downloads/part-01-how-cattle-digest-forage.pdf)<br>[Lesson 2 — Dry Matter and Feed Intake (PDF)](lessons/livestock-nutrition-fundamentals/downloads/part-02-dry-matter-and-feed-intake.pdf)<br>[Lesson 3 — Energy, Protein, and Fiber (PDF)](lessons/livestock-nutrition-fundamentals/downloads/part-03-energy-protein-and-fiber.pdf)<br>[Lesson 4 — Reading a Hay Test (PDF)](lessons/livestock-nutrition-fundamentals/downloads/part-04-reading-a-hay-test.pdf)<br>[Lesson 5 — Water, Minerals, and Vitamins (PDF)](lessons/livestock-nutrition-fundamentals/downloads/part-05-water-minerals-and-vitamins.pdf)<br>[Lesson 6 — Feeding Cattle at Different Life Stages (PDF)](lessons/livestock-nutrition-fundamentals/downloads/part-06-feeding-cattle-at-different-life-stages.pdf)<br>[Lesson 7 — Supplementation and Ration Arithmetic (PDF)](lessons/livestock-nutrition-fundamentals/downloads/part-07-supplementation-and-ration-arithmetic.pdf)<br>[Lesson 8 — A Winter Feeding Plan for Cedar Run (PDF)](lessons/livestock-nutrition-fundamentals/downloads/part-08-a-winter-feeding-plan-for-cedar-run.pdf) |
<!-- PUBLISHED-LESSONS:END -->

## Organization

```text
index.json                       Published lesson index for the website
lessons/<lesson-id>/README.md     Editable lesson and instructions
lessons/<lesson-id>/downloads/    Published PDFs and worksheets
lessons/<lesson-id>/source/       Editable source files for those documents
templates/lesson.md               Starting point for a new lesson
scripts/validate.py              Check the index and linked files
scripts/update_contents.py       Update the table of contents from the index
```

Only lessons listed in `index.json` are intended for the website. The first class is [Agronomy Fundamentals](lessons/agronomy-fundamentals/README.md), beginning with Lesson 1: Soil Science & Farm Management. Multiple PDFs for the same class belong together in one class folder and one index entry, with a numbered download for each part. Files committed anywhere in this public repository remain publicly accessible, even if they are not in the index.

## Add a lesson

1. Create a descriptive folder such as `lessons/building-healthy-soil/`.
2. Copy `templates/lesson.md` to that folder as `README.md` and write the lesson.
3. Put finished PDFs in `downloads/` and their editable source files in `source/`.
4. Add an entry to `index.json`, choosing a topic from its `topics` list. Use paths relative to this repository, not local computer paths.
5. Run `python3 scripts/update_contents.py` to validate the index and refresh the table of contents, then review and commit/push the changes to GitHub.

When adding another PDF to an existing class, append it to that class’s `downloads` list in `index.json` and run the same command. The table of contents lists only published classes/lessons and their available PDFs. Do not edit the generated table directly; edit the index instead. Check it without changing files with `python3 scripts/update_contents.py --check`.

Each published lesson entry uses this structure (example only; the files must exist before adding it):

```json
{
  "id": "building-healthy-soil",
  "title": "Building Healthy Soil",
  "topic": "soil-and-compost",
  "summary": "A practical introduction to caring for living soil.",
  "lesson_file": "lessons/building-healthy-soil/README.md",
  "downloads": [
    {
      "label": "Lesson PDF",
      "file": "lessons/building-healthy-soil/downloads/lesson.pdf"
    }
  ]
}
```

## Website integration

The Farm Learning section reads a reviewed snapshot of `index.json` at build time and generates the library and class pages. Download links must use the GitHub repository rather than copying the PDFs into the website deployment. For example, a file committed on `main` can be downloaded from:

```text
https://github.com/agmrozek/tripplebfarms_education/raw/refs/heads/main/lessons/<lesson-id>/downloads/<filename>.pdf
```

Use an exact Git commit instead of `main` when publishing a version that must retain identical materials. The website is published at https://www.tripplebfarms.com/education. Repository changes become visible there after the website lesson snapshot is refreshed and rebuilt; GitHub updates do not automatically redeploy the website.

Keep ordinary lesson PDFs reasonably small. Store large videos in the existing video/media hosting and link to them from lessons. Do not add passwords, API keys, student information, private farm records, or third-party documents without permission to redistribute them.

The repository's existing LICENSE is retained. Review licensing before adding material created by other authors.
