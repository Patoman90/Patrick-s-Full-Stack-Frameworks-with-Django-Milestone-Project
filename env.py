import os

os.environ.setdefault("STRIPE_PUBLISHABLE", os.getenv("STRIPE_PUBLISHABLE"))
os.environ.setdefault("STRIPE_SECRET", os.getenv("STRIPE_SECRET"))
os.environ.setdefault("DATABASE_URL", os.getenv("DATABASE_URL"))
os.environ.setdefault("SECRET_KEY", os.getenv("SECRET_KEY"))
os.environ.setdefault("AWS_ACCESS_KEY_ID", os.getenv("AWS_ACCESS_KEY_ID"))
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", os.getenv("AWS_SECRET_ACCESS_KEY"))
os.environ.setdefault("AWS_STORAGE_BUCKET_NAME", "patricks-milestone4")
