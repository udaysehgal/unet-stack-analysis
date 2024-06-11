received_packets = set()
dropped_packets = set()
count = 0
count2 = 0
count3 = 0
count4 = 0

with open('aloha_1sim.nam', 'r') as file:
        for line in file:
            if line.startswith('r') :
                packet_info = line.split()
                dest_addr = packet_info[2]
                if (dest_addr) not in received_packets:
                    count += 1
                    received_packets.add(dest_addr)
            
            if line.startswith('d'):
                packet_info = line.split()
                dest_addr = packet_info[2]
                if (dest_addr) not in dropped_packets:
                    count2 += 1
                    dropped_packets.add(dest_addr)
                    
            if line.startswith('+'):
                count3+=1
            
            if line.startswith('-'):
                count4+=1

print('Total received packets: ', count)
print('Total dropped packet count: ', count3-count)
print('Enqueued packets: ', count3)
print('Dequeued packets: ', count4)


