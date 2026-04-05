trail = list(map(int, input().split()))
trail_energy = 0
for i in range(len(trail) - 1):
    current_step = trail [i]
    next_step = trail [i + 1]
    if current_step < next_step:
        gained = next_step - current_step
        total_energy =total_energy + gained
    if current_step > next_step:
        trail_energy == 0    
print(total_energy)