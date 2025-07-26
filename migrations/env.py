# migrations/env.py
import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config # <--- ADD THIS IMPORT
from sqlalchemy import pool             # <--- ADD THIS IMPORT

from alembic import context

# Add your project's root directory to the Python path
# This is crucial for imports like 'app.database.session'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your Base metadata object
# This import should now be safe as session.py is lazily initializing engine/SessionLocal
from app.database.session import Base # <--- Keep this import
from app.models.user import User 

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target_metadata to your Base.metadata
target_metadata = Base.metadata # <--- Make sure this line is uncommented and correct

# You can remove or comment out any lines that try to import 'settings' or 'app' directly
# For example, if you had:
# from app.core.config import settings # <--- REMOVE OR COMMENT THIS
# from main import app # <--- REMOVE OR COMMENT THIS


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # Get the database URL from alembic.ini's [sqlalchemy] section
    alembic_config_section = config.get_section(config.config_ini_section, {})
    print(f"DEBUG: Alembic config section content: {alembic_config_section}") 
  # This line should be indented correctly
    connectable = engine_from_config(
          config.get_section("sqlalchemy", {}), # This line also needs to be correctly indented relative to 'connectable ='
          prefix="sqlalchemy.",                 # And this one
          poolclass=pool.NullPool,              # And this one
      )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # include_object=include_object, # Keep if you had it
            # process_revision_directives=process_revision_directives, # Keep if you had it
            # render_as_batch=True # Good for MySQL for ALTER TABLE, uncomment if needed
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()