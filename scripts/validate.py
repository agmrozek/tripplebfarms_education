"""Validate the public lesson index and download paths; Python standard library only."""
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')


def check(condition, message):
    if not condition:
        raise ValueError(message)


def local_file(path, lesson_id, *, pdf=False):
    check(isinstance(path, str) and '\\' not in path, 'Use repository-relative forward-slash paths')
    parts = PurePosixPath(path)
    check(not parts.is_absolute() and '..' not in parts.parts, 'A file path must stay in its lesson folder')
    check(path.startswith('lessons/' + lesson_id + '/'), 'Each file must belong to its lesson folder')
    file = ROOT / path
    check(file.resolve().is_relative_to(ROOT.resolve()) and not file.is_symlink(), 'Linked files must stay in the repository')
    check(file.is_file(), 'Missing file: ' + path)
    check(file.stat().st_size < 50 * 1024 * 1024, 'Keep published lesson files under 50 MiB: ' + path)
    if pdf:
        check(file.suffix.lower() == '.pdf' and file.read_bytes()[:5] == b'%PDF-', 'Download must be a PDF: ' + path)


def validate():
    data = json.loads((ROOT / 'index.json').read_text())
    check(data.get('schema_version') == 1, 'Unsupported lesson index version')
    check(isinstance(data.get('topics'), list) and isinstance(data.get('lessons'), list), 'Topics and lessons must be lists')
    topics = set()
    for topic in data['topics']:
        check(isinstance(topic, dict), 'Each topic must be an object')
        slug = topic.get('id')
        check(isinstance(slug, str) and SLUG.fullmatch(slug), 'Use a lowercase topic slug')
        check(slug not in topics, 'Duplicate topic: ' + slug)
        check(isinstance(topic.get('title'), str) and topic['title'].strip(), 'Each topic needs a title')
        topics.add(slug)
    lessons = set()
    for lesson in data['lessons']:
        check(isinstance(lesson, dict), 'Each lesson must be an object')
        slug = lesson.get('id')
        check(isinstance(slug, str) and SLUG.fullmatch(slug), 'Use a lowercase lesson slug')
        check(slug not in lessons, 'Duplicate lesson: ' + slug)
        lessons.add(slug)
        check(lesson.get('topic') in topics, 'Choose an existing topic for ' + slug)
        for field in ['title', 'summary']:
            check(isinstance(lesson.get(field), str) and lesson[field].strip(), 'Missing ' + field + ' for ' + slug)
        local_file(lesson.get('lesson_file'), slug)
        check(isinstance(lesson.get('downloads'), list), 'Downloads must be a list for ' + slug)
        for download in lesson['downloads']:
            check(isinstance(download, dict), 'Each download must be an object')
            check(isinstance(download.get('label'), str) and download['label'].strip(), 'Each download needs a label')
            local_file(download.get('file'), slug, pdf=True)
    print(f"Valid lesson index: {len(topics)} topics, {len(lessons)} published lessons.")


if __name__ == '__main__':
    try:
        validate()
    except (ValueError, TypeError, KeyError) as error:
        raise SystemExit('Invalid lesson index: ' + str(error))
