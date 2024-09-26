from typing import List, Tuple, Optional

def sum_of_ranges(ranges: List[Tuple[int, int]]) -> int:
    """
    Calculate the total length covered by a list of ranges.
    """
    return sum(end - start for start, end in ranges)

def union_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Merge overlapping or contiguous ranges.
    """
    if not ranges:
        return []

    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged_ranges = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged_ranges[-1]

        if current_start <= last_end:
            merged_ranges[-1] = (last_start, max(last_end, current_end))
        else:
            merged_ranges.append((current_start, current_end))

    return merged_ranges

def intersect_two_ranges(range1: Tuple[int, int], range2: Tuple[int, int]) -> Optional[Tuple[int, int]]:
    """
    Find the intersection of two ranges.
    """
    start1, end1 = range1
    start2, end2 = range2

    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)

    if intersect_start <= intersect_end:
        return (intersect_start, intersect_end)
    else:
        return None  # No intersection

def difference(ranges: List[Tuple[int, int]], target: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Subtract a target range from a list of ranges.
    """
    result = []
    target_start, target_end = target

    for start, end in ranges:
        if end < target_start or start > target_end:
            result.append((start, end))
        else:
            if start < target_start and end > target_end:
                result.append((start, target_start))
                result.append((target_end, end))
            elif start < target_start:
                result.append((start, target_start))
            elif end > target_end:
                result.append((target_end, end))
            # Else, range is fully contained and removed

    return result

def find_target_in_document(document: str, target: str) -> Optional[Tuple[int, int]]:
    """
    Find the start and end indices of a target string within a document.
    """
    start_index = document.find(target)
    if start_index == -1:
        return None
    end_index = start_index + len(target)
    return start_index, end_index
