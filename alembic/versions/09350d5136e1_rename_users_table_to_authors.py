"""rename users table to authors

Revision ID: 09350d5136e1
Revises: 3354070d09ac
Create Date: 2023-03-22 18:54:55.780367

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '09350d5136e1'
down_revision = '3354070d09ac'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('users', 'authors')


def downgrade() -> None:
    op.rename_table('authors', 'users')
