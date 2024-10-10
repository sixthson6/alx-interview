#!/usr/bin/python3
"""
Traverse lockboxes
"""


def canUnlockAll(boxes):
    """Check if all locked boxes can
    be unlocked"""
    unlocked = set([0])
    keys = set()

    for i in range(len(boxes)):
        if i in unlocked:
            keys.update(boxes[i])

            for key in keys:
                if key not in unlocked and key < len(boxes):
                    unlocked.add(key)
    return len(unlocked) == len(boxes)
