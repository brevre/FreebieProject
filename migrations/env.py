import sys
import os
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

# Import database and models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Base
import models  # Ensure models.py is imported

# Configure logging
fileConfig(context.config.config_file_name)

# Set the target metadata for Alembic
target_metadata = Base.metadata  # This is the missing piece!

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(url=context.config.get_main_option("sqlalchemy.url"), target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(context.config.get_section(context.config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
