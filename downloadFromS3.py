import boto3
import sys
import os

def download_from_s3(bucket_name, object_key):
    try:
        # S3クライアントを作成
        s3 = boto3.client('s3')
        
        # オブジェクトキーからファイル名を取得
        file_name = os.path.basename(object_key)
        
        # ファイルをダウンロード
        s3.download_file(bucket_name, object_key, file_name)
        
        print(f"{object_key}を{file_name}としてダウンロードしました。")
    except boto3.exceptions.Boto3Error as e:
        print(f"Boto3エラーが発生しました: {str(e)}")
        if 'response' in dir(e) and 'Error' in e.response:
            print(f"エラーコード: {e.response['Error'].get('Code', 'Unknown')}")
            print(f"エラーメッセージ: {e.response['Error'].get('Message', 'No message')}")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python downloadFromS3.py <バケット名> <オブジェクトキー>")
        sys.exit(1)
    
    bucket_name = sys.argv[1]
    object_key = sys.argv[2]
    
    download_from_s3(bucket_name, object_key)
