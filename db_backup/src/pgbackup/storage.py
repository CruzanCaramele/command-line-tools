def local(input_file, output_file):
        output_file.write(input_file.read())
        output_file.close()
        input_file.close()

def s3(client, input_file, bucket, name):
        client.upload_fileobj(input_file, bucket, name)