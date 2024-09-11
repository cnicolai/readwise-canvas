import uuid

EXAMPLES = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
]


PATH = "/Users/christoph/Documents/Obsidian/Zettelkasten/Canvas"


def get_uuid():
    while True:
        yield uuid.uuid4().hex[:16]


def get_canvas(EXAMPLES, width=800, height=400, padding=20):
    nodes = [
        {
            "id": next(get_uuid()),
            "type": "text",
            "text": example,
            "x": 0,
            "y": 0 + idx * (height + padding),
            "width": width,
            "height": height,
        }
        for idx, example in enumerate(EXAMPLES)
    ]
    canvas = {"nodes": nodes, "edges": []}
    return canvas
