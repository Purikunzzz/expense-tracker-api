"""
Database seeder: creates default categories for a user.

Usage:
    SEED_USER_ID=1 python seed.py
"""

import asyncio
import os
import sys

from dotenv import load_dotenv

# Must run before any app.* import — app.core.database builds its engine at
# import time from app.core.config.settings.DATABASE_URL, and pydantic-settings
# lets a real shell-exported DATABASE_URL silently win over the .env file.
# override=True forces the .env value (the Render URL) to take precedence,
# so this script never accidentally falls back to a local Postgres role.
load_dotenv(override=True)

from app.core.database import SessionLocal  # noqa: E402
from app.models.user import User  # noqa: E402
from app.schemas.categories import CategoryCreate  # noqa: E402
from app.services.category import create_category, get_categories  # noqa: E402

DEFAULT_CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Entertainment",
    "Health",
    "Education",
    "Others",
]


async def seed_categories(user_id: int) -> None:
    async with SessionLocal() as session:
        user = await session.get(User, user_id)
        if user is None:
            print(f"No user found with id={user_id}. Aborting.")
            return

        existing_names = {c.name for c in await get_categories(session, user_id)}

        created = []
        for name in DEFAULT_CATEGORIES:
            if name in existing_names:
                print(f"Skipping '{name}' (already exists for user {user_id})")
                continue
            await create_category(session, user_id, CategoryCreate(name=name))
            created.append(name)

        if created:
            print(f"Created {len(created)} categories for user {user_id}: {', '.join(created)}")
        else:
            print("No new categories to create.")


def main() -> None:
    user_id_raw = os.getenv("SEED_USER_ID")
    if not user_id_raw:
        print("SEED_USER_ID environment variable is required.")
        sys.exit(1)

    try:
        user_id = int(user_id_raw)
    except ValueError:
        print(f"SEED_USER_ID must be an integer, got: {user_id_raw!r}")
        sys.exit(1)

    asyncio.run(seed_categories(user_id))


if __name__ == "__main__":
    main()
