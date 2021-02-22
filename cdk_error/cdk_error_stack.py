from aws_cdk import core

from aws_cdk import (
    core,
	aws_codebuild as codebuild,
    aws_codecommit as codecommit,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_iam as iam,
)

class CdkErrorStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        build_env = codebuild.BuildEnvironment(
            privileged = True,
        )
        repo_name = 'demo'
        branch_name = 'main'
        repository = codecommit.Repository.from_repository_name(
            self,
            repo_name + '-repo',
            repo_name
        ) 
        build_spec = codebuild.BuildSpec.from_source_filename('buildspec.yml')
        pipeline_role = iam.Role(
            scope = self,
            id = 'pipeline-role',
            assumed_by = iam.ServicePrincipal('codepipeline.amazonaws.com')
        )
        pipeline_action_role = iam.Role(
            scope = self,
            id = 'pipeline-action-role',
            assumed_by = iam.ServicePrincipal('codepipeline.amazonaws.com')
        )
        pipeline_role.assume_role_policy.add_statements(
            iam.PolicyStatement(
                actions = ["sts:AssumeRole"],
                principals = [
                    iam.ServicePrincipal(
                        'codebuild.amazonaws.com' 
                    )
                ],
                effect = iam.Effect.ALLOW
            )
        )
        pipeline_role.attach_inline_policy(
            iam.Policy(
                self,
                "pipeline-role-policy",
                document = iam.PolicyDocument(
                    statements = [
                        iam.PolicyStatement(
                            actions = [
                                "sts:AssumeRole"
                            ],
                            effect = iam.Effect.ALLOW,
                            resources = [
                                pipeline_action_role.role_arn
                            ]
                        )
                    ]
                ),
            )
            
        )
        pipeline_action_role.assume_role_policy.add_statements(
            iam.PolicyStatement(
                actions = ["sts:AssumeRole"],
                principals = [
                    pipeline_role
                ],
                effect = iam.Effect.ALLOW
            )
        )
        build_proj = codebuild.PipelineProject(
            self,
            'pipeplineproj',
            role = pipeline_role,
        )

        source_output = codepipeline.Artifact()
        build_action = codepipeline_actions.CodeBuildAction(
            action_name = 'build-action',
            input = source_output,
            project = repository,
        )

        pipeline_name = 'pipeline'

        # comment out lines 74+ to show error does not occur when commented out. This will allow the cdk deployment to work, such that the roles are successfully generated, such that you can see what the generated roles' trust policies are in the AWS console
        pipeline = codepipeline.Pipeline(
            scope = self,
            id = pipeline_name,
            pipeline_name = pipeline_name,
            role = pipeline_role,
            stages = [
                codepipeline.StageProps(
                    stage_name = 'source',
                    actions = [
                       codepipeline_actions.CodeCommitSourceAction(
                            action_name = 'codeCommitSource',
                            repository = repository,
                            branch = branch_name,
                            output = source_output, 
                            role = pipeline_action_role,
                        ),
                    ],
                ),
                codepipeline.StageProps(
                    stage_name = pipeline_name + 'build',
                    actions = [
                       codepipeline_actions.CodeBuildAction(
                            project = build_proj,
                            action_name = 'codeCommitSource',
                            input = source_output,
                            role = pipeline_action_role,
                        ) 
                    ],
                ),
            ]
        )