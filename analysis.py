sims = 0
sim_lines = []

def analyze_simulation(lines):
    received_packets = set()
    r_count = 0
    enqueued_packets = 0
    dequeued_packets = 0
    flag = False
    first_time = 0
    last_time = 0
    
    for line in reversed(lines):
        last_time = float(line.split()[2])
        break

    for line in lines:
        if float(line.split()[2]) >= 900:
            if(flag==False):
                first_time = float(line.split()[2])
                flag = True
                
            if line.startswith('r'):
                packet_info = line.split()
                dest_addr = packet_info[2]
                if dest_addr not in received_packets:
                    r_count += 1
                    received_packets.add(dest_addr)

            if line.startswith('+'):
                enqueued_packets += 1

            if line.startswith('-'):
                dequeued_packets += 1
    
    sim_time = last_time-first_time
    
    print('Enqueued packets : ', enqueued_packets)
    print('Dequeued packets : ', dequeued_packets)
    print('Received packets : ', r_count)
    print('Dropped packets  : ', max(enqueued_packets-r_count,0))
    print('Offered load     : ', f"{enqueued_packets/sim_time:.4f}")
    print('Throughput       : ', f"{r_count/sim_time:.4f}")
    print('\n')
    
with open('aloha.nam', 'r') as file:
    for line in file:
        if line.startswith('#'):
            sims += 1
            if sim_lines: 
                print('SIMULATION #',(int)((sims+1)/3))
                analyze_simulation(sim_lines)
                sim_lines = []
        else:
            sim_lines.append(line)

    if sim_lines:
        analyze_simulation(sim_lines)
