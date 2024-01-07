from collections import defaultdict


def get_seeds_and_maps(input_file_name: str):
    maps: dict[str, list[tuple[int, int, int]]] = defaultdict(list)

    with open(f"./{input_file_name}", "r") as f:
        # first line is the list of seeds
        seeds = list(map(int, f.readline().strip().split(": ")[1].split(" ")))
        # ignore line break
        f.readline()
        # each map is separated by a line break
        # read each map name and its entries
        current_map_name = f.readline().strip()
        while line := f.readline():
            if line == "\n":
                current_map_name = f.readline().strip()
                continue

            dest_start, source_start, range_len = map(int, line.strip().split())
            maps[current_map_name].append((dest_start, source_start, range_len))

    return seeds, maps


def get_value_mapping(value: int, value_map: list[tuple[int, int, int]]) -> int:
    for dest_start, source_start, range_len in value_map:
        if source_start <= value <= source_start + range_len:
            mapped_value = (value - source_start) + dest_start
            return mapped_value

    return value


seeds, maps = get_seeds_and_maps(input_file_name="small_input.txt")

mapping_order = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:",
]

seeds = [79, 79 + 14, 55, 55 + 13]

mapped_values = seeds
for map_name in mapping_order:
    mapped_values = list(
        map(lambda value: get_value_mapping(value, maps[map_name]), mapped_values)
    )

print(seeds)
print(mapped_values)
# print(min(mapped_values))
