from project import app, corrector
import sys
from flask import request, jsonify, Flask
from utils.api_utils import correctFunction, postprocessing_result
import concurrent.futures
from flask_socketio import SocketIO
from flask_cors import CORS
import socket
import concurrent.futures
import time
import websockets
import json
import asyncio
from server import receive_data
# def process_text(text):
#     try:
#         if not text or text == "" or len(text) < 10:
#             response_data = {"error": f"Received short text '{text}'"}
#         else:
#             # Thực hiện xử lý của bạn ở đây
#             # Ví dụ: out = correctFunction(text, corrector)
#             # result = postprocessing_result(out)
#             out = correctFunction(text, corrector)
#             result = postprocessing_result(out)
#             response_data = {"correction": result}
#         return response_data
#     except Exception as e:
#         return {"error": "An error occurred"}
# 
# @app.route('/spelling', methods=['POST'])
# def correct():
#     print("Response: Nguyễn Trọng Nghĩa")
#     try:
#         if 'file' not in request.files:
#             return jsonify({"error": "No file part"})
# 
#         uploaded_file = request.files['file']
#         text = uploaded_file.read().decode("utf-8")
#         print("text: ", text)
#         # Sử dụng một pool thread để xử lý yêu cầu đồng thời
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             future = executor.submit(process_text, text)
#             response_data = future.result()
#         return jsonify(response_data)
#     except Exception as e:
#         return jsonify({"error": "An error occurred"})

def process_text(text):
    try:
        if not text or text == "" or len(text) < 10:
            response_data = {"error": f"Received short text '{text}'"}
        else:
            # Thực hiện xử lý của bạn ở đây
            # Ví dụ: out = correctFunction(text, corrector)
            # result = postprocessing_result(out)
            out = correctFunction(text, corrector)
            result = postprocessing_result(out)
            response_data = {"correction": result}
        return response_data
    except Exception as e:
        return {"error": "An error occurred"}




# @app.route('/spelling', methods=['POST'])
# def correct():
#     try:
#         # Đọc dữ liệu text từ yêu cầu POST
#         text = request.data.decode("utf-8")
# 
#         # Sử dụng một pool thread để xử lý yêu cầu đồng thời
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             future = executor.submit(process_text, text)
#             response_data = future.result()
# 
#         return jsonify(response_data)
#     except Exception as e:
#         return jsonify({"error": "An error occurred"})

# @app.route("/receive_data", methods=["POST"])
# def receive_data_from_server1():
#     try:
#         server1_address = ('127.0.0.1', 8081)  # Change the port number to an available port
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             s.bind(server1_address)
#             s.listen(1)
#             conn, addr = s.accept()
#             print("Server 2: Connection established with Server 1")
# 
#             with conn:
#                 length_bytes = conn.recv(4)  # Nhận độ dài của dữ liệu
#                 length = int.from_bytes(length_bytes, byteorder='big')  # Chuyển đổi byte độ dài thành số nguyên
#                 user_json = conn.recv(length).decode('utf-8')  # Nhận dữ liệu JSON từ Server1
#                 print('Received data:', user_json)
#                 # Process the received data (user_json) if needed
#                 return "Data received from Server1"
#     except Exception as e:
#         return jsonify({"error": "An error occurred"})

            


    
    




