# Tripple B Farms Education

Free farming and homesteading lessons from Tripple B Farms in Raber, Michigan.

This repository is the source for lesson text, printable PDFs, worksheets, and other learning materials. The farm website will present the lessons and link to downloads hosted in this repository. Visitors do not need a GitHub account to download public files.

## Organization

```text
index.json                       Published lesson index for the website
lessons/<lesson-id>/README.md     Editable lesson and instructions
lessons/<lesson-id>/downloads/    Published PDFs and worksheets
lessons/<lesson-id>/source/       Editable source files for those documents
templates/lesson.md               Starting point for a new lesson
scripts/validate.py              Check the index and linked files
```

Only lessons listed in `index.json` are intended for the website. The first class is [Agronomy Fundamentals](lessons/agronomy-fundamentals/README.md), beginning with Part 1: Soil Science & Farm Management. Multiple PDFs for the same class belong together in one class folder and one index entry, with a numbered download for each part. Files committed anywhere in this public repository remain publicly accessible, even if they are not in the index.

## Add a lesson

1. Create a descriptive folder such as `lessons/building-healthy-soil/`.
2. Copy `templates/lesson.md` to that folder as `README.md` and write the lesson.
3. Put finished PDFs in `downloads/` and their editable source files in `source/`.
4. Add an entry to `index.json`, choosing a topic from its `topics` list. Use paths relative to this repository, not local computer paths.
5. Run `python3 scripts/validate.py`, review the changes, and commit/push them to GitHub.

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

The future Farm Learning section can read `index.json` at build time and generate its topic and lesson pages. Download links must use the GitHub repository rather than copying the PDFs into the website deployment. For example, a file committed on `main` can be downloaded from:

```text
https://github.com/agmrozek/tripplebfarms_education/raw/refs/heads/main/lessons/<lesson-id>/downloads/<filename>.pdf
```

Use an exact Git commit instead of `main` when publishing a version that must retain identical materials. The website integration has not been built or published yet.

Keep ordinary lesson PDFs reasonably small. Store large videos in the existing video/media hosting and link to them from lessons. Do not add passwords, API keys, student information, private farm records, or third-party documents without permission to redistribute them.

The repository's existing LICENSE is retained. Review licensing before adding material created by other authors.
