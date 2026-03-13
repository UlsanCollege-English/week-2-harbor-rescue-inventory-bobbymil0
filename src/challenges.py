<<<<<<< HEAD
def mission_snapshot(items: list[object]) -> tuple[object | None, object | None]:
    """
    Return the first and last item in the list.
    If the list is empty return (None, None).
    """
    if len(items) == 0:
        return (None, None)

    return (items[0], items[-1])


def cargo_window(items: list[object], start: int, size: int) -> list[object]:
    """
    Return up to size items starting from index start.
    """
    if start < 0 or start >= len(items):
        return []

    if size <= 0:
        return []

    return items[start:start + size]


def first_supply_index(items: list[object], target: object) -> int:
    """
    Return the first index of target or -1 if not found.
    """
    for i in range(len(items)):
        if items[i] == target:
            return i

    return -1


def supply_report(items: list[object], target: object) -> tuple[int, int]:
    """
    Return (count, first_index) of target.
    """
    count = 0
    first_index = -1

    for i in range(len(items)):
        if items[i] == target:
            count += 1
            if first_index == -1:
                first_index = i

    if count == 0:
        return (0, -1)

    return (count, first_index)


def priority_load(items: list[object], urgent_item: object) -> list[object]:
    """
    Return a new list with urgent_item added to the front.
    """
    return [urgent_item] + items
=======

"""Week 2 starter code for Harbor Rescue Inventory."""

from __future__ import annotations


def mission_snapshot(items: list[object]) -> tuple[object | None, object | None]:
    """Return the first and last items in the list.

    Return (None, None) if the list is empty.
    """
    raise NotImplementedError


def cargo_window(items: list[object], start: int, size: int) -> list[object]:
    """Return up to ``size`` items starting at index ``start``.

    Return an empty list if ``start`` is out of range or if ``size <= 0``.
    """
    raise NotImplementedError


def first_supply_index(items: list[object], target: object) -> int:
    """Return the index of the first occurrence of ``target``.

    Return -1 if the target is not found.
    Do not use ``items.index(...)`` for this challenge.
    """
    raise NotImplementedError


def supply_report(items: list[object], target: object) -> tuple[int, int]:
    """Return (count, first_index) for ``target`` in ``items``.

    Return (0, -1) if the target does not appear.
    """
    raise NotImplementedError


def priority_load(items: list[object], urgent_item: object) -> list[object]:
    """Return a new list with ``urgent_item`` added at the front.

    Do not mutate the original input list.
    This is a stretch challenge.
    """
    raise NotImplementedError
>>>>>>> 894c5f936fea79a75e5896e431e4d3e1ef7e3d4d
