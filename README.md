
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

How can I get rid of the Not Authorized to Perform AssumeRole Error upon `cdk deploy`?

