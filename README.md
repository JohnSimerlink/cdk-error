
# CDK CodePipeline Assume Role Error

# Setup
- `$ python3 -m venv .venv`
- `$ source .venv/bin/activate`
- `$ pip install -r requirements.txt`
- `$ cdk synth`
# Deploy
- `$ cdk deploy`

A permissions error that shows up in the local terminal.
![](https://i.imgur.com/YdgEtQk.png)

Which seems to be inconsistent with the shown permissions in the AWS Console.

If you comment out lines 73 - 104, in cdk_error_stack.py, `cdk synth` will successfully deploy, upon which you can inspect the roles in the AWS IAM Console. Doing so, shows the following trust relationships for pipeline_action_role.
![](https://i.imgur.com/ZV7XYrw.png)

Clicking on "Edit Trust Relationship" Shows the following JSON for the trust relationship
![](https://i.imgur.com/1einnaY.png)

This reflects the explicit assume role policy set up on line 49
![](https://i.imgur.com/PZfJARs.png)

The reason I am manually specifying roles on lines 78, 88, 99 is because I was also getting an assumeRole error if I used the roles implicitly created in the `codepipepline.Pipeline` and `codepipeline.StageProps` constructs.

How can I get rid of the Not Authorized to Perform AssumeRole Error upon `cdk deploy`?

The below related issues/questions on the internet do not appear to be the same question I have:
- [aws pipeline role is not authorized to perform AssumeRole on cross account role](https://stackoverflow.com/questions/60958114/aws-pipeline-role-is-not-authorized-to-perform-assumerole-on-cross-account-role)
- [[aws-codepipeline-actions] Cannot assume role by code pipeline on code pipeline action AWS CDK #10068](https://github.com/aws/aws-cdk/issues/10068)

OS: `MacOS Catalina 10.15.2 (19C57)`

Python: `3.8.6`

CDK CLI Version: `1.85.0 (build 5f44668)`

My package versions as thru `pip list` are as follows:

--------------------------------------- ------- ----------------------------------------------------------------
- attrs                                   20.3.0
- aws-cdk.assets                          1.85.0
- aws-cdk.aws-apigateway                  1.85.0
- aws-cdk.aws-apigatewayv2                1.85.0
- aws-cdk.aws-applicationautoscaling      1.85.0
- aws-cdk.aws-autoscaling                 1.85.0
- aws-cdk.aws-autoscaling-common          1.85.0
- aws-cdk.aws-autoscaling-hooktargets     1.85.0
- aws-cdk.aws-batch                       1.85.0
- aws-cdk.aws-certificatemanager          1.85.0
- aws-cdk.aws-cloudformation              1.85.0
- aws-cdk.aws-cloudfront                  1.85.0
- aws-cdk.aws-cloudwatch                  1.85.0
- aws-cdk.aws-codebuild                   1.85.0
- aws-cdk.aws-codecommit                  1.85.0
- aws-cdk.aws-codedeploy                  1.85.0
- aws-cdk.aws-codeguruprofiler            1.85.0
- aws-cdk.aws-codepipeline                1.85.0
- aws-cdk.aws-codepipeline-actions        1.85.0
- aws-cdk.aws-cognito                     1.85.0
- aws-cdk.aws-ec2                         1.85.0
- aws-cdk.aws-ecr                         1.85.0
- aws-cdk.aws-ecr-assets                  1.85.0
- aws-cdk.aws-ecs                         1.85.0
- aws-cdk.aws-efs                         1.85.0
- aws-cdk.aws-elasticloadbalancing        1.85.0
- aws-cdk.aws-elasticloadbalancingv2      1.85.0
- aws-cdk.aws-events                      1.85.0
- aws-cdk.aws-events-targets              1.85.0
- aws-cdk.aws-iam                         1.85.0
- aws-cdk.aws-kinesis                     1.85.0
- aws-cdk.aws-kinesisfirehose             1.85.0
- aws-cdk.aws-kms                         1.85.0
- aws-cdk.aws-lambda                      1.85.0
- aws-cdk.aws-logs                        1.85.0
- aws-cdk.aws-route53                     1.85.0
- aws-cdk.aws-route53-targets             1.85.0
- aws-cdk.aws-s3                          1.85.0
- aws-cdk.aws-s3-assets                   1.85.0
- aws-cdk.aws-sam                         1.85.0
- aws-cdk.aws-secretsmanager              1.85.0
- aws-cdk.aws-servicecatalog              1.85.0
- aws-cdk.aws-servicediscovery            1.85.0
- aws-cdk.aws-sns                         1.85.0
- aws-cdk.aws-sns-subscriptions           1.85.0
- aws-cdk.aws-sqs                         1.85.0
- aws-cdk.aws-ssm                         1.85.0
- aws-cdk.aws-stepfunctions               1.85.0
- aws-cdk.cloud-assembly-schema           1.85.0
- aws-cdk.core                            1.85.0
- aws-cdk.custom-resources                1.85.0
- aws-cdk.cx-api                          1.85.0
- aws-cdk.region-info                     1.85.0
- boto3                                   1.17.10
- botocore                                1.20.10
- cattrs                                  1.1.2
- cdk-error                               0.0.1   /Users/john/dev/spine/cdk-error/cdk_error
- cdk-pipeline-assume-role-not-authorized 0.0.1   /Users/john/dev/spine/cdk-pipeline-assumeRole-notAuthorized/demo
- constructs                              3.3.27
- jmespath                                0.10.0
- jsii                                    1.21.0
- pip                                     20.2.1
- publication                             0.0.3
- python-dateutil                         2.8.1
- s3transfer                              0.3.4
- setuptools                              49.2.1
- six                                     1.15.0
- typing-extensions                       3.7.4.3
- urllib3                                 1.26.3
