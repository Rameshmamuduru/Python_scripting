import boto3
import logging
import os

# ======================================================
# Configure Logging
# ======================================================

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# ======================================================
# AWS Clients
# ======================================================

ec2 = boto3.client("ec2")
sns = boto3.client("sns")

# ======================================================
# Environment Variables
# ======================================================

ENVIRONMENT = os.environ["ENVIRONMENT"]
AUTO_SCHEDULE = os.environ["AUTO_SCHEDULE"]
SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]


def lambda_handler(event, context):

    logger.info("========== Lambda Execution Started ==========")

    try:

        # --------------------------------------------------
        # Get all running EC2 instances matching our tags
        # --------------------------------------------------

        response = ec2.describe_instances(
            Filters=[
                {
                    "Name": "tag:Environment",
                    "Values": [ENVIRONMENT]
                },
                {
                    "Name": "tag:AutoSchedule",
                    "Values": [AUTO_SCHEDULE]
                },
                {
                    "Name": "instance-state-name",
                    "Values": ["running"]
                }
            ]
        )

        instance_ids = []
        instance_names = []

        # --------------------------------------------------
        # Read EC2 Details
        # --------------------------------------------------

        for reservation in response["Reservations"]:

            for instance in reservation["Instances"]:

                instance_ids.append(instance["InstanceId"])

                instance_name = "Unknown"

                if "Tags" in instance:

                    for tag in instance["Tags"]:

                        if tag["Key"] == "Name":

                            instance_name = tag["Value"]
                            break

                instance_names.append(instance_name)

        # --------------------------------------------------
        # No Matching EC2 Instances
        # --------------------------------------------------

        if not instance_ids:

            message = f"""
EC2 Automation Report

Status : SUCCESS

No running EC2 instances found.

Environment : {ENVIRONMENT}
"""

            logger.warning(message)

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="EC2 Automation Report",
                Message=message
            )

            return {
                "statusCode": 200,
                "body": message
            }

        # --------------------------------------------------
        # Stop EC2 Instances
        # --------------------------------------------------

        logger.info(f"Stopping Instances : {instance_ids}")

        ec2.stop_instances(
            InstanceIds=instance_ids
        )

        # --------------------------------------------------
        # Build Report
        # --------------------------------------------------

        report = f"""
EC2 Automation Report

Status : SUCCESS

Environment : {ENVIRONMENT}

Total Instances Stopped : {len(instance_ids)}

Stopped Instances

"""

        for name, instance_id in zip(instance_names, instance_ids):

            report += f"- {name} ({instance_id})\n"

        # --------------------------------------------------
        # Log Report
        # --------------------------------------------------

        logger.info(report)

        # --------------------------------------------------
        # Send SNS Notification
        # --------------------------------------------------

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="EC2 Automation Successful",
            Message=report
        )

        logger.info("========== Lambda Execution Completed ==========")

        return {
            "statusCode": 200,
            "body": report
        }

    except Exception as error:

        logger.exception("Lambda execution failed.")

        error_message = f"""
EC2 Automation FAILED

Environment : {ENVIRONMENT}

Reason

{str(error)}
"""

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="EC2 Automation FAILED",
            Message=error_message
        )

        raise
