import argparse
import json
from readwise import select_source, get_highlights
from obsidian import get_canvas

if __name__ == "__main__":
    # get path from command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument("--path", help="path to save the canvas", type=str)
    parser.add_argument("--width", help="width of each node", type=int, default=600)
    parser.add_argument("--height", help="height of each node", type=int, default=300)
    parser.add_argument("--padding", help="padding between nodes", type=int, default=20)

    args = parser.parse_args()

    path = args.path
    if not path:
        raise ValueError("Please provide a path to save the canvas")

    source = select_source()
    highlights = get_highlights(source["id"])
    highlights_and_notes = [
        (highlight["text"], highlight["note"]) for highlight in highlights
    ]
    canvas = get_canvas(highlights_and_notes, args.width, args.height, args.padding)
    title = source["title"]

    # save canvas to path
    with open(f"{path}/{title}.canvas", "w") as f:
        json.dump(canvas, f)
