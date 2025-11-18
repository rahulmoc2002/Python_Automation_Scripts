# parser.py
from typing import Dict, Any, List, Optional
import re
from . import patterns
from .entities import normalize_text, find_between_markers, extract_instance_type, extract_region_for_cloud

DEFAULT_TAGS = {"owner": "unknown", "environment": "dev", "project": "poc"}

def _detect_action(text: str) -> Optional[str]:
    for action, kws in patterns.ACTION_KEYWORDS.items():
        for kw in kws:
            if kw in text:
                return action
    return None

def _detect_cloud(text: str) -> Optional[str]:
    for cloud, kws in patterns.CLOUD_KEYWORDS.items():
        for kw in kws:
            if kw in text:
                return cloud
    return None

def _detect_resource(text: str) -> Optional[str]:
    for res, kws in patterns.RESOURCE_KEYWORDS.items():
        for kw in kws:
            if kw in text:
                return res
    return None

def parse_user_prompt(text: str) -> Dict[str, Any]:
    warnings: List[str] = []
    try:
        if text is None:
            text = ""
        raw = text
        text = normalize_text(text)

        action = _detect_action(text)
        cloud = _detect_cloud(text)
        resource = _detect_resource(text)

        payload: Dict[str, Optional[str]] = {
            "name": None,
            "region": None,
            "instance_type": None,
        }

        name = find_between_markers(text, patterns.NAME_MARKERS)
        if name:
            payload["name"] = name

        project = None
        if "project" in text:
            m = re.search(r"project\s+([a-z0-9-_.]+)", text)
            if m:
                project = m.group(1)

        instance = extract_instance_type(text, patterns.INSTANCE_PATTERNS)
        if instance:
            payload["instance_type"] = instance

        region = extract_region_for_cloud(text, cloud, patterns.REGION_KEYWORDS)
        if region:
            payload["region"] = region

        if not action:
            warnings.append("action missing")
        if not cloud:
            warnings.append("cloud missing")
        if not resource:
            warnings.append("resource_type missing")
        if payload["instance_type"] is None and resource == "vm":
            warnings.append("instance_type missing")
        if payload["region"] is None:
            warnings.append("region missing")

        tags = DEFAULT_TAGS.copy()
        if project:
            tags["project"] = project
            payload["project"] = project

        payload["tags"] = tags

        return {
            "action": action or "",
            "cloud": cloud or "",
            "resource_type": resource or "",
            "payload": payload,
            "warnings": warnings,
            "raw_input": raw
        }

    except Exception as e:
        return {
            "action": "",
            "cloud": "",
            "resource_type": "",
            "payload": {"name": None, "region": None, "instance_type": None, "tags": DEFAULT_TAGS},
            "warnings": [f"parser_exception: {str(e)}"],
            "raw_input": text
        }
