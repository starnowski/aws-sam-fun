# aws-sam-fun

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html

### Testing api-gateway lambda locally
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html

```shell
sam local start-api
```

```shell
curl http://127.0.0.1:3000/hello
```

```shell
curl -X POST  http://127.0.0.1:3000/some_resource -H 'Content-Type: application/json' -d '{"res_name":"Test"}'
```

### How to set up github action
https://github.com/aws-actions/setup-sam

https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html

### Example of AWS ApiGateway tutorial for Lambda and Dynamodb
https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html

### SAM example projects
https://github.com/amazon-archives/serverless-app-examples/tree/master/python

https://aws.amazon.com/about-aws/whats-new/2019/02/develop-and-test-aws-step-functions-workflows-locally/
https://hub.docker.com/r/amazon/aws-stepfunctions-local
https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-lambda.html
