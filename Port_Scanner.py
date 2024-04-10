import sys
import socket
import pyfiglet
import threading
from queue import Queue

ascii_banner = pyfiglet.figlet_format("Hacker Man")
print(ascii_banner)

ip = '10.10.10.233'
open_ports = []

ports = range(1, 65535)

print_lock = threading.Lock()

queue = Queue()

def probe_port(ip, port, result=1):
    try:
        progress = str(round(((port/65535)*100), 2))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        print(f"\r{progress}% Done Scanning {ip}", end='', flush=True)
        if result == 0:
            with print_lock:
                print(f"\nPort {port} is open")
                open_ports.append(port)
        sock.close()
    except Exception as e:
        pass
    return result

def worker():
    while not queue.empty():
        port = queue.get()
        probe_port(ip, port)  # Notice the `ip` is now being passed correctly
        queue.task_done()

thread_count = 500

# Fill the queue with ports
for port in ports:
    queue.put(port)

# Start threads
for t in range(thread_count):
    thread = threading.Thread(target=worker)
    thread.daemon = True  # Allow program to exit even if thread is blocked
    thread.start()

# Wait for all threads to complete
queue.join()

# Print results
if open_ports:
    print("\nOpen Ports are: ")
    print(sorted(open_ports))
else:
    print("\nLooks like no ports are open :(")



