import socket
import pickle
res = []
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('0.0.0.0', 8888))
data = (['/nfs/data8/hannan/stream_agent/restore/frame_0.png'],"car")
client_socket.send(pickle.dumps(data))
result_data = client_socket.recv(4096)
res = pickle.loads(result_data)
print("Message: ", res)
