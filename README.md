<<<<<<< HEAD
Week 2 – Harbor Rescue Inventory
Summary

The Harbor Rescue Inventory program manages a list of emergency supplies for rescue missions.
It uses different list functions to check cargo, find supplies, and create reports.
Each function helps rescuers quickly locate items and organize inventory.
The program also checks priority supplies for urgent missions.

Approach

mission_snapshot:
Returns a copy of the full supply list so the original list stays unchanged.

cargo_window:
Returns a portion (slice) of the supply list between two positions.

first_supply_index:
Searches the list and returns the first position of the target supply item.

supply_report:
Counts how many times a supply item appears in the list.

priority_load (stretch):
Creates a new list where priority supplies are placed first without changing the original list.

Complexity Reasoning
Function	Time Complexity	Why
mission_snapshot	O(n)	It copies every element in the list once
cargo_window	O(k)	It copies only the sliced portion
first_supply_index	O(n)	It may need to check every item
supply_report	O(n)	It scans the full list to count items
priority_load (stretch)	O(n)	It goes through the list to reorder items
Edge-Case Checklist

✔ empty list
✔ one-item list
✔ target missing
✔ repeated values
✔ slice goes past end
✔ size is zero
✔ size is negative
✔ original list unchanged in priority_load

Assistance / Sources

Person / tool / website:
Blackbox and Google 

Help received:
Help understanding list operations, slicing, and time complexity explanation.

Person / tool / website:
Class slides / Professor Ben

Help received:
Explanation of list functions and algorithm concepts.
=======
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/HYC1dWeQ)
# Week 2 README Template

## Summary
Write 3–6 lines explaining what the Harbor Rescue Inventory assignment does.

## Approach
Use bullets to explain how each function works.

- `mission_snapshot`:
- `cargo_window`:
- `first_supply_index`:
- `supply_report`:
- `priority_load` (stretch):

## Complexity reasoning

| Function | Time complexity | Why |
|---|---|---|
| `mission_snapshot` |  |  |
| `cargo_window` |  |  |
| `first_supply_index` |  |  |
| `supply_report` |  |  |
| `priority_load` (stretch) |  |  |

## Edge-case checklist
Mark the cases you tested.

- [ ] empty list
- [ ] one-item list
- [ ] target missing
- [ ] repeated values
- [ ] slice goes past end
- [ ] size is zero
- [ ] size is negative
- [ ] original list unchanged in `priority_load`

## Assistance / Sources
List any help you used and what kind of help it gave.

- Person / tool / website:
  - Help received:

- Person / tool / website:
  - Help received:
>>>>>>> 894c5f936fea79a75e5896e431e4d3e1ef7e3d4d
