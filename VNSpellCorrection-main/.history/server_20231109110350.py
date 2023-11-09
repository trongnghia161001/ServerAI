#Project Flask MVC

from flask import Flask
import websockets
import asyncio
import json
from utils.api_utils import correctFunction, postprocessing_result
from project import app, corrector
import boto3
from botocore.exceptions import NoCredentialsError
import pandas as pd
import docx
import io
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
from docx import Document
import requests
import tqdm

async def receive_data(websocket, path):
    async for message in websocket:
        user_id = message  # Tin nhắn nhận được từ kết nối websocket
        bucket_name = "laptrinhmangnangcao"
        region_name = "ap-southeast-1"
        s3 = boto3.resource(
             "s3", aws_access_key_id="AKIA5IACU6HRNBHF4AWX", aws_secret_access_key="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"
        )

        bucket = s3.Bucket(bucket_name)
        objects = list(bucket.objects.filter(Prefix=f"{user_id}_"))
        total_objects = len(objects)
        
        complete_text = ""  # Khởi tạo complete_text ở đây
        total_paragraphs = 0  # Khởi tạo số đoạn văn
        total_processed_paragraphs = 0  # Khởi tạo số đoạn văn đã xử lý
        
        with tqdm.tqdm(total=total_objects) as pbar:
            for obj in objects:
                if obj.key.split("_")[0] == str(user_id):
                    object_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{obj.key}"
                    response = requests.get(object_url)
                    if response.status_code == 200:
                        docx_bytes = response.content
                        docx_file = BytesIO(docx_bytes)
                        doc = Document(docx_file)
                        paragraphs = [paragraph.text for paragraph in doc.paragraphs]
                        total_paragraphs += len(paragraphs)

                        for paragraph in paragraphs:
                            corrections = process_text(paragraph)
                            if 'correction' in corrections:
                                correctionsFix = corrections['correction']
                                complete_text += build_complete_text(correctionsFix)
                            else:
                                # Handle the case where 'correction' key is not present
                                # You might want to add default behavior or log a message here
                                pass

                            total_processed_paragraphs += 1
                            progress = (total_processed_paragraphs / total_paragraphs) * 100
                            print(f"Processed {total_processed_paragraphs} out of {total_paragraphs} paragraphs. Progress: {progress:.2f}%")
                            await websocket.send(f"Processed {total_processed_paragraphs} out of {total_paragraphs} paragraphs. Progress: {progress:.2f}%")

                            await asyncio.sleep(0.1)  # Optional sleep to control the rate of messages being sent

                    pbar.update(1)  # Cập nhật tiến trình của thanh tiến trình

                if total_processed_paragraphs == total_paragraphs:  # Kiểm tra xem đã xử lý hết đoạn văn chưa
                    break  # Thoát khỏi vòng lặp khi tất cả các đoạn văn đã được xử lý

        await websocket.send(complete_text)






                            
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
     
def build_complete_text(corrections):
    complete_text = ""
    for correction in corrections:
        index = correction[0]
        if index == 0:
            complete_text += correction[1]
        elif index == 1 and len(correction) > 2:
            complete_text += correction[2]
        else:
            complete_text += correction[1]
    return complete_text


        
if __name__ == '__main__':
    start_server = websockets.serve(receive_data, "127.0.0.1", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

