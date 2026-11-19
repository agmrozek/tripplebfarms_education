"""Generate the README's published lesson table from index.json."""
import argparse
import json
from pathlib import Path
from urllib.parse import quote

from validate import validate

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- PUBLISHED-LESSONS:START -->'
END = '<!-- PUBLISHED-LESSONS:END -->'


def text(value):
    return value.replace('\\', '\\\\').replace('|', '\\|').replace('[', '\\[').replace(']', '\\]').replace('\n', ' ')


def contents(data):
    topics = {topic['id']: topic['title'] for topic in data['topics']}
    lines = ['## Table of Contents', '', '| Class / lesson | Topic | Published PDFs |', '| --- | --- | --- |']
    for lesson in data['lessons']:
        title = '[' + text(lesson['title']) + '](' + quote(lesson['lesson_file'], safe='/') + ')'
        downloads = '<br>'.join('[' + text(item['label']) + '](' + quote(item['file'], safe='/') + ')' for item in lesson['downloads']) or 'No PDFs published yet'
        lines.append('| ' + title + ' | ' + text(topics[lesson['topic']]) + ' | ' + downloads + ' |')
    if not data['lessons']:
        return '## Table of Contents\n\nNo lessons have been published yet.'
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if the README needs updating')
    args = parser.parse_args()
    validate()
    data = json.loads((ROOT / 'index.json').read_text())
    path = ROOT / 'README.md'
    original = path.read_text()
    if original.count(START) != 1 or original.count(END) != 1:
        raise SystemExit('README must contain one published-lessons start/end marker pair')
    before, rest = original.split(START, 1)
    _, after = rest.split(END, 1)
    updated = before + START + '\n' + contents(data) + '\n' + END + after
    if args.check:
        if updated != original:
            raise SystemExit('Table of contents is out of date. Run python3 scripts/update_contents.py')
        print('Table of contents is current.')
    else:
        path.write_text(updated)
        print('Updated README table of contents from the published lesson index.')


if __name__ == '__main__':
    main()
