# patterns.py
ACTION_KEYWORDS = {
    "create": ["create", "launch", "spin up", "start", "provision", "add"],
    "delete": ["delete", "destroy", "remove", "terminate"],
    "update": ["update", "modify", "change"]
}

CLOUD_KEYWORDS = {
    "aws": ["aws", "amazon", "ec2"],
    "gcp": ["gcp", "google", "gce", "google cloud"],
    "azure": ["azure", "az", "vmss", "microsoft"]
}

RESOURCE_KEYWORDS = {
    "vm": ["vm", "instance", "virtual machine", "virtualmachine", "compute"],
    "bucket": ["bucket", "storage", "bucket storage", "s3"],
    "db": ["database", "db", "rds", "sql", "postgres", "mysql"]
}

REGION_KEYWORDS = {
    "aws": ["us-east-1", "us-west-2", "eu-west-1", "ap-south-1"],
    "gcp": ["us-central1", "europe-west1", "asia-south1"],
    "azure": ["eastus", "westus2", "centralindia"]
}

INSTANCE_PATTERNS = ["t2.", "t3.", "m5.", "e2-", "n1-", "standard_b", "Standard_B"]

NAME_MARKERS = ["named", "name", "called", "for project", "project"]
