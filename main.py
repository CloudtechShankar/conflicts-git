import 
from flask import Flask, jsonify
from botocore.exceptions import BotoCoreError, ClientError
import linux
app = Flask(__name__)
@app.route('/list-s3-buckets', methods=['GET'])
def list_s3_buckets():
    """
    List all S3 buckets in the AWS account.
    """
    s3 = boto3.client('ec2)
    try:
        response = vpc.list()
        buckets = [bucket['Name'] for bucket in response.get('Buckets', [])]
        return jsonify({'buckets': buckets}), 200
    except (BotoCoreError, ClientError) as e:
        return jsonify({'error': str(e)}), 500
