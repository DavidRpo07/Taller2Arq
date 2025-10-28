import os, boto3

S3_BUCKET  = os.getenv("S3_BUCKET")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

s3 = boto3.client("s3", region_name=AWS_REGION)

def _public_url(key: str) -> str:
    # URL dependiendo de la región, pero us-east-1 usa el dominio sin región
    if AWS_REGION and AWS_REGION != "us-east-2":
        return f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{key}"
    return f"https://{S3_BUCKET}.s3.amazonaws.com/{key}"

def list_image_urls(prefix: str = ""):
    resp = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=prefix)
    urls = []
    for obj in resp.get("Contents", []):
        key = obj["Key"]
        if key.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
            urls.append(_public_url(key))
    return urls
