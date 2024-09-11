import uuid


def get_uuid():
    while True:
        yield uuid.uuid4().hex[:16]


def get_canvas(hightlights_and_notes, width, height, padding):
    nodes = [
        {
            "id": next(get_uuid()),
            "type": "text",
            "text": (
                highlight[0]
                if highlight[1] == ""
                else highlight[0] + "\n> " + highlight[1]
            ),
            "x": 0,
            "y": 0 + idx * (height + padding),
            "width": width,
            "height": height,
        }
        for idx, highlight in enumerate(hightlights_and_notes)
    ]
    canvas = {"nodes": nodes, "edges": []}
    return canvas
