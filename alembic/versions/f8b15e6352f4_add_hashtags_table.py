"""add hashtags table

Revision ID: f8b15e6352f4
Revises: e9205f7c4cf5
Create Date: 2023-03-22 18:35:51.207312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8b15e6352f4'
down_revision = 'e9205f7c4cf5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'hashtags',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('creation_date', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )


def downgrade() -> None:
    op.drop_table('hashtags')
