"""add registraion column in users

Revision ID: e9205f7c4cf5
Revises: 16a108cddbe4
Create Date: 2023-03-22 18:18:16.018307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9205f7c4cf5'
down_revision = '16a108cddbe4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('registration_date', sa.DateTime(), nullable=True)
    )


def downgrade() -> None:
    op.drop_column('users', 'registration_date')
