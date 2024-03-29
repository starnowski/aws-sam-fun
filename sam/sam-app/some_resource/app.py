import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:",  context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    print("Path parameters:", event['pathParameters'])
    print("Query parameters:", event["queryStringParameters"])
    print("Http method:", event['httpMethod'])
    print("Http path:", event['path'])
    print("Http resource:", event['resource'])
    print("Http body:", event['body'])
    message = "hello world"
    if event['resource'] == "/some_resource/{id}" and event['httpMethod'] == "GET":
        message = "someResource: get with id parameter '" + event['pathParameters']["id"] + "'"
    if event['resource'] == "/some_resource" and event['httpMethod'] == "POST":
        jr = json.loads(event['body'])
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "someResource: post",
                "res_name": jr["res_name"]
            }),
        }
    if event['resource'] == "/some_resource/{id}" and event['httpMethod'] == "PUT":
        jr = json.loads(event['body'])
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "someResource: put with id parameter '" + event['pathParameters']["id"] + "'",
                "res_name": jr["res_name"]
            }),
        }
    if event['resource'] == "/some_resource" and event['httpMethod'] == "GET":
        message = "someResource: get"
    if event['resource'] == "/some_resource/{id}" and event['httpMethod'] == "DELETE":
        message = "someResource: delete with id parameter '" + event['pathParameters']["id"] + "'"
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            # "location": ip.text.replace("\n", "")
        }),
    }
