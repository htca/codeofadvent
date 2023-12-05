text_file = "assignment.txt"
with open(text_file,"r") as file:
    data = file.read().splitlines()


def update_numbers():
    for i, n in enumerate(numbers):
        for j, rng in enumerate(ranges):
            if n in rng:
                numbers[i] += deltas[j]
                break

def update_ranges():
    if len(ranges) == 0:
        return seed_ranges
    new_seed_ranges = []
    while len(seed_ranges) > 0:
        rng_1 = seed_ranges.pop(0)
        found = False
        for j, rng_2 in enumerate(ranges):
            # Full seedrange in range
            if rng_2.start <= rng_1.start < rng_2.stop and rng_2.start < rng_1.stop <= rng_2.stop:
                new_rng = range(rng_1.start + deltas[j], rng_1.stop + deltas[j])
                new_seed_ranges.append(new_rng)
                found = True
                break
            # start seedrange in range; end out of range
            elif rng_2.start <= rng_1.start < rng_2.stop:
                new_rng_a = range(rng_1.start + deltas[j], rng_2.stop + deltas[j])
                new_rng_b = range(rng_2.stop, rng_1.stop)
                new_seed_ranges.append(new_rng_a), seed_ranges.append(new_rng_b)
                found = True
                break
            # end seedrange in range; start out of range
            elif rng_2.start < rng_1.stop <= rng_2.stop:
                new_rng_a = range(rng_1.start, rng_2.start)
                new_rng_b = range(rng_2.start + deltas[j], rng_1.stop + deltas[j])
                seed_ranges.append(new_rng_a), new_seed_ranges.append(new_rng_b)
                found = True
                break
            # goal range in seedrange
            elif rng_1.start <= rng_2.start < rng_1.stop and rng_1.start < rng_2.stop <= rng_1.stop:
                new_rng_a = range(rng_1.start, rng_2.start)
                new_rng_b = range(rng_2.start + deltas[j], rng_2.stop + deltas[j])
                new_rng_c = range(rng_2.stop, rng_1.stop)
                seed_ranges.append(new_rng_a), new_seed_ranges.append(new_rng_b), seed_ranges.append(new_rng_c)
                found = True
                break
            # print(f'Check 1 {rng_1.start < rng_2.start and rng_1.stop <= rng_2.start} or check 2 {rng_1.start >= rng_2.stop and rng_1.stop > rng_2.stop}')
        # When not in range add values
        if not found:
            new_seed_ranges.append(rng_1)
    new_seed_ranges = sorted(new_seed_ranges, key=lambda x: x.start)
    return new_seed_ranges

seed_ranges =[]
for line in data:
    if "seeds:" in line:
        numbers = list(map(int, data[0].split(': ')[1].split()))
        i = 0
        while i < len(numbers):
            rng = range(numbers[i], numbers[i] + numbers[i + 1])
            seed_ranges.append(rng)
            i += 2
ranges, deltas = [], []
for line in data[1:]:
    if 'map' in line:
        update_numbers()
        seed_ranges=update_ranges()
        ranges, deltas = [],[]
    elif line!='':
        rng = range(int(line.split()[1]), int(line.split()[1]) + int(line.split()[2])) # begin en einde range originator
        delta = int(line.split()[0]) - int(line.split()[1]) # verschil destination and origin
        ranges.append(rng), deltas.append(delta)
update_numbers()
seed_ranges=update_ranges()

pt2 = float('inf')
for rng in seed_ranges:
    pt2 = min(pt2, rng.start)
print(pt2)