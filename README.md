
# Welcome to your CDK Python project!

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

