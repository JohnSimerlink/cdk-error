#!/usr/bin/env python3

from aws_cdk import core

from cdk_error.cdk_error_stack import CdkErrorStack


app = core.App()
CdkErrorStack(app, "cdk-error")

app.synth()
